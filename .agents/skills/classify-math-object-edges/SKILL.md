---
name: classify-math-object-edges
description: Decide whether an edge between two already-approved mathematical object nodes should appear in a strict object-centered knowledge graph, and assign the retained edge type or reject the edge. Use when reviewing a math ontology DAG, classifying proposed edges, removing redundant shortcuts, or enforcing policies such as is_a, defined_over, modeled_on, and requires_object.
---

# Skill: Classify Math Object Edges

## Purpose

This skill defines how an agent must decide whether an edge should exist between two already-approved object nodes in a strict, object-centered mathematical knowledge graph.

It assumes the following upstream node policy is already in force:

1. Nodes represent **core mathematical object classes only**.
2. **Structures on objects** are not standalone nodes and must be merged into their owning core object node.
3. **Stable object constructions** are not standalone nodes and must be merged into their owning core object node.
4. The main graph is a **minimal structural DAG**, not a theorem dependency graph, learning path graph, history graph, or analogy graph.

Under this policy, the graph should preserve only the smallest set of edge types needed to express the backbone of the object system.

---

## Scope

This skill applies only to:

- deciding whether an edge should exist between two candidate nodes that are already valid under the node policy;
- choosing the correct retained edge type;
- rejecting unnecessary, ambiguous, or redundant edges;
- keeping the DAG sparse, readable, and semantically stable.

This skill does **not** apply to:

- theorem dependencies;
- proof methods;
- properties;
- analogies;
- historical influence;
- applications;
- pedagogical prerequisites;
- internal subsections within a node.

---

## Core Principle

An edge should exist **only if** it expresses a stable, object-level structural relation that is:

1. **semantically necessary**,
2. **direct**,
3. **non-redundant**, and
4. **allowed by the retained edge type policy**.

Default posture:

> **Do not add an edge unless the policy clearly justifies it.**

---

## Retained Edge Types

Only the following edge types may be used in the main DAG.

### 1. `is_a`

**Meaning**

`A is_a B` means that `A` is a specialization of `B` as an object class.

**Interpretation**

Every instance of `A` is naturally an instance of `B`, without projecting away part of the object or changing semantic role.

**Typical use**

- type refinement
- parent-child object hierarchy
- nearest valid superclass relation

**Examples**

- `field -> ring`
- `Banach space -> normed space`
- `Hilbert space -> inner product space`
- `Lie group -> manifold`

**Non-examples**

- `ring -> group` is not valid as `is_a` if the claim only becomes true by taking the additive part of the ring.
- `topological space -> topology` is not valid because a topological space is not a topology.

---

### 2. `defined_over`

**Meaning**

`A defined_over B` means that the definition of `A` requires `B` as an external core object parameter, scalar source, coefficient source, or foundational dependency, while `A` is not a specialization of `B`.

**Interpretation**

`B` is not the parent type of `A`, but `A` cannot be properly defined without explicitly referring to `B`.

**Typical use**

- scalar field dependencies
- coefficient ring dependencies
- external parameter object dependencies

**Examples**

- `vector space -> field`
- `module -> ring`
- `algebra -> field`
- `representation -> group` if `representation` is retained as a node in a broader policy

**Non-examples**

- do not use `defined_over` for internal technical ingredients such as maps, operations, axioms, or clauses that are not themselves retained core object nodes;
- do not use `defined_over` if the relation is already better expressed by `is_a`.

---

### 3. `modeled_on`

**Meaning**

`A modeled_on B` means that `B` is the standard local model or prototype object for `A`, and this modeling relation is part of the identity of `A`.

**Interpretation**

This is stronger than a generic dependency and weaker than subtype inclusion. It should be used only when "being locally like `B`" or "being built from `B` as a standard model" is central to the object definition.

**Typical use**

- geometric objects with local models
- prototype-based object semantics

**Examples**

- `manifold -> Euclidean space`
- `affine space -> vector space`

**Non-examples**

- do not use it as a generic substitute for `defined_over`;
- do not use it when the relation is merely helpful intuition rather than part of the formal object identity.

**Status**

This type is **conditionally retained**. It should be enabled only when the graph includes geometric or locally modeled object families where this distinction adds real structural value.

---

### 4. `requires_object`

**Meaning**

`A requires_object B` means that the standard theory of `A` stably depends on `B` as an object class, but the relation is neither subtype inclusion, nor explicit definitional parameterization, nor local modeling.

**Interpretation**

This is a last-resort edge type for object-level structural dependency that cannot be expressed by the other retained types.

**Typical use**

Very limited. Only for rare cases where a genuine object-level backbone dependency exists but does not fit `is_a`, `defined_over`, or `modeled_on`.

**Examples**

- `measure space -> measurable space` if both are retained under a broader object policy
- `scheme -> ring` in a broader algebraic geometry policy, depending on repository conventions

**Non-examples**

- do not use for "often studied together";
- do not use for theorem dependence;
- do not use for pedagogical sequencing;
- do not use as a catch-all for uncertainty.

