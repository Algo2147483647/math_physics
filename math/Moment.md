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

#### Include

* Correlation & Covariance  
  $$
  \begin{align*}
    Corr(X,Y) &= \mathbb E(X Y)  &\tag{Correlation}  \\
  
    Cov(X,Y) 
    &= \mathbb E((X-\bar X) (Y-\bar Y))   \tag{Covariance}  \\
    &= \mathbb E(X Y) - \mathbb E(X) \mathbb E(Y)  \\
    &= Corr(X,Y) - \mathbb E(X) \mathbb E(Y)  \\
  
    R_{\boldsymbol X\boldsymbol X} &= \mathbb E(\boldsymbol X \boldsymbol X^T)  \\
    &= \left(\begin{matrix} E(X_i X_j) & ... \\ \vdots & \ddots \end{matrix}\right)  \tag{AutoCorrelation matrix}  \\
    \boldsymbol \Sigma_{\boldsymbol X\boldsymbol X} &= \mathbb E((\boldsymbol X - \bar{\boldsymbol X}) (X - \bar{\boldsymbol X})^T)  \tag{AutoCovariance matrix}\\
    &= \left(\begin{matrix} E((X_i - \bar X_i) (X_j - \bar X_j)) & ... \\ \vdots & \ddots \end{matrix}\right)  
  \end{align*}
  $$
  
  - Include
    * Correlation Coefficient
      $$
      \begin{align*}
        \rho 
        &= \frac{Cov(X,Y)}{Cov(X,X) Cov(Y,Y)}  \\
        &= \frac{\mathbb E(XY) - \mathbb E(X) \mathbb E(Y)}{\sqrt{\mathbb E(X^2) - \mathbb E(X)^2} \sqrt{\mathbb E(Y^2) - \mathbb E(Y)^2}}
      \end{align*}
      $$
      
      - Property
        - $\rho_{XY} \in [-1, 1]$, Correlations equal to $+1$ or $-1$ correspond to data points lying exactly on a line.
        - $\rho_{XY} = \rho_{YX}$
        - $\rho_{XY} = \rho_{(a + b X)\ (c + d Y)} \quad; b, d > 0$  
          it is invariant under separate changes in location and scale in the two variables.
  
  - Property
    - $Cov(X,Y) = Cov(Y,X)$
    - $Cov(X,X) = Var(X,X)$
    - relation between AutoCorrelation & AutoCovariance matrix
      $$
      \boldsymbol \Sigma_{\boldsymbol X\boldsymbol X} = \boldsymbol R_{\boldsymbol X\boldsymbol X} - \bar{\boldsymbol X} \bar{\boldsymbol X}^T
      $$
    - Autocovariance matrix $\Sigma_{\boldsymbol X\boldsymbol X}$ is a positive semi-definite matrix.
    - $\boldsymbol Y = \boldsymbol A \boldsymbol X \Rightarrow \boldsymbol \Sigma_{\boldsymbol Y\boldsymbol Y} = \boldsymbol A \boldsymbol \Sigma_{\boldsymbol X\boldsymbol X} \boldsymbol A^T$

### Moment Generating Function

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

