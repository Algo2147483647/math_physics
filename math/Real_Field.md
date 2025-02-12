# Real Field

[TOC]

## Define

$$
\mathbb R
$$

Real numbers is defined through the Dedekind cut of rational number sets $\mathbb Q$. The Dedekind cut is a pair of sets A and B that divide the [rational number](./Rational_Number_Field.md) set $\mathbb Q$ into two parts, satisfying:

- $A \neq \empty, A \neq \mathbb Q$
- if $p, q \in \mathbb Q, p < q, q \in A$, then $p \in A$. 
- No maximum element in $A$, if $q \in A$, then there must be $p \in \mathbb Q, p > q$, let $p \in A$.


Each Dedekind cut defines a real number: if the cut represents a rational number, it is that rational number, otherwise it is an irrational number.



The set of real numbers, denoted $\mathbb{R}$, together with the operations of addition and multiplication, is called the [field](./Field.md) of real numbers if the following axioms are satisfied:

**Field Axioms**:
- (A1) $a + b = b + a$ for all $a, b \in \mathbb{R}$ (Commutativity of Addition).
- (A2) $a + (b + c) = (a + b) + c$ for all $a, b, c \in \mathbb{R}$ (Associativity of Addition).
- (A3) There exists an element $0 \in \mathbb{R}$ such that $a + 0 = a$ for all $a \in \mathbb{R}$ (Existence of Additive Identity).
- (A4) For every $a \in \mathbb{R}$, there exists an element $-a \in \mathbb{R}$ such that $a + (-a) = 0$ (Existence of Additive Inverse).
- (M1) $a \cdot b = b \cdot a$ for all $a, b \in \mathbb{R}$ (Commutativity of Multiplication).
- (M2) $a \cdot (b \cdot c) = (a \cdot b) \cdot c$ for all $a, b, c \in \mathbb{R}$ (Associativity of Multiplication).
- (M3) There exists an element $1 \in \mathbb{R}$, $1 \neq 0$, such that $a \cdot 1 = a$ for all $a \in \mathbb{R}$ (Existence of Multiplicative Identity).
- (M4) For every $a \in \mathbb{R}$ with $a \neq 0$, there exists an element $a^{-1} \in \mathbb{R}$ such that $a \cdot a^{-1} = 1$ (Existence of Multiplicative Inverse).
- (D) $a \cdot (b + c) = (a \cdot b) + (a \cdot c)$ for all $a, b, c \in \mathbb{R}$ (Distributive Law).

**Order Axioms**:
- (O1) For every $a, b \in \mathbb{R}$, exactly one of the following holds: $a < b$, $a = b$, $a > b$.
- (O2) If $a < b$ and $b < c$, then $a < c$.
- (O3) If $a < b$ and $c > 0$, then $a \cdot c < b \cdot c$.
- (O4) If $a < b$ and $c < 0$, then $a \cdot c > b \cdot c$.

## Properties



## Include

- [Complex_Field](./Complex_Field.md): 

- [Euclidean_Space](./Euclidean_Space.md): 

- [Quaternion_Ring](./Quaternion_Ring.md): 

- [Real_Value_Function](./Real_Value_Function.md): 

## Parents

- [Field](./Field.md): 

- [Rational_Number_Field](./Rational_Number_Field.md): 

