# Power Set

[TOC]

## Define

$$
P(S) = \{X \ |\ X \subseteq S\}  \tag{Power Set}
$$
The Power Set of a set $S$ is the set of all subset of $S$, including $\emptyset$ and $S$ itself.

<img src="./assets/Hasse_diagram_of_powerset_of_3.svg" alt="Hasse_diagram_of_powerset_of_3" style="zoom: 40%;" />

## Properties

- The number of elements in the power set of a set $S$ is $2^n$, where $n$ is the number of elements in the set $S$.
  $$
  |P(S)| = 2^{|S|}
  $$


### Combination

- Define
  $$
  f_\text{Conbination}(S, k) = \{ X \ |\ X \subseteq S , |X| = k\}  \tag{Conbination}
  $$
  Combination, is the selection of $k$ elements from a set of $n$ elements without any regard to the order in which they are chosen.

  The number of Combination $C(n, r)$,
  $$
  C(n, r) = |f_\text{Conbination}(S, k)| = \frac{n!}{(n - m)! m!}  \tag{number of Conbination}
  $$

- Property    
  - $C(n,r) = C(n-1,r-1) + C(n-1,r)$
  - $C(n,r) = C(n,n-r)$
  - The union of all Combination of a set $S$ is the power set $P(S)$ of the set $S$.
    $$
    \bigcup_{k=0}^n f_\text{Conbination}(S, k) = P(S)
    $$
    $$
    \begin{align*}
      \sum_{i=0}^n C(n,i) &= 2^n  \\
      \sum_{i=0}^n C(n,i)^2 &= C(2n, n)  \\
      \sum_{i=0}^n C(k+i,k)^2 &= C(n+k+1, k+1) 
    \end{align*}
    $$

## Include

- [Measurable_Space](./Measurable_Space.md): 

- [Sigma_Algebra](./Sigma_Algebra.md): 

- [Topological_Space](./Topological_Space.md): 

## Parents

- [Set](./Set.md): 

