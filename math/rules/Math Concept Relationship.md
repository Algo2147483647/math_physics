# Math Object Edges

## Core Principle

An edge should exist **only if** it expresses a stable, object-level structural relation that is:

1. **semantically necessary**,
2. **direct**,
3. **non-redundant**, and
4. **allowed by the retained edge type policy**.

Default posture:

> **Do not add an edge unless the policy clearly justifies it.**

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

## Edge Acceptance Criteria

An edge `A -> B` may be added to the main DAG only if all of the following are true:

1. `A` and `B` are already valid retained object nodes.
2. The relation between `A` and `B` is object-level, stable, and mathematically standard.
3. The relation fits one of the allowed retained edge types in the current policy mode.
4. The edge is direct rather than better expressed through an intermediate node.
5. The edge is not redundant under the transitive structure already present.
6. The edge improves the global skeleton of the graph rather than merely adding detail.

If any of these fail, the edge must be rejected.