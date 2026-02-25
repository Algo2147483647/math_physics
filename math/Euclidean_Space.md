# Euclidean Space

[TOC]

## Define

Euclidean space is a finite dimensional [Hilbert space](./Hilbert_Space.md) over a [real number field](./Real_Field.md), and has a standard dot product as its inner product. Let $n \in \mathbb{N}$ (the set of natural numbers). The $n$-dimensional Euclidean space, denoted as $\mathbb{R}^n$, is the set of all ordered $n$-tuples of real numbers. That is,
$$
\mathbb{R}^n = \{(x_1, x_2, \dots, x_n) : x_i \in \mathbb{R} \text{ for } i = 1,2, \dots, n\}
$$

In $\mathbb{R}^n$, we define the following operations:

1. **Vector Addition:** For any two vectors $\mathbf{v} = (v_1, v_2, \dots, v_n)$ and $\mathbf{w} = (w_1, w_2, \dots, w_n)$ in $\mathbb{R}^n$, their sum is given by:
$$
\mathbf{v} + \mathbf{w} = (v_1 + w_1, v_2 + w_2, \dots, v_n + w_n)
$$

2. **Scalar Multiplication:** For any scalar $c \in \mathbb{R}$ and vector $\mathbf{v} = (v_1, v_2, \dots, v_n)$ in $\mathbb{R}^n$, the scalar product is:
$$
c \cdot \mathbf{v} = (c v_1, c v_2, \dots, c v_n)
$$

3. **Inner Product (Dot Product):** The inner product of two vectors $\mathbf{v} = (v_1, v_2, \dots, v_n)$ and $\mathbf{w} = (w_1, w_2, \dots, w_n)$ in $\mathbb{R}^n$ is defined as:
$$
\mathbf{v} \cdot \mathbf{w} = v_1 w_1 + v_2 w_2 + \dots + v_n w_n
$$

From this inner product, we can derive the **Euclidean norm** of a vector $\mathbf{v}$ as:
$$
||\mathbf{v}|| = \sqrt{\mathbf{v} \cdot \mathbf{v}}
$$

With these operations, $\mathbb{R}^n$ becomes a **real inner product space**. The geometry induced by the inner product is the familiar Euclidean geometry, and the distance between two vectors $\mathbf{v}$ and $\mathbf{w}$ is given by the norm of their difference:
$$
d(\mathbf{v}, \mathbf{w}) = ||\mathbf{v} - \mathbf{w}||
$$

## Properties

### Classical geometric shapes

A table of the area and perimeter formulas for classic 2D geometric shapes:

| Shape                         | Area (A)                              | Perimeter (P)                                      |
| ----------------------------- | ------------------------------------- | -------------------------------------------------- |
| **Square**                    | $A = a^2$                           | $P = 4a$                                         |
| **Rectangle**                 | $A = l \times w$ | $P = 2(l + w)$                                   |
| **Parallelogram**             | $A = b \times h$                    | $P = 2(a + b)$                                   |
| **Rhombus**                   | $A = \frac{d_1 \times d_2}{2}$      | $P = 4a$                                         |
| **Triangle**                  | $A = \frac{1}{2} b \times h$<br />$A=\sqrt{s(s-a)(s-b)(s-c)}, s = \frac{a+b+c}{2}$ | $P = a + b + c$                                  |
| **Equilateral Triangle**      | $A = \frac{\sqrt{3}}{4} s^2$ | $P = 3s$                                         |
| **Isosceles Triangle**        | $A = \frac{b}{4} \sqrt{4a^2 - b^2}$ | $P = 2a + b$                                     |
| **Circle**                    | $A = \pi r^2$                       | $P = 2\pi r$                                     |
| **Ellipse**                   | $A = \pi a b$                       | $P \approx \pi [ 3(a+b) - \sqrt{(3a+b)(a+3b)} ]$ |
| **Trapezoid**                 | $A = \frac{1}{2} (b_1 + b_2) h$     | $P = a + b_1 + b_2 + c$                          |
| **Regular Polygon (n sides)** | $A = \frac{1}{4} n a^2 \cot(\pi/n)$ | $P = n a$                                       |

* $a$ = side length
* $l, w$ = length, width
* $a, b, c$ = triangle sides
* $b_1, b_2$ = trapezoid bases
* $h$ = height
* $d_1, d_2$ = diagonals of rhombus
* $r$ = radius of circle
* $a, b$ = semi-axes of ellipse
* $n$ = number of sides for a regular polygon



