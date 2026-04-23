# Examples

Use these examples as precedents when the quick anchors in the main skill are not enough.

## Navigation

- Return to [../SKILL.md](../SKILL.md) for the main workflow and output schema.
- Read [ontology-rules.md](ontology-rules.md) for the full definitions behind each example.
- Read [borderline-cases.md](borderline-cases.md) when the example depends on policy.

## Contents

- Positive examples
- Negative examples
- Policy-sensitive examples

## Positive Examples

### Example 1: `group`

```text
candidate: group
policy: STRICT
decision: CREATE_NODE
classification: core_object
reasoning:
  - It satisfies object criteria O1-O4.
  - It is not merely extra structure on another repository-level parent object under the default ontology.
  - It is not a standard construction derived from another object.
  - It serves as a central subject of a stable local theory.
merge_target: null
storage_location:
  - main node
confidence: high
```

### Example 2: `topological space`

```text
candidate: topological space
policy: STRICT
decision: CREATE_NODE
classification: core_object
reasoning:
  - It satisfies object criteria O1-O4.
  - Under this ontology, the space is the node, while the topology itself is merged into it.
  - It is a central subject of a stable local theory.
merge_target: null
storage_location:
  - main node
confidence: high
```

### Example 3: `vector space`

```text
candidate: vector space
policy: STRICT
decision: CREATE_NODE
classification: core_object
reasoning:
  - It satisfies object criteria O1-O4.
  - It is a central object class with morphisms, subobjects, quotients, properties, and standard constructions.
merge_target: null
storage_location:
  - main node
confidence: high
```

## Negative Examples

### Example 4: `compactness`

```text
candidate: compactness
policy: STRICT
decision: DO_NOT_CREATE_NODE__NON_OBJECT_INFORMATION
classification: property
reasoning:
  - Compactness is a property of objects such as topological spaces or metric spaces.
  - It does not satisfy the object criterion in the ontology.
merge_target: null
storage_location:
  - properties section inside topological space or metric space
confidence: high
```

### Example 5: `spectral theorem`

```text
candidate: spectral theorem
policy: STRICT
decision: DO_NOT_CREATE_NODE__NON_OBJECT_INFORMATION
classification: theorem
reasoning:
  - It is a theorem, not an object class.
merge_target: null
storage_location:
  - main theorems section inside the relevant operator, inner product space, or Hilbert space parent node
confidence: high
```

### Example 6: `topology`

```text
candidate: topology
policy: STRICT
decision: DO_NOT_CREATE_NODE__MERGE_INTO_TOPOLOGICAL_SPACE
classification: structure_on_object
reasoning:
  - A topology is additional structure placed on an underlying set.
  - Under this ontology, structures on objects are not standalone nodes.
merge_target: topological space
storage_location:
  - defining data
  - structures carried by this object
confidence: high
```

### Example 7: `dual space`

```text
candidate: dual space
policy: STRICT
decision: DO_NOT_CREATE_NODE__MERGE_INTO_VECTOR_SPACE
classification: stable_object_construction
reasoning:
  - A dual space is a standard construction from a vector space.
  - It is not treated as an independent node under this ontology.
merge_target: vector space
storage_location:
  - standard constructions
  - derived objects
confidence: high
```

### Example 8: `Banach space` under `STRICT`

```text
candidate: Banach space
policy: STRICT
decision: DO_NOT_CREATE_NODE__MERGE_INTO_NORMED_SPACE
classification: structure_on_object
reasoning:
  - A Banach space is treated here as a normed space with additional completeness requirements.
  - Under STRICT policy, specialized object classes are merged upward.
merge_target: normed space
storage_location:
  - special subclasses
  - important object families
confidence: medium
```

### Example 9: `Banach space` under `PERMISSIVE`

```text
candidate: Banach space
policy: PERMISSIVE
decision: CREATE_NODE
classification: core_object
reasoning:
  - In mathematical practice, Banach spaces often function as a stable central discourse subject.
  - PERMISSIVE policy allows specialized object classes as nodes.
merge_target: null
storage_location:
  - main node
confidence: medium
```
