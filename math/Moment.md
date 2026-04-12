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

### Expectation

$$
\begin{align*}
  \mathbb E(X) = \mu_x &= \sum x_i \mathbb P_X(x_i)  \tag{Discrete}  \\
    &= \int_{-\infty}^\infty x f_X(x) \mathrm d x  \tag{Continuous}  \\
  \mathbb E(\boldsymbol X) &= \left(\begin{matrix} \bar X_i \\ \vdots \end{matrix}\right) 
\end{align*}
$$

- Property
  $$
  \begin{align*}
    \mathbb E(Y) &= \int_{-\infty}^\infty g(x) f_X(x) \mathrm d x  \\
    Y &= g(X)  \tag{$g$ is a measurable function}
  \end{align*}
  $$

### Variance & Standard Deviation

$$
\begin{align*}
  Var(X) = \sigma_x^2 &= \mathbb E((X - \mu_x)^2)  \tag{Variance}\\
  \sigma_x &= \sqrt{\mathbb E((X - \mu_x)^2)}  \tag{Standard Deviation}
\end{align*}
$$

- Property
  - $Var(X) = \mathbb E((X - \mu_x)^2) = \mathbb E(X^2) - \mathbb E(X)^2$

### Skewness  

$$
\mathbb E\left(\frac{(X - \mu_x)^3}{\sigma_x^3}\right)  \tag{3-order Central Moment}
$$

### Kurtosis  

$$
\mathbb E\left(\frac{(X - \mu_x)^4}{\sigma_x^4}\right)  \tag{4-order Central Moment}
$$

### Mixed Moment  

$$
\begin{align*}
  &\mathbb E(X^i Y^j) \tag{$ij$-order Joint Moment}  \\
  &\mathbb E((X-\bar X)^i (Y-\bar Y)^j) \tag{$ij$-order Joint Central Moment}
\end{align*}
$$

##

## Include

## Parents

- [Random_Variable](./Random_Variable.md): property_of

