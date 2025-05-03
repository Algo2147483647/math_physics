# Differential Manifold

[TOC]

## Define

Differential manifold $M$ of dimension $n$ is a [manifold](./Manifold.md) and equipped with a differentiable structure. Differentiable structure refers to there exists a collection of charts $\{(U_\alpha, \varphi_\alpha)\}$ such that $\bigcup_{\alpha}U_{\alpha}=M$, for all overlapping charts $(U_{\alpha},\varphi_{\alpha}), (U_{\beta},\varphi_{\beta})$ in the atlas with $U_{\alpha}\cap U_{\beta}\neq\varnothing$, then the transition maps $\varphi_{\beta}\circ\varphi_{\alpha}^{-1}:\varphi_{\alpha}(U_{\alpha}\cap U_{\beta})\to\varphi_{\beta}(U_{\alpha}\cap U_{\beta})$ are smooth (infinitely differentiable $C^\infty$) map. This collection of charts is called an smooth atlas.

<img src="./assets/Two_coordinate_charts_on_a_manifold.svg" alt="Two_coordinate_charts_on_a_manifold"  />

## Properties


### Relationship between multiply differential manifolds

#### Continuity

$f: M \to M'$ is a $C^r$ mapping $\Leftrightarrow$ $\forall p \in M, \psi_\beta \circ f \circ \psi_\alpha^{-1}$ is $C^r$

- $\psi_\alpha: M \to \mathbb R^{n}$
- $\psi_\beta: M' \to \mathbb R^{n'}$
- $f = \psi_\beta \circ f \circ \psi_\alpha^{-1}$

#### Diffeomorphic

$M, M'$ is Diffeomorphic $\leftrightarrow \exist f: M \to M'$ is one to one, and $f, f^{-1}$ is $C^{\infty}$

### Relationship between differential manifolds and $\mathbb R^n$

#### Scalar Field: $M \to \mathbb R$

The function $f: M \to \mathbb R$ is intrinsically defined and unique in itself, requiring no dependence on the choice of coordinate system. When combine with a special coordinate system $(O, \psi)$, we obtain the coordinate representation of this function in the local coordinates — an n-variable function $f (x_1, \cdots, x_n)$ expressed through coordinate parameters. This coordinate-dependent representation undergoes corresponding variations depending on the chosen coordinate system.

#### Curve: $\mathbb R \to M$

$$
C: (I \in \mathbb R) \to M
$$

##### Tangent vector

$$
T(f) = \frac{\mathrm d (f \circ C)}{\mathrm d t} |_{t_0}  \quad ,\forall f \in \mathcal F_M
$$



### Christopher Symbol

The Christopher Symbol can compare tensors at different locations on the manifold instead of viewing them in isolation, so the K-Schmidt symbol is also called the connection coefficient.
$$
\var A^i = -\Gamma^i_{kl} A^k \mathrm{d} x^l
$$
Property
$$
\Gamma^k_{ij} = \frac{1}{2} g^{kl} \left( \frac{\partial g_{il}}{\partial x^j} + \frac{\partial g_{jl}}{\partial x^i} - \frac{\partial g_{ij}}{\partial x^l} \right)
$$

### Geodesic equation

$$
\frac{d^2 x^k}{d\tau^2} + \Gamma^k_{ij} \frac{dx^i}{d\tau} \frac{dx^j}{d\tau} = 0
$$

## Include

- [Euclidean_Space](./Euclidean_Space.md): 

## Parents

- [Manifold](./Manifold.md): 

