# Alternating Direction Method of Multipliers

[TOC]

## Problem

$$
\begin{align*}
  \min_{x, z} \quad & f(x) + g(y)  \\
  s.t. \quad & A x + B y + c = 0
\end{align*}
$$

where, $f(x), g(z)$ is convex functions.

## Solving

Augmented Lagrangian
$$
\begin{align*}
L_{\rho} (x, y) 
=& f(x) + g(y) + u^T(A x + B y + c) + \frac{\rho}{2} \|A x + B y + c\|_2^2  \\
=& f(x) + g(y) + \\
&\frac{\rho}{2} \left( \frac{2 u^T}{\rho}(A x + B y + c) + (A x + B y + c)^T(A x + B y + c) + \frac{u^T u}{\rho^2}\right) - \frac{u^T u}{2 \rho}  \\
=& f(x) + g(y) + \frac{\rho}{2}\left\|A x + B y + c + \frac{u}{\rho}\right\|_2^2 -  \frac{u^T u}{2 \rho} \\
=& f(x) + g(y) + \frac{\rho}{2}\left\|A x + B y + c + w\right\|_2^2 - \frac{\rho}{2} \|w\|_2^2 \\
\end{align*}
$$

Update Rule:
$$
\begin{align*}
x^{(k+1)} 
&= \arg\min_x L_{\rho}(x, y^{(k)}, w^{(k)}) \\
&= \arg\min_x \left( f(x) + \frac{\rho}{2}\left\|A x + B y^{(k)} + c + w^{(k)}\right\|_2^2 \right) \\
y^{(k+1)} 
&= \arg\min_y L_{\rho}(x^{(k+1)}, y, u^{(k)}) \\
&= \arg\min_y \left( g(y) +  \frac{\rho}{2}\left\|A x^{(k+1)} + B y + c + w^{(k)}\right\|_2^2\right) \\
w^{(k+1)} &= w^{(k)} +  (A x^{(k+1)} + B y^{(k+1)} + c )
\end{align*}
$$