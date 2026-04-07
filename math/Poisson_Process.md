# Poisson Process

[TOC]

## Define

A Poisson process $(N_t)_{t \ge 0}$ with rate $\lambda > 0$ is a counting process such that

- $N_0 = 0$
- it has independent increments
- it has stationary increments
- for $0 \le s < t$,
$$
N_t - N_s \sim \operatorname{Poisson}(\lambda (t-s))
$$

## Properties

### Counting Interpretation

$N_t$ counts the number of arrivals up to time $t$. It is the basic model for random arrivals occurring independently at a constant average rate.

### Derived Facts

- The waiting times between jumps are independent exponential random variables with parameter $\lambda$.
- One has
$$
\mathbb E[N_t] = \lambda t,
\qquad
\operatorname{Var}(N_t) = \lambda t
$$

### Structural Role

A Poisson process is a [Markov process](./Markov_Process.md), and it is the canonical pure-jump analogue of Brownian motion.

## Include

## Parents

- [Markov_Process](./Markov_Process.md): subtype_of
