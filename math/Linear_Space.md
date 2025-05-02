# Linear Space

[TOC]

## Define

$$
(\mathbb R, V, +, \cdot)  \tag{Linear Space}
$$
Linear Space is a special [module](./Module.md) including non empty set $V$ with addition and scalar multiplication, and satisfying:

- Additive Closure: $x+y \in V$
- Scalar Multiplication Closure: $k x \in V$
- Identity element of vector addition: $x+0=x$
- Inverse elements of vector addition: $x+(-x) = 0$
- Identity element of scalar multiplication: $1x = x$
- Commutativity of vector addition: $x+y = y+x$
- Associativity of vector addition: $x+(y+z) = (x+y) +z$
- Compatibility of scalar multiplication with field multiplication: $a(bx) = (a b)x$
- Distributivity of scalar multiplication with respect to vector addition: $a(x+y) = a x + a y$
- Distributivity of scalar multiplication with respect to field addition: $(a+b)x = ax+bx$

## Properties

### Representation: Base 

$$
\begin{align*}
  \boldsymbol v 
  &= \sum_{i=1}^n a_i \boldsymbol x_i \quad, \forall \boldsymbol v \in V  \\
  &= \boldsymbol X \boldsymbol a
\end{align*}
$$
Base is a linearly independent vector group $\boldsymbol X = (\boldsymbol x_1, ... , \boldsymbol x_n)$, All vectors in the linear space are linear combinations of the vector group.

- $\boldsymbol x_i$: Base vector
- $a_i$: coordinate

#### Base Transformation & Coordinate Transformation

Base transformation, is a transformation between new bases $\boldsymbol Y$ and old bases $\boldsymbol X$, where $\boldsymbol C$ is the Transformation Matrix.
$$
\boldsymbol Y = \boldsymbol X \boldsymbol C
$$

Coordinate Transformation, is solving a new coordinate $\boldsymbol a_y$ in new base $\boldsymbol Y$ from old coordinate $\boldsymbol a_x$ in old base $\boldsymbol X$.
$$
\boldsymbol a_x = \boldsymbol C \boldsymbol a_y
$$

> Proof
> 
> $$
> \begin{align*}
>   \boldsymbol v 
>   &= \boldsymbol X \boldsymbol a_x  \\
>   &= \boldsymbol Y \boldsymbol a_y  \\ 
>   &= \boldsymbol X \boldsymbol C \boldsymbol a_y  \\ 
>   \Rightarrow \boldsymbol a_x &= \boldsymbol C \boldsymbol a_y
> \end{align*}
> $$


- Property
  The base transformation matrix $\boldsymbol C$ is nonsingular.


#### Dimension  
In linear space, the maximum number of vectors contained in a linearly independent vector group.

#### Span
$$
Span(\boldsymbol x_1,...,\boldsymbol x_n) = \left\{\boldsymbol v | \boldsymbol v = \sum_{i=1}^n a_i \boldsymbol x_i \right\}
$$
A representation of a linear space given by a basis vector.


### Representation

#### Vector

$$
\mathbb R^{n}, n \in \mathbb Z
$$
A vector is a one-dimensional array of numbers. It can be represented as a row or a column.

#### Matrix 

$$
\mathbb R^{m \times n}, m, n \in \mathbb Z
$$

$$
\boldsymbol A = \left(\begin{matrix} a_{11} & \cdots & a_{1n} \\ \vdots & \ddots & \vdots \\ a_{m1} & \cdots & a_{mn} \end{matrix}\right)
$$



A matrix is a two-dimensional array of numbers, symbols, or expressions, arranged in rows and columns.

##### Operations

- Addition:

$$
\boldsymbol A_{m \times n} + \boldsymbol B_{m \times n} = \boldsymbol C_{m \times n}  \tag{addition}
$$
$$
c_{ij} = a_{ij} + b_{ij}
$$

- Scalar multiplication,

