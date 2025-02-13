# Stochastic Process

[TOC]

## Define

A Stochastic Process $X(t, \omega), \omega \in \Omega, t \in T$ is defined as a collection of random variables defined on a [Probability Space](./Probability_Space.md) $(Ω, \mathcal F, P)$, and these random variables indexed by set $T$.

Note
- When the time $t$ is fixed, the random process degenerates into a random variable.
- When the random sample $ζ$ is determined, the random process degenerates into a continuous time function

## Properties

* Correlation Function & Covariance Function
  - Define  
    $$
    \begin{align*} 
      Corr(X(t_1), Y(t_2)) 
      &= \mathbb E(X(t_1) Y(t_2))  \tag{Correlation function}\\
    
      Corr(X(t_1), X(t_2)) 
      &= \mathbb E(X(t_1) X(t_2))  \tag{AutoCorrelation function}\\
    
      Cov(X(t_1), Y(t_2)) 
      &= \mathbb E((X(t_1) - \mu_X(t_1)) (Y(t_2) - \mu_Y(t_2)))  \tag{Covariance function}\\
      &= \mathbb E(X(t_1) X(t_2)) - \mu_X(t_1) \mu_Y(t_2)  \\
      &= Corr(X(t_1), Y(t_2)) - \mu_X(t_1) \mu_Y(t_2)  \\
    
      Cov(X(t_1), X(t_2)) 
      &= \mathbb E((X(t_1) - \mu(t_1)) (X(t_2) - \mu(t_2)))  \tag{AutoCovariance function}\\
      &= \mathbb E(X(t_1) X(t_2)) - \mu(t_1) \mu(t_2)  \\
      &= Corr(X(t_1), X(t_2)) - \mu(t_1) \mu(t_2) 
    \end{align*} 
    $$

  - Property  
    - $X, Y \ \text{Uncorrelated} \Leftrightarrow Cov(X(t_1), Y(t_2)) = 0, \quad \forall t_1, t_2$

    - $X, Y \ \text{Orthogonality} \Leftrightarrow Corr(X(t_1), Y(t_2)) = 0, \quad \forall t_1, t_2$

- Independence



Example: 

- Simple process
  $$
  X(t, ζ) = X(ζ) f(t)
  $$

- Random Sine Wave
  $$
  X(t, ζ) = A(ζ) \sin(\omega_0 t + \Theta(ζ))
  $$



### Stationary Process & Weakly Stationary Process


$$
\mathbb P (x(t_1), ... , x(t_n)) = \mathbb P (x(t_1+\tau), ..., x(t_n+\tau)) \quad ;\forall \tau, t_1, ..., t_n \in \mathbb R, n \in \mathbb N  \tag{Stationary}
$$
Stationary process is a stochastic process in which the joint distribution of any set of time-indexed random variables is invariant to shifts in time (the statistical properties of the process are constant over time).

$$
R_{XX}(t_1 - t_2 ,0) = R_{XX}(t_1, t_2) \quad; \forall t_1, t_2 \in \mathbb R  \tag{Weakly Stationary}
$$
Weakly stationary process is a stochastic process in which the mean, variance and autocovariance (or autocorrelation) of the process are constant over time, but the joint distribution of the variables may depend on the time index.
- Property
- Power Spectral Density  
  Power Spectral Density is the Fourier transform of autocorrelation function of Weak-sense stationary process.  
  Power Spectral Density consists of real numbers greater than 0.

#### Problem: Test the Stationary
* Unit Root Test 

### Gaussian Process

$$
\{X_t \ |\ t \in T, (X_{t_1},...,X_{t_k}) \sim \mathcal N(\cdot, \cdot), \forall t_1,...,t_k \in T\}
$$
Gaussian Process is a time continuous stochastic process $\{X_t \ |\ t \in T\}$ such that the random vector $(X_{t_1},...,X_{t_k})$ obeys multivariate Gaussian distribution for any finite set of indices $t_1,...,t_k \in T$.

* Autoregressive Process
  $$
  X_t = \epsilon_t + \alpha_0 + \sum\limits_{i=1}^p \alpha_i X_{t-i}  \tag{Autoregressive}
  $$

  Autoregressive Process is a discrete-time stochastic process in which the current value of a time series variable depends linearly on its past values. Where $p$ is the order of autoregressive process, which means the length of the associated historical value.

### Stochastic Point Process

Stochastic Point Process is a collection of random variables $\{X(t) : t \ge 0\}$, where $X(t)$ represents the location or time of occurrence of a point at time $t$. 

Include
* Poisson Point Process
  
  Poisson point process is a stochastic process that models the random spatial distribution of events in a continuous space, which satisfies,
  * Spatial homogeneity. For any region $A$, the value of the number of events occurring in the region $N(A)$ depends only on the size of the Lebesgue measure  (such as area, volume) of $A$ and is independent of the position and shape of $A$. 
  * Independent. For any disjoint measurable regions $A_1, A_2, \ldots, A_n$, the random variables $N(A_1), N(A_2), \ldots, N(A_n)$ are independent of each other.
  * The average rate of occurrence of events is constant throughout the space. And, $N(A)$ follows a Poisson distribution with constant intensity $\lambda> 0$. Where $\mu_A$ is the Lebesgue measure of $A$,
      $$
      \mathbb P(N(A) = n) = \frac{\lambda \cdot \mu_A}{n!} e^{\lambda \cdot \mu_A}
      $$
      $$
      \mathbb E(N(A)) = \lambda \cdot \mu_A
      $$

## Include

- [Markov_Process](./Markov_Process.md): 

- [Martingale](./Martingale.md): 

## Parents

- [Probability_Space](./Probability_Space.md): 

