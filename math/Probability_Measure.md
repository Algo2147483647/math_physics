# Probability Measure

[TOC]

## Define

A probability measure is a [measure](./Measure.md) $\mathbb P$ on a measurable space $(\Omega, \mathcal F)$ such that
$$
\mathbb P(\Omega) = 1
$$

Thus a probability measure assigns total mass one to the whole sample space and gives a rigorous semantics to random events.

## Properties

### Basic Identities

- Nonnegativity:
$$
\mathbb P(A) \in [0, 1]
\qquad (A \in \mathcal F)
$$

- Complement rule:
$$
\mathbb P(A^c) = 1 - \mathbb P(A)
$$

- Inclusion-exclusion for two events:
$$
\mathbb P(A \cup B) = \mathbb P(A) + \mathbb P(B) - \mathbb P(A \cap B)
$$

- Continuity:
if $A_n \uparrow A$, then $\mathbb P(A_n) \to \mathbb P(A)$; if $A_n \downarrow A$, then $\mathbb P(A_n) \to \mathbb P(A)$.

### Interpretation

Probability measures are special finite measures. This allows essentially all of measure theory to be applied to probability, with normalization providing the additional probabilistic interpretation.

### Canonical Examples

- Bernoulli measure on $\{0,1\}$
- Gaussian law on $\mathbb R$
- Poisson law on $\mathbb N$

## Include

- [Distribution](./Distribution.md): subtype_of

## Parents

- [Measure](./Measure.md): subtype_of
