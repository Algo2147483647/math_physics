# $Descent\ Method$

[TOC]

## Include 

### Gradient Descent Method  

$$
\boldsymbol x_{k+1} = x_k - \alpha_k \nabla f(\boldsymbol x_k)
$$

- Include
  * Steepest Descent Method
    $$
    \boldsymbol x_{k+1} = \boldsymbol x_k + \alpha_k \cdot \arg\min \{ (\nabla f(\boldsymbol x_k))^T \boldsymbol v \ |\ ||\boldsymbol v|| = 1 \}
    $$

  * Stochastic Gradient Descent

  * Adaptive Moment Estimation

### Newton-Raphson Method

$$
\boldsymbol x_{k+1} = \boldsymbol x_k - \alpha_k (\nabla^2 f(\boldsymbol x_k))^{-1} \nabla f(\boldsymbol x_k)
$$

```python
def newton_method(f, grad, hessian, x0, tol=1e-6, max_iter=100):
    x = x0
    for _ in range(max_iter):
        g = grad(x)
        H = hessian(x)
        # Compute Newton direction and step size
        dx = np.linalg.solve(H, -g)
        x += dx
        # Check for convergence
        if np.linalg.norm(dx) < tol:
            break
    return x
```

### Quasi-Newton Method

$$
\boldsymbol x_{k+1} = \boldsymbol x_k - \alpha_k B_k^{-1} \nabla f(\boldsymbol x_k)
$$

Where, $B_k^{-1}$ is an approximate Hessian matrix to simplify the time consuming calculation of the Hessian matrix.

### Block coordinate descent

### Alternating Direction Method of Multipliers

交替方向乘子法（Alternating Direction Method of Multipliers）通常用于解决存在两个优化变量的只含等式约束的优化类问题，其中 $f, g$ 都是凸函数
$$
\min_{x, y} \quad& f(x) + g(z)\\
s.t. \quad& A x + B z = c
$$
算法流程: 每一步只更新一个变量而固定另外两个变量，如此交替重复更新。

### Proximal Gradient Descent

适用于：带有可分离非光滑正则化项的凸优化，如L1正则化。对于凸优化问题，当其目标函数存在不可微部分时，近端梯度下降法才会派上用场。

假设目标函数 $f(x) = g(x) + h(x)$, 其中，限定 $g(x)$ 其中，限定 $h(x)$ 是不可微 (或局部不可微) 的凸函数。