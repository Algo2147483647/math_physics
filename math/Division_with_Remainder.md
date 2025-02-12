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

## Include

- [Prime](./Prime.md): 

## Parents

- [Integer_Ring](./Integer_Ring.md): 

