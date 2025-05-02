# Topological Space

[TOC]

## Define

$$
(S, \tau)
$$

A **Topological space** is a pair $(S, \tau)$,  where $S$ is a set and $\tau$ is a **topology** on $S$. A topology $\tau$ is a collection of subsets of a set $S$ (a subset of [power set](./Power_Set.md) $P(S)$) that satisfies the following axioms.

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

### Open Set

The elements of $\tau$ are called **open sets** in the topological space $(S,\tau)$, and the selection of open sets determines the topological structure of the space.

## Properties

### Continuity

A function $f: X\rightarrow Y$ between two topological spaces $(X, \tau_X)$ and $(Y, \tau_Y)$ is said to be continuous if the pre-image of every open set in $Y$ is an open set in $X$.
$$
f^{- 1}(U)\in\tau_X \quad (\forall U\subseteq \tau_Y)
$$

- $f^{-1}(U)=\{x\in X:f(x)\in U\}$ represents the pre-image of the set $U\subseteq \tau_Y$ under the function $f$.

### Homeomorphism

A function $f: X \to Y$ between two topological spaces is a homeomorphism if it has the following properties,
- $f$ is a bijection 
- $f$ is continuous
- the inverse function $f^{-1}$ is continuous ($f$ is an open mapping).

### Chart & Atlas

**Chart** $(U, \phi)$ on a set is a bijection $\phi: U \subseteq M \to \phi(U) \subseteq \mathbb R^n$, where $U, \phi(U)$ is open. A chart $(U, \phi)$ is centered at $p$ for $p \in U$ if $\phi(p) = 0$.

**Atlas** is a set of charts $\{(U_i, \phi_i)\}$, that collectively cover a manifold $M$.
$$
\{(U_i, \phi_i)\}
$$

### Borel $\sigma$-algebra 

### Genus
Genus of a non-empty connected surface is defined as the maximum number of non-intersecting simple closed curves that can be drawn on the surface without dividing it into two disconnected pieces. The genus is a topological invariant that characterizes its "number of holes". 

Genus $g$ can be defined in terms of the Euler characteristic $\chi$, where $b$ is the number of boundary components.

$$
g = \frac{2 - \chi - b}{2}  \tag{Genus}
$$

### Euler Characteristic
 Euler Characteristic is a topological invariant and defined as an alternating sum of the ranks of the homology groups of the space.

In a polyhedra, the Euler characteristic was classically defined for surfaces of polyhedra with the numbers of vertices $V$ (corners), edges $E$ and faces $F$. Any convex polyhedron's surface has Euler characteristic $\chi = 2$.
$$
\chi = V - E + F  \tag{Euler Characteristic}
$$



### Closed Set

Closed Set is the complementary set of Open Set. A set can be both closed and open at the same time.

### Compact

A topological space $X$ is compact if every open cover of $X$ has a finite subcover.

- Open cover: A collection of open sets $\{U_\alpha\}$ such that $X \subseteq \bigcup\limits_\alpha U_\alpha$.
- Finite subcover: A finite subset $\{U_1, U_2, \cdots, U_n\}$ of the open cover that still satisfies $X \subseteq \bigcup\limits_{i=1}^n U_i$

## Include

- [Hausdorff_Space](./Hausdorff_Space.md): 

- [Metric_Space](./Metric_Space.md): 

## Parents

- [Power_Set](./Power_Set.md): 

