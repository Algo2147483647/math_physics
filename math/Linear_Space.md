# Linear Space

[TOC]

## Define

$$
(F, V, +, \cdot)  \tag{Linear Space}
$$

A linear space (vector space) over a field $F$ is a special [module](./Module.md) consisting of a non-empty set $V$ with vector addition and scalar multiplication, satisfying:

- Additive closure: $x + y \in V$
- Scalar multiplication closure: $k x \in V$
- Identity element of vector addition: $x + 0 = x$
- Inverse elements of vector addition: $x + (-x) = 0$
- Identity element of scalar multiplication: $1x = x$
- Commutativity of vector addition: $x + y = y + x$
- Associativity of vector addition: $x + (y + z) = (x + y) + z$
- Compatibility of scalar multiplication with field multiplication: $a(bx) = (ab)x$
- Distributivity of scalar multiplication with respect to vector addition: $a(x + y) = ax + ay$
- Distributivity of scalar multiplication with respect to field addition: $(a + b)x = ax + bx$

## Properties

### Relationship between vectors

#### Linear Independence and Linear Dependence

For a finite list of vectors $(\boldsymbol x_1, \dots, \boldsymbol x_n)$:

Linear independence means
$$
\sum_{i=1}^n a_i \boldsymbol x_i = \boldsymbol 0 \Rightarrow a_1 = \cdots = a_n = 0
$$

Linear dependence means
$$
\exists (a_1,\dots,a_n) \ne (0,\dots,0) \text{ such that } \sum_{i=1}^n a_i \boldsymbol x_i = \boldsymbol 0
$$

### Representation of vectors: Basis

$$
\boldsymbol v = \sum_{i=1}^n a_i \boldsymbol x_i = \boldsymbol X \boldsymbol a
$$

A basis is a linearly independent vector family $\boldsymbol X = (\boldsymbol x_1, \dots, \boldsymbol x_n)$ whose span is the whole space $V$. Every vector $\boldsymbol v \in V$ can be uniquely expressed as a linear combination of basis vectors.

- $\boldsymbol x_i$: basis vector
- $a_i$: coordinate

#### Basis Transformation and Coordinate Transformation

If $\boldsymbol Y$ is a new basis and $\boldsymbol X$ is an old basis, then the basis transformation matrix $\boldsymbol C$ is defined by
$$
\boldsymbol Y = \boldsymbol X \boldsymbol C
$$

Coordinates transform by
$$
\boldsymbol a_x = \boldsymbol C \boldsymbol a_y
$$

> Proof
>
> $$
> \begin{align*}
> \boldsymbol v
> &= \boldsymbol X \boldsymbol a_x  \\
> &= \boldsymbol Y \boldsymbol a_y  \\
> &= \boldsymbol X \boldsymbol C \boldsymbol a_y
> \end{align*}
> $$
> Hence $\boldsymbol a_x = \boldsymbol C \boldsymbol a_y$.

- Property  
  The basis transformation matrix $\boldsymbol C$ is nonsingular.

#### Dimension

The dimension of a finite-dimensional vector space is the number of vectors in any basis.

#### Span

$$
\operatorname{Span}(\boldsymbol x_1,\dots,\boldsymbol x_n) = \left\{\boldsymbol v \mid \boldsymbol v = \sum_{i=1}^n a_i \boldsymbol x_i \right\}
$$

The span is the set of all linear combinations of the given vectors.

### Linear Subspace

A linear subspace is a nonempty subset of a linear space that is closed under vector addition and scalar multiplication.

- Additive closure: $x,y\in V_1 \Rightarrow x+y \in V_1$
- Scalar multiplication closure: $x \in V_1 \Rightarrow kx \in V_1$

### Dual Space

$$
V^*=\left\{f:V\rightarrow F \mid f \text{ is a linear map}\right\}
$$

The dual space $V^*$ of $V$ is the vector space of all linear functionals from $V$ to the base field $F$. For a finite-dimensional real column vector, a dual vector can be represented as a row vector.

$$
\left(\begin{matrix}v^*_1  & \cdots & v^*_n\end{matrix} \right)
\left(\begin{matrix}v_1 \\ \vdots \\ v_n\end{matrix} \right) = a \in \mathbb R
$$

### Matrix Decomposition

#### LU Decomposition

$$
A = LU
$$

The matrix $A$ is decomposed into the product of a lower triangular matrix $L$ and an upper triangular matrix $U$.

#### LDL Decomposition

$$
A = L D L^T
$$

For suitable symmetric matrices, $A$ can be decomposed into a lower triangular matrix $L$, a diagonal matrix $D$, and $L^T$.

#### Cholesky Decomposition

$$
A = G G^T
$$

If $A$ is symmetric positive definite, then $A$ can be decomposed into the product of a lower triangular matrix $G$ and its transpose.

#### QR Decomposition

$$
A = QR
$$

The matrix $A$ is decomposed into the product of an orthogonal matrix $Q$ and an upper triangular matrix $R$.

#### Full Rank Decomposition

$$
A = FG
$$

If $\operatorname{rank}(A)=r$, then $A$ can be written as the product of an $m \times r$ matrix $F$ and an $r \times n$ matrix $G$.

#### Eigenvalue Decomposition

For a square matrix $\boldsymbol A \in \mathbb R^{n \times n}$,

$$
\boldsymbol A = \boldsymbol Q \boldsymbol \Lambda \boldsymbol Q^{-1}
$$

If $\boldsymbol A$ is diagonalizable, $\boldsymbol Q$ is formed from eigenvectors and $\boldsymbol \Lambda$ is the diagonal matrix of eigenvalues.

#### Singular Value Decomposition

For a matrix $\boldsymbol A \in \mathbb R^{m \times n}$,
$$
\boldsymbol A = \boldsymbol U \boldsymbol \Sigma \boldsymbol V^{\mathrm T}
$$

- $\boldsymbol U$ and $\boldsymbol V$ are orthogonal matrices
- $\boldsymbol \Sigma$ is a diagonal matrix whose diagonal entries are the singular values

## Include

- [Affine_Space](./Affine_Space.md): defined_on

- [Linear_Transformation](./Linear_Transformation.md): defined_on

- [Normed_Linear_Space](./Normed_Linear_Space.md): subtype_of

- [Projective_Space](./Projective_Space.md): defined_on

- [Tensor](./Tensor.md): defined_on

## Parents

- [Module](./Module.md): subtype_of
