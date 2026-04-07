# Measure Space

[TOC]

## Define

$$
(E, \mathcal E, \mu)
\tag{Measure Space}
$$

A measure space is a [measurable space](./Measurable_Space.md) $(E, \mathcal E)$ together with a [measure](./Measure.md) $\mu$ on $(E, \mathcal E)$.

This is the standard ambient object for integration, almost-everywhere arguments, product constructions, and probability theory.

## Properties

### Important Classes

- Finite:
$$
\mu(E) < \infty
$$

- $\sigma$-finite:
there exist measurable sets $E_n \in \mathcal E$ such that
$$
E = \bigcup_{n=1}^{\infty} E_n,
\qquad
\mu(E_n) < \infty
$$

- Complete:
every subset of every null set is measurable.

### Why Measure Spaces Matter

Many central results are naturally stated on measure spaces rather than specifically on probability spaces:

- Lebesgue integration
- Fubini-Tonelli theory
- Radon-Nikodym theory
- $L^p$ spaces

Probability spaces are simply normalized measure spaces.

### Typical Examples

- $(\mathbb R^n, \mathcal B(\mathbb R^n), m)$ with Lebesgue measure $m$
- $(\Omega, \mathcal P(\Omega), \#)$ with counting measure
- every [probability space](./Probability_Space.md)

## Include

- [Probability_Space](./Probability_Space.md): subtype_of

- [Product_Measure](./Product_Measure.md): defined_on

## Parents

- [Measurable_Space](./Measurable_Space.md): subtype_of
