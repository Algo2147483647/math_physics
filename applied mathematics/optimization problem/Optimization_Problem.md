# Optimization Problem

[TOC]
## Define

$$
\begin{align*}
  \min \quad & f_0(x)  \tag{Objective Function}\\
  s.t. \quad & f_i(x) \le  0  \tag{Inequality Constraint}\\
        & h_i(x) = 0  \tag{Equality Constraint}
\end{align*}
$$

$$
p^*= \inf \{f_{0}(x) | f_i(x) \le  0, h_i(x) = 0 \}  \tag{Optimal solution}
$$

Optimization Problem aims to find the minimal values called optimal solution $p^*$ of objective function $f_0(\cdot)$, subject to the constraints $f_i(\cdot), h_i(\cdot)$.


## Property

### Lagrange Function  

$$
L(\boldsymbol x, \boldsymbol \lambda , \boldsymbol ν) = f_0(\boldsymbol x) + \sum_i \lambda _i f_i(\boldsymbol x) + \sum_i ν_i h_i(\boldsymbol x)
$$
- $f_0, f_i, h_i$ is the objective function and constraint function of the standard form optimization problem.

### Lagrange Dual function & Dual Problem

$$
\begin{align*}
  g(\boldsymbol \lambda , \boldsymbol ν) &= \inf_{\boldsymbol x \in D}\ L(\boldsymbol x, \boldsymbol \lambda , \boldsymbol ν)  \\
    &= \inf_{\boldsymbol x \in D}\ f_0(\boldsymbol x) + \sum_i \lambda _i f_i(\boldsymbol x) + \sum_i ν_i h_i(\boldsymbol x)
\end{align*}
$$

Dual Problem
$$
\begin{align*}
  \max_{\boldsymbol \lambda , \boldsymbol ν} \quad & g(\boldsymbol \lambda , \boldsymbol ν)  \\
  s.t. \quad & \boldsymbol \lambda  ⪰ 0
\end{align*}
$$

Symbol:

- $L: \mathbb  R^n \times  \mathbb  R^m \times  \mathbb  R^p \to \mathbb  R,\quad  dom\ L: D \times  \mathbb  R^m \times  \mathbb  R^p$

#### Property

- Even if the original problem is non convex, the Dual function is still a concave function.


$$
g(\boldsymbol \lambda , \boldsymbol ν) \le  p^*
$$

Dual function构成原问题的下界. 
Dual function是一族关于$(\boldsymbol \lambda , \boldsymbol ν)$的仿射函数的逐点下确界.

> Proof
> 设$\tilde{\boldsymbol x}$是原问题的一个可行点,  
> 
> $$
> \begin{align*}
> \Rightarrow \lambda _i f_i(\tilde{\boldsymbol x}) &\le  0  \tag{$\boldsymbol \lambda  ⪰ 0, f(\tilde{\boldsymbol x}) \le  0$}  \\
> ν_i h_i(\tilde{\boldsymbol x}) &= 0  \tag{$h(\tilde{\boldsymbol x}) = 0$}  \\
> \Rightarrow \sum_i \lambda _i f_i(\tilde{\boldsymbol x}) + \sum_i ν_i h_i(\tilde{\boldsymbol x}) &\le  0 \\
> \Rightarrow  L(\tilde{\boldsymbol x}, \boldsymbol \lambda , \boldsymbol ν) = f_0(\tilde{\boldsymbol x}) + \sum_i \lambda _i f_i(\tilde{\boldsymbol x}) + \sum_i ν_i h_i(\tilde{\boldsymbol x}) &\le  f_0(\tilde{\boldsymbol x})  \\
> \Rightarrow  g(\boldsymbol \lambda , \boldsymbol ν) &\le  p^*
> \end{align*}
> $$

##### Duality
Weak Duality: $p^* ≥ d^*$ 一定存在
Strong Duality: $p^* = d^*$

##### Slate Condition

##### Karush-Kuhn-Tucker Optimality Conditions

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

> Proof
> - (1)(2) 式, 说明$\boldsymbol x^*$是原问题的可行解.
> - (3) 式, 说明$\boldsymbol x^*$是对偶问题的可行解. 又$\because$ 原问题是凸问题, $\therefore$ $L()$函数是$\boldsymbol x$的凸函数.
> - (5) 式, 说明$L(\boldsymbol x, \boldsymbol λ^*, \boldsymbol ν^*)$ 在$\boldsymbol x^*$处取得极值. 又$\because$ $L()$函数是$\boldsymbol x$的凸函数, $\therefore$ $L()$ 在$\boldsymbol x^*$取得极小值.  
>   $$
>   \begin{align*}
>     \Rightarrow g(\boldsymbol λ^*, \boldsymbol ν^*) &= \inf_{\boldsymbol x} L(\boldsymbol x, \boldsymbol λ^*, \boldsymbol ν^*)  \\
>       &= L(\boldsymbol x^*, \boldsymbol λ^*, \boldsymbol ν^*)  \tag{$L()$在$\boldsymbol x^*$取极小}
>   \end{align*}
>   $$
>
> - (4) 式, 说明$\boldsymbol x^*$处, $L(\boldsymbol x^*, \boldsymbol λ^*, \boldsymbol ν^*) = f_0(\boldsymbol x^*)$  
>   $$
>   \Rightarrow g(\boldsymbol λ^*, \boldsymbol ν^*) = f_0(\boldsymbol x^*)  \tag{代入}
>   $$
>   又$\because$ 弱对偶性有,   
>   $$
>   \max_{\boldsymbol λ, \boldsymbol ν} g(\boldsymbol λ, \boldsymbol ν) ≤ \min_{\boldsymbol x} f_0(\boldsymbol x)
>   $$
>   $\therefore$ 强对偶性成立, 且在$\boldsymbol x = \boldsymbol x^*$和$(\boldsymbol λ^*, \boldsymbol ν^*)$处取得原问题和对偶问题的最优值, 对偶间隙为零.  

