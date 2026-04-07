# Probability Space

[TOC]

## Define

$$
(\Omega, \mathcal F, \mathbb P)
\tag{Probability Space}
$$

A probability space is a [measure space](./Measure_Space.md) whose measure is a [probability measure](./Probability_Measure.md). It consists of

- $\Omega$: sample space
- $\mathcal F$: a $\sigma$-algebra of events
- $\mathbb P$: a probability measure on $(\Omega, \mathcal F)$

## Properties

### Structural Meaning

- $\Omega$ contains the possible outcomes.
- $\mathcal F$ specifies which subsets of $\Omega$ are meaningful events.
- $\mathbb P$ assigns probabilities to those events.

### Basic Probability Laws

- Every event $A \in \mathcal F$ has probability $\mathbb P(A)$.

- If $A_1, A_2, \dots$ are pairwise disjoint events, then
$$
\mathbb P\left(\bigcup_{n=1}^{\infty} A_n\right)
=
\sum_{n=1}^{\infty} \mathbb P(A_n)
$$

- The whole sample space has probability one:
$$
\mathbb P(\Omega) = 1
$$

### Canonical Examples

- Finite models such as dice and card experiments
- Countable sequence spaces such as coin-toss processes
- Continuous spaces such as $(\mathbb R, \mathcal B(\mathbb R), \mu)$ where $\mu$ is a probability measure

## Include

- [Event](./Event.md): defined_on

- [Filtration](./Filtration.md): defined_on

- [Random_Variable](./Random_Variable.md): defined_on

- [Stochastic_Process](./Stochastic_Process.md): defined_on

## Parents

- [Measure_Space](./Measure_Space.md): subtype_of
