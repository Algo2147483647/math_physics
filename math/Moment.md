# Moment

[TOC]

## Define

K-order Moment & K-order Central Moment:
$$
\begin{align*}
  \mathbb E(X^k) &= \sum_i x_i^k \mathbb P_X(x_i)  \tag{Moment (Discrete)}  \\
    &= \int_{-\infty}^\infty x^k f_X(x) \mathrm d x  \tag{Moment (Continuous)}  \\
  \mathbb E((X-\mu_x)^k) &= \sum_i (x_i-\mu_x)^k \mathbb P_X(x_i)  \tag{Central Moment (Discrete)}  \\
    &= \int_{-\infty}^\infty (x-\mu_x)^k f_X(x) \mathrm d x  \tag{Central Moment (Continuous)}
\end{align*}
$$

Symbol: $\mu_x = \mathbb E(X)$

## Properties

### Moment Generating Function

#### Define

Let $X$ be a random variable with CDF $F_X$, the moment generating function $M_X(t)$ of $X$ (or $F_X$) is 
$$
M_X(t) = \mathbb E(e^{tX})
$$

#### Property

- $M_X(t)$ always exists and is equal to 1.

- The moment-generating function is so named because it can be used to find the moments of the distribution. By using the moment generating function, we can calculate the various moments of the random variable $X$. Specifically, the $n$-th moment of $X$ can be obtained by the nth derivative of the moment generating function at $t=0$.
  $$
  E(X^n) = M_X^{(n)}(0)
  $$

- Differentiating $M_X(i)$ $i$ times with respect to $t$ and setting $t=0$, we obtain the i-th moment.
  $$
  \begin{align*}
  M_X(t) &= \mathbb E(e^{tX}) \\
   &= 1 + t E(X) + \frac{t^2 E(X^2)}{2!} + \cdots + \frac{t^n E(X^n)}{n!} + \cdots  \\
   &= 1 + t m_1 + \frac{t^2 m_2}{2!} + \cdots + \frac{t^n m_n}{n!} + \cdots  \\
  \end{align*}
  $$

- If $X$ is a continuous random variable, the following relation between its moment-generating function $M_X(t)$ and the two-sided Laplace transform of its probability density function $f_X(x)$ holds:
  $$
  M_X(t) = \mathcal L\{f_X\}(-t)
  $$
  since the PDF's two-sided Laplace transform is given as
  $$
  \mathcal L\{f_X\}(s) = \int_{-\infty}^{+\infty} e^{-sx} f_X(x) dx
  $$
  and the moment-generating function's definition expands (by the law of the unconscious statistician) to
  $$
  M_X(t) =  \mathbb E(e^{tX}) = \int_{-\infty}^{+\infty} e^{-tx} f_X(x) dx
  $$

## Include

## Parents

- [Random_Variable](./Random_Variable.md): 