**Status**

This type is **disabled by default**. It is allowed only under an explicitly expanded policy.

---

## Recommended Default Policy

For a strict and readable main DAG, the default retained set should be:

- `is_a`
- `defined_over`

The following are optional or disabled:

- `modeled_on`: optional, enabled only when locally modeled geometric objects are important to the graph
- `requires_object`: disabled by default

### Recommended modes

#### STRICT_MINIMAL
Allowed edge types:
- `is_a`

Use when the graph should behave like a pure object hierarchy.

#### STRICT_DEFAULT
Allowed edge types:
- `is_a`
- `defined_over`

Use when the graph should capture both hierarchy and essential external definitional dependencies.

#### STRICT_GEOMETRIC
Allowed edge types:
- `is_a`
- `defined_over`
- `modeled_on`

Use when geometric objects with local models are central.

#### EXPANDED_EXPERT
Allowed edge types:
- `is_a`
- `defined_over`
- `modeled_on`
- `requires_object`

Use only when the repository explicitly accepts a denser, expert-level object graph.

---

## Edge Acceptance Criteria

An edge `A -> B` may be added to the main DAG only if all of the following are true:

1. `A` and `B` are already valid retained object nodes.
2. The relation between `A` and `B` is object-level, stable, and mathematically standard.
3. The relation fits one of the allowed retained edge types in the current policy mode.
4. The edge is direct rather than better expressed through an intermediate node.
5. The edge is not redundant under the transitive structure already present.
6. The edge improves the global skeleton of the graph rather than merely adding detail.

If any of these fail, the edge must be rejected.

---

## Edge Typing Decision Procedure

For any ordered pair of retained object nodes `A`, `B`, the agent must apply the following decision procedure in order.

### Step 1. Test `is_a`

Ask:

1. Is every instance of `A` naturally an instance of `B`?
2. Does `A` differ from `B` only by extra conditions, extra axioms, or stronger restrictions?
3. Is this true without projecting to only part of the structure of `A`?
4. Is `B` one of the nearest valid parent object classes of `A`?

If all answers are yes, assign:

- `edge_type = is_a`

Then stop.

---

### Step 2. Test `defined_over`

Ask:

1. Is `A` not a subtype of `B`?
2. Does the definition of `A` explicitly require `B` as an external object parameter, scalar source, coefficient source, or equivalent foundational object?
3. Is `B` a retained core object rather than an internal technical ingredient?
4. Would removing this relation materially obscure where the definition of `A` comes from?

If all answers are yes, assign:

- `edge_type = defined_over`

Then stop.

---

### Step 3. Test `modeled_on` if enabled

Ask:

1. Is the identity of `A` formally based on being locally like `B` or built from `B` as a standard model?
2. Is this modeling relation stronger than a generic definitional dependency?
3. Is the relation a standard mathematical description of the object class, not merely pedagogical intuition?

If all answers are yes, assign:

- `edge_type = modeled_on`

Then stop.

---

### Step 4. Test `requires_object` only if explicitly enabled

Ask:

1. Is there a stable object-level dependency from `A` to `B`?
2. Does the relation fail to fit `is_a`, `defined_over`, and `modeled_on`?
3. Is this dependency part of the object-level backbone rather than a theorem dependency or learning dependency?
4. Would omitting the edge meaningfully distort the object graph?

If all answers are yes, assign:

- `edge_type = requires_object`

Then stop.

---

### Step 5. Default rejection

If no retained type fits, the result must be:

- `decision = reject_edge`

The agent must prefer no edge over a weak or overgeneral edge.

---

## Redundancy Control Policy

The graph must remain sparse. Even a semantically correct edge should be rejected if it is graph-theoretically unnecessary or structurally noisy.

### Rule R1. Nearest-parent rule for `is_a`

For `is_a`, connect a node only to its nearest valid parent object class or nearest valid parents when multiple immediate parents are genuinely necessary.

**Keep**
- `Hilbert space -> inner product space`

**Reject as redundant**
- `Hilbert space -> vector space` if `Hilbert space -> inner product space` and `inner product space -> vector space` already exist.

---

### Rule R2. No transitive redundancy

If an edge of the same semantic type is already implied by a shorter path of retained edges, reject the direct edge unless the repository explicitly preserves transitive shortcuts.

Default behavior:

> **Reject transitive shortcuts.**

---

### Rule R3. Core-dependency rule for `defined_over`

Only connect `A` to indispensable external core objects needed to define `A`.

Do not connect to:
- operations,
- functions,
- clauses,
- axioms,
- internal components,
- technical gadgets that are not retained object nodes.

---

### Rule R4. Backbone-only rule

A retained edge must improve the global skeleton of the object graph.

Reject edges that are:
- technically true but graphically unhelpful,
- obvious from node internals,
- too low-level,
- too contextual,
- too repository-specific.

---

### Rule R5. Default non-edge rule

If the relation is plausible but not clearly justified under the retained edge policy, reject it.

---

## Parent-Child Object Rule

