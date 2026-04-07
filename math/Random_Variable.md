# Random Variable

[TOC]

## Define

A random variable is a [measurable function](./Measurable_Function.md)
$$
X: \Omega \to \mathbb R
$$
from a [probability space](./Probability_Space.md) $(\Omega, \mathcal F, \mathbb P)$ to the real line equipped with its [Borel sigma algebra](./Borel_Sigma_Algebra.md).

## Properties

### Measurability Criterion

For every Borel set $B \subseteq \mathbb R$,
$$
X^{-1}(B) \in \mathcal F
$$

Equivalently, it is enough to require
$$
\{X \le a\} \in \mathcal F
\qquad \forall a \in \mathbb R
$$

### Related Objects

- A random vector is a measurable map
$$
X: \Omega \to \mathbb R^n
$$

- The law of a random variable is its [distribution](./Distribution.md).

- Moments, expectations, variances, and conditional laws are all derived from the random variable together with the underlying probability measure.

### Typical Classes

- Discrete random variables
- Absolutely continuous random variables
- Gaussian, Poisson, Bernoulli, and other classical families

## Include

- [Distribution](./Distribution.md): induces

- [Moment](./Moment.md): property_of

- [Stopping_Time](./Stopping_Time.md): subtype_of

## Parents

- [Measurable_Function](./Measurable_Function.md): subtype_of

- [Probability_Space](./Probability_Space.md): defined_on
