---
name: classify-math-concept-node
description: Decide whether a mathematical concept should be a standalone node in a strictly object-centered mathematical knowledge base. Use when normalizing a math ontology, filtering extracted concepts, reviewing a note hierarchy, or deciding whether a term like group, compactness, dual space, or Banach space should be a node, merged into a parent object, or stored as non-object information.
---

# Skill: Determine Whether a Mathematical Concept Should Be a Node

## Purpose

Decide whether a mathematical concept should be represented as a standalone node in a strictly object-centered mathematical knowledge base.

Use this skill to classify candidate concepts consistently under a narrow ontology. Focus on node-boundary decisions rather than mathematical exposition unless a short explanation is required for classification.

## Core Rule

Create a node if and only if the concept is a core mathematical object class under the active policy.

Apply the following defaults:

- Merge structures into their parent object node.
- Merge stable object constructions into their source object node.
- Store properties, relations, theorems, methods, procedures, representations, invariants, and similar non-object information inside object nodes rather than as standalone nodes.

## Policy

Default to `STRICT` unless the repository explicitly allows specialized object classes as nodes.

- Use `STRICT` when ontology compression and consistency matter more than disciplinary convenience.
- Use `PERMISSIVE` only when the repository explicitly allows specialized object classes to become nodes.

When classifying specialized or ambiguous concepts such as `Banach space`, `Hilbert space`, or `Riemannian manifold`, read [references/borderline-cases.md](references/borderline-cases.md).

## Minimal Definitions

Use these working definitions in the main procedure:

- `object`: a concept that can naturally serve as the value of a quantified variable, has multiple instances, admits standard object-level comparisons, and supports stable mathematical discourse
- `core object`: an object class that is not merely extra structure on a more basic object and not merely a standard construction from another object
- `structure on an object`: extra data, axioms, or organizing structure placed on an underlying object
- `stable object construction`: a standard derived object whose meaning depends on a source object
- `non-object information`: properties, relations, theorems, methods, procedures, representations, invariants, and similar content that should live inside object nodes

Read [references/ontology-rules.md](references/ontology-rules.md) for full definitions, category lists, merge rules, and storage guidance.

## Decision Procedure

Follow this procedure in order. Do not skip steps.

### Step 1. Normalize the candidate

Normalize the candidate term before classifying it.

- Singularize where appropriate.
- Remove leading articles.
- Resolve obvious naming variants when the intended concept is clear.

### Step 2. Test whether the candidate is an object

Ask all of the following:

1. Can one naturally say `Let X be a C`?
2. Does `C` have multiple nontrivial instances?
3. Do instances of `C` admit standard comparisons such as equality, isomorphism, inclusion, or morphisms?
4. Can `C` serve as a stable subject of a local mathematical theory?

If any answer is clearly no, classify the concept as non-object information and do not create a node.

### Step 3. Exclude obvious non-object categories

Check whether the candidate is better classified as one of the standard non-object categories.

- property
- relation
- theorem, proposition, lemma, or criterion
- method or technique
- procedure or operation
- representation
- invariant
- problem template

If yes, return non-object information and specify where it should be stored inside the relevant object node.

### Step 4. Test whether the candidate is structure on an object

Ask:

1. Is the concept fundamentally something attached to another object?
2. Is it naturally described as `a C on an X`?
3. Can the same underlying object carry many different choices of `C`?

If yes, do not create a node. Merge it into the appropriate parent object.

### Step 5. Test whether the candidate is a stable object construction

Ask:

1. Is the concept fundamentally constructed from some more basic object?
2. Does it lose its meaning if its source object is unspecified?
3. Is it normally introduced as a standard construction inside the theory of another object?

If yes, do not create a node. Merge it into the appropriate source object.

### Step 6. Apply policy and decide

If the concept:

- passes the object test,
- is not excluded as non-object information,
- is not structure on an object,
- is not a stable object construction,
- and functions as a central local subject,

then create a node.

If the concept is object-like but specialized or policy-sensitive, apply the active policy and consult [references/borderline-cases.md](references/borderline-cases.md) before deciding.

### Step 7. Prefer compression when uncertain

If classification remains ambiguous after the previous steps, prefer the smaller ontology and choose the least fragmenting merge that preserves meaning.

## Required Output

Always return the following schema. The `decision` field must be one of the allowed values.

```text
candidate: <normalized concept>
policy: <STRICT | PERMISSIVE>
decision: <CREATE_NODE | DO_NOT_CREATE_NODE__MERGE_INTO_<TARGET> | DO_NOT_CREATE_NODE__NON_OBJECT_INFORMATION>
classification: <core_object | structure_on_object | stable_object_construction | property | relation | theorem | method | procedure | invariant | representation | other>
reasoning:
  - <brief rule-based justification>
merge_target: <core object name or null>
storage_location:
  - <where the concept should live if it is not a node>
confidence: <high | medium | low>
```

For batch classification:

1. Classify each candidate independently.
2. Keep sibling decisions consistent.
3. Prefer fewer nodes when the ontology is ambiguous.

## Minimal Examples

Use these as quick anchors:

- `group` -> `CREATE_NODE`
- `compactness` -> `DO_NOT_CREATE_NODE__NON_OBJECT_INFORMATION`
- `topology` -> `DO_NOT_CREATE_NODE__MERGE_INTO_TOPOLOGICAL_SPACE`
- `dual space` -> `DO_NOT_CREATE_NODE__MERGE_INTO_VECTOR_SPACE`

Read [references/examples.md](references/examples.md) for a larger example set.

## References

Use this navigation map to keep context small. Do not read every reference file by default.

- Read [references/ontology-rules.md](references/ontology-rules.md) when you need full definitions, category inventories, merge rules, or storage guidance.
- Read [references/borderline-cases.md](references/borderline-cases.md) when the concept is specialized, policy-sensitive, or ambiguous under `STRICT` vs `PERMISSIVE`.
- Read [references/examples.md](references/examples.md) when you want precedent examples for common or edge-case terms.

## One-Sentence Operational Criterion

Create a node only when the concept is a core mathematical object class; merge structures into objects, merge constructions into source objects, and store everything else as non-object information inside object nodes.
