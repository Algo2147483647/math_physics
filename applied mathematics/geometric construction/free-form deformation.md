# Free-Form Deformation

[TOC]

## Problem

Free-form deformation is designed to solve the problem of **smoothly deforming a geometric object through a small control structure**.

- How can a model be bent, twisted, stretched, or compressed without editing every vertex?
- How can deformation remain smooth across the whole object?
- How can a complex mesh be edited with a low-dimensional set of handles?

## Core Idea

Free-form deformation embeds the object inside a control lattice.

Instead of directly moving each point of the object, we:

1. Map each object point into lattice coordinates.
2. Move the lattice control points.
3. Re-evaluate the embedded point using the deformed lattice.

The practical essence of FFD is:

1. **Use a lattice as a deformation coordinate system**
2. **Use basis functions to blend control point motion**
3. **Apply the resulting smooth mapping to the embedded geometry**

## Solution

### Lattice Coordinates

Suppose an object point $X$ lies inside a lattice volume.

It is assigned local coordinates:
$$
(s,t,u) \in [0,1]^3
$$

These coordinates are computed in the undeformed lattice and then kept fixed during deformation.

### Trivariate Bernstein Basis

Classical FFD uses trivariate Bernstein polynomials.

For lattice degrees $l, m, n$, the basis is:
$$
B_{i,j,k}(s,t,u) = B_{i,l}(s)B_{j,m}(t)B_{k,n}(u)
$$

where:
$$
B_{i,l}(s) = {l \choose i}s^i(1-s)^{l-i}
$$

### Deformed Position

Let $P_{i,j,k}$ be the lattice control points. The deformed point is:
$$
X'(s,t,u) =
\sum_{i=0}^{l}
\sum_{j=0}^{m}
\sum_{k=0}^{n}
P_{i,j,k} B_{i,l}(s)B_{j,m}(t)B_{k,n}(u)
$$

Moving a control point changes all embedded points whose basis weights depend on it.

### Algorithm Steps

#### Initialize

1. Build a lattice around the model.
2. Choose lattice resolution, such as $(l+1)(m+1)(n+1)$ control points.
3. Compute local coordinates $(s,t,u)$ for each object point.

#### Edit

Move selected lattice control points according to the desired deformation.

Typical edits include:

- bending
- twisting
- tapering
- stretching
- local bulging

#### Evaluate

For each object point:

1. Read its stored lattice coordinates.
2. Evaluate the trivariate basis.
3. Compute the weighted sum of deformed lattice control points.
4. Replace the point position with the resulting value.

### Variants

FFD can be generalized by changing the control structure or basis.

Common variants include:

- B-spline FFD for more local control
- cage-based deformation
- mean value coordinates
- harmonic coordinates
- skeleton-driven deformation

##  Boundaries

### Requires A Meaningful Embedding

Classical FFD works best when the object can be reasonably embedded inside a simple lattice volume.

Objects with complex topology or very thin parts may be difficult to control with a coarse regular lattice.

### Global Influence

Bernstein-basis FFD has relatively global influence. Moving one control point may affect a large region.

B-spline FFD or cage coordinates are often better when local control is required.

### Detail Preservation Is Not Automatic

FFD moves geometry smoothly, but it does not automatically preserve:

- volume
- edge length
- local rigidity
- sharp features

Additional constraints or post-processing may be needed.

### Self-Intersection Is Possible

Large lattice movements can fold the deformation map and create self-intersections.

## Cost

The main cost of FFD lies in the trade-off between **simple high-level shape control** and **basis evaluation for many embedded points**.

### Time Cost

For $N$ object points and a lattice with $(l+1)(m+1)(n+1)$ control points:

- Precompute lattice coordinates: **O(N)**
- Evaluate naive Bernstein FFD: **O(Nlmn)**
- Move control points: depends on the user edit, usually small

With tensor-product evaluation and low lattice degree, the practical cost is often close to linear in the number of object points.

### Space Cost

FFD stores:

- lattice control points
- local coordinates for each embedded object point
- optional precomputed basis weights

The space cost is:
$$
O(N + lmn)
$$

### Engineering Cost

In real systems, implementing FFD requires careful decisions about:

- lattice placement and orientation
- coordinate computation
- basis type
- local versus global control
- handling points outside the lattice
- preventing fold-over and self-intersection

So while the deformation formula is clean, good editing behavior depends strongly on lattice design.
