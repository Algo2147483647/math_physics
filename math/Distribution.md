# Distribution

[TOC]

## Define

Let $X$ be a [random variable](./Random_Variable.md) from a probability space $(\Omega, \mathcal F, \mathbb P)$ to a measurable space $(E, \mathcal E)$. The distribution of $X$ is the [probability measure](./Probability_Measure.md) on $(E, \mathcal E)$ defined by
$$
\mu_X(B) = \mathbb P(X \in B) = \mathbb P(X^{-1}(B)),
\qquad B \in \mathcal E
$$
Equivalently,
$$
\mu_X = \mathbb P \circ X^{-1}
$$
so the distribution is the pushforward of the underlying probability measure by $X$.

## Properties

### Conceptual Role

The distribution records all probability information about $X$ that depends only on values of $X$, not on the particular sample-space realization.

Thus two random variables may have the same distribution without being equal pointwise.

### Integration Against a Distribution

For a measurable function $g$,
$$
\mathbb E[g(X)] = \int_E g(x)\,\mu_X(\mathrm d x)
$$
whenever the integral exists.

This is the measure-theoretic basis of the law-of-the-unconscious-statistician.

### Discrete Probability Distribution 

#### 0-1 distribution ; Bernoulli distribution

- Define  
  It is the discrete probability distribution of a random variable which 
  $$
  \begin{align*}
  \mathbb P(X = 1) &= p  \\
  \mathbb P(X = 0) &= 1 - p
  \end{align*}
  $$

