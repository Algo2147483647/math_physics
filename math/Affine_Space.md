# Affine Space

[TOC]

## Define

$$
(\mathcal{A}, V, \phi)
$$

Let $V$ be a [vector space](./Linear_Space.md) over a field $K$. An affine space $\mathcal{A}$ over $V$ is a non-empty set of elements called points together with a function

$$
\phi: V \times \mathcal{A} \rightarrow \mathcal{A}
$$

that associates to each point $p \in \mathcal{A}$ and each vector $v \in V$ a point $q = \phi(v, p)$, written as $q = p + v$, such that the following axioms hold:

1. For every point $p \in \mathcal{A}$, $p + 0 = p$, where $0$ is the zero vector in $V$.
2. For every point $p \in \mathcal{A}$ and all vectors $u, v \in V$, $p + (u + v) = (p + u) + v$.
3. For any two points $p, q \in \mathcal{A}$, there exists a unique vector $v \in V$ such that $q = p + v$.



> *Affine space is extended on the basis of vector space, removing the uniqueness of the origin. Its basic idea is to liberate geometric research from specific numerical values (i.e. vector coordinates) and instead focus on the relative positions and arrangements between points.*

## Properties

### Affine Set

- Define
  Affine Set is a set such that the lines drawn by any two points in the set are still in the set.  

$$
\forall \boldsymbol x_i \in C, θ_i \in R, \sum θ_i = 1 \quad \text{, then}\quad \sum θ_i x_i \in C
$$

- Property

  - Affine Hull

    - Define  
      $$
      \text{aff}(C) = \left\{\sum θ_i x_i\ |\ x_i\in C,theta_i \in R, \sum θ_i = 1  \right\}
      $$
      Affine Hull is a set such that affine combinations of all points in the set constitutes an affine hull.

- Include

  - Convex Set

    - Define
      $$
      \forall \boldsymbol x_i \in C \subseteq \mathbb R^n, a_i \in [0,1], \sum a_i = 1 \quad \text{, then}\quad \sum a_i x_i \in C
      $$

      A convex set $C$ is a set such that the line segment between any two points in the set is still in the set. Convex sets are a special class of affine sets.

    - Property

      - Convex Set $C$的任意边界点, 均存在支撑超平面.

      - Convex Hull
        $$
          \text{conv}(C) = \left\{\sum θ_i x_i\ |\ x_i\in C, θ_i \in [0,1], \sum θ_i = 1 \right\}
        $$

          A convex hull is a set of points is the smallest convex polygon that contain all the input points.

          The set of convex combinations of all points in the set constitutes a convex hull This convex hull is also the smallest Convex Set containing all points in a given set.

        $$
          \mathcal X_{\text{Convex\ Hull}} \subseteq \mathcal X_{\text{input}}
        $$
        $$
        \mathcal X_{\text{input}} \subseteq \text{Polygon}(\mathcal X_{\text{Convex\ Hull}})
        $$



### Cone
- Define  
$$
\forall \boldsymbol x \in C, θ > 0, \quad \text{, then}\quad θ \boldsymbol x \in C
$$
以零点为起点的射线的集合.

- Include
  * Convex Cone
    - Define  
    $$
    \forall \boldsymbol x_1, \boldsymbol x_2 \in C, θ_1,θ_2 ≥ 0 \quad \text{, then}\quad θ_1 \boldsymbol x_1 + θ_2 \boldsymbol x_2 \in C
    $$

### [Polyhedron](./Polyhedron.md)

### Hyperplane & Half Space

- Define
  $$
  \begin{align*}
    \{\boldsymbol x \ |\ \boldsymbol a^T \boldsymbol x = b\}  \tag{Hyperplane}\\
    \{\boldsymbol x \ |\ \boldsymbol a^T \boldsymbol x ≤ b\}  \tag{Half-Space}
  \end{align*}
  $$

- Property
  - Hyperplane & Half-Space is Convex Set

## Include

- [Polyhedron](./Polyhedron.md): 

## Parents

- [Linear_Space](./Linear_Space.md): 

