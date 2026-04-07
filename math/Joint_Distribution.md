# Joint Distribution

[TOC]

## Define

Let $X_1, \dots, X_n$ be [random variables](./Random_Variable.md) on the same probability space. The joint distribution of $(X_1, \dots, X_n)$ is the [distribution](./Distribution.md) of the random vector
$$
(X_1, \dots, X_n): \Omega \to \mathbb R^n
$$

Equivalently, for measurable $B \subseteq \mathbb R^n$,
$$
\mu_{(X_1,\dots,X_n)}(B)
=
\mathbb P\big((X_1,\dots,X_n) \in B\big)
$$

## Properties

### Marginals

Marginal distributions are obtained by projection. For example, the law of $X_1$ is the pushforward of the joint law by the projection map
$$
\pi_1(x_1,\dots,x_n)=x_1
$$

### Independence

The variables $X_1, \dots, X_n$ are independent if and only if their joint distribution factors as the product of their marginal distributions.

### Densities

When a joint density exists, marginal densities are obtained by integrating out coordinates, and conditional distributions are derived from the joint law.

## Include

## Parents

- [Distribution](./Distribution.md): subtype_of
