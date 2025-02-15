# Linear Transformation

[TOC]

## Define

$$
T(k \boldsymbol x + l \boldsymbol y) = k(T \boldsymbol x) + l(T \boldsymbol y)
$$
Linear Transformation is a [mapping](./Function.md) $T: V \to V$ for a [linear space](./Linear_Space.md) $V$, $\forall \boldsymbol x \in V$ there is a unique $\boldsymbol y \in V$ corresponding to it, and the linear condition is satisfied. Meanwhile, linear Transformation can represent by matrix $\boldsymbol A$ and matrix multiply, where the matrix $\boldsymbol A$ can be obtained by the unit base vectors $(\boldsymbol e_1, ..., \boldsymbol e_n)$ after transformation, 

$$
T(\boldsymbol x) = \boldsymbol A \boldsymbol x \\
\boldsymbol A = (T(\boldsymbol e_1), ..., T(\boldsymbol e_n))
$$

> **Proof**: $T(\boldsymbol x) = \boldsymbol A \boldsymbol x$,   
> $$
>\begin{align*}
> T(\boldsymbol x)
> &= T \left(\sum_{i=1}^{\dim} x_i \boldsymbol e_i \right) \tag{$\boldsymbol x 
> = \sum_{i=1}^{\dim} x_i \boldsymbol e_i$} \\
>   &= \sum_{i=1}^{\dim} x_i T(\boldsymbol e_i)  \tag{Linear Transformation}\\
>   &= \sum_{i=1}^{\dim} x_i \boldsymbol a_i  \tag{$T(\boldsymbol e_i) = \boldsymbol a_i$}\\
>   &= \boldsymbol A \boldsymbol x
> \end{align*}
> $$

<img src="./assets/transformations-1694683776868-3.svg" alt="transformations-1694683776868-3" style="zoom: 13%;" />

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


### Invariant Subspace
$$
\forall x \in V_1, V_1 \subseteq V, T x \in V_1
$$
### Eigenvalues & Eigenvectors

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

  - Hamilton-Cayley Theorem
    $$
    \varphi(A) = A^n + a_1 A^{n-1}+ ... +a_{n-1} A + a_n I = 0
    $$
    Matrix is the root of its characteristic polynomial.

### Moore-Penrose Inverse

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

### Special linear transformation

#### Identity transformation

$$
T x = x \quad (\forall x \in V) \\
$$

#### Zero transformation

$$
T x = 0 \quad (\forall x \in V)
$$

#### Orthogonal Transformation

$$
\langle x, x \rangle = \langle T x, T x \rangle
$$
Orthogonal Transformation is a linear transformation in the inner product space that keeps the length of any vector unchanged.
Orthogonal matrix:
$$
\boldsymbol A \boldsymbol A^T = \boldsymbol I  \\
\boldsymbol A \boldsymbol A^H = \boldsymbol I
$$

##### Rotation Transformation

Rotation Transformation Matrix:  

$$
\boldsymbol A = \left(\begin{matrix}
\boldsymbol I \\ & cos \theta |_{(i,i)}&  & \sin \theta |_{(i,j)} \\ & & \boldsymbol  I \\ & -\sin \theta |_{(j,i)} & & \cos \theta |_{(j,j)} \\ & & & & \boldsymbol  I
\end{matrix}\right)
$$

- $\theta$ is the angle of clockwise rotation between dimension $i$ and $j$.

##### Reflection Transformation

$$
y = H x = (I - 2 e_2 e_2^T) x
$$
- Proof  
$$
\begin{align*}
x - y &= e_2 · (e_2^T x)  \\
\Rightarrow y &= (I-2 e_2 e_2^T) x
\end{align*}
$$

#### Symmetry Transformation

$$
\langle T x, y \rangle = \langle x, T y \rangle
$$
Symmetry Matrix:
$$
\boldsymbol A^T = \boldsymbol A  \\
\boldsymbol A^H = \boldsymbol A
$$

#### Projection transformation & Orthogonal Projection transformation

Projection transformation: Suppose the subspace $L$ of the linear space and its complement $M$, the projection transformation is the transformation of the projection of the linear space along $M$ to $L$.

Projection matrix:  
$$
P_{L|M} = \left(\begin{matrix} X & 0 \end{matrix}\right) \left(\begin{matrix} X & Y \end{matrix}\right)^{-1}
$$

Orthogonal Projection transformation: Assume the subspace $L$ of the linear space and its orthogonal complement $L_\bot$. The transformation of the projection of the linear space along $L_\bot$ to $L$ is called orthogonal projection transformation.

Orthogonal Projection matrix:  
$$
P_L = X(X^H X)^{-1}X^H
$$
- $X = (x_1, ... , x_r)$: basis of the projected subspace.

- Property  
  - $P_{L|M}^2 = P_{L|M}$ 
  - $P_L (a \boldsymbol x + b \boldsymbol y) = a (P_L \boldsymbol x) + b (P_L \boldsymbol y)$
  - $x \in L \Leftrightarrow P_L x = x$
  - $x \in L_\bot \Leftrightarrow P_L x = 0$
  - if $H$ is a inner product space, and $L$ is a subspace of $H$ with Orthonormal Basis $\{u_1, ...u_n\}$, then the projection of $x \in H$ is
    $$
    \hat x = \sum_{i=1}^n \frac{u_i^T x}{u_i^T u_i} u_i
    $$

#### Sheer transformation

Sheer transformation Matrix:  The $(i,j)-$th element of the identity matrix is changed to the shear ratio $a_{ij}$

##### Scale Transformation

Scale Transformation Matrix:
$$
T = \left(\begin{matrix} Δx_1 \\ & Δx_2 \\ & & \ddots \\ & & & Δx_n \end{matrix}\right)
$$

## Include

## Parents

- [Function](./Function.md): 

- [Linear_Space](./Linear_Space.md): 

