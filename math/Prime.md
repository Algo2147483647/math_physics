# Prime

[TOC]

## Define

$$
\nexists a \in (\mathbb N - \{1, p\}), \text{ let } a | p  \tag{Prime}
$$
Prime is a number $p$ that can only be divided by $1$ and itself.

## Properties

### Fundamental Theorem of Arithmetic
Any integer $n$ greater than $1$ can be uniquely expressed in the form of prime $p_i$ product.   
$$
n = \prod_i p_i^{\alpha_i} \quad n \in \mathbb Z, n > 1
$$

### Fermat's Little Theorem

$$
a^{p-1} \equiv 1 \mod p
$$
Where $p$ is a prime and $a$ is an any integer that is not a multiple of $p$.

- Property
  $$
  \frac{a}{b} \mod p \equiv a \times b^{p-2} \mod p
  $$

  - Proof

      $$
      \frac{a}{b} \mod p = a \times b^{-1} \mod p  \\
      b^{p-1} \equiv 1 \mod p \\
      b \times b^{p-1} \equiv 1 \mod p  \\
      \Rightarrow \quad b^{-1} \equiv b^{p-2}  \mod p \\
      \Rightarrow \quad \frac{a}{b} \mod p \equiv a \times b^{p-2} \mod p
      $$

  ### Goldbach's Conjecture
  
  every even natural number greater than 2 is the sum of two prime numbers.
  $$
  \forall n \in \mathbb{Z}^+ \, (\, n > 2 \, \land \, \text{even}(n) \, ) \, \exists \, p, q \in \text{Primes} \, (\, n = p + q \, )
  $$

## Include

## Parents

- [Division_with_Remainder](./Division_with_Remainder.md): 

