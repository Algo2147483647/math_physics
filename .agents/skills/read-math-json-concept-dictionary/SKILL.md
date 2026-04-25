---
name: read-math-json-concept-dictionary
description: Use this when extracting a definition, hierarchy relation, child-concept list, or property summary from math_physics\math\lib\math.json. The file is a large concept-dictionary JSON whose top-level keys are canonical math concept names, and each node contains the fields define, parents, children, and properties.
---

# Skill: Read `math.json` as a Concept Dictionary

## Scope

Use this skill for requests grounded in `math_physics\math\lib\math.json`.

Treat that file as a stable concept dictionary, not as an unknown generic JSON blob. Do not spend tokens re-inferring the schema on each use unless there is evidence that the file format changed.

## Default Mental Model

- The file is one top-level object.
- Each top-level key is a canonical concept name such as `Affine_Space` or `Banach_Space`.
- Each top-level value is a concept node.
- A concept node is read primarily through four fields:
  - `define`: the main definition block
  - `parents`: incoming concept relations
  - `children`: outgoing concept relations
  - `properties`: supplementary mathematical content

## Fast Read Order

Read only the fields needed for the user question.

- If the user asks what a concept is, read `define` first.
- If the user asks what it belongs to, read `parents`.
- If the user asks for subtypes, refinements, or downstream related concepts, read `children`.
- If the user asks for properties, formulas, theorems, remarks, or extra detail, read `properties` after `define`.
- If the user asks for comparison or relation between concepts, read the relevant nodes plus the relation maps.

Do not load the whole file into context when one or a few nodes are enough.

## Deterministic Helpers

Use the bundled scripts before manual JSON inspection when the task is mostly lookup, comparison, or validation.

- For concept key resolution or selective field reads, run `scripts/lookup_concept.py`.
- For pairwise concept-relation comparison, run `scripts/compare_concepts.py`.
- For edit-impact checks before changing or deleting a node, run `scripts/find_references.py`.
- For schema validation, relation-label counts, and snapshot statistics, run `scripts/validate_math_json.py`.

Prefer `--json` when another agent step needs structured output.

## Output Contract

Prefer this response layout when answering from the file:

- `Term`
- `Definition`
- `Parents`
- `Children`
- `Properties`
- `Notes`

If a section has no source content, say it is absent or empty in the source instead of guessing.

## Handling Rules

- Preserve Markdown, LaTeX, relative links, and local resource paths. Do not casually rewrite formulas.
- Treat `parents` and `children` as concept-relation mappings, not as prose text.
- Treat `properties` as expandable supporting material. Summarize first when it is long; quote or unfold only the relevant part.
- Do not infer missing facts from naming alone.
- Resolve the user term to the nearest top-level key before reading the node.

## Reference Loading

This file is enough for ordinary question answering.

Read [references/schema.md](references/schema.md) only when you need:

- the exact data model and field semantics;
- the current observed shape of the file;
- edge-case handling for empty, missing, or very long fields;
- guidance for assembling a compact structured answer.

Read [references/editing-rules.md](references/editing-rules.md) when you need to add, update, delete, normalize, or batch-edit concept nodes or relation mappings in `math.json`.
