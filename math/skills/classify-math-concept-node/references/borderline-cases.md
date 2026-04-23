# Borderline Cases

Use this file when the candidate concept is specialized, policy-sensitive, or ambiguous.

## Navigation

- Return to [../SKILL.md](../SKILL.md) for the main workflow and output schema.
- Read [ontology-rules.md](ontology-rules.md) for the full category definitions and merge rules.
- Read [examples.md](examples.md) when you want worked precedents for a similar concept.

## Contents

- `STRICT` vs `PERMISSIVE`
- Borderline concept defaults
- Batch consistency rules

## Strictness Policy

This skill supports two policy levels. Default to `STRICT` unless explicitly told otherwise.

### STRICT

Core object classes should become nodes by default.

For specialized object classes, use a more tolerant default than before.

Create a node under `STRICT` when the specialized object class is:

- mathematically classical
- frequently used across standard texts, courses, or research discussions
- a stable subject of its own local theory

Merge specialized object classes upward under `STRICT` when they are essentially:

- a more basic object plus extra structure
- a more basic object plus a property
- niche, rarely used, or mostly meaningful through the parent object

Typical `STRICT` create-node cases:

- `Banach space`
- `Hilbert space`
- `Lie group`
- `probability space`
- `Riemannian manifold`

Typical `STRICT` merges:

- a repository-specific niche subclass -> its nearest parent object

Use `STRICT` when ontology compression and consistency are more important than disciplinary convenience.

### PERMISSIVE

Allow specialized object classes to become nodes by default if they function as stable central discourse subjects in mathematical practice.

Examples that may become nodes under `PERMISSIVE`:

- `Banach space`
- `Hilbert space`
- `probability space`
- `Lie group`
- `Riemannian manifold`

Use `PERMISSIVE` only if the repository explicitly allows specialized object classes as nodes.

If policy is unspecified, use `STRICT`.

## Borderline Guidance

### Topology, Metric, Norm, Inner Product, Measure

Even though these can be treated as objects in some mathematical contexts, classify them here as `structure_on_object`.

Default decisions:

- topology -> merge into `topological space`
- metric -> merge into `metric space`
- norm -> merge into `normed space`
- inner product -> merge into `inner product space`
- measure -> merge into `measure space` or the repository-specific parent target

### Subgroup, Quotient Group, Dual Space, Tensor Product, Tangent Space

These are objects in ordinary mathematics, but classify them here as `stable_object_construction`.

Default decisions:

- subgroup -> merge into `group`
- quotient group -> merge into `group`
- dual space -> merge into `vector space`
- tensor product -> merge into `vector space`
- tangent space -> merge into `manifold`

### Banach Space, Hilbert Space, Riemannian Manifold, Probability Space

Classify these as `specialized_object_class`, not `structure_on_object`.

Under `STRICT`, create a node when they are classical or frequently used enough to support independent discussion.

Under `PERMISSIVE`, they should usually become nodes.

Practical defaults:

- `Banach space` -> usually create node
- `Hilbert space` -> usually create node

If the repository has no explicit override, choose `STRICT`, but apply the tolerant rule above for classical or frequently used specialized object classes.

## Batch Consistency Rules

When classifying many concepts at once:

1. Normalize terms first.
2. Apply the decision procedure independently to each candidate.
3. Enforce consistency across sibling concepts.
4. Prefer fewer nodes when classification is ambiguous.
5. Always specify merge targets for rejected node candidates whenever they are object-adjacent concepts.

Consistency anchors:

- If `metric` is merged into `metric space`, do not later create a standalone `metric` node.
- If `STRICT` creates `Banach space` and `Hilbert space` as nodes because they are classical discourse subjects, do not later merge them upward without a policy change.
