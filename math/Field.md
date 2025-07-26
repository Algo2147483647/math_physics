# Field

[TOC]

## Define

$$
(G, +, \cdot)
$$

Field is a [ring](./Ring.md) that satisfies the existence of multiplicative inverses for every nonzero element.

- $(G, +)$ is a commutative group

- $(G \setminus\{0\}, \cdot)$ is a commutative group

- Distributive law: multiplication is distributive with respect to addition,
  $$
  \begin{align*}
    a \cdot (b + c) &= a \cdot b + a \cdot c  \\
    (b + c) \cdot a &= b \cdot a + c \cdot a
  \end{align*}
  $$

## Properties

### Field extension

$$
E/F
$$

A field extension is a pair of fields $E$ and $F$ such that the operations of $F$ are those of $E$ restricted to $F$. In other words, $F$ is a subset of $E$, and the addition and multiplication of elements of $F$ in $E$ coincide with their addition and multiplication in $F$. When $F$ is a subfield of $E$, we often say that $E$ is an extension of $F$ and write $E/F$.

### Field Automorphism

$$
\begin{align*}
f(a + b) &= f(a) + f(b) \\
f(a \cdot b) &= f(a) \cdot f(b)
\end{align*}
$$



### Galois Group

$$
Gal(K/F) = \{\phi: K \to K \ |\ \phi(a) = a, \forall a \in F\}
$$

**Galois group** of a field extension $K/F$, is the group of all field automorphisms of $K$ that fix $F$ pointwise.

## Include

- [Complex_Field](./Complex_Field.md): is-a

- [Rational_Number_Field](./Rational_Number_Field.md): is-a

- [Real_Field](./Real_Field.md): is-a

## Parents

- [Integer_Ring](./Integer_Ring.md): is-a