- Property
  | property | value |
  |---|---|
  | Support | $k\in \{0,1\}$ |
  | Probability mass function | $\begin{array}{ll} \mathbb P(X = 1) = p\\ \mathbb P(X = 0) = 1 - p\end{array}$ |
  | Cumulative distribution function | $\mathbb P(X \le x) = \left\{\begin{array}{ll} 0 & \text { if } x<0 \\ 1-p & \text { if } 0 \leq x<1 \\ 1 & \text { if } x \geq 1 \end{array}\right.$ |
  | Mean | $\mathbb E(x) = p$ |
  | Variance | $D(x) = p (1 - p)$ |
  | Skewness | $\frac{1 - 2 p}{\sqrt{p (1 - p)}}$ |
  | Kurtosis | $\frac{1 - 6 p (1 - p)}{p (1 - p)}$ |
  | Entropy | $-p \ln p - (1-p) \ln (1-p)$ |


#### Binomial distribution 

- Define  
  When n independent Bernoulli trials are performed with the same success probability $p$, the Binomial distribution with parameters $n$ and $p$ is the distribution of $X$, which is the number $n$ of successes.
  $$\mathbb P(X = k) = C^k_n p^k (1-p)^{n-k}$$

- Property  
  | property | value |
  |---|---|
  | Mean | $\mathbb E(x) = n p$ |
  | Variance | $D(x) = n p(1 - p)$ |
  |||

#### Geometric distribution 

- Define  
  $$\mathbb P(X = k) = p (1-p)^{n-1}$$
  描述连续独立重复实验中, 首次成功所进行的实验次数.

- Property
  | property | value |
  |---|---|
  | Mean | $\mathbb E(x) = \frac{1}{p}$ |
  | Variance | $D(x) = \frac{1 - p}{p^2}$ |
  |||

#### Hypergeometric distribution 

- Define  
  $$\mathbb P(X = k) = \frac{C_M^k C_{N_M}^{n-k}}{C_N^n}$$

- Property  
  | property | value |
  |---|---|
  | Mean | $\mathbb E(x) = \frac{n M}{N}$ |
  | Variance | $D(x) = \frac{n M}{N} (1 - \frac{M}{N}) \frac{N - M}{N - 1}$ |
  |||

#### Poisson distribution 

- Define  
  Poisson process： 
  $$\mathbb P(X = k) = \frac{λ^k}{k!} e^{-λ}$$

  2D & n-D Poisson process：
  - the number of events in a region A is distributed $Pois(\lambda · area(A))
  - the numbers of events in disjoint regions are independent of each other.

- Property  
  | property | value |
  |---|---|
  | Mean | $\mathbb E(x) = λ$ |
  | Variance | $D(x) = λ$ |
  |||

- Theorem{Poisson定理}  
  $$\lim_{n \to \infty, p \to 0, λ = n p} \frac{C_M^k C_{N_M}^{n-k}}{C_N^n} = \frac{λ^k}{k!} e^{-λ}$$

### Continuity Probability Distribution 

#### Uniformity distribution 

- Define  
  $$
  \begin{align*}
    f(x) = \left\{\begin{matrix} \frac{1}{b-a} &\quad a < x < b \\ 0 &\quad other \end{matrix}\right.  \\
    F(x) = \left\{\begin{matrix} 0 &\quad x < a \\ \frac{1}{b-a} &\quad a ≤ x < b \\ 1 &\quad b ≤ x \end{matrix}\right.
  \end{align*}
  $$

- Property  
  | property | value |
  |---|---|
  | Mean | $\mathbb E(x) = \frac{a + b}{2}$ |
  | Variance | $D(x) = \frac{(b - a)^2}{12}$ |
  |||

#### Normal distribution 

- Define
  $$
  \begin{align*}
    f_X(x) &= \frac{1}{\sqrt{2 π} \sigma} e^{-\frac{(x - μ)^2}{2 \sigma^2}} \quad; x \in (-\infty, +\infty)  \\
    f_{\boldsymbol X}(\boldsymbol x) &= \frac{1}{(2 π)^{\frac{n}{2}} |\boldsymbol Σ|^{\frac{1}{2}}} e^{-\frac{(\boldsymbol x - \boldsymbol μ)\boldsymbol Σ^{-1}(\boldsymbol x - \boldsymbol μ)^T}{2}} \tag{Multivariate Normal distribution }
  \end{align*}
  $$

  * Standard Normal distribution 
    $$f_X(x) = \frac{1}{\sqrt{2 π}} e^{-\frac{x^2}{2}} \quad; x \in (-\infty, +\infty)$$
    $$μ = 0, \sigma^2 = 1$$

- Property  
  - basic parameters 
    | property | value |
    |---|---|
    | Mean | $\mathbb E(x) = μ$ |
    | Variance | $\begin{array}{ll} D(x) = \sigma^2 \\ D(\boldsymbol x) = \boldsymbol Σ \end{array}$ |
    |||


> Proof  
> $$
> \begin{align*}
>   D(x) &= \frac{1}{(2 π)^{\frac{D}{2}}} \frac{1}{|\boldsymbol Σ|^{\frac{1}{2}}} \sum_{i=1}^D \sum_{j=1}^D \boldsymbol u_i \boldsymbol u_j^T \int e^{-\sum\limits_{k=1}^D \frac{\boldsymbol y_k^2}{2 λ_k}} y_i y_j \mathrm d \boldsymbol y   \\
>     &= \frac{1}{(2 π)^{\frac{D}{2}}} \frac{1}{|\boldsymbol Σ|^{\frac{1}{2}}} \sum_{i=1}^D \boldsymbol u_i \boldsymbol u_i^T \int e^{-\sum\limits_{k=1}^D \frac{y_k^2}{2 λ_k}} y_i^2 \mathrm d \boldsymbol y  \tag{$i ≠ j, \boldsymbol u_i \boldsymbol u_j^T=0, \boldsymbol u_i \boldsymbol u_j$ 正交}  \\
>     &= \frac{1}{(2 π)^{\frac{D}{2}}} \frac{1}{|\boldsymbol Σ|^{\frac{1}{2}}} \sum_{i=1}^D \boldsymbol u_i \boldsymbol u_i^T \int \prod_{k=1}^D e^{-\frac{y_k^2}{2 λ_k}} y_i^2 \mathrm d \boldsymbol y   \\
>     &= \frac{1}{(2 π)^{\frac{D}{2}}} \frac{1}{|\boldsymbol Σ|^{\frac{1}{2}}} \sum_{i=1}^D \boldsymbol u_i \boldsymbol u_i^T \left(\int_{-\infty}^{+\infty} e^{-\frac{y_i^2}{2 λ_i}} y_i^2 \mathrm d y_i × \prod_{k=1, k ≠ i}^D \int_{-\infty}^{+\infty} e^{-\frac{y_X^2}{2 λ_k}} \mathrm d y_k \right)  \tag{积分乘法结合律}  \\
>     &= \frac{1}{(2 π)^{\frac{D}{2}}} \frac{1}{|\boldsymbol Σ|^{\frac{1}{2}}} \sum_{i=1}^D \boldsymbol u_i \boldsymbol u_i^T \left((2 π λ_i)^{\frac{1}{2}} · λ_i × \prod_{k=1, k ≠ i}^D(2 π λ_k)^{\frac{1}{2}} \right)  \tag{见下面推导}  \\
>     &= \frac{1}{(2 π)^{\frac{D}{2}}} \frac{1}{|\boldsymbol Σ|^{\frac{1}{2}}}  · \left((2 π)^{\frac{D}{2}} \prod_{k=1}^D λ_k \right) · \left(\sum_{i=1}^D \boldsymbol u_i \boldsymbol u_i^T λ_i\right)   \\
>     &= \sum_{i=1}^D \boldsymbol u_i \boldsymbol u_i^T λ_i  \tag{$\prod_{k=1}^D λ_k=|\boldsymbol Σ|^{\frac{1}{2}}$}  \\
>     &= \boldsymbol Σ
> \end{align*}
> $$
>
> when $k = i$,
> $$
> \begin{align*}
>   \int_{-\infty}^{+\infty} e^{-\frac{y_λ^2}{2 λ_i}} y_i^2 \mathrm d y_i &=(λ_i \sqrt{2 λ_i}) · \int_{-\infty}^{+\infty} \left(\frac{y_i^2}{2 λ_i} \right)^{\frac{1}{2}} e^{-\frac{y_λ^2}{2 λ_i}} \mathrm d \frac{y_i^2}{2 λ_i}   \\
>   &= (λ_i \sqrt{2 λ_i}) · 2 Γ(3/2)  \tag{$Γ(z) = \int_0^{+\infty} x^{z-1} e^{-x} \mathrm d x$}  \\
>   &= \sqrt{2 π λ_i} · λ_i  \tag{$Γ(3/2) = \frac{\sqrt{π}}{2}$}
> \end{align*}
> $$
>
> when $k ≠ i$,
> $$
> \begin{align*}
>   \int_{-\infty}^{+\infty} e^{-\frac{y_λ^2}{2 λ_k}} \mathrm d y_k &=(\sqrt{\frac{λ_k}{2}}) · \int_{-\infty}^{+\infty} \left(\frac{y_k^2}{2 λ_k} \right)^{-\frac{1}{2}} e^{-\frac{y_λ^2}{2 λ_k}} \mathrm d \frac{y_k^2}{2 λ_k}   \\
>   &= \left(\sqrt{\frac{λ_k}{2}}\right) · 2 Γ(\frac{1}{2})  \tag{$Γ(z) = \int_0^{+\infty} x^{z-1} e^{-x} \mathrm d x$}  \\
>   &= \sqrt{2 π λ_k}  \tag{$Γ(\frac{1}{2}) = \sqrt{π}$}
> \end{align*}
> $$
> $\square$

- Conditional Distributions  
  A multivariable $\boldsymbol x$ is partitioned as follows
  $$
  \boldsymbol x = \left(\begin{matrix}\boldsymbol x_1 \\ \boldsymbol x_2\end{matrix}\right) \sim \mathcal N \left(\left(\begin{matrix}\boldsymbol \mu_1 \\ \boldsymbol \mu_2\end{matrix}\right), \left(\begin{matrix} \boldsymbol \Sigma_{11} & \boldsymbol \Sigma_{12}\\ \boldsymbol \Sigma_{21} & \boldsymbol \Sigma_{22}\end{matrix}\right)\right)
  $$

  Then the distribution of $\boldsymbol x_1$ conditional on $\boldsymbol x_2 = a$ is still a multivariate normal 
  $$
  (\boldsymbol x_1\ |\ \boldsymbol x_2 = \boldsymbol a) \sim \mathcal N\left(\boldsymbol \mu_1 + \boldsymbol \Sigma_{12} \boldsymbol \Sigma_{22}^{-1} (\boldsymbol a - \boldsymbol \mu_2), \boldsymbol \Sigma_{11} - \boldsymbol \Sigma_{12} \boldsymbol \Sigma_{22}^{-1} \boldsymbol \Sigma_{21} \right)
  $$

#### Rayleigh  distribution

- Define  
  $$
    f_X(x) = \frac{x}{σ^2} e^{\frac{-x^2}{2 σ^2}}
  $$

#### $Γ$ distribution 

- Define
  $$
    f(x) = \left\{\begin{matrix} \frac{1}{β^α Γ(α)} x^{a^{-1}} e^{-x / β} &\quad x \in (0, +\infty) \\ 0 &\quad x \in (-\infty, 0] \end{matrix}\right.
  $$
- Property  
  | property | value |
  |---|---|
  | Mean | $\mathbb E(x) = α β$ |
  | Variance | $D(x) = α β^2$ |
  |||

  when $α=1$, $Γ$ distribution 退化为Exponential distribution;  
  when $α=\frac{n}{2}, β=\frac{1}{2}$, $Γ$ distribution 退化为$\chi^2$ distribution.

#### Exponential distribution 

- Define  
  $$
  f(x) = \left\{\begin{matrix} λ e^{-λ x} &\quad x \in (0, +\infty) \\ 0 &\quad x \in (-\infty, 0] \end{matrix}\right.
  $$
  $$
  F(x) = \left\{\begin{matrix} λ 1 - e^{-λ x} &\quad x \in (0, +\infty) \\ 0 &\quad x \in (-\infty, 0] \end{matrix}\right.
  $$

- Property
  | property | value |
  |---|---|
  | Mean | $\mathbb E(x) = θ$ |
  | Variance | $D(x) = θ^2$ |
  |||

#### $\chi^2$ distribution 

- Define
  $$
  \frac{1}{2^{\frac{n}{2}} Γ(\frac{n}{2})} x^{\frac{n}{2} - 1} e^{-x / 2}
  $$

- Property
  | property | value |
  |---|---|
  | Mean | $\mathbb E(x) = n$ |
  | Variance | $D(x) = 2 n$ |
  |||

## Include

- [Joint_Distribution](./Joint_Distribution.md): subtype_of

## Parents

- [Probability_Measure](./Probability_Measure.md): subtype_of

- [Random_Variable](./Random_Variable.md): induces
