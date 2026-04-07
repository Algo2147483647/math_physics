# Borel Sigma Algebra

[TOC]

## Define

Let $(X, \tau)$ be a [topological space](./Topological_Space.md). The Borel $\sigma$-algebra on $X$ is the smallest [sigma algebra](./Sigma_Algebra.md) containing all open sets:
$$
\mathcal B(X) = \sigma(\tau)
$$

Its elements are called Borel sets.

## Properties

### Basic Content

- $\mathcal B(X)$ contains all open sets and all closed sets.
- It is also closed under countable unions, countable intersections, and complements.

### On Euclidean Spaces

For $X = \mathbb R^n$, the Borel $\sigma$-algebra is generated equivalently by

- open sets
- closed sets
- open balls
- intervals or rectangles with rational endpoints

### Why It Matters

The Borel $\sigma$-algebra is the standard measurable structure placed on topological spaces in analysis and probability. Real-valued random variables are usually understood as measurable maps into $(\mathbb R, \mathcal B(\mathbb R))$.

## Include

## Parents

- [Sigma_Algebra](./Sigma_Algebra.md): subtype_of

- [Topological_Space](./Topological_Space.md): defined_on
