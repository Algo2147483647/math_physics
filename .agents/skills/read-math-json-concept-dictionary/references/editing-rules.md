# `math.json` Editing Rules

## When To Read This File

Read this file only for edit tasks on `D:\Algo\Notes\math_physics\math\lib\math.json`.

Typical cases:

- add a new concept node;
- update an existing concept node;
- add, remove, or rename a relation in `parents` or `children`;
- delete a concept node;
- normalize or batch-fix node shape.

For ordinary question answering, use `SKILL.md` and `schema.md` instead.

## Editing Defaults

Use these defaults unless the user explicitly asks otherwise:

- prefer the smallest safe edit over full-node rewrites;
- preserve untouched fields exactly;
- preserve Markdown, LaTeX, relative links, and local resource paths verbatim;
- do not invent missing mathematical content to make a node feel complete;
- keep key spelling and relation labels exact;
- keep field types stable;
- inspect the affected node directly before editing it.

## Canonical Node Template

Use this as the default shape for a concept node:

```json
{
  "Concept_Name": {
    "define": "",
    "parents": {},
    "children": {},
    "properties": []
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

## Key Naming Rules

- use the canonical top-level concept key format already present in the file;
- prefer underscore-separated keys such as `Banach_Space`;
- if the user gives a natural-language term, resolve it to the repository key before editing;
- if the intended canonical key is unclear, stop and ask rather than creating a duplicate concept under a near-match name.

## Add Rules

When adding a new concept:

1. confirm that no existing top-level key already represents the same concept;
2. create the new node with the canonical four-field template;
3. add only content explicitly requested or supported by nearby repository conventions;
4. keep `define` concise if source material is limited;
5. leave unknown fields empty rather than guessing.

When adding relations:

- add a `parents` entry when the user is specifying an upward or dependency relation from the current concept;
- add a `children` entry when the user is specifying a downstream relation from the current concept;
- inspect both involved nodes before deciding whether to update one side or both sides;
- do not assume every relation must be mirrored automatically.

## Update Rules

When updating an existing concept:

- edit only the field that answers the request;
- for `define`, patch the relevant span instead of rewriting the whole block unless a full rewrite is explicitly requested;
- for `parents` or `children`, preserve unrelated mapping entries exactly;
- for `properties`, update only the relevant item or append a new item if that is clearly the smallest coherent edit;
- if a property block is long, avoid reformatting unrelated sections;
- keep mathematical notation stable unless the user explicitly wants a reformulation.

## Relation Editing Rules

Treat `parents` and `children` as relation maps, not as prose.

When changing a relation:

1. inspect the source node;
2. inspect the linked node;
3. identify whether the relation is currently represented on one side only or on both sides;
4. make the smallest edit that preserves the repository's local convention for that pair.

Current observed pattern in the 2026-04-24 snapshot:

- most `parents` edges have a corresponding reverse entry in the related node's `children`;
- a small number of edges are intentionally or historically one-sided.

Because of that:

- do not force global bidirectional synchronization as an invariant;
- if a relation is already mirrored on both sides, keep it mirrored when editing;
- if a relation is one-sided in the current data, do not add the missing reverse edge unless the task explicitly calls for normalization or the local neighborhood strongly supports it;
- if you add a brand new relation and the surrounding pattern is unclear, prefer updating the directly requested side and note the ambiguity.

## Delete Rules

Deleting a concept is not only removing one top-level key.

Before deleting:

1. inspect the target node;
2. find all other nodes that reference the target key in `parents`;
3. find all other nodes that reference the target key in `children`;
4. decide whether those references should be removed, replaced, or escalated for human review.

During deletion:

- remove the top-level key;
- remove stale references to that key from other nodes when the correct action is unambiguous;
- do not silently retarget relations to a guessed replacement concept.

After deletion:

- no remaining node should mention the removed key in `parents` or `children`;
- if any cleanup decision is ambiguous, leave a clear note instead of guessing.

## Missing And Empty Content Rules

- if a field is absent in a legacy or malformed node, restore the standard field shape only when the task includes normalization or when the edit clearly requires it;
- if a field is present but empty, treat that as valid stored emptiness, not corruption;
- do not create filler text for empty `define` or `properties`.

## Batch Edit Rules

For batch updates:

- apply one consistent rule across the batch;
- avoid mixing schema normalization, content rewriting, and ontology redesign in one pass unless explicitly requested;
- keep a record of what was changed conceptually, especially when touching relations;
- validate after the whole batch, not only per node.

## Validation Checklist

After any edit, verify:

- the edited JSON is still valid;
- the intended top-level key exists or was removed as requested;
- each edited node still uses the four standard fields unless the task explicitly preserves a legacy exception;
- `define` is a string;
- `parents` is an object;
- `children` is an object;
- `properties` is an array;
- each `properties` item is a string;
- no unintended relation entries were dropped;
- no broken references were introduced by the edit you made;
- Markdown and LaTeX survived unchanged except where the task required content edits.

## Operational Reminder

The purpose of this file is to help the agent edit safely without rediscovering local conventions each time. Favor minimal, typed, source-preserving edits and treat relation synchronization as a local decision, not as an assumed global invariant.
