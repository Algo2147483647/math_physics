# Canonical Judgments

## Contents

- [Example 1: Hilbert space -> inner product space](#example-1-hilbert-space---inner-product-space)
- [Example 2: Hilbert space -> vector space](#example-2-hilbert-space---vector-space)
- [Example 3: vector space -> field](#example-3-vector-space---field)
- [Example 4: ring -> group](#example-4-ring---group)
- [Example 5: manifold -> Euclidean space](#example-5-manifold---euclidean-space)
- [Example 6: topological space -> set](#example-6-topological-space---set)

Use these as precedent examples when the main decision procedure is not enough by itself.

## Example 1: Hilbert space -> inner product space

**Input**: `Hilbert space -> inner product space`

```yaml
source_node: Hilbert space
target_node: inner product space
policy_mode: STRICT_DEFAULT
decision: add_edge
edge_type: is_a
confidence: high
reasoning:
  - Every Hilbert space is naturally an inner product space.
  - The distinction is completeness, which is an extra restriction rather than a change of object role.
  - This is the nearest valid parent object class.
redundancy_check:
  transitive_redundancy: false
  nearest_parent_violation: false
  low_value_edge: false
notes: null
```

## Example 2: Hilbert space -> vector space

**Input**: `Hilbert space -> vector space`

```yaml
source_node: Hilbert space
target_node: vector space
policy_mode: STRICT_DEFAULT
decision: reject_edge
edge_type: null
confidence: high
reasoning:
  - Although every Hilbert space is a vector space, the direct edge skips the nearer parent inner product space.
  - The relation is already captured by transitive structure.
  - Keeping the shortcut would reduce DAG readability.
redundancy_check:
  transitive_redundancy: true
  nearest_parent_violation: true
  low_value_edge: false
notes: null
```

## Example 3: vector space -> field

**Input**: `vector space -> field`

```yaml
source_node: vector space
target_node: field
policy_mode: STRICT_DEFAULT
decision: add_edge
edge_type: defined_over
confidence: high
reasoning:
  - A vector space is not a subtype of field.
  - Its definition explicitly requires a field as scalar source.
  - The field is a retained external core object, not an internal technical ingredient.
redundancy_check:
  transitive_redundancy: false
  nearest_parent_violation: false
  low_value_edge: false
notes: null
```

## Example 4: ring -> group

**Input**: `ring -> group`

```yaml
source_node: ring
target_node: group
policy_mode: STRICT_DEFAULT
decision: reject_edge
edge_type: null
confidence: high
reasoning:
  - The relation only holds after projecting to the additive structure of a ring.
  - The whole ring object is not itself simply a group object in the retained parent-child sense.
  - This does not satisfy the strict `is_a` criterion.
redundancy_check:
  transitive_redundancy: false
  nearest_parent_violation: false
  low_value_edge: false
notes: Store additive-group content inside the ring node rather than as a main DAG edge.
```

## Example 5: manifold -> Euclidean space

**Input**: `manifold -> Euclidean space`

```yaml
source_node: manifold
target_node: Euclidean space
policy_mode: STRICT_GEOMETRIC
decision: add_edge
edge_type: modeled_on
confidence: medium
reasoning:
  - A manifold is locally modeled on Euclidean space.
  - The local-model relation is part of the defining identity of manifolds.
  - This is not subtype inclusion and not merely a scalar-parameter dependency.
redundancy_check:
  transitive_redundancy: false
  nearest_parent_violation: false
  low_value_edge: false
notes: null
```

## Example 6: topological space -> set

**Input**: `topological space -> set`

Possible judgments depend on repository strictness.

Under a very sparse graph:

```yaml
source_node: topological space
target_node: set
policy_mode: STRICT_DEFAULT
decision: reject_edge
edge_type: null
confidence: medium
reasoning:
  - The graph may treat set-level dependence as universal background rather than explicit structure.
  - Keeping only higher-value object relations may improve readability.
  - This edge is definitional but may be too low-level for the retained backbone.
redundancy_check:
  transitive_redundancy: false
  nearest_parent_violation: false
  low_value_edge: true
notes: Keep set-level dependence in node internals if the repository suppresses universal background edges.
```

Under a repository that explicitly preserves foundational object dependencies, the same pair may be accepted as `defined_over`.
