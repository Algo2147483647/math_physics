# Stochastic Process

[TOC]

## Define

A stochastic process is a family of [random variables](./Random_Variable.md)
$$
(X_t)_{t \in T}
$$
defined on the same [probability space](./Probability_Space.md), where $T$ is an index set, typically interpreted as time.

Equivalently, a stochastic process can be viewed as a map
$$
X: T \times \Omega \to E
$$
such that for each fixed $t \in T$, the map $\omega \mapsto X_t(\omega)$ is a random variable.

## Properties

### Two Complementary Viewpoints

- For fixed $t$, $X_t$ is a random variable.
- For fixed $\omega$, the map $t \mapsto X_t(\omega)$ is a sample path.

Modern probability constantly moves between these two perspectives.

### Finite-Dimensional Laws

The joint laws of
$$
(X_{t_1}, \dots, X_{t_n})
$$
for finite collections of times are called the finite-dimensional distributions of the process. These are a core invariant of the process.

### Further Structure

Important subclasses arise by adding extra structure:

- Markov property
- Gaussian finite-dimensional laws
- martingale property relative to a filtration
- continuity or cadlag path regularity

## Include

- [Gaussian_Process](./Gaussian_Process.md): subtype_of

- [Markov_Process](./Markov_Process.md): subtype_of

- [Martingale](./Martingale.md): subtype_of

## Parents

- [Probability_Space](./Probability_Space.md): defined_on
