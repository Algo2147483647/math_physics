# Transition Kernel

[TOC]

## Define

Let $(E, \mathcal E)$ and $(F, \mathcal F)$ be [measurable spaces](./Measurable_Space.md). A transition kernel from $E$ to $F$ is a map
$$
K: E \times \mathcal F \to [0,1]
$$
such that

- for each $x \in E$, the set function $B \mapsto K(x, B)$ is a probability measure on $(F, \mathcal F)$
- for each $B \in \mathcal F$, the function $x \mapsto K(x, B)$ is measurable on $E$

## Properties

### Interpretation

For each current state $x$, the kernel $K(x, \cdot)$ is the law of the next state.

### Discrete-State Case

When $E$ and $F$ are countable, a transition kernel is exactly a stochastic matrix:
$$
K(i,\{j\}) = p_{ij}
$$

### Role in Markov Theory

Transition kernels are the correct measurable-space generalization of transition matrices. They are central in the construction of Markov chains, Markov semigroups, and conditional distributions.

## Include

## Parents

- [Measurable_Space](./Measurable_Space.md): defined_on
