# Differential Manifold

[TOC]

## Define

Differential manifold $M$ of dimension $n$ is a [manifold](./Manifold.md) and equipped with a differentiable structure. Differentiable structure refers to there exists a collection of charts $\{(U_\alpha, \varphi_\alpha)\}$ such that $\bigcup_{\alpha}U_{\alpha}=M$, for all overlapping charts $(U_{\alpha},\varphi_{\alpha}), (U_{\beta},\varphi_{\beta})$ in the atlas with $U_{\alpha}\cap U_{\beta}\neq\varnothing$, then the transition maps $\varphi_{\beta}\circ\varphi_{\alpha}^{-1}:\varphi_{\alpha}(U_{\alpha}\cap U_{\beta})\to\varphi_{\beta}(U_{\alpha}\cap U_{\beta})$ are smooth (infinitely differentiable $C^\infty$) map. This collection of charts is called an smooth atlas.

<img src="./assets/Two_coordinate_charts_on_a_manifold.svg" alt="Two_coordinate_charts_on_a_manifold"  />

## Properties

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

