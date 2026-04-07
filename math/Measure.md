# Measure

[TOC]

## Define

Let $(E, \mathcal E)$ be a [measurable space](./Measurable_Space.md). A measure on $(E, \mathcal E)$ is a function
$$
\mu: \mathcal E \to [0, \infty]
$$
such that

- $\mu(\emptyset) = 0$
- for every pairwise disjoint sequence $(A_n)_{n \ge 1} \subseteq \mathcal E$,
$$
\mu\left(\bigcup_{n=1}^{\infty} A_n\right) = \sum_{n=1}^{\infty} \mu(A_n)
\tag{countable additivity}
$$

## Properties

### Basic Consequences

- Monotonicity:
$$
A \subseteq B \Rightarrow \mu(A) \le \mu(B)
$$

- Countable subadditivity:
$$
\mu\left(\bigcup_{n=1}^{\infty} A_n\right) \le \sum_{n=1}^{\infty} \mu(A_n)
$$

- Continuity from below:
if $A_n \uparrow A$, then
$$
\mu(A_n) \to \mu(A)
$$

- Continuity from above:
if $A_n \downarrow A$ and $\mu(A_1) < \infty$, then
$$
\mu(A_n) \to \mu(A)
$$

### Null Sets and Completeness

A set $N \in \mathcal E$ with $\mu(N) = 0$ is called a null set. Measures distinguish genuine size from negligible sets, and many analytical statements are meaningful only up to null sets.

A measure space is called complete if every subset of every null set is measurable.

### Canonical Examples

- Counting measure:
$$
\mu(A) = \#A
$$
on a countable set.

- Dirac measure at $x_0 \in E$:
$$
\delta_{x_0}(A) =
\begin{cases}
1, & x_0 \in A \\
0, & x_0 \notin A
\end{cases}
$$

- Lebesgue measure on $\mathbb R^n$.

## Include

- [Probability_Measure](./Probability_Measure.md): subtype_of

- [Product_Measure](./Product_Measure.md): subtype_of

## Parents

- [Measurable_Space](./Measurable_Space.md): defined_on
