# Martingale

[TOC]

## Define

Martingale is a discrete-time [stochastic process](./Stochastic_Process.md) that satisfies for any time $n$,
$$
\mathbb E(|X_n|) < \infty
$$
$$
\mathbb E(X_{n+1} \ |\ X_1, ..., X_n) = X_n
$$

The second condition means that the conditional expected value of the next observation, given all the past observations, is equal to the most recent observation.

## Properties

- Doob-Meyer decomposition


### Stopping Time

- Define
  Stopping Time $\tau: \Sigma \to \bar T, \bar T = T \cup \{\infty\}$ is a random variable defined on the filtered probability space $(\Omega, \mathcal F, (\mathcal F_n)_{n \in \mathbb N}, P)$ with value in $T = [0, +\infty)$, such that 
  $$
  \{\tau \le t\} \in \mathcal F_t \quad, \forall t \in T
  $$

- Property

  - Optional stopping theorem

    Consider a stochastic process $\{X_t\}$ and a stopping time $\tau$ (a random variable that represents the time at which some event of interest occurs). The optional stopping theorem provides conditions under which
    $$
    \mathbb E(X_\tau) = \mathbb E(X_0)
    $$

## Include

## Parents

- [Stochastic_Process](./Stochastic_Process.md): 

