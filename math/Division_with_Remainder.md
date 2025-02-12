# Division with Remainder

[TOC]

## Define

([Integer_Ring](./Integer_Ring.md))

For $a,b \in \mathbb Z, b \neq 0$, there are unique $q,r\in \mathbb Z, 0 ≤ r < b$ satisfy
$$
a = q \times b + r
$$

we called $q$ is Division, $r$ is Remainder.
$$
\begin{align*}
  a / b &= q  \tag{Division}\\
  a \% b &= r  \tag{Remainder}\\
  a &\equiv r \mod b
\end{align*}
$$

If $r = 0$, then we called the $q$ and $b$ is two Factors of $a$, and $b$ divides $a$, $b | a$. For any $a$, $1, a$ are always Factors of $a$.
$$
b | a \quad\Leftrightarrow\quad (\exists c \in \mathbb Z) a = b \times c
$$

## Properties

- /
  $$
  \begin{align*}
    (a + b) \% c &= (a \% c + b \% c) \% c  \\
    (a - b) \% c &= (a \% c - b \% c + c) \% c  \\
    (a · b) \% c &= ((a \% c) · (b \% c)) \% c  \\
    (a / b) \% c &= (a · b^{-1}) \% c = ((a \% c) · (b^{-1} \% c)) \% c  \tag{$b^{-1}$:$b$的逆元}
  \end{align*}
  $$

- Inverse element
  $(a · c) % b = 1$, 则$c$是$a$在$mod\ b$下的逆元$a^{-1}$

### [Prime](./Prime.md)

### Common Divisor & Common Multiple

- Define  
  A Common Divisor $c$ of two number $a, b \in \mathbb Z$ is a number such that 
  $$
  a = k_a \times c, \quad b = k_b \times c
  $$

  A Common Multiple $c$ of two number $a, b \in \mathbb Z$ is a number such that 
  $$
  c = k_a \times a, k_b \times b
  $$

