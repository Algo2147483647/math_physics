# Markov Chain

[TOC]

## Define

A Markov chain is a discrete-time [Markov process](./Markov_Process.md) $(X_n)_{n \ge 0}$ such that for every $n$,
$$
\mathbb P(X_{n+1} \in B \mid X_0, \dots, X_n)
=
\mathbb P(X_{n+1} \in B \mid X_n)
$$
for every measurable set $B$ in the state space.

In a discrete state space, the one-step transition probabilities are
$$
p_{ij} = \mathbb P(X_{n+1} = j \mid X_n = i)
$$

## Properties

### Transition Matrix

The matrix $P = (p_{ij})$ is row-stochastic:
$$
p_{ij} \ge 0,
\qquad
\sum_j p_{ij} = 1
$$

The $n$-step transition probabilities are entries of $P^n$.

### Classification Questions

Modern Markov-chain theory studies notions such as

- irreducibility
- recurrence and transience
- periodicity
- invariant and stationary distributions
- mixing behavior

### Stationary Distribution

A probability vector $\pi$ is stationary if
$$
\pi P = \pi
$$

## Include

## Parents

- [Markov_Process](./Markov_Process.md): subtype_of
