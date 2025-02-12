# Complex Field

[TOC]

## Define

$$
\mathbb C
$$

The set of complex numbers, denoted $\mathbb{C}$, consists of all ordered pairs of [real numbers](./Real_Field.md) $(a, b)$. Each such number is usually written as $a + bi$, where $a$ is called the real part, $b$ is called the imaginary part, and $i$ is the imaginary unit with the property that $i^2 = -1$.
$$
\mathbb C = \{a + b i \ |\ a, b \in \mathbb R ,i^2  = 1\}
$$
The operations of addition and multiplication are defined as:
- Addition: $(a + bi) + (c + di) = (a + c) + (b + d)i$.
- Multiplication: $(a + bi)(c + di) = (ac - bd) + (ad + bc)i$.

The set $\mathbb{C}$ with these operations forms a [field](./Field.md) that satisfies all the field axioms (A1-A4, M1-M4, D). It also has the property that every non-constant polynomial equation with coefficients in $\mathbb{C}$ has a root in $\mathbb{C}$ (this is the statement of the Fundamental Theorem of Algebra).

## Properties

- module and argument
$$
\begin{align*}
r &= |z| = \sqrt{a^2 + b^2}  \tag{module}\\
\theta &= \arg(z) = \arctan(b/a)  \tag{argument}
\end{align*}
$$
$$
z = a + b i = r (\cos \theta + i \sin \theta) = r e^{i \theta}
$$

- Fundamental theorem of algebra

  Every non-constant single-variable polynomial with complex coefficients has at least one complex root.

- sub & div
$$
\begin{align*}
z_1 - z_2 &= (a - b i) + (c - d i) = (a - b) + (c - d) i  \tag{sub}\\
\frac{z_1}{z_2} &= \frac{a - b i}{c - d i} = \frac{a c + b d}{c^2 + d^2} + \frac{b c + a d}{c^2 + d^2} i  \tag{div}
\end{align*}
$$
- conjugate: 

$$
\bar z = a - b i  \tag{conjugate}
$$
- power: 

$$
z^p = r^p (\cos θ + i \sin θ)^p = r^p (\cos (p θ) + i \sin(p θ))  \tag{De Moiver's theorem}
$$

## Include

- [Complex_Value_Function](./Complex_Value_Function.md): 

## Parents

- [Field](./Field.md): 

- [Real_Field](./Real_Field.md): 

