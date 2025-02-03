# Binary Search

[TOC]

## Purpose  
For a sorted array, we aim to find a target value $v$ in the array $a$.

<img src="./assets/7ec7c64b0df75bdd50bcb08f0fcc54ef.png" alt="Binary Search | Binary, Linear search, Algorithm" style="zoom: 50%;" />

## Property  
we assume an ascending array $a = \{a_1, ..., a_n\}$, $a_i \le a_j , i \le j$, then,
$$
a_i < v \quad\Rightarrow\quad a_j < v, \forall a_j \in \{a_1, ..., a_i\}
$$
$$
a_i > v \quad\Rightarrow\quad a_j > v, \forall a_j \in \{a_i, ..., a_n\}
$$

## Process  
We divide the search interval in half, $\text{mid} = \frac{\text{start} + \text{end}}{2}$, and determine whether the middle value $a_{\text{mid}}$ meets the target at each iteration $(t)$. 
$$
a^{(t)} = \{a_{\text{start}},..., a_{\text{end}}\} \to \{a_{\text{start}},..., a_{\text{mid}-1}\} \cup \{a_{\text{mid}}\} \cup \{a_{\text{mid}+1},..., a_{\text{end}}\}
$$

- If satisfied, $a_{\text{mid}}$ is the answer. 
- If not satisfied, just select the half interval that may meet the target value for the naxt interation.

$$
\begin{align*}
    a_{\text{mid}} = v &\quad\Rightarrow\quad \{a_{\text{mid}}\}  \\
    a_{\text{mid}} > v &\quad\Rightarrow\quad a^{(t+1)} = \{a_{\text{start}},..., a_{\text{mid}-1}\}  \\
    a_{\text{mid}} < v &\quad\Rightarrow\quad a^{(t+1)} = \{a_{\text{mid}+1},..., a_{\text{end}}\}
\end{align*}
$$

We repeat the above operation untill the search interval can't be divided and return that there is no target value in the array $a$.

$$\text{start} > (\text{mid}-1) \text{ or } (\text{mid} + 1) > \text{end} \quad\Rightarrow\quad a^{(t+1)} \text{ is invalid}$$