# Category

[TOC]

## Define

> A category is a collection of objects and morphisms together with associative composition and identity morphisms.

A **category** $\mathcal C$ consists of:

- a class of objects $\operatorname{Ob}(\mathcal C)$,
- for each pair of objects $X,Y$, a set of morphisms
$$
\operatorname{Hom}_{\mathcal C}(X,Y),
$$
- a composition law
$$
\operatorname{Hom}(Y,Z)\times\operatorname{Hom}(X,Y)\to\operatorname{Hom}(X,Z),
$$
- identity morphisms $\operatorname{id}_X\in\operatorname{Hom}(X,X)$.

These satisfy associativity and identity axioms.

## Properties

### Composition

For composable morphisms $f:X\to Y$ and $g:Y\to Z$, the composite is
$$
g\circ f:X\to Z.
$$

### Examples

Typical examples are the category of sets, topological spaces, groups, and vector spaces.

## Include

## Parents