$$
k \boldsymbol A_{m \times n} = (k a_{ij})_{m \times n}  \tag{scalar multiplication}
$$


  - multiplication
    $$
    \boldsymbol A_{m \times n} \times \boldsymbol B_{n \times p} = \boldsymbol C_{m \times p}
    $$
    $$
    c_{ij} = \sum_{k \in 1:n} a_{ik} b_{kj}
    $$

  - multiplication of elements, Hadamard product
    $$
    \boldsymbol A_{m \times n} \odot \boldsymbol B_{m \times n} = \boldsymbol C_{m \times n}
    $$
    $$
    c_{ij} = a_{ij} b_{ij}
    $$

### Linear Independence & Linear Dependence

For a vector group $(\boldsymbol x_1, ... , \boldsymbol x_n)$, we said  

Linear Independence,
$$
\nexists\ \boldsymbol a ≠ \boldsymbol 0 \Rightarrow \sum_{i=1}^n a_i \boldsymbol x_i = \boldsymbol 0
$$

Linear Dependence,
$$
\exists\ \boldsymbol a ≠ \boldsymbol 0 \Rightarrow \sum_{i=1}^n a_i \boldsymbol x_i = \boldsymbol 0
$$

### Linear Subspace

A nonempty set in a linear space that is closed to linear operations.

- Additive Closure: $x,y\in V_1 ,\quad x+y \in V_1$
- Scalar Multiplication Closure: $x \in V_1, k x \in V_1$

### Dual Space

$$
V^*=\left\{f:V\rightarrow \mathbb R \mid f \text{ is a linear map}\right\}
$$

Let $V$ be a vector space over a field $\mathbb R $, the dual space $V^*$ of $V$ is the vector space of all linear functionals from $f: V \to \mathbb R$ called dual vector. For a finite-dimensional column vector, its dual vector is in the form of a row vector.
$$
\left(\begin{matrix}v^*_1  & \cdots & v^*_n\end{matrix} \right) \left(\begin{matrix}v_1 \\ \vdots \\ v_n\end{matrix} \right) = a \in \mathbb R
$$

### Matrix Decomposition

#### LU decomposition

$$
A = L R
$$

The matrix $A$ is decomposed into the product of upper triangular matrix $R$ and lower triangular matrix $L$.

#### Upper and lower triangular diagonal decomposition

将矩阵A化成上三角矩阵R, 对角矩阵D, 下三角矩阵L的乘积.$A = L D R$

#### Symmetric triangular decomposition

$$
A = G G^T
$$

将对称正定矩阵化成对称的两个上下三角矩阵.

- Algorithm
  - first LU decomposition
    Because symmetric positive definite matrix
    $$A = L D U = L D L^T$$
    $$
    \begin{align*}
      A &= L (\sqrt{D})^2 L^T  \\
        &= (L \sqrt{D}) (\sqrt{D} L^T)  \\
        &= (L \sqrt{D}) (L \sqrt{D})^T  \\
        &= G G^T
    \end{align*}
    $$

#### QR decomposition

$$
A = Q R
$$

The nonsingular matrix A is decomposed into the product of orthogonal matrix Q and nonsingular upper triangular matrix R

##### Algorithm

- Schmidt Orthogonalization method
  - $A = (a_1, ..., a_n)$
  - Schmidt Orthogonalization
    $$
    b_i = a_i - \sum_{k=1}^{i-1} \frac{<a_i,b_j>}{<b_j,b_j>}b_j
    $$
    
    $$
    \begin{align*}
      Q &= ( \frac{b_1}{|b_1|}, ... , \frac{b_n}{|b_n|} )  \\
      R &= \left(\begin{matrix} |b_1|\\ & \ddots\\ && |b_n| \end{matrix}\right) \left(\begin{matrix} 1 & k_{21} & ... & k_{n1} \\ & 1 & ... & k_{n2} \\& & \ddots & \vdots \\& & & 1 \end{matrix}\right) \quad; k_{ij} = \frac{<a_i,b_j>}{<b_j,b_j>}  \\
      A &= Q R
    \end{align*}
    $$