- Property
  * Greatest Common Divisor & Least Common Multiple
    - Define  
      Greatest Common Divisor is the maximum Common Divisor of two number $a, b \in \mathbb Z$ except $1$. 

      $$
      gcd(a, b) = \arg\max_c\ c \quad s.t.\ c | a, c | b
      $$

      Least Common Multiple is the minimum Common Multiple of two number $a, b \in \mathbb Z$.

      $$
      lcm(a, b) = \arg\min_c\ c \quad s.t.\ a | c, b | c
      $$
      
    - Property
      - /
        $$
        \begin{align*}
          gcd(a, b) &= gcd(b, a)  \\
          gcd(a, b) &= gcd(a - b, b) \quad;(a ≥ b)  \\
          gcd(a, b) &= gcd(a \% b, b)  \\
          gcd(k a, k b) &= gcd(k a, b)  \\
        \end{align*}
        $$

      - $lcm(a, b) = \frac{a \times b}{gcd(a, b)}$

      - $c | a, c | b \Rightarrow c | (u a + v b)$ 
        - proof
          $$
          \begin{align*}  
            u a + v b 
            &= u \times k_a \times c + v \times k_b \times c \\
            &= k \times c
          \end{align*}
          $$

      - $gcd(a, b) = gcd(b, a \% b)$
        - proof  
          For $a = q \times b + r$,  
          $$
          \begin{align*}  
            gcd(a, b) = gcd(b, a \% b) \Leftrightarrow \left\{\begin{matrix}
            c | a, c | b &\Rightarrow  c | r  &\text{(1)}\\
            c | b, c | r &\Rightarrow  c | a  &\text{(2)}
            \end{matrix}\right.
          \end{align*}
          $$
          For (1), 
          $$
          \begin{align*}
            \Rightarrow\quad k_a \times c &= k_b \times c \times q + r  \\
            \Rightarrow\quad r &= (k_b \times q - k_a) \times c  
          \end{align*}
          $$
  
          For (2), 
          $$
          \begin{align*}
            \Rightarrow\quad a 
            &= k_b \times c \times q + k_r  \times c  \\
            &= (k_b \times q + k_r)  \times c
          \end{align*}
          $$
  
    - Algorithm: Euclid's Algorithm -- finding Greatest Common Divisor
      $$
      \begin{align*}
        a = q \times b + r &\Rightarrow gcd(a, b) = gcd(b, a \% b)  \\
        a = q \times b &\Rightarrow gcd(a, b) = b
      \end{align*}
      $$
  
      ```cpp
      int gcd(int a, int b) { return b == 0 ? a : gcd(b, a %b); }
      ```

### Linear Diophantine Equation

- Define
  $$a x + b y = c$$
  where, $a, b, c \in \mathbb Z$ is ciefficient, $x, y  \in \mathbb Z$ is unknown number.

- Property
  - $ax + by = c$ has a solution $\quad\Leftrightarrow\quad$ $\text{gcd}(a, b) \% c = 0$

- Algorithm
  * Extended Euclidean Algorithm
    - Purpose  
      Solve the $x, y  \in \mathbb Z$ in equations:
      $$a x + b y = \text{gcd}(a, b)$$

    - Process  
      Start with two integers $a, b \in \mathbb Z$, where $a \ge b$.

      If $b \% a = 0$, return $gcd(a, b) = b$, $(x, y) = (0, 1)$, because of $0 \cdot a + 1 \cdot b = b$.

      If $b \% a \neq 0$, we solve $b x' + (a \% b) y' = gcd(b, a \% b)$, and
      $$\begin{align*}
        x &= y'\\
        y &= x' - \text{int}(a / b) \cdot y'
      \end{align*}$$

      ```c
      // a >= b
      int gcdExtended(int a, int b, int *x, int *y) {
          if (b == 0) { *gcd = a; *x = 1; *y = 0; return a; }
      
          int x1, y1, gcd = gcdExtended(b, a % b, &x1, &y1);
          *x = y1;
          *y = x1 - (a / b) * y1;
          return gcd;
      }
      ```

- Include
  * System of Linear Diophantine Equations
    - Define  
      $$A X = C$$ 
      where, $A \in \mathbb Z^{m \times n}$ is a matrix of integers, $X \in \mathbb Z^n$ is a vector of unknowns and $C \in \mathbb Z^m$ is a vector of integers.

    - Include
      * Chinese Remainder Theorem
        - Purpose   
          Solve a class of linear Diophantine systems of equations: 
          $$\begin{align*}
            x - n_1 x_1 &= a_1  \\
            \vdots &= \vdots  \\
            x - n_k x_k &= a_k
          \end{align*}$$  
          
          where, $(n_1, ..., n_k \in \mathbb Z)$ are pairwise coprime integers greater than one, $(x, x_1, ..., x_k \in \mathbb Z)$ are unknowns.

### Congruence Equation

- Define  
  Solve the unknown $0 \le x < m, x \in \mathbb Z$ 
  $$
  f(x) \equiv b \mod m
  $$

- Include
  * Linear Congruence Equation
    - Define  
      A type of Congruence Equation with $f(x) = a x$.
      $$
      a x \equiv b \mod m
      $$

    - Include
      * System of Linear Congruence Equations
        - Purpose
          $$
          \begin{align*}
            \left\{\begin{matrix} x \equiv a_1 \mod m_1 \\ \vdots \\ x \equiv a_n \mod m_n \end{matrix}\right.
          \end{align*}
          $$

          $$
          x = k \prod_{i=1}^n m_i + \sum_{i=1}^n a_i \left(\prod_{j=1, j≠i}^n m_j\right) \left(\prod_{j=1, j≠i}^n m_j\right)^{-1}
          $$

### Power Module

- Purpose
  $$
  b = (a^k) \% m
  $$

- Algorithm
  - 逐次平方法
    - 将 k 二进制展开
      $$k = \sum_{i=0}^r u_i·2^i$$

      - Note
        计算机里, k内存天然是二进制

    - 逐次平方制作模$m$的$a$幂次表, $i\in[0,r]$
      $$
      \begin{align*}
        a^{2^0} &= a = A_0 \% m  \\
        a^{2^i} &= (a^{2^{i-1}})^2 = A^{2(i-1)} = A_i % m
      \end{align*}
      $$

    - 乘积
      $$
      \prod_{i=0}^r A_i^{u_i} \% m
      $$
    
    - proof
      $$
      a^k = a^{\sum\limits_{i=0}^r u_i·2^i}
      $$

## Include

- [Prime](./Prime.md): 

## Parents

- [Integer_Ring](./Integer_Ring.md): 