When repository users ask for a "parent-child" object relation, the agent should interpret this as:

- a candidate `is_a` edge,
- not a generic dependency,
- not a construction relation,
- not a property relation.

### Valid parent-child examples

- `field -> ring`
- `Banach space -> normed space`
- `Lie group -> manifold`

### Invalid parent-child examples

- `ring -> group` if only the additive structure yields the group
- `topological space -> topology`
- `vector space -> field`
- `manifold -> chart`

Only true object-class specialization counts as parent-child.

---

## References

Use this navigation map to keep context small. Do not read every reference file by default.

- Read [references/canonical-judgments.md](references/canonical-judgments.md) when you need worked examples or precedent for ambiguous edge decisions.
- Read [references/excluded-edge-types.md](references/excluded-edge-types.md) when a proposed edge label falls outside the retained policy or you need guidance on where rejected relations should live.

---

## Required Output Schema

When using this skill, the agent must output the result in the following schema.

```yaml
source_node: <string>
target_node: <string>
policy_mode: <STRICT_MINIMAL | STRICT_DEFAULT | STRICT_GEOMETRIC | EXPANDED_EXPERT>
decision: <add_edge | reject_edge>
edge_type: <is_a | defined_over | modeled_on | requires_object | null>
confidence: <high | medium | low>
reasoning:
  - <short bullet 1>
  - <short bullet 2>
  - <short bullet 3>
redundancy_check:
  transitive_redundancy: <true | false>
  nearest_parent_violation: <true | false>
  low_value_edge: <true | false>
notes: <string or null>
```

### Output requirements

- `edge_type` must be `null` if `decision = reject_edge`.
- `reasoning` must refer to the actual retained policy, not vague intuitions.
- `redundancy_check` must always be present.
- `notes` may be used to indicate "store internally under node content instead of as an edge".

---

## Agent Behavior Requirements

When applying this skill, the agent must:

1. classify only among retained edge types allowed in the current policy mode;
2. reject edges that are semantically plausible but graphically unnecessary;
3. prefer the nearest valid parent over distant ancestors;
4. keep the DAG sparse and interpretable;
5. avoid inventing new edge types;
6. avoid collapsing internal node content into graph edges;
7. state uncertainty when repository conventions affect the decision.

The agent must not:

1. use retained edges as a substitute for internal documentation;
2. add edges only because two objects often appear together;
3. add theorem, proof, historical, pedagogical, or analogy relations to the main DAG;
4. preserve transitive shortcuts by default.

---

## How to Use This Skill

### Standard workflow

Use this skill only after the node policy has already determined that the candidate endpoints are valid retained nodes.

Recommended order:

1. run the `classify-math-object-nodes` skill on candidate concepts;
2. keep only valid retained nodes;
3. apply this edge skill pairwise or to proposed edge lists;
4. store accepted edges in the main DAG;
5. move rejected relations into node internals when appropriate.

---

### Invocation pattern: single edge

Prompt template:

```text
Use the SKILL "Retained Edge Types Policy for an Object-Centered Mathematical Knowledge Graph".
Evaluate whether the edge `Hilbert space -> inner product space` should exist.
Policy mode: STRICT_DEFAULT.
Return the result using the required output schema.
```

---

### Invocation pattern: batch classification

Prompt template:

```text
Use the SKILL "Retained Edge Types Policy for an Object-Centered Mathematical Knowledge Graph".
Classify the following proposed edges under STRICT_DEFAULT:
- field -> ring
- Hilbert space -> vector space
- vector space -> field
- ring -> group
Return one output block per edge using the required output schema.
```

---

### Invocation pattern: repository cleanup

Prompt template:

```text
Use the SKILL "Retained Edge Types Policy for an Object-Centered Mathematical Knowledge Graph".
Review the attached edge list for a strict object-centered repository.
Policy mode: STRICT_DEFAULT.
For each edge, decide whether to keep it, delete it, or move its content into node internals.
Return one result block per edge using the required output schema.
```

---

## Implementation Guidance for Agents

### If you are unsure which policy mode to use

Default to:

- `STRICT_DEFAULT`

unless the repository explicitly says:
- hierarchy only -> use `STRICT_MINIMAL`
- strong geometric local-model semantics -> use `STRICT_GEOMETRIC`
- expert dense graph -> use `EXPANDED_EXPERT`

### If a relation feels true but not graph-worthy

Reject the edge and explain where the information belongs instead.

### If a relation is mathematically true in multiple senses

Prefer the narrowest retained edge type that matches the repository policy.

### If multiple edge types seem possible

Use this priority order:

1. `is_a`
2. `defined_over`
3. `modeled_on`
4. `requires_object`

Never assign more than one retained edge type to the same directed pair in a single pass.

---

## Final Rule

The main DAG should encode the **smallest stable object-level backbone** of the repository.

Therefore:

> Keep only edges that are structurally necessary, semantically precise, and non-redundant under the retained edge policy.

When in doubt:

> Reject the edge.
