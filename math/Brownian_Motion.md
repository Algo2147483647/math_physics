# Brownian Motion

[TOC]

## Define

A Brownian motion (or Wiener process) is a stochastic process $(W_t)_{t \ge 0}$ such that

- $W_0 = 0$ almost surely
- it has independent increments
- for $0 \le s < t$,
$$
W_t - W_s \sim \mathcal N(0, t-s)
$$
- its sample paths are almost surely continuous

## Properties

### Structural Character

Brownian motion is simultaneously

- a [Gaussian process](./Gaussian_Process.md)
- a [Markov process](./Markov_Process.md)
- a martingale with respect to its natural filtration

### Covariance Structure

Its covariance function is
$$
\operatorname{Cov}(W_s, W_t) = \min\{s,t\}
$$

### Central Role

Brownian motion is the canonical continuous-time random fluctuation. It underlies diffusion equations, stochastic differential equations, Ito calculus, and scaling limits of random walks.

## Include

## Parents

- [Gaussian_Process](./Gaussian_Process.md): subtype_of

- [Markov_Process](./Markov_Process.md): subtype_of
