# Filtration

[TOC]

## Define

Let $(\Omega, \mathcal F, \mathbb P)$ be a [probability space](./Probability_Space.md) and let $T$ be an ordered index set. A filtration is an increasing family of sub-$\sigma$-algebras
$$
(\mathcal F_t)_{t \in T},
\qquad
\mathcal F_s \subseteq \mathcal F_t \subseteq \mathcal F
\quad (s \le t)
$$

It models the flow of information through time.

## Properties

### Adaptation

A stochastic process $(X_t)$ is adapted to $(\mathcal F_t)$ if each $X_t$ is $\mathcal F_t$-measurable. This means the value at time $t$ is observable using information available by time $t$.

### Natural Filtration

Every process $(X_t)$ generates a filtration:
$$
\mathcal F_t^X = \sigma(X_s : s \le t)
$$
called the natural filtration of the process.

### Role in Modern Probability

Filtrations are indispensable for

- martingales
- stopping times
- stochastic integration
- Markov and diffusion theory

## Include

- [Stopping_Time](./Stopping_Time.md): defined_on

- [Martingale](./Martingale.md): defined_on

## Parents

- [Probability_Space](./Probability_Space.md): defined_on
