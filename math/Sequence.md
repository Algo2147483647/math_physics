# Sequence

[TOC]

## Define

$$
f: \mathbb N \to S  \tag{Sequence}
$$
$$
(a_1, a_2, \cdots, a_n)  \tag{Finite sequence}
$$
$$
(a_1, a_2, \cdots)  \tag{Infinite sequence}
$$

A sequence $f: \mathbb N \to S$ can be defined as a [function](./Function.md) from natural numbers (the positions of elements in the sequence) to the elements at each position.

## Properties

### Limitation

- Define  
  $$
  \lim_{n \to \infty} x_n=a \Leftrightarrow |x_n-a|<ε, \forall ε>0, \exists N \in Z_+, n > N  \tag{Limit of Sequence}
  $$

- Property
  - Uniqueness
  - Boundedness
  - 保号性

### Series

- Define

  A series refers to the sum of the terms of a sequence. Given a sequence $a_n$, the series $S$ is given by:
  $$
  S = \sum_{i=0}^\infty a_i  \\
  S_n = \sum_{i=0}^n a_i
  $$

### Convergence of sequence

### Subsequence

- Define  
  Subsequence of a sequence $(a_n)$ is $(a_{g(n)})$ where $g : \mathbb N \to \mathbb N$ is strictly increasing.  

- Problem 
  * Sort

  * Maximum Subarray Sum
    - Purpose  
      For a given sequence $a$, we aim to find the maximum sum of a contiguous subarray.
      $$
      \begin{align*}
        \max_{x \subseteq a} \sum x
      \end{align*}
      $$

    - Algorithm  
      Dynamic Program,
      $$
      f_i = \max(f_{i-1}, 0) + a_i
      $$
      $$
      s^* = \max_{i=1}^n(f_i)
      $$
      where $f_i$ refer to the maximum sum of a contiguous subarray ending at $a_i$. 

  * Longest Subsequence Problem
  * Sequence Palindrome
    - Include
      * Longest Palindrome Subsequence 
        - Purpose 
          $$
          \begin{align*}
            \max_{x \subseteq a} \quad & n_x = \text{number}(x)  \\
            s.t. \quad & x_i = x_{n_x - i + 1}  \quad ; i = 1:n_x  \tag{Palindrome}
          \end{align*}
          $$

        - Algorithm  
          Dynamic programming,
          $$
          \begin{align*}
            f(s,e) &= \left\{\begin{matrix}
              f(s-1,e+1) + 2 \quad & f(s,e) > 0 \ \text{and}\  a_{s-1} = a_{e+1}  \\
              0 \quad & other.
              \end{matrix}\right.  \\
            f(s,s) &= 1  \tag{initial}  \\
            f(s,s+1) &= 2 \quad ;a_s = a_{s+1}  \\
          \end{align*}
          $$
          $f()$: $a_{s:e}$的回文字数, 不是回文序列则为0.

      * Maximum Palindrome Prefix
        - Purpose  
          $$
          \begin{align*}
            \max_{x \in 1:n_a} \quad & x  \\
            s.t. \quad & a_i = x_{x - i + 1}  \quad ; i = 1:x  \tag{Palindrome}
          \end{align*}
          $$

  * Sequence Matching
    - Purpose  
      For two given sequences $a, b$, where $\text{number}(b) \le \text{number}(a)$, and we aim to find the first place where $b$ matching the successive subsequence of $a$.
      $$
      \begin{align*}
        \min\quad& k \\
        s.t.\quad& b = a_{k:k+n_b-1}
      \end{align*}
      $$

    - Property  
      - The next place possible matched is $k+i-l_i$, from the place $k$ in $a$ and $b_{1:i} = a_{k:k+i-1}$.

        $$
        l_i = \text{length}_\text{Longest Prefix-Suffix}(b_{1:i})
        $$
        $$
        \begin{align*}
          b_{1:i} = a_{k:k+i-1} \Rightarrow
          b_{1:l_i} &= a_{k+i-l_i:k+i-1}  \tag{match}\\
          b_{1:l'} &≠ a_{k+i-l':k+i-1}  \quad ; l' > l_i  \tag{mismatch}
        \end{align*}
        $$

    - Algorithm
      * Knuth-Morris-Pratt Algorithm  
        For a place $k$ in sequence $a$ and $b_{1:i} = a_{k:k+i-1}$, we judge whether is the matched place. If not, we use the property above to arrive the place $k'$ possible matched and do the same thing, untill find the answer.
        $$
        \begin{matrix}
          k \gets& k+i-l_i \quad; b_{i+1} \neq a_{k+i}\\
          i \gets& i+1 \quad; b_{i+1} = a_{k+i}\\
        \end{matrix}
        $$

  * Dynamic Time Warping , DTW

## Include

## Parents

- [Function](./Function.md): 

