# Power Set

[TOC]

## Define

$$
P(S) = \{X \ |\ X \subseteq S\}  \tag{Power Set}
$$
The power set of a set $S$ is the set of all subsets of $S$, including $\emptyset$ and $S$ itself.

<img src="./assets/Hasse_diagram_of_powerset_of_3.svg" alt="Hasse_diagram_of_powerset_of_3" style="zoom: 40%;" />

## Properties

- The number of elements in the power set of a set $S$ is $2^n$, where $n$ is the number of elements in the set $S$.
  $$
  |P(S)| = 2^{|S|}
  $$


### Combination

- Define
  $$
  f_\text{Combination}(S, k) = \{ X \ |\ X \subseteq S , |X| = k\}  \tag{Combination}
  $$
  A combination is the selection of $k$ elements from a set of $n$ elements without regard to order.

  The number of combinations is
  $$
  C(n, k) = |f_\text{Combination}(S, k)| = \frac{n!}{(n - k)! k!}  \tag{number of combinations}
  $$

- Property    
  - $C(n,r) = C(n-1,r-1) + C(n-1,r)$
  - $C(n,r) = C(n,n-r)$
  - The union of all combinations of a set $S$ is the power set $P(S)$ of the set $S$.
    $$
    \bigcup_{k=0}^n f_\text{Combination}(S, k) = P(S)
    $$
    $$
    \begin{align*}
      \sum_{i=0}^n C(n,i) &= 2^n  \\
      \sum_{i=0}^n C(n,i)^2 &= C(2n, n)  \\
      \sum_{i=0}^n C(k+i,k)^2 &= C(n+k+1, k+1) 
    \end{align*}
    $$

## Include

- [Measurable_Space](./Measurable_Space.md): defined_on

- [Sigma_Algebra](./Sigma_Algebra.md): subtype_of

- [Topological_Space](./Topological_Space.md): defined_on

## Parents

- [Set](./Set.md): subtype_of

