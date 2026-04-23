# Excluded Edge Types

Use this file when a proposed edge label falls outside the retained policy and you need to decide whether to reject it or store the information somewhere else.

| Edge type | Why excluded | Where to place instead |
|---|---|---|
| `has_subobject` | Subobjects are not standalone nodes under the node policy. | Inside the owner node under standard constructions. |
| `has_quotient` | Quotient objects are not standalone nodes. | Inside the owner node under standard constructions. |
| `constructs` | Stable constructions are merged into owner nodes. | Inside standard constructions. |
| `has_core_morphism` | Morphisms are not retained object nodes. | Inside the node section for morphisms. |
| `instance_of` | The main DAG is class-level, not instance-level. | In an examples database or examples section. |
| `generalizes` / `specializes` | Too vague and overlapping with `is_a`. | In explanatory notes only. |
| `equivalent_to` | Not naturally DAG-shaped and often symmetric. | In internal notes. |
| `analog_of` | Analogy is not backbone structure. | In an analogy map. |
| `motivates` | Historical or conceptual, not structural. | In motivation or history notes. |
| `applies_to` | Application relation is not object skeleton structure. | In application notes. |
| `contrasts_with` | Contrast is not a structural relation. | In confusion notes. |
| theorem dependency edges | Different graph semantics entirely. | In a theorem dependency graph. |
| learning prerequisite edges | Pedagogical, not structural. | In a learning path graph. |
