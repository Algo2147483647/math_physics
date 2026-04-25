# Math Concept Node Schema


## Schema

Use this as the default schema for a concept node:

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

Apply the template rules strictly:

- keep all four standard fields;
- use `""` for an empty `define`;
- use `{}` for empty `parents` and `children`;
- use `[]` for empty `properties`;
- do not use `null`;
- do not replace `properties` with a bare string.

## Field Semantics

Reading Priority By Question Type:

- "What is X?" -> `define`
- "What does X belong to?" -> `parents`
- "What falls under X?" -> `children`
- "What properties, formulas, or remarks does X have?" -> `properties`
- "How is X related to Y?" -> read both nodes and compare `parents` / `children` first, then `define` if needed


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

Read `define` first for almost every concept question.

### `parents`

- Type: object mapping `RelatedConcept -> relation_label`
- Meaning: concept-level parent or dependency relations pointing upward or outward from the current concept
- Best use:
  - answering "What class does this belong to?"
  - identifying direct superconcepts or definitional dependencies
  - summarizing where the concept sits in the ontology

Do not flatten this into plain prose without keeping the relation label. 

### `children`

- Type: object mapping `RelatedConcept -> relation_label`
- Meaning: concept-level child or downstream relations from the current concept
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

