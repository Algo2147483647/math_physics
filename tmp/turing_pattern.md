# Turing pattern

[TOC]

## Gray-Scott

$$
\frac{\partial u}{\partial t} = D_u \nabla^2 u - uv^2 + F(1 - u)  \\
\frac{\partial v}{\partial t} = D_v \nabla^2 v + uv^2 - (F + k)v
$$

- $u$ and $v$: represent the concentrations of the activator and inhibitor, respectively.
- $D_u$ and $D_v$: represent the diffusion coefficients of the activator and inhibitor, respectively.
- $F$: represents the supply rate of the activator.
- $k$: represents the removal rate of the inhibitor.
- $-uv^2$: represents the nonlinear reaction term of the activator and inhibitor, generating a new inhibitor $v$.


<img src="./assets/xmorphia-parameter-map.jpg" alt="xmorphia-parameter-map" style="zoom: 50%;" />

## FitzHugh-Nagumo
$$
\frac{\partial u}{\partial t} = D_u \nabla^2 u + u - \frac{u^3}{3} - v  \\
\frac{\partial v}{\partial t} = D_v \nabla^2 v + \epsilon (u + \beta - \gamma v)
$$