# Measurable Space

[TOC]

## Define

A measurable space is a pair $(E, \mathcal E)$, where $E$ is a set and $\mathcal E$ is a [$\sigma$-algebra](./Sigma_Algebra.md) on $E$.

A measure space is a triple $(E, \mathcal E, \mu)$, where $E$ is a set, $\mathcal E$ is a $\sigma$-algebra on $E$, and $\mu$ is a measure on $(E, \mathcal E)$.

### Measure

A measure on a measurable space $(E, \mathcal E)$ is a function $\mu: \mathcal E \to [0, \infty]$ such that

- $\mu(\emptyset) = 0$
- Countable additivity: for any pairwise disjoint sequence $(A_i)_{i=1}^{\infty}$ with $A_i \in \mathcal E$,
$$
\mu \left(\bigcup_{i=1}^{\infty} A_i\right) = \sum_{i=1}^{\infty} \mu(A_i)
$$

## Properties

### Lebesgue measure  
For a measurable subset $E \subseteq \mathbb{R}^n$, the Lebesgue measure $\mathrm m(E)$ can be defined by
$$
\mathrm m(E) = \inf\left\{\sum_{i=1}^\infty \mathrm{vol}(Q_i) \ \middle|\ E \subseteq \bigcup_{i=1}^\infty Q_i,\ Q_i \text{ are open boxes}\right\}
\tag{Lebesgue Measure}
$$

### Probability

### Product Measure

Let $(X, \mathcal A, \mu)$ and $(Y, \mathcal B, \nu)$ be [measure spaces](./Measure_Space.md). The product measure
$$
\mu \otimes \nu
$$
is the measure on the product measurable space $(X \times Y, \mathcal A \otimes \mathcal B)$ characterized by
$$
(\mu \otimes \nu)(A \times B) = \mu(A)\nu(B)
$$
for measurable rectangles $A \in \mathcal A$, $B \in \mathcal B$.

## Include

- [Probability_Space](./Probability_Space.md): subtype_of

## Parents

- [Power_Set](./Power_Set.md): defined_on
