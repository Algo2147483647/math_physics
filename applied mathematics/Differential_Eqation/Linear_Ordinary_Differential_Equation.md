# Linear Ordinary differential equation

[TOC]

## Define

[Ordinary differential equation](./Ordinary_Differential_Equation.md)

### Homogeneous linear differential equation

$$
\frac{d^n y}{dx^n} + a_{1}\frac{d^{n-1} y}{dx^{n-1}} + \cdots + a_{n-1}\frac{dy}{dx} + a_n y = 0
$$
### Non-homogeneous Linear Differential Equation

$$
\frac{d^n y}{dx^n} + a_{1}\frac{d^{n-1} y}{dx^{n-1}} + \cdots + a_{n-1}\frac{dy}{dx} + a_n y = f(x)
$$

## Solve

Homogeneous linear differential equation

特征方程
$$
a_n r^n + a_{n-1} r^{n-1} + \cdots + a_1 r + a_0 = 0
$$

1. 如果特征方程有$n$个不同的实根$r_1, r_2, ..., r_n$，则方程的通解是这些根对应的指数函数的线性组合：
   $$
   y(x) = c_1 e^{r_1 x} + c_2 e^{r_2 x} + \cdots + c_n e^{r_n x}
   $$

2. 如果特征方程有重根，比如说$r_1$是一个$m$重根，那么每个重根会对应$m$个线性独立的解，形如$e^{r_1 x}, xe^{r_1 x}, ..., x^{m-1}e^{r_1 x}$。

3. 如果特征方程有复数根，它们将以共轭对的形式出现，比如$\alpha \pm \beta i$。对于每对复共轭根，相应的解将是实部和虚部的指数函数和三角函数的组合：
   $$
   e^{\alpha x}(c_3 \cos(\beta x) + c_4 \sin(\beta x))
   $$

将所有这些类型的解组合起来，就可以得到$n$阶齐次线性微分方程的通解。通解中将包含$n$个独立的任意常数，这些常数需要根据具体的初始条件或边界条件来确定。

## Include

### Homogeneous First order linear differential equation

$$
\frac{dy}{dx} + P(x)y = 0
$$



#### Solve

$$
\int \frac{dy}{y} = \int -P(x) dx  \\
y(x) = e^{\int -P(x) dx} + C
$$

### Non-homogeneous First order linear differential equation

$$
\frac{dy}{dx} + P(x)y = Q(x)
$$

#### Solve

$$
\mu(x) = e^{\int P(x) dx}
$$

$$
\Rightarrow\quad y(x) = \frac{1}{\mu(x)} \left(\int \mu(x) Q(x) dx + C \right)
$$

- Proof
  $$
  \begin{align*}
  \mu(x)\frac{dy}{dx} + \mu(x)P(x)y &= \mu(x)Q(x) \\
  \frac{d}{dx}(\mu(x)y) &= \mu(x)Q(x)  \\
  \mu(x)y &= \int \mu(x)Q(x) dx + C \\
  \Rightarrow\quad y(x) &= \frac{1}{\mu(x)} \left(\int \mu(x) Q(x) dx + C \right)
  \end{align*}
  $$

### Homogeneous Second-order linear differential equation

$$
\frac{d^2 y}{dx^2}  + a(x) \frac{dy}{dx} + b(x) y = 0
$$

$$
\frac{d^2 y}{dx^2}  + a(x) \frac{dy}{dx} + b(x) y = 0
$$

#### Solve

characteristic equation
$$
r^2 + pr + q = 0
$$
解这个二次方程将会得到两个根 $r_1$ 和 $r_2$。根据这两个根的性质，方程的通解有以下几种可能的形式。在这些解中，$C_1$ 和 $C_2$ 是积分常数，这些常数通常通过初始条件或边界条件来确定。

1. **实数且不相等的根** ($r_1 \neq r_2$):
   $$
   y(x) = C_1e^{r_1x} + C_2e^{r_2x}
   $$

