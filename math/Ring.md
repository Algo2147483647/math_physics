# Ring

[TOC]

## Define

$$
(G, +, \cdot)
$$

Ring is an algebraic structure, where $G$ is a set, $\cdot$ and $+$ are binary operations, and satisfy:  

- $(G, +)$ is a commutative group
- $(G, \cdot)$ is a monoid
  - $(G, \cdot)$ satisfies associative law, $a \cdot (b \cdot c) = (a \cdot b) \cdot c$
  - $(G, \cdot)$ exists multiplicative identity, $\exist 1: 1 \cdot x = x \cdot 1 = x, \forall x \in G$
- Distributive law: multiplication is distributive with respect to addition,
  $$
  \begin{align*}
    a \cdot (b + c) &= a \cdot b + a \cdot c  \\
    (b + c) \cdot a &= b \cdot a + c \cdot a
  \end{align*}
  $$

## Properties

### Ideal

- Define

  Let $R$ be a ring and $I$ be a subring of $R$, if $\forall i \in I, \forall r \in R$, $i\cdot r = r \cdot i \in I$,  we call $I$ is the ideal subring of $R$.

- Property
  - Quotient Ring

- Include

  - Prime Ideal

    An ideal $I$ of a commutative ring $R$ is called a prime ideal if, whenever the product of two elements $a, b \in R$ is an element of $I$, at least one of $a$ or $b$ is in $I$. Symbolically, if $I$ is a prime ideal and $ab \in I$, then either $a \in I$ or $b \in I$.

  - Maximal Ideal

    An ideal $I$ of a ring $R$ is called a maximal ideal if it is a proper ideal (i.e., $I \neq R$) and there are no other proper ideals properly containing $I$. In other words, there does not exist another ideal $J$ such that $I \subsetneq J \subsetneq R$.

### Polynomial Ring

The polynomial ring $K[x]$ in $x$ over a field (or, more generally, a commutative ring) $K$ defined as the set of all polynomials in the variable $x$ with coefficients $p_i \in K$ and a non-negative integer $n$ (representing the degree of the polynomial). 
$$
f(x) = p_{0}+p_{1}x+p_{2}x^{2}+\cdots +p_{n}x^{n}
$$

- **Addition**: $g(x) + f(x)$ is the polynomial whose coefficient of $x_i$ is $a_i + b_i$ for each $i$.
- **Multiplication**: Given two polynomials $f, g$, their product $f \cdot g$ is computed using the distributive property.

  

### Commutative Ring

A Ring satisfying commutative law.
$$
a \cdot b = b \cdot a \quad; \forall a, b \in G
$$

## Include

- [Field](./Field.md): 

- [Integer_Ring](./Integer_Ring.md): 

- [Module](./Module.md): 

- [Quaternion_Ring](./Quaternion_Ring.md): 

## Parents

- [Algebra_Structure](./Algebra_Structure.md): 

