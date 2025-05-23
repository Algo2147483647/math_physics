# Function

[TOC]

## Define

$$
f: X \to Y  \tag{Function}
$$
$$
\forall x \in X, \exists_{= 1} y \in Y, f(x) = y
$$
Mapping, refer to a [binary relation](./Relation.md) from the element of set $X$ to that of set $Y$, and satisfy any element in $X$ has a unique element in $Y$ corresponding to it (One-to-many is not allowed).

$X$: domain of Definition.


### Injective

$$
\forall x, x', f(x) = f(x') \Rightarrow x = x'
$$
Each mapped element $y$ has a unique element $x$ corresponding to it.

### Surjection

$$
\forall y \in Y, \exists x \in X, f(x) = y
$$
Each element $y$ in set $Y$ has a element $x$ in set $X$ corresponding to it.

### Bijection, One-to-One Correspondence

$$
\forall y \in Y, \exists_{= 1} x \in X, f(x) = y
$$
A map that is both injective and surjective. Each element $y$ in set $Y$ has a unique element $x$ in set $X$ corresponding to it. Meanwhile, each element $x$ in set $X$ has a unique element $y$ in set $Y$ corresponding to it.

<img src="assets/R-16983288702011.png" alt="R" style="zoom: 30%;" />

## Properties

* Inverse Function
  if $f$ is a bijection, its inverse function is $f^{-1}(b) = a \Leftrightarrow f(a) = b$

## Include

- [Bessel_Function](./Bessel_Function.md): is-a

- [Complex_Value_Function](./Complex_Value_Function.md): is-a

- [Dirac_Delta_Function](./Dirac_Delta_Function.md): is-a

- [Exponential_Function](./Exponential_Function.md): is-a

- [Hilbert_Transform](./Hilbert_Transform.md): is-a

- [Laplace_Transform](./Laplace_Transform.md): is-a

- [Linear_Transformation](./Linear_Transformation.md): is-a

- [Polynomial_Function](./Polynomial_Function.md): is-a

- [Radon_Translation](./Radon_Translation.md): is-a

- [Real_Value_Function](./Real_Value_Function.md): is-a

- [Sequence](./Sequence.md): is-a

## Parents

- [Relation](./Relation.md): is-a

