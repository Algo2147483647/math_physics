# Proximal Gradient Descent

[TOC]

## Define

**Proximal Operator**:

The proximal operator of a function $g(x)$ is defined as:
$$
\text{prox}_{\lambda g}(v) = \arg\min_{x} \left( g(x) + \frac{1}{2\lambda} \|x - v\|^2 \right)
$$
where $\lambda$ is a positive scalar. Essentially, the proximal operator gives us the point $x$ that balances between being close to $v$ and having a small value of $g(x)$. ([Convex_Optimization_Problem](./Convex_Optimization_Problem.md))

## Process

The steps for the PGD are as follows:
1. Start with an initial point $x_0$.
2. For each iteration $k$:
   - Compute the gradient of the smooth function at the current point: $ \nabla f(x_k) $.
   - Take a gradient step: $ y_{k+1} = x_k - \lambda \nabla f(x_k) $.
   - Apply the proximal operator to update $x$: $ x_{k+1} = \text{prox}_{\lambda g}(y_{k+1}) $.
3. Repeat until convergence.