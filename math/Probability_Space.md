# Probability Space

[TOC]

## Define

$$
<Ω, \mathcal F, \mathbb P>  \tag{Probability Space}
$$
Probability Space is a [measure space](./Measurable_Space.md) including, 

- $Ω$: sample space
- $\mathbb P$: Probability, a measure of the sample space $Ω$.
- $\mathcal F$: a $\sigma$-algebra of the sample space $Ω$.

### Probability

$$
\mathbb P: \mathcal F \to [0, 1]  \tag{Probability}
$$

Probability is a set function, a measure of a set, and satisfies (Kolmogorov axiomatization):

- Nonnegativity $\mathbb P(A) \in [0, 1] \quad ; \forall A \in F$
- Normative $\mathbb P(Ω) = 1$
- Countable Additivity 
$$
\mathbb P \left(\bigcup_i A_i \right) = \sum_i \mathbb P(A_i)
$$

## Properties

### Large number theorem

$$
\begin{align*}
\lim\limits_{n \to ∞} \mathbb P \left(\left|\frac{1}{N} \sum_{k=1}^n X_k-μ \right|<ε \right) = 1  \tag{Weak large number theorem}\\
\lim\limits_{n \to ∞} \mathbb P\left(\left|\frac{f_A}{n}-p \right|<ε\right) = 1  \tag{Bernoulli large number theorem}
\end{align*}
$$

### Central Limit Theorem

$$
\begin{align*}
  \lim\limits_{n \to ∞} F_n(x) &= \lim\limits_{n \to ∞} \mathbb P \left(\frac{\sum\limits_{k=1}^n X_k - n μ}{\sqrt{n} σ} ≤ x \right)  \\
  &= \int_{-∞}^x \frac{1}{\sqrt{2 π}} e^{-t^2 / 2} \mathrm d t  \\
  &= \Phi(x)
\end{align*}
$$

### Joint Probability

$$
\mathbb P(A B)
$$
The probability of A and B occurring together.

### Conditional Probability

$$
\mathbb P(B | A)
$$
Probability of occurrence of $B$ under the condition that $A$ occurs.

#### Property

- Independence 
  $$
  Independence \Leftrightarrow \mathbb P(A B) = \mathbb P(A) \mathbb P(B)
  $$
  The occurrence of $A$ and $B$ does not affect each other.

- relationship between Joint \& Conditional probability
  $$
  \begin{align*}
    \mathbb P(B | A) &= \frac{\mathbb P(A B)}{\mathbb P(A)}  \\
    \mathbb P(A B) &= \mathbb P(B | A) \mathbb P(A) = \mathbb P(A | B) \mathbb P(B)
  \end{align*}
  $$

- Theorem -- Total Probability Theorem
  $$
  \mathbb P(A) = \sum_i \mathbb P(A|B_i) \mathbb P(B_i) \quad; \sum_i A_i = Ω
  $$

- Bayes formula
  $$
  \begin{align*}
    \mathbb P(A | B) &= \frac{\mathbb P(B | A) \mathbb P(A)}{\mathbb P(B)}  \\
    \mathbb P(A_i | B) &= \frac{\mathbb P(B | A_i) \mathbb P(A_i)}{\sum\limits_j \mathbb P(B|A_j) \mathbb P(A_j)}; \sum_j A_j = Ω
  \end{align*}
  $$

## Include

- [Random_Variable](./Random_Variable.md): 

- [Stochastic_Process](./Stochastic_Process.md): 

## Parents

- [Measurable_Space](./Measurable_Space.md): is-a

