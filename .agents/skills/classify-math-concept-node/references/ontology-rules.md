# Ontology Rules

Use this file when the main skill procedure is not enough and you need the full rule inventory.

## Navigation

- Return to [../SKILL.md](../SKILL.md) for the main workflow and output schema.
- Read [borderline-cases.md](borderline-cases.md) when the concept is policy-sensitive or specialized.
- Read [examples.md](examples.md) when you want a precedent before deciding.

## Contents

- Normative definitions
- Node and non-node categories
- Merge and storage rules
- Minimal checklist

## Normative Definitions

### 1. Object

A concept `C` counts as an `object` only if all of the following conditions are satisfied.

#### O1. Variable-bearing capacity

`C` can naturally serve as the value-type of a quantified variable in ordinary mathematical language.

Valid examples:

- `Let G be a group.`
- `Let X be a topological space.`
- `Given a vector space V`

Invalid examples:

- `Let X be a compactness.`
- `Let T be a spectral theorem.`
- `Let M be a diagonal argument.`

If the phrase does not naturally support this usage, it is not an object.

#### O2. Instance plurality

`C` has multiple nontrivial instances.

You should be able to ask:

- What are examples of `C`?
- Are these two instances of `C` equal?
- Are these two instances of `C` isomorphic or equivalent?

If `C` is merely a proposition, an attribute, or a procedure, it fails this condition.

#### O3. Standard comparability

Instances of `C` admit at least one standard mathematical comparison relation, such as:

- equality
- isomorphism, equivalence, or homeomorphism
- inclusion or subobjecthood
- existence of morphisms

If instances cannot be compared in any standard object-level way, `C` is not an object for this ontology.

#### O4. Persistent subjecthood

`C` can serve as a stable subject of mathematical discourse.

That means one can naturally organize a local theory around:

- examples of `C`
- morphisms between instances of `C`
- subobjects of `C`
- properties of instances of `C`
- theorems about instances of `C`
- classification questions for instances of `C`

If `C` appears only as a modifier, criterion, or theorem label, it fails this condition.

### 2. Core Object

A concept `C` counts as a `core object` only if:

1. `C` is already an object under `O1-O4`.
2. `C` is not merely additional structure placed on a more basic object.
3. `C` is not merely the result of a standard construction applied to another object.
4. `C` functions as a central subject of a local mathematical theory.

Only core objects may become nodes under the base rule.

### 3. Specialized Object Class

A concept `C` counts as a `specialized object class` if:

1. `C` is already an object under `O1-O4`.
2. `C` is narrower than a more general parent object class.
3. `C` is not merely extra attached structure and not merely a standard construction from another object.
4. `C` may function as an independent discourse subject in mathematical practice even though it sits below a parent object class.

Typical signals:

- `Banach space` inside `normed space`
- `Hilbert space` inside `inner product space`
- `Riemannian manifold` inside `manifold`
- `probability space` inside `measure space`

Classification rule:

- Do not classify these as `structure_on_object` unless the term really names the attached structure itself.
- If the specialized object class is mathematically classical, frequently used, or supports a stable local theory, it may receive its own node.
- Otherwise, merge it upward into the nearest appropriate parent object under a stricter ontology.

### 4. Structure on an Object

A concept `C` is a `structure on an object` if its meaning is fundamentally of the form:

- a structure on some underlying object
- extra data attached to some underlying object
- additional axioms imposed on some underlying object

Typical signals:

- `a topology on a set`
- `a metric on a set`
- `an inner product on a vector space`
- `a measure on a measurable space`
- `a Riemannian metric on a manifold`

Structures on objects are not standalone nodes. Merge them into the appropriate parent object node.

### 5. Stable Object Construction

A concept `C` is a `stable object construction` if its meaning is fundamentally of the form:

- a subobject of an object
- a quotient of an object
- a product of objects
- a dual of an object
- a tensor product of objects
- a completion of an object
- an invariant object extracted from an object

Typical signals:

- subgroup
- quotient group
- dual space
- tensor product
- tangent space
- fundamental group
- homology group
- completion

Stable object constructions are not standalone nodes. Merge them into the appropriate source core object node.

## What Counts as a Node

A concept may be a node if it is either:

- a core object class, or
- a specialized object class that is mathematically classical, frequently used, or treated as a stable central discourse subject

Typical positive examples:

- set
- function
- sequence
- matrix
- polynomial
- graph
- group
- ring
- field
- module
- vector space
- topological space
- metric space
- normed space
- inner product space
- manifold
- category

For specialized object classes such as `Banach space`, `Hilbert space`, `probability space`, and `Riemannian manifold`, consult [borderline-cases.md](borderline-cases.md).

