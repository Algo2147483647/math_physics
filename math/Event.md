# Event

[TOC]

## Define

Let $(\Omega, \mathcal F, \mathbb P)$ be a [probability space](./Probability_Space.md). An event is a measurable subset
$$
A \in \mathcal F
$$

So events are not arbitrary subsets of $\Omega$, but exactly those subsets to which the probability measure is allowed to assign a value.

## Properties

### Event Algebra

- If $A$ is an event, then $A^c$ is an event.

- If $A_n \in \mathcal F$, then
$$
\bigcup_{n=1}^{\infty} A_n \in \mathcal F
$$
and
$$
\bigcap_{n=1}^{\infty} A_n \in \mathcal F
$$

Thus events form a $\sigma$-algebra rather than merely a Boolean algebra of finite operations.

### Common Types of Events

- Elementary events: singleton outcomes in discrete spaces
- Tail events in infinite product spaces
- Hitting events for stochastic processes

### Probabilistic Role

Probability is fundamentally assigned to events first. Random variables, distributions, and stochastic processes are built from event-level measurability.

## Include

## Parents

- [Probability_Space](./Probability_Space.md): defined_on
