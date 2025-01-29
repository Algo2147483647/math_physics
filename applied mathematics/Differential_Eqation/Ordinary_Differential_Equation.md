# Ordinary Differential Equation

[TOC]

## Define

Ordinary Differential Equation (ODE) is an equation involving a function $y(x)$ of a single variable $x$ and its derivatives. where $y'$ represents the first derivative of $y$ with respect to $x$, $y''$ the second derivative, and $y^{(n)}$ the $n$-th derivative. ([Differential Equation](./Differential_Equation.md))
$$
F(x, y, y', y'', ..., y^{(n)}) = 0
$$

## Solve

### Runge-Kutta Methods

$$
\begin{align*}
  \boldsymbol y' &= f(\boldsymbol  x, \boldsymbol  y)  \\
  \boldsymbol  y(\boldsymbol  x_0) &= \boldsymbol  y_0
\end{align*}
$$
Iterative solve Numerical solution for a point/interval of $\boldsymbol  y(x)$. Over an interval from $t_n$ to $t_{n+1}$, the RK4 method computes the next value $y_{n+1}$ using the current value $y_n$ and the weighted average of four increments, where each increment is a product of the step size $h$ and an estimated slope. These slopes are computed as follows:
$$
y(x + dx) = y(x) + \frac{dx}{6} · (k_1 + 2 k_2 + 2 k_3 + k_4)
$$

$$
\begin{align*}
      k_1 &= f \left(x_n , y_n \right)            \tag{Interval start slope}  \\
      k_2 &= f \left(x_n + \frac{dx}{2}, y_n + \frac{dx}{2}·k_1 \right)   \\
      k_3 &= f \left(x_n + \frac{dx}{2}, y_n + \frac{dx}{2}·k_2 \right)  \\
      k_4 &= f \left(x_n + dx, y_n + dx·k_3 \right)  \tag{Interval end slope}
    \end{align*}
$$

The RK4 method is a single-step method (each $y_{n+1}$ is computed only from $y_n$), but it achieves fourth-order accuracy, which means that the error per step is proportional to $h^5$, and the total error is proportional to $h^4$ when integrated over an interval.

```python
def runge_kutta_4(ode_func, y0, t0, tf, n_steps):
    """
    Fourth Order Runge-Kutta method (RK4) for solving ODEs

    :param ode_func: The ODE to solve (function)
    :param y0: Initial condition (float)
    :param t0: Initial time (float)
    :param tf: Final time (float)
    :param n_steps: Number of steps (int)
    :return: Tuple of numpy arrays (t, y)
    """
    # Define the step size
    h = (tf - t0) / n_steps

    # Initialize the arrays to store the solution
    t = np.linspace(t0, tf, n_steps + 1)
    y = np.zeros(n_steps + 1)

    # Set the initial condition
    y[0] = y0

    # Perform the RK4 iteration
    for i in range(n_steps):
        k1 = h * ode_func(t[i], y[i])
        k2 = h * ode_func(t[i] + h / 2, y[i] + k1 / 2)
        k3 = h * ode_func(t[i] + h / 2, y[i] + k2 / 2)
        k4 = h * ode_func(t[i] + h, y[i] + k3)

        y[i + 1] = y[i] + (k1 + 2 * k2 + 2 * k3 + k4) / 6

    return t, y
```

理论上，Runge-Kutta 方法可以用于求解任意的常微分方程初值问题，只要满足以下条件：

1. **函数 \( f(t, y) \) 需要是良定义的**：对于所有在初值问题中考虑的 \( t \) 和 \( y \) 值，函数 \( f(t, y) \) 必须有明确定义的值。

2. **函数 \( f(t, y) \) 应该满足利普希茨条件**：简而言之，这意味着函数的斜率不能在任何区间内无限增大，这是为了确保解的存在性和唯一性。

## Include

### Linear ordinary differential equation


### Nonlinear ordinary differential equation