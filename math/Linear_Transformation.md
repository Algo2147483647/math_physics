# Linear Transformation

[TOC]

## Define

$$
T(k \boldsymbol x + l \boldsymbol y) = k(T \boldsymbol x) + l(T \boldsymbol y)
$$
Linear Transformation is a [mapping](./Function.md) $T: V \to V$ for a [linear space](./Linear_Space.md) $V$, $\forall \boldsymbol x \in V$ there is a unique $\boldsymbol y \in V$ corresponding to it, and the linear condition is satisfied.

<img src="./assets/transformations-1694683776868-3.svg" alt="transformations-1694683776868-3" style="zoom: 13%;" />

We can represent Linear Transformation by matrix $\boldsymbol A$ and matrix multilpy, where the matrix $\boldsymbol A$ can be obtained by the unit base vectors $(\boldsymbol e_1, ..., \boldsymbol e_n)$ after transformation, 
$$
T(\boldsymbol x) = \boldsymbol A \boldsymbol x
$$

$$
\boldsymbol A = (T(\boldsymbol e_1), ..., T(\boldsymbol e_n))
$$

- Proof
  We assume $\boldsymbol A = (T(\boldsymbol e_1), ..., T(\boldsymbol e_n))$, then 

  Proof $T(\boldsymbol e_i) = \boldsymbol A \boldsymbol e_i$, 
  $$
  \begin{align*}
    T(\boldsymbol e_i) 
    &= (T(\boldsymbol e_1), ..., T(\boldsymbol e_n)) (0,...,0,1_i,0,...,0)^T  \\
    &= \boldsymbol A \boldsymbol e_i
  \end{align*}
  $$

  Proof $T(\boldsymbol x) = \boldsymbol A \boldsymbol x$,   
  $$
  \begin{align*}
    \boldsymbol x 
    &= \sum_{i=1}^{\dim} x_i \boldsymbol e_i \\
    \Rightarrow T(\boldsymbol x)
    &= T \left(\sum_{i=1}^{\dim} x_i \boldsymbol e_i \right)  \\
    &= \sum_{i=1}^{\dim} x_i T(\boldsymbol e_i)  \tag{Linear Transformation}\\
    &= \sum_{i=1}^{\dim} x_i \boldsymbol A \boldsymbol e_i   \tag{$T(\boldsymbol e_i) = \boldsymbol A \boldsymbol e_i$}\\
    &= \boldsymbol A \boldsymbol E \boldsymbol x  \\
    &= \boldsymbol A \boldsymbol x
  \end{align*}
  $$

## Properties

### Range 

$$
Range(T)=\{T x | x \in V\}
$$
In linear space,  
the set of results of all vectors after linear transformation;   
the linear space after linear transformation.

- Rank
  $$
  rank(A) = \dim Range(A) = \dim Range(A^T)
  $$
  The dimension of space after transformation.
  The dimension of the range.

### Null Space

$$
Null(T) = \{x | T x = 0\}
$$
In linear space, the set of all original vectors that are linearly transformed into zero vectors.

- $\dim V = \dim Range(A) + \dim Null(A)$  
  变换前线性空间维数 = 值域维数 + 零空间维数. 


### Invariant Subspace

$$
\forall x \in V_1, V_1 \subseteq V, T x \in V_1
$$

### Eigenvalues & Eigenvectors

- Define
  $$
  \boldsymbol A \boldsymbol x = λ \boldsymbol x
  $$
  
  - $x$: Eigenvectors, a vector whose direction does not change before and after linear transformation;  
  - $λ$: Eigenvalues, proportion of length change of eigenvector after linear transformation.

- Property
  * Eigenvalue Decomposition & Singular Value Decomposition
  
  - Characteristic polynomial
    $$
    \varphi(λ) = |λ I - A| = λ^n + a_1 λ^{n-1} + ... + a_{n-1} λ + a_n
    $$

  - Theorem -- Hamilton-Cayley Theorem
    $$
    \varphi(A) = A^n + a_1 A^{n-1}+ ... +a_{n-1} A + a_n I = 0
    $$
    Matrix is the root of its characteristic polynomial.

### Moore-Penrose Inverse

- Define  
  The solution satisfying the following equation,
  $$
    \left\{\begin{matrix}
      A X A = A\\
      X A X = X\\
      (A X)^H = A X\\
      (X A)^H = A X\\
    \end{matrix}\right.
  $$
  When the rank of cols is full, $A^+ = (A^H A)^{-1} A^H$   
  When the rank of rows is full,  $A^+ = A^H (A A^H)^{-1}$

- Property
  - $rank(A) = rank(A^H A) = rank(A A^H)$
  - 满秩分解算广义逆 $A^+ = G^H (F^H A G^H)^{-1} F^H$

### Similarity

- Define  
  $A$ is similar to $B$, $A ~ B$:
  $$
  \exists \text{Nonsingular Matrix}P \Rightarrow B = P^{-1} A P
  $$

- Property 
  - $A ~ A$ 
  - $A ~ B \Leftrightarrow B ~ A$ 
  - $A ~ B, B ~ C \Leftrightarrow A ~ C$
  - The eigenvalues and eigenvectors of similar matrices are the same.
  - The trace of similar matrix is the same.

### Transformation of linear transformation matrix under different bases

$$
A_Y = C^{-1} A_X C \quad ; Y = C X
$$

- Proof
  $$
  \begin{align*}
    T Y &= Y A_Y     \tag{Define}\\ 
    T X C &= X C A_Y   \tag{$ Y = X C $}\\
    X A_X C &= X C A_Y   \tag{$ T X = X A_X $}\\
    A_X C &= C A_Y  \\
    A_Y &= C^{-1} A_X C
  \end{align*}
  $$

## Include

## Parents

- [Function](./Function.md): 

- [Linear_Space](./Linear_Space.md): 

