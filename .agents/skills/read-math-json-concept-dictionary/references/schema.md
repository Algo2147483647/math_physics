# `math.json` Schema Reference

## When To Read This File

Read this reference only when the main `SKILL.md` is not enough.

Typical reasons:

- you need the exact meaning of `define`, `parents`, `children`, or `properties`;
- you need to know how to interpret relation maps;
- you need to handle empty or very long content safely;
- you need to answer in a structured way without reopening the whole JSON.

## File Identity

- Path: `D:\Algo\Notes\math_physics\math\lib\math.json`
- Role: large concept-dictionary JSON for mathematical terms
- Current observed snapshot on 2026-04-24:
  - top-level type: object
  - top-level keys: 100 concept names
  - every current node contains `define`, `parents`, `children`, and `properties`
  - current node field types are stable:
    - `define`: string
    - `parents`: object
    - `children`: object
    - `properties`: array of strings

Treat this observed regularity as a strong default, but still answer defensively if a future node is incomplete.

## Overall Data Model

Interpret the file as:

`concept_name -> concept_node`

Where:

- `concept_name` is the canonical identifier used by the repository
- `concept_node` stores definition text, hierarchy relations, and supplementary notes for that concept

This is not a list of records. It is a keyed dictionary for direct term lookup.

## Top-Level Keys

Each top-level key is a math concept name such as `Affine_Space`, `Banach_Space`, or `Real_Field`.

Read top-level keys as canonical term identifiers.

- They are the primary lookup handle.
- They often use underscore-separated naming.
- They should be preserved exactly when citing the source key.
- When the user writes a natural-language term, resolve it to the nearest matching key before reading the node.

## Standard Concept Node Shape

Use this as the default schema:

```json
{
  "Concept_Name": {
    "define": "Markdown definition text with possible LaTeX",
    "parents": {
      "ParentConcept": "relation_label"
    },
    "children": {
      "ChildConcept": "relation_label"
    },
    "properties": [
      "Supplementary Markdown content"
    ]
  }
}
```

## Field Semantics

### `define`

- Type: string
- Meaning: the primary definition block for the concept
- Typical content:
  - Markdown paragraphs
  - block quotes
  - LaTeX display math
  - inline math
  - links to related notes
- Best use:
  - answering "What is X?"
  - giving the formal or repository-native definition
  - extracting the main mathematical formula or setup
- Current observed length range:
  - roughly 225 to 4348 characters

Read `define` first for almost every concept question.

### `parents`

- Type: object mapping `RelatedConcept -> relation_label`
- Meaning: concept-level parent or dependency relations pointing upward or outward from the current concept
- Typical content:
  - `"Normed_Space": "subtype_of"`
  - `"Field": "over_field"`
  - `"Vector_Space": "modeled_on"`
- Best use:
  - answering "What class does this belong to?"
  - identifying direct superconcepts or definitional dependencies
  - summarizing where the concept sits in the ontology

Do not flatten this into plain prose without keeping the relation label.

### `children`

- Type: object mapping `RelatedConcept -> relation_label`
- Meaning: concept-level child or downstream relations from the current concept
- Typical content:
  - subtype children
  - structured descendants
  - other repository-defined outward relations
- Best use:
  - answering "What specializations are listed under this concept?"
  - enumerating directly stored child concepts
  - showing outward structure from the current node

Do not assume `children` means examples. It is a relation map, not an example list.

### `properties`

- Type: array of strings
- Meaning: supplementary content blocks associated with the concept
- Typical content:
  - additional properties
  - formulas
  - theorem-like remarks
  - structured Markdown sections
  - lists, headings, image links, relative links, or local paths
- Current observed shape:
  - currently always a string array
  - currently one array item per node in this snapshot
  - that single string may be empty or very long
- Current observed length range of a property block:
  - roughly 0 to 13838 characters
- Best use:
  - answering "What properties or extra facts are recorded?"
  - retrieving formulas and extended notes
  - surfacing non-core detail after the main definition

Do not dump all of `properties` by default. Summarize first, then expand selectively.

## Relation Labels

The values inside `parents` and `children` are relation labels, not descriptive sentences.

Observed relation labels include:

- `subtype_of`
- `field_extension_of`
- `modeled_on`
- `induced_by`
- `has_underlying_set`
- `has_base_space`
- `has_ambient_space`
- `has_domain`
- `has_codomain`
- `over_field`
- `over_ring`
- `projectivization_of`

Keep the label visible when it matters. Do not silently collapse all relations into "is a".

## Reading Priority By Question Type

- "What is X?" -> `define`
- "What does X belong to?" -> `parents`
- "What falls under X?" -> `children`
- "What properties, formulas, or remarks does X have?" -> `properties`
- "How is X related to Y?" -> read both nodes and compare `parents` / `children` first, then `define` if needed

Default order for a single concept:

1. resolve the top-level key
2. read `define`
3. read `parents`
4. read `children`
5. read only the relevant slice of `properties`

## Empty, Missing, and Long Fields

Use these rules:

- If a field is missing, report it as missing in the source. Do not infer replacement content.
- If a field is present but empty, treat that as "no data recorded here", not as negative evidence.
- `parents` and `children` may legitimately be empty objects.
- `properties` may contain an empty string.
- Long `define` or `properties` content should be summarized first, then expanded only if the user wants detail.

Current observed examples:

- some concepts have empty `parents`
- many concepts have empty `children`
- some concepts have empty `properties`
- no current concept has an empty `define`

## Formatting And Preservation Rules

- Preserve Markdown structure when quoting or excerpting.
- Preserve LaTeX exactly unless the user explicitly asks for paraphrase or conversion.
- Preserve relative links and local resource paths as source content.
- Do not normalize bilingual content into one language unless asked.

## Answer Assembly

Prefer this structure:

- `Term`: exact top-level key or the resolved canonical term
- `Definition`: concise summary from `define`, with short quoted formulas only when useful
- `Parents`: relation map rendered as `ParentConcept (relation_label)`
- `Children`: relation map rendered as `ChildConcept (relation_label)`
- `Properties`: short summary of only the relevant property content
- `Notes`: missing fields, ambiguity in key resolution, or notice that more long-form content exists

Good default behavior:

- summarize `define` rather than copying it in full
- list `parents` and `children` explicitly
- keep `properties` short unless the user asks for the full mathematical detail
- mention when additional source content was omitted for brevity

## Operational Reminder

The main purpose of this skill is to remove repeated schema re-discovery. Assume this data model first, read only the necessary node fields, and spend context on the user's mathematical question rather than on reinterpreting the file format.