- 初等旋转变换方法
  - 对第1列, 初等旋转变换使其变为 $T_i a_1 = (b_{11}, 0,...,0)$
  - $T_i = \prod_{i=0}^{n-1} T_{i(n-1-j)}$
  - 重复上面步骤, 直至将 $A_i$ 化为上三角矩阵
    $$
    \begin{align*}
      R &= A_{n-1}
      Q &= \left(\prod_{i=0}^{n-1} T_{n-1-i} \right)^T
      A &= Q R
    \end{align*}
    $$

- 初等反射变换方法
  - 对第1列, 初等旋转变换使其变为 $H_i a_1 = (b_{11}, 0,...,0)$
    $$
    \begin{align*}
      u_i &= \frac{b_i - |b_i|}{| b_i - |b_i| |}
      H_i &= I - 2 u u^T
      A_{i+1} &= H_i A_i
    \end{align*}
    $$

  - Repeat the above steps, until $A_i$ into upper triangular matrix
    $$
    \begin{align*}
      R &= A_{n-1}
      Q &= \left(\prod_{i=0}^{n-1} H_{n-1-i} \right)^T
      A &= Q R
    \end{align*}
    $$

#### Full Rank decomposition

$$
A = F G
$$

##### Proof  
$$
A =P^{-1} B = \left(\begin{matrix} F & S \end{matrix}\right) \left(\begin{matrix} G\\ 0 \end{matrix}\right) = F G
$$

##### Algorithm  
$$
A = F G
$$
初等行变换, 取A左侧rank(A)列作为F, 则
$$
A \to \left(\begin{matrix} G \\ 0 \end{matrix}\right)
$$

#### Eigenvalue Decomposition

Eigenvalue Decomposition, for a square matrix $\boldsymbol A \in \mathbb R^{n \times n}$, 

$$
\begin{align*}
  \boldsymbol A 
  &= \boldsymbol Q \boldsymbol \Lambda \boldsymbol Q^{-1}  \\
  &= \boldsymbol Q \boldsymbol \Lambda \boldsymbol Q^{\mathrm T}  \\
\end{align*}
$$

- $\boldsymbol Q$ is an orthogonal matrix $\boldsymbol Q^{\mathrm T} \boldsymbol Q = \boldsymbol I$ composed of eigenvectors $\boldsymbol v$
- $\Lambda$ is composed of eigenvalues $\lambda$, 

$$
\begin{align*}
  \boldsymbol Q &= (\boldsymbol v_1, ..., \boldsymbol v_n)  \\
  \boldsymbol \Lambda &= \left(\begin{matrix} \lambda_1 && 0 \\ &\ddots \\ 0 && \lambda_n \end{matrix}\right)
\end{align*}
$$

##### Proof
$$
\boldsymbol A \boldsymbol v_i = \lambda_i \boldsymbol v_i
$$

$$
\begin{align*}
\Rightarrow \boldsymbol A (\boldsymbol v_1, ..., \boldsymbol v_n) &= (\boldsymbol v_1, ..., \boldsymbol v_n) \left(\begin{matrix} \lambda_1 && 0 \\ &\ddots \\ 0 && \lambda_n \end{matrix}\right)  \\
\boldsymbol A &= (\boldsymbol v_1, ..., \boldsymbol v_n) \left(\begin{matrix} \lambda_1 && 0 \\ &\ddots \\ 0 && \lambda_n \end{matrix}\right) (\boldsymbol v_1, ..., \boldsymbol v_n)^{-1}  \\
\boldsymbol A &= \boldsymbol Q \Lambda \boldsymbol Q^{-1}
\end{align*}
$$

##### Note  
The geometric significance of Eigenvalue Decomposition is that a linear transformation $\boldsymbol A \boldsymbol x$ is equivalent to (1) $\boldsymbol Q^{-1} \boldsymbol x$, convert to a new coordinate system with eigenvectors of $\boldsymbol A$ as unit bases; (2)$\boldsymbol \Lambda (\boldsymbol Q^{-1} \boldsymbol x)$, a scale transform; (3)$\boldsymbol Q (\boldsymbol \Lambda \boldsymbol Q^{-1} \boldsymbol x)$, convert to original coordinate system.

#### Singular Value Decomposition

