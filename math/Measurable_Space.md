# Measurable Space

[TOC]

## Define

A Measurable Space is a pair $(E, \mathcal E)$, where $E$ is a set and $\mathcal E$ is its [$\sigma$-algebra](./Power_Set.md).

A Measure Space is a pair $(E, \mathcal E, \mu)$, where $E$ is a set and $\mathcal E$ is its $\sigma$-algebra, $\mu$ is a Measure on $(E, \mathcal E)$

### Measurex

A Measure on a measurable space $(E, \mathcal E)$ is a function $\mu: \mathcal E \to [0, \infty)$ such that 

- $\mu (\emptyset) = 0$
- Countable additivity: For any disjoint sequence $(A_1, ..., A_n), A_i \in \mathcal E$, then
$$
\mu \left(\bigcup_i A_i\right) = \sum_i \mu(A_i)
$$

## Properties

- Lebesgue Measure 
  For a measurable subset $E \subseteq \mathbb{R}^n$, $E$ is Lebesgue measurable, if for any $\epsilon > 0$, there exist a finite number of open boxes $Q_1, Q_2, \ldots, Q_m$ and their volumes $\text{vol}(Q_i)$, such that
  $$
  E \subset \bigcup_{i=1}^m Q_i
  $$
  $$
  \sum_{i=1}^m \text{vol}(Q_i) < \text{vol}(E) + \epsilon  \tag{Lebesgue measurable}
  $$

  And Lebesgue measure $\text{m}(E)$ of a measurable subset $E$ is defined as,
  $$
  \text{m}(E) = \inf\left\{\sum_{i=1}^\infty \text{vol}(Q_i) \ \middle|\ E \subset \bigcup_{i=1}^\infty Q_i \right\}  \tag{Lebesgue Measure}
  $$

- Probability

## Include

- [Probability_Space](./Probability_Space.md): is-a

## Parents

- [Power_Set](./Power_Set.md): 