2. **重根** ($r_1 = r_2 = r$):
   $$
   y(x) = (C_1 + C_2x)e^{rx}
   $$

3. **复数根** ($r_1 = \alpha + \beta i$, $r_2 = \alpha - \beta i$):
   $$
   y(x) = e^{\alpha x}(C_1\cos(\beta x) + C_2\sin(\beta x))
   $$

### Non-homogeneous Second-order linear differential equation

$$
\frac{d^2 y}{dx^2}  + a(x) \frac{dy}{dx} + b(x) y = Q(x)
$$

#### Solve

$$
y(x) = y_0(x) + y^*(x)
$$

解包括两部分：齐次解$y_0(x)$和一个特定的非齐次解 $y^*(x)$。

非齐次解 $y_p(x)$ 可以通过几种不同的方法找到，例如：

1. **常数变易法**: 通过设定 $y_p(x)$ 为齐次解的形式但将常数替换为 $x$ 的函数来求解。

2. **待定系数法**: 如果 $f(x)$ 是多项式、指数、正弦或余弦函数，或者这些函数的线性组合，可以通过假设 $y_p(x)$ 是与 $f(x)$ 形式相似的函数，并确定这个假设函数的系数来求解。

3. **格林函数法**: 这是一种更为复杂的方法，涉及到积分变换和对方程的格林函数的使用。

### Bernoulli differential equation

$$
\frac{dy}{dx} + P(x)y = Q(x)y^n \quad, n \neq 0,1
$$

#### Solve

$$
(1-n) y^{-n}\frac{dy}{dx} + P(x)(1-n) y^{1-n} = (1-n) Q(x)
$$

let $z = y^{1-n}$, and $\frac{dz}{dx} = (1 - n) y^{-n} \frac{dy}{dx}$
$$
\frac{dz}{dx} + (1-n)P(x) z = (1-n) Q(x)  \\
$$

### Euler Cauchy equation

$$
x^n \frac{d^n y}{dx^n} + a_{1}x^{n-1}\frac{d^{n-1} y}{dx^{n-1}} + \cdots + a_{n-1}x\frac{dy}{dx} + a_n y = 0
$$

#### Solve

let $x = e^t$
$$
\begin{align*}
\frac{dy}{dx} &= \frac{dy}{dt} \cdot \frac{dt}{dx} = \frac{1}{x} \frac{dy}{dt}  \\
\frac{d^2y}{dx^2} &= \frac{d}{dx}\left(\frac{1}{x} \frac{dy}{dt}\right) = \frac{1}{x^2} \frac{d^2y}{dt^2} - \frac{1}{x^2} \frac{dy}{dt}  \\
\vdots  \\
\frac{d^ny}{dx^n} &= \frac{1}{x^n} \frac{d^ny}{dt^n} - \text{lower order terms}.
\end{align*}
$$

$$
\frac{d^ny}{dt^n} + b_{1}\frac{d^{n-1} y}{dt^{n-1}} + \cdots + b_{n-1}\frac{dy}{dt} + b_n y = 0
$$

特征方程
$$
r^n + b_{1}r^{n-1} + \cdots + b_{n-1}r + b_n = 0
$$
解这个代数方程将得到 $n$ 个根，它们可能是实数或复数，可以是简单的或重复的。对于每个不同的实数根 $r$，解的一部分将是 $e^{rt}$ 的形式；对于重根，解将包括 $t$ 的相应幂次乘以 $e^{rt}$；对于复数根，解会包含指数和三角函数。

最后，由于 $t = \ln(x)$，我们必须将解中的 $t$ 替换为 $\ln(x)$，并且因为 $e^{\ln(x)} = x$，最终解的形式将涉及 $x$ 的幂次。

### Legendre equation

$$
(1 - x^2) \frac{d^2 y}{dx^2} - 2x \frac{dy}{dx} + n(n+1)y = 0
$$

### Bessel equation

$$
x^2 \frac{d^2 y}{dx^2} + x \frac{dy}{dx} + (x^2 - n^2)y = 0
$$
