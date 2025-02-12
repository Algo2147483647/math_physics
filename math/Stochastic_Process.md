# Stochastic Process

[TOC]

## Define

A Stochastic Process $X(t, \omega), \omega \in \Omega, t \in T$ is defined as a collection of random variables defined on a [Probability Space](./Probability_Space.md) $(Ω, \mathcal F, P)$, and these random variables indexed by set $T$.

- Note
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

## Include

- [Markov_Process](./Markov_Process.md): 

- [Martingale](./Martingale.md): 

## Parents

- [Probability_Space](./Probability_Space.md): 