##### Lagrange 对偶问题理解

<img src="./assets/20220409.jpg" alt="20220409" style="zoom:12%;" />

- 优化问题
  目标函数不一定是凸函数  
  $$
  \begin{align*}
    \min \quad & f_0(\boldsymbol x)  \tag{目标函数}  \\
    s.t. \quad & f_i(\boldsymbol x) \le  0  \quad  i = 1,...,m  \tag{不等式约束}  \\
      & h_i(\boldsymbol x) = 0  \quad  i = 1,...,p  \tag{等式约束}
  \end{align*}
  $$

- 可行集
  $$
  \begin{align*}
    G &= \{(f_1(x), ... , f_2(x), h_1(x), ... , h_2(x), f_0(x)) \in \mathbb  R^m \times  \mathbb  R^n \times  \mathbb  R \ |\  x \in D\}  \\
      &= \{(\boldsymbol u, \boldsymbol v, t) \ |\  u_i = f_i(x), v_i = h_i(x), t = f_0(x), x \in D\}
  \end{align*}
  $$
  图1. 以只有一个不等式约束为例, 可行集$G$区域如图所示.

- 原问题
  $$
  \begin{align*}
    p^* = \inf\{t \ |\  (\boldsymbol u, \boldsymbol v, t) \in G, \boldsymbol u ⪯ \boldsymbol 0, \boldsymbol v = \boldsymbol 0\}
  \end{align*}
  $$
  图2. 因为$\boldsymbol u ⪯ \boldsymbol 0$, 所以原问题$f_0(\boldsymbol x)$ 最优值如图中$p^*$所示.

- Lagrange 函数
  $$
  \begin{align*}
    L(\boldsymbol x, \boldsymbol \lambda , \boldsymbol ν) &= (\boldsymbol \lambda , \boldsymbol ν, 1)^T (\boldsymbol u, \boldsymbol v, t)  \tag{$(\boldsymbol u, \boldsymbol v, t) \in G, \boldsymbol \lambda  ⪰ 0$}  \\
      &= \sum_i \lambda _i u_i + \sum_i ν_i v_i + t
  \end{align*}
  $$
  图3. 对于可行集$G$中任意一点$(u, t) \in G$, Lagrange 函数的值是经过该点$(u, t)$以斜率$k=-\lambda $的直线, 与纵坐标$t$的交点值. 同时, 因为$\lambda  ⪰ 0$, 所以直线只能斜向下or水平.

- Dual Function
  $$
  \begin{align*}
    g(\boldsymbol \lambda , \boldsymbol ν) &= \inf_{\boldsymbol x}\ L(\boldsymbol x, \boldsymbol \lambda , \boldsymbol ν)  \\
      &= \inf_{\boldsymbol x}((\boldsymbol \lambda , \boldsymbol ν, 1)^T (\boldsymbol u, \boldsymbol v, t))
  \end{align*}
  $$
  图4. Dual function$g(\lambda _0)$是在直线斜率$\lambda  = \lambda _0$固定的情况下, Lagrange 函数的最小值, 即点$(u, t)$在可行集$G$内时, 直线与纵坐标$t$ 最低的交点的值. 同时, 使得直线的可行集$G$下半部分的斜向下的切线.

- 对偶问题
  $$
  d^* = \max_{\boldsymbol \lambda , \boldsymbol ν} \quad  g(\boldsymbol \lambda , \boldsymbol ν)
  $$
  图5. 对偶问题是"最大的最小值", Dual function的最大值, $\max_{\boldsymbol \lambda , \boldsymbol ν} \inf_{\boldsymbol x}\ L(\boldsymbol x, \boldsymbol \lambda , \boldsymbol ν)$.  
  即, 找到可行集$G$下半部分的一条斜向下的切线, 使其与纵坐标的交点的值最大. 如图中$d^*$所示.

- 强对偶性判定  
  弱对偶性: 一定有$p^* ≥ d^*$    
  强对偶性: $p^* = d^*$  
  图6. 图中显示了该问题的对偶性强弱, 因为最优对偶间隙$p^* - d^* > 0$, 故该问题不满足强对偶性.  


## Include

### Feasibility Problem

$$
\begin{align*}
  \min_x \quad & const. \\
  s.t. \quad & f_i(x) \le  0  \\
        & h_i(x) = 0
\end{align*}
$$

If the objective function is equal to a constant, the optimal solution is 0 (Feasible set is not empty) or $\infty$ (Feasible set is empty).

### [Convex Optimization Problem](./Convex_Optimization_Problem.md)

### [Integer Programming & Mixed Integer Programming](./Integer_Programming.md)

### Nonconvex Optimization Problem