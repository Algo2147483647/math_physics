# Topological Space

[TOC]

## Define

$$
(S, \tau)
$$

A **Topological space** is a pair $(S, \tau)$,  where $S$ is a set and $\tau$ is a **topology** on $S$. A topology $\tau$ is a collection of subsets of a set $S$ (so $\tau$ is a subset of [power set](./Power_Set.md) $P(S)$) that satisfies the following axioms. The elements of $\tau$ are called **open sets** of the topological space, and the selection of open sets determines the topological structure on $S$. Thus, a topological space fundamentally defines which subsets of $S$ are considered open.

(*Topological Space is a space in which open sets are defined.*)

- The empty set and the whole set $S$ itself belong to $\tau$.
$$
\{\emptyset, S\} \subseteq \tau
$$

- The intersection of any finite members of $\tau$ belongs to $\tau$. If $U_{1},U_{2},\cdots,U_{n}$ are sets in $\tau$, then 
$$
\bigcap_{i = 1}^{n}U_{i}\in\tau
$$

- Any arbitrary (finite or infinite) union of members of $\tau$ belongs to $\tau$. If $\{U_{\alpha}\}_{\alpha\in I}$ is an arbitrary collection of sets in $\tau$, where $I$ is an index set, then 
$$
\bigcup_{\alpha\in I}U_{\alpha}\in\tau
$$

```
import Set
import CompleteBooleanAlgebra

class TopologicalSpace (X : Type u) where
  IsOpen : Set X → Prop
  
  isOpen_univ : IsOpen univ
  isOpen_inter : ∀ s t, IsOpen s → IsOpen t → IsOpen (s ∩ t)
  isOpen_sUnion : ∀ s, (∀ t ∈ s, IsOpen t) → IsOpen (⋃₀ s)
```

## Properties

### Closed Set

Closed Set is the complementary set of Open Set. A set can be both closed and open at the same time.

### Compact

A topological space $X$ is compact if every open cover of $X$ has a finite subcover.

- Open cover: A collection of open sets $\{U_\alpha\}$ such that $X \subseteq \bigcup\limits_\alpha U_\alpha$.
- Finite subcover: A finite subset $\{U_1, U_2, \cdots, U_n\}$ of the open cover that still satisfies $X \subseteq \bigcup\limits_{i=1}^n U_i$



Properties:

- Compact space is is still a compact space under a continuous mapping.

### Borel $\sigma$-algebra 

### Genus
Genus of a non-empty connected surface is defined as the maximum number of non-intersecting simple closed curves that can be drawn on the surface without dividing it into two disconnected pieces. The genus is a topological invariant that characterizes its "number of holes". 

Genus $g$ can be defined in terms of the Euler characteristic $\chi$, where $b$ is the number of boundary components.

$$
g = \frac{2 - \chi - b}{2}  \tag{Genus}
$$

### Euler Characteristic

$$
\chi = V - E + F  \tag{Euler Characteristic}
$$

Euler Characteristic is a topological invariant and defined as an alternating sum of the ranks of the homology groups of the space.

Euler Characteristic of sphere, in a polyhedra, the Euler characteristic was classically defined for surfaces of polyhedra with the numbers of vertices $V$ (corners), edges $E$ and faces $F$. Any convex polyhedron's surface has Euler characteristic $\chi = 2$.

### Relationship between multiple topological spaces

#### Continuity

A function $f: X\rightarrow Y$ between two topological spaces $(X, \tau_X)$ and $(Y, \tau_Y)$ is said to be continuous if the pre-image of every open set in $Y$ is an open set in $X$.

(*The pre-image of an open set retains its openness.*)
$$
f^{- 1}(U)\in\tau_X \quad (\forall U\subseteq \tau_Y)
$$

- $f^{-1}(U)=\{x\in X:f(x)\in U\}$ represents the pre-image of the set $U\subseteq \tau_Y$ under the function $f$.

#### Homeomorphism

A function $f: X \to Y$ between two topological spaces is a homeomorphism if it has the following properties,
- $f$ is a bijection 
- $f$ is continuous
- the inverse function $f^{-1}$ is continuous ($f$ is an open mapping).

## Include

- [Hausdorff_Space](./Hausdorff_Space.md): is-a

- [Metric_Space](./Metric_Space.md): is-a

## Parents

- [Power_Set](./Power_Set.md): 

