# Gaussian Process

[TOC]

## Define

A Gaussian process is a [stochastic process](./Stochastic_Process.md) $(X_t)_{t \in T}$ such that for every finite set of indices $t_1, \dots, t_n \in T$, the random vector
$$
(X_{t_1}, \dots, X_{t_n})
$$
has a multivariate normal distribution.

## Properties

### Determining Data

Whenever first and second moments exist, a Gaussian process is determined by

- its mean function
$$
m(t) = \mathbb E[X_t]
$$

- its covariance kernel
$$
K(s,t) = \operatorname{Cov}(X_s, X_t)
$$

### Importance

Gaussian processes appear throughout probability, statistics, machine learning, and stochastic analysis because many limit objects are Gaussian and many constructions reduce to covariance analysis.

### Canonical Example

[Brownian motion](./Brownian_Motion.md) is the basic Gaussian process with covariance kernel
$$
K(s,t)=\min\{s,t\}
$$

## Include

- [Brownian_Motion](./Brownian_Motion.md): subtype_of

## Parents

- [Stochastic_Process](./Stochastic_Process.md): subtype_of
