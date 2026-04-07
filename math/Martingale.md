# Martingale

[TOC]

## Define

Let $(\mathcal F_t)_{t \in T}$ be a [filtration](./Filtration.md). A stochastic process $(X_t)_{t \in T}$ is a martingale if

- each $X_t$ is integrable
- each $X_t$ is $\mathcal F_t$-measurable
- for $s \le t$,
$$
\mathbb E[X_t \mid \mathcal F_s] = X_s
$$

## Properties

### Interpretation

A martingale is the mathematical model of a fair evolution relative to the information flow $(\mathcal F_t)$.

### Related Classes

- Submartingale:
$$
\mathbb E[X_t \mid \mathcal F_s] \ge X_s
$$

- Supermartingale:
$$
\mathbb E[X_t \mid \mathcal F_s] \le X_s
$$

### Central Role

Martingales are foundational in

- optional stopping
- stochastic integration
- Brownian motion and diffusion theory
- modern concentration inequalities

## Include

## Parents

- [Stochastic_Process](./Stochastic_Process.md): subtype_of

- [Filtration](./Filtration.md): defined_on
