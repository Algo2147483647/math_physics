# Markov Process

[TOC]

## Define

A Markov process is a [stochastic process](./Stochastic_Process.md) $(X_t)_{t \in T}$ such that the conditional law of the future depends on the past only through the present state.

In discrete time, this is expressed as
$$
\mathbb P(X_{n+1} \in B \mid X_0, \dots, X_n)
=
\mathbb P(X_{n+1} \in B \mid X_n)
$$
for every measurable set $B$.

## Properties

### Markov Property

The Markov property is a structural memorylessness statement. It does not say the process has independent increments; it says all relevant predictive information is contained in the present state.

### Transition Description

Markov processes are described by transition probabilities, often encoded by a [transition kernel](./Transition_Kernel.md). In time-homogeneous settings, these transition laws depend only on time differences.

### Fundamental Examples

- discrete-time [Markov chains](./Markov_Chain.md)
- [Brownian motion](./Brownian_Motion.md)
- [Poisson processes](./Poisson_Process.md)

## Include

- [Markov_Chain](./Markov_Chain.md): subtype_of

- [Brownian_Motion](./Brownian_Motion.md): subtype_of

- [Poisson_Process](./Poisson_Process.md): subtype_of

## Parents

- [Stochastic_Process](./Stochastic_Process.md): subtype_of
