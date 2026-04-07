# Stopping Time

[TOC]

## Define

Let $(\mathcal F_t)_{t \in T}$ be a [filtration](./Filtration.md). A random time
$$
\tau: \Omega \to T \cup \{\infty\}
$$
is a stopping time if for every $t \in T$,
$$
\{\tau \le t\} \in \mathcal F_t
$$

This means that by time $t$ one can determine whether the stopping event has already occurred.

## Properties

### Intuition

Stopping times are random times that are observable from present and past information, never requiring knowledge of the future.

### Typical Examples

- First hitting time of a set
- First exit time from a domain
- Deterministic times as trivial stopping times

### Why They Matter

Stopping times are fundamental in martingale theory, optional sampling, strong Markov properties, and stochastic control.

## Include

## Parents

- [Random_Variable](./Random_Variable.md): subtype_of

- [Filtration](./Filtration.md): defined_on
