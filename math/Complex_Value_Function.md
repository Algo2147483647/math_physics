# Complex Value Function

[TOC]

## Define

$$
f: \mathbb C \to \mathbb C
$$

A complex function $f: \mathbb C \to \mathbb C$ is a [function](./Function.md) from [complex numbers](./Complex_Field.md) to complex numbers.

## Properties

- Differentiability: Holomorphic functions (or analytic functions) are differentiable everywhere within their domain of definition. For complex functions, holomorphism and analyticity are equivalent. 

  Let $U$ be an open set in the complex plane $\mathbb C$ and let $f : U \to \mathbb C$ be a function. The function ,is said to be analytic (or holomorphic) on $U$ if for every $z_0 \in U$, there exists an open disk $D$ centered at $z_0$ such that $f$ is differentiable at every point in $D$.

### Residue & Residue Theorem
$$
\operatorname{Res}(f,a)  \tag{Residue}
$$
$$
\oint_C f(z)\,\mathrm{d}z=2\pi i\sum_{k=1}^n \operatorname{Res}(f,a_k)  \tag{Residue Theorem}
$$

For an analytic function $f(z)$ on an open set $D$ and a simple closed curve $C$ that encircles counterclockwise all the isolated singularities $a_1,a_2,\ldots,a_n$ of $f(z)$, then the integral of $f(z)$ along $C$ can be expressed as the sum of the residues of $f(z)$ at these singularities. And $\operatorname{Res}(f,a_k)$ denotes the residue of $f(z)$ at the point $a_k$.

### Laurent Series

The Laurent series for a complex function $f(z)$ about a point $c$ is given by
$$
f(z) = \sum^{\infty}_{n=-\infty} a_n(z-c)^n\\
a_n = \frac{1}{2\pi i} \oint_\gamma \frac{f(z)}{(z-c)^{n+1}}\mathrm{d}z
$$
The path of integration $\gamma$ is counterclockwise around a Jordan curve enclosing $c$ and lying in an annulus $A$ in which $f(z)$ is holomorphic (analytic). The expansion for $f(z)$ will then be valid anywhere inside the annulus.

## Include

- [Gamma_Function](./Gamma_Function.md): 

- [Holomorphic_Function](./Holomorphic_Function.md): 

- [Hypergeometric_Function](./Hypergeometric_Function.md): 

- [Riemann_Zeta_Function](./Riemann_Zeta_Function.md): 

## Parents

- [Complex_Field](./Complex_Field.md): 

- [Function](./Function.md): 