## What Must Never Be a Node

The following classes must never become standalone nodes.

### Properties

Examples:

- compactness
- connectedness
- completeness
- separability
- Hausdorffness
- local compactness
- abelianness
- Noetherianity
- measurability
- boundedness
- smoothness
- closedness
- density

Disposition:

- `DO_NOT_CREATE_NODE__NON_OBJECT_INFORMATION`

Store under:

- `Properties`
- `Equivalent characterizations`
- `Examples and counterexamples`

### Relations

Examples:

- isomorphism
- homeomorphism
- equivalence
- embedding
- conjugacy
- orthogonality
- independence
- quotient map
- covering map

Disposition:

- `DO_NOT_CREATE_NODE__NON_OBJECT_INFORMATION`

Store under:

- `Morphisms and relations`
- `Equivalence notions`

### Theorems, Propositions, Lemmas, Criteria

Examples:

- Heine-Borel theorem
- Hahn-Banach theorem
- Sylow theorems
- spectral theorem
- Fubini theorem
- Riesz representation theorem

Disposition:

- `DO_NOT_CREATE_NODE__NON_OBJECT_INFORMATION`

Store under:

- `Main theorems`
- `Standard results`
- `Characterization theorems`

### Methods and Techniques

Examples:

- diagonal argument
- induction
- proof by contradiction
- compactness method
- variational method
- generating function method
- probabilistic method

Disposition:

- `DO_NOT_CREATE_NODE__NON_OBJECT_INFORMATION`

Store under:

- `Methods used with this object`
- `Proof patterns`

### Procedures and Operations

Examples:

- completion
- localization
- diagonalization
- taking closures
- taking quotients
- dualization
- tensoring
- taking limits

Disposition:

- `DO_NOT_CREATE_NODE__NON_OBJECT_INFORMATION`

Store under:

- `Standard constructions`
- `Derived objects`

### Representations and Invariants

Examples:

- coordinate representation
- matrix representation
- dimension
- determinant
- trace
- genus
- Euler characteristic
- spectrum when treated as an invariant

Disposition:

- `DO_NOT_CREATE_NODE__NON_OBJECT_INFORMATION`

Store under:

- `Invariants`
- `Representations`
- `Derived data`

### Structures on Objects

Examples:

- topology
- metric
- norm
- inner product
- measure
- differentiable structure
- Riemannian metric
- symplectic structure
- complex structure

Disposition:

- `DO_NOT_CREATE_NODE__MERGE_INTO_<PARENT_OBJECT>`

Typical merges:

- topology -> `topological space`
- metric -> `metric space`
- norm -> `normed space`
- inner product -> `inner product space`
- measure -> `measure space` or the repository-specific parent target
- differentiable structure -> `manifold`
- Riemannian metric -> `Riemannian manifold` or `manifold` under a stricter policy

### Stable Object Constructions

Examples:

- subgroup
- normal subgroup
- quotient group
- direct product group
- subspace
- quotient space
- dual space
- tensor product
- tangent space
- cotangent space
- fundamental group
- homology group
- covering space
- completion

Disposition:

- `DO_NOT_CREATE_NODE__MERGE_INTO_<SOURCE_OBJECT>`

Typical merges:

- subgroup -> `group`
- quotient group -> `group`
- dual space -> `vector space`
- tensor product -> `vector space`
- tangent space -> `manifold`
- fundamental group -> `topological space`
- homology group -> `topological space` or the repository-specific parent target
- completion -> `metric space` or `normed space`

## Merge Rules

If a concept is rejected as a node, it must still be placed somewhere.

Use the following storage targets:

- property -> `Properties`, `Equivalent characterizations`, `Examples and counterexamples`
- relation -> `Morphisms and relations`, `Equivalence notions`
- theorem -> `Main theorems`, `Standard results`, `Characterization theorems`
- method -> `Methods used with this object`, `Proof patterns`
- procedure or construction -> `Standard constructions`, `Derived objects`
- structure on object -> `Defining data`, `Structures carried by this object`, `Alternative structures`
- stable object construction -> `Standard constructions`, `Derived objects`, `Canonical associated objects`

## Minimal Checklist

Before creating a node, verify all of the following:

- The concept is an object under `O1-O4`.
- The concept is not a property.
- The concept is not a relation.
- The concept is not a theorem.
- The concept is not a method.
- The concept is not a procedure.
- The concept is not a representation or invariant.
- The concept is not structure on a more basic object.
- The concept is not a stable object construction.
- The concept is a core object or an allowed specialized object class under the current policy.
