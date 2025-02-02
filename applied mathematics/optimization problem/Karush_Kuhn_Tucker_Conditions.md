# $Karush\text{-}Kuhn\text{-}Tucker\ Optimality\ Conditions$
[TOC]

## Describe

$$
\begin{align*}
  f_i(\boldsymbol x^*) &≤ 0  \quad , i = 1,...,m  \tag{Primal feasibility}  \\
  h_i(\boldsymbol x^*) &= 0  \quad , i = 1,...,p  \\
  \boldsymbol λ^* &⪰ 0  \tag{Dual feasibility}  \\
  λ_i^* f_i(\boldsymbol x^*) &= 0 \quad , i = 1,...,m  \tag{Complementary slackness, $L(\boldsymbol x^*, \boldsymbol λ^*, \boldsymbol ν^*) = f_0(\boldsymbol x^*)$对偶间隙为零}  \\
  ∇L(\boldsymbol x^*, \boldsymbol λ^*, \boldsymbol ν^*) &= ∇ f_0(\boldsymbol x^*) + \sum_i λ_i^* ∇ f_i(\boldsymbol x^*) + \sum_i ν_i^* ∇ h_i(\boldsymbol x^*) = 0  \tag{Stationarity, $L(\boldsymbol x, \boldsymbol λ^*, \boldsymbol ν^*)$ 在$\boldsymbol x^*$取极值}
\end{align*}
$$
Where, the objective function $f_0$ and constraint function $f_i, h_i$ are differentiable.  

If the original problem is nonconvex, and $\boldsymbol x^*, (\boldsymbol λ^*, \boldsymbol ν^*)$ is the optimal solution of the original problem and dual problem $\Rightarrow (\boldsymbol x^*, \boldsymbol λ^*, \boldsymbol ν^*)$ meet the KKT conditions.

If the original problem is convex, we have $(\boldsymbol x^*, \boldsymbol λ^*, \boldsymbol ν^*)$ meet the KKT conditions $\Leftrightarrow \boldsymbol x^*, (\boldsymbol λ^*, \boldsymbol ν^*)$ are the optimal solutions of the original problem and the dual problem respectively.

- Proof
  - (1)(2) 式, 说明$\boldsymbol x^*$是原问题的可行解.
  - (3) 式, 说明$\boldsymbol x^*$是对偶问题的可行解. 又$\because$ 原问题是凸问题, $\therefore$ $L()$函数是$\boldsymbol x$的凸函数.
  - (5) 式, 说明$L(\boldsymbol x, \boldsymbol λ^*, \boldsymbol ν^*)$ 在$\boldsymbol x^*$处取得极值. 又$\because$ $L()$函数是$\boldsymbol x$的凸函数, $\therefore$ $L()$ 在$\boldsymbol x^*$取得极小值.  
    $$
    \begin{align*}
      \Rightarrow g(\boldsymbol λ^*, \boldsymbol ν^*) &= \inf_{\boldsymbol x} L(\boldsymbol x, \boldsymbol λ^*, \boldsymbol ν^*)  \\
        &= L(\boldsymbol x^*, \boldsymbol λ^*, \boldsymbol ν^*)  \tag{$L()$在$\boldsymbol x^*$取极小}
    \end{align*}
    $$

  - (4) 式, 说明$\boldsymbol x^*$处, $L(\boldsymbol x^*, \boldsymbol λ^*, \boldsymbol ν^*) = f_0(\boldsymbol x^*)$  
    $$
    \Rightarrow g(\boldsymbol λ^*, \boldsymbol ν^*) = f_0(\boldsymbol x^*)  \tag{代入}
    $$
    又$\because$ 弱对偶性有,   
    $$
    \max_{\boldsymbol λ, \boldsymbol ν} g(\boldsymbol λ, \boldsymbol ν) ≤ \min_{\boldsymbol x} f_0(\boldsymbol x)
    $$
    $\therefore$ 强对偶性成立, 且在$\boldsymbol x = \boldsymbol x^*$和$(\boldsymbol λ^*, \boldsymbol ν^*)$处取得原问题和对偶问题的最优值, 对偶间隙为零.  
