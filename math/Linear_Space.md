# Linear Space

[TOC]

## Define

$$
(\mathbb R, V, +, \cdot)  \tag{Linear Space}
$$
Linear Space is a special [module](./Module.md) including non empty set $V$ with addition and scalar multiplication, and satisfying:

- Additive Closure: $x+y \in V$
- Multiplication Closure: $k x \in V$
- Identity element of vector addition: $x+0=x$
- Inverse elements of vector addition: $x+(-x) = 0$
- Identity element of scalar multiplication: $1x = x$
- Commutativity of vector addition: $x+y = y+x$
- Associativity of vector addition: $x+(y+z) = (x+y) +z$
- Compatibility of scalar multiplication with field multiplication: $a(bx) = (a b)x$
- Distributivity of scalar multiplication with respect to vector addition: $a(x+y) = a x + a y$
- Distributivity of scalar multiplication with respect to field addition: $(a+b)x = ax+bx$

## Properties

### Representation

#### Vector

##### Define

$$
\mathbb R^{n}, n \in \mathbb Z
$$
A vector is a one-dimensional array of numbers. It can be represented as a row or a column.

#### Matrix 

##### Define

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

### Dimension  
In linear space, the maximum number of vectors contained in a linearly independent vector group.

### Base 

#### Define

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

#### Property 

- Base Transformation & Coordinate Transformation  
  Base transformation, is a transformation between new bases $\boldsymbol Y$ and old bases $\boldsymbol X$, where $\boldsymbol C$ is the Transformation Matrix.
  $$
  \boldsymbol Y = \boldsymbol X \boldsymbol C
  $$
  
  Coordinate Transformation, is solving a new coordinate $\boldsymbol a_y$ in new base $\boldsymbol Y$ from old coordinate $\boldsymbol a_x$ in old base $\boldsymbol X$.
  $$
  \boldsymbol a_x = \boldsymbol C \boldsymbol a_y
  $$
  
  
  - Proof
    $$
    \begin{align*}
      \boldsymbol v 
      &= \boldsymbol X \boldsymbol a_x  \\
      &= \boldsymbol Y \boldsymbol a_y  \\ 
      &= \boldsymbol X \boldsymbol C \boldsymbol a_y  \\ 
      \Rightarrow \boldsymbol a_x &= \boldsymbol C \boldsymbol a_y
    \end{align*}
    $$

  - Property  
    The base transformation matrix $\boldsymbol C$ is nonsingular.

- Span
  $$
  Span(\boldsymbol x_1,...,\boldsymbol x_n) = \left\{\boldsymbol v | \boldsymbol v = \sum_{i=1}^n a_i \boldsymbol x_i \right\}
  $$
  A representation of a linear space given by a basis vector.

### Linear Subspace

A nonempty set in a linear space that is closed to linear operations.

- 加法封闭 $x,y\in V_1 ,\quad x+y \in V_1$
- 数乘封闭 $x \in V_1, k x \in V_1$

### [Linear Transformation](./Linear_Transformation.md)

## Include

- [Affine_Space](./Affine_Space.md): 

- [Linear_Transformation](./Linear_Transformation.md): 

- [Normed_Linear_Space](./Normed_Linear_Space.md): 

- [Projective_Space](./Projective_Space.md): 

## Parents

- [Module](./Module.md): 

