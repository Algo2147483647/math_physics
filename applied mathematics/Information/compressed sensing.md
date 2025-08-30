# Compressed Sensing

[TOC]

## Problem

### Context

如何从少量的线性测量中重建一个稀疏或可压缩的信号？



- How to design $A$
- How to solve $x$


$$
\min_{\boldsymbol x} \quad & ||\boldsymbol x||_0 \\
s.t. \quad & \boldsymbol A \boldsymbol x = \boldsymbol b
$$

- $A \in \mathbb C^{m\times n}$
- $\boldsymbol x \in \mathbb C^n$
- $\boldsymbol b \in \mathbb C^m, m << n$

求有无穷多解的线性方程问题.

简化: L0范数非凸且问题为NP-hard, 通过转换为L1范数问题, 将问题简化:
$$
\min_{\boldsymbol x} \quad & ||\boldsymbol x||_1 = \sum_{i=1}^n |x_i|\\
s.t. \quad & \boldsymbol A \boldsymbol x = \boldsymbol b
$$

## Resolution

Restricted Isometry Property
$$
(1 - \delta) ||\boldsymbol x|| ≤ ||\boldsymbol A \boldsymbol x|| ≤ (1 + \delta) ||\boldsymbol x||
$$

- isometry constant

### Orthogonal Matching Pursuit

每次迭代选取一个与信号最匹配的解来逐步逼近原始信号，并计算信号的残差，然后从残差中找出最优的解。

$$
\begin{align*}
\boldsymbol A &= (\boldsymbol a_1, ..., \boldsymbol a_n)\\
\hat{\boldsymbol A} &= (\frac{\boldsymbol a_1}{||\boldsymbol a_1||}, ..., \frac{\boldsymbol a_n}{||\boldsymbol a_n||})
\end{align*}
$$
$$
\boldsymbol w = \boldsymbol A^T \boldsymbol b = \left(\begin{matrix} \hat{\boldsymbol a_1}^T \boldsymbol b \\ \vdots \\ \hat{\boldsymbol a_n}^T \boldsymbol b \end{matrix}\right)
$$
**步骤**

- 初始化
$$
\begin{align*}
\boldsymbol r_0 &\gets \boldsymbol b\\
Λ_0 &\gets \emptyset \\
\boldsymbol x_0 &\gets \boldsymbol 0_{n}
\end{align*}
$$
- 迭代
$$
for\ k \gets 1:s
$$
- 计算贡献度，并找到贡献最大的基向量，
$$
Λ_k = Λ_{k-1} \cap \{ \arg\max_{i \in 1:n, i \notin Λ_{k-1}} |\boldsymbol a_i^T \boldsymbol r_{k-1}| \}
$$
$$
\boldsymbol A_k = \boldsymbol A_{Λ_k}
$$

- 计算残差, 最小均方误差

$$
\begin{align*}
\boldsymbol x_k(i \in Λ_k) &\gets \arg\min_{\boldsymbol x} ||\boldsymbol A_k \boldsymbol x - \boldsymbol b||_2 = \boldsymbol A_k^+ \boldsymbol b\\
\boldsymbol x_k(i \notin Λ_k) &\gets 0\\
\boldsymbol r_k &\gets \boldsymbol b - \boldsymbol A \boldsymbol x_k
\end{align*}
$$

