# Measurable Function

[TOC]

## Define

Let $(X, \mathcal A)$ and $(Y, \mathcal B)$ be [measurable spaces](./Measurable_Space.md). A function
$$
f: X \to Y
$$
is measurable if for every $B \in \mathcal B$,
$$
f^{-1}(B) \in \mathcal A
$$

In other words, measurable structure is preserved under taking inverse images.

## Properties

### Equivalent Tests

For real-valued functions it is enough to check inverse images of a generating family, for example
$$
(-\infty, a], \qquad a \in \mathbb R
$$

### Stability

- If $f: X \to Y$ and $g: Y \to Z$ are measurable, then $g \circ f$ is measurable.
- If $f_n: X \to \mathbb R$ are measurable, then pointwise suprema, infima, and pointwise limits are measurable whenever defined.

### Typical Examples

- Continuous maps between topological spaces equipped with Borel $\sigma$-algebras
- Indicator functions of measurable sets
- Random variables

## Include

- [Random_Variable](./Random_Variable.md): subtype_of

## Parents

- [Function](./Function.md): subtype_of

- [Measurable_Space](./Measurable_Space.md): defined_on