A table of **volume and surface area formulas** for classic 3D geometric solids:

| Solid                                | Volume (V)                                         | Surface Area (S)                                                                                     |
| ------------------------------------ | -------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Cube**                             | $V = s^3$                                        | $S = 6s^2$                                                                                         |
| **Rectangular Prism (Cuboid)**       | $V = l \cdot w \cdot h$                          | $S = 2(lw + lh + wh)$                                                                              |
| **Sphere**                           | $V = \frac{4}{3} \pi r^3$                        | $S = 4 \pi r^2$                                                                                    |
| **Cylinder**                         | $V = \pi r^2 h$                                  | $S = 2 \pi r (r + h)$                                                                              |
| **Cone**                             | $V = \frac{1}{3} \pi r^2 h$                      | $S = \pi r (r + l)$, $l = \sqrt{r^2 + h^2}$ (slant height)                                       |
| **Rectangular Pyramid**              | $V = \frac{1}{3} l w h$                          | $S = lw + l \sqrt{(w/2)^2 + h^2} + w \sqrt{(l/2)^2 + h^2}$                                         |
| **Square Pyramid**                   | $V = \frac{1}{3} s^2 h$                          | $S = s^2 + 2 s \sqrt{(s/2)^2 + h^2}$                                                               |
| **Triangular Prism**                 | $V = \frac{1}{2} b h_{tri} \cdot L$              | $S = (b h_{tri}) + L(a + b + c)$                                                                   |
| **Triangular Pyramid (Tetrahedron)** | $V = \frac{1}{3} \cdot \text{Base Area} \cdot h$ | $S = \text{sum of 4 triangular faces}$                                                             |
| **Ellipsoid**                        | $V = \frac{4}{3} \pi a b c$                      | $S \approx 4 \pi \left( \frac{(a b)^p + (a c)^p + (b c)^p}{3} \right)^{1/p} ), ( p \approx 1.6075 )$ |
| **Torus**                            | $V = 2 \pi^2 R r^2$                              | $S = 4 \pi^2 R r$                                                                                  |

* $s$ = side length (cube, square pyramid)
* $l, w, h$ = length, width, height (cuboid, pyramid)
* $r$ = radius (sphere, cylinder, cone, torus)
* $h$ = height (prism, cone, pyramid)
* $l$ = slant height (cone, pyramid)
* $a, b, c$ = axes of ellipsoid or sides of triangle
* $R$ = major radius of torus (center to tube center)
* $r$ = minor radius of torus (tube radius)
* $L$ = length of prism
* $h_{tri}$ = height of triangular base

### Tessellation

A tessellation or tiling is the covering of a surface, often a plane, using one or more geometric shapes, called tiles, with no overlaps and no gaps.

#### Convex regular polygon tiling

There are three methods for dense tiling of a monohedral regular polygon in a plane: equilateral triangle, square, and regular hexagon.

<img src="assets/1-uniform_n11.svg" alt="1-uniform_n11" style="zoom:8%;" /><img src="assets/1-uniform_n5.svg" alt="1-uniform_n5" style="zoom:20%;" /><img src="assets/1-uniform_n1.svg" alt="1-uniform_n1" style="zoom:8%;" />

There are 17 combinations of regular convex polygons that form 21 types of plane-vertex tilings.

<img src="assets/image-20240209012125223.png" alt="image-20240209012125223" style="zoom: 33%;" />

#### Space-Filling Polyhedron

<img src="assets/SpaceFillingPolyhedra_1000.svg" alt="SpaceFillingPolyhedra" style="zoom: 25%;" />

#### Monohedral Pentagonal tiling

<img src="assets/image-20240209013213739.png" alt="image-20240209013213739" style="zoom:20%;" />

#### Penrose tiling

A Penrose tiling is an example of an aperiodic tiling.

<img src="assets/Penrose_Tiling_(Rhombi).svg" alt="Penrose_Tiling_(Rhombi)" style="zoom:25%;" />

## Include

- [Convex_Hull](./Convex_Hull.md): 

- [Knot](./Knot.md): 

## Parents

- [Differential_Manifold](./Differential_Manifold.md): is-a

- [Hilbert_Space](./Hilbert_Space.md): is-a

- [Real_Field](./Real_Field.md): 