for a matrix $\boldsymbol A \in \mathbb R^{m \times n}$,  
$$
\boldsymbol A = \boldsymbol U \left(\begin{matrix} \boldsymbol \Sigma & \boldsymbol 0 \\ \boldsymbol 0 & \boldsymbol 0 \end{matrix}\right) \boldsymbol V^{\mathrm H}
$$

- $\boldsymbol U \in \mathbb R^{m \times m}, \boldsymbol V \in \mathbb R^{n \times n}$ are unitary matrixs $\boldsymbol U^{\mathrm H} \boldsymbol U = \boldsymbol I, \boldsymbol V^{\mathrm H} \boldsymbol V = \boldsymbol I$
- $\boldsymbol \Sigma$ is composed of nonzero singular values.

##### Note
$$
\exists \text{Unitary Matrix} U, V \Rightarrow U^H A V = \left(\begin{matrix} Σ & 0 \\ 0 & 0 \end{matrix}\right)
$$

##### Algorithm  
$A^{\mathrm T} A$ 计算特征值 $λ$, 特征向量$v'$, 并归一化求得 $\boldsymbol V, \boldsymbol Σ, \boldsymbol U$,

$$
(\boldsymbol A^{\mathrm T} \boldsymbol A) \boldsymbol v'_i = \lambda_i \boldsymbol v'_i
$$

$$
\begin{align*}
  \boldsymbol V &= \left(\frac{\boldsymbol v'_1}{\|\boldsymbol v'_1\|_2}, ... ,\frac{\boldsymbol v'_n}{\|\boldsymbol v'_n\|_2} \right)  \\
  \boldsymbol Σ &= \text{diag}\left(\sqrt{λ_1}, ... ,\sqrt{λ_n}\right)  \\
  \boldsymbol U' &= \boldsymbol A \boldsymbol V \boldsymbol Σ^{-1}  \\
  \boldsymbol U &= \left(\frac{\boldsymbol u'_1}{\|\boldsymbol u'_1\|_2}, ... ,\frac{\boldsymbol u'_n}{\|\boldsymbol u'_n\|_2} \right)  
\end{align*}
$$

##### Property
$$
\begin{align*}
  Range(A) &= Span(u_1, ..., u_r)  \\
  Null (A) &= Span(v_{r+1}, ... , v_n)  \\
  Range(A^{\mathrm T}) &= Span(v_1, ..., v_r)  \\
  Null (A^{\mathrm T}) &= Span(u_{r+1}, ... , u_m)  \\
  A &= \sum_{i=1}^{r} σ_i u_i v_i^H
\end{align*}
$$

##### Proof
$$
\begin{align*}
A &= \left(\begin{matrix} U_{1:r} & U_{r+1:m} \end{matrix}\right) \left(\begin{matrix} Σ & 0 \\ 0 & 0 \end{matrix}\right) \left(\begin{matrix} V_{1:r}^H \\ V_{r+1:n}^H \end{matrix}\right)  \tag{定义式变形}  \\
&= U_{1:r} Σ V_{1:r}^H
\end{align*}
$$

$$
\begin{align*}
Range(A) &= \{y\ |\ A x = y\}  \\
&= \{y\ |\ U_{1:r} (Σ V_{1:r}^H x) = y\}  \tag{代入}  \\
&\subseteq Range(U_{1:r})  \\
Range(U_{1:r}) &= \{y\ |\ U_{1:r} x = y\}  \\
&= \{y\ |\ A (V_{1:r} Σ^{-1} x) = y\}  \tag{$U_{1:r} = A V_{1:r} Σ^{-1}$}  \\
&\subseteq Range(A)
\end{align*}
$$

$$
\begin{align*}
\Rightarrow Range(A) = Range(U_{1:r}) = Span(u_1, ..., u_r)
\end{align*}
$$

## Include

- [Affine_Space](./Affine_Space.md): 

- [Linear_Transformation](./Linear_Transformation.md): 

- [Normed_Linear_Space](./Normed_Linear_Space.md): 

- [Projective_Space](./Projective_Space.md): 

- [Tensor](./Tensor.md): 

## Parents

- [Module](./Module.md): 

