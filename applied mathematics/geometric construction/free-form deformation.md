# Free-Form Deformation


### Principle of Free-Form Deformation (FFD)

**Embedding in a Lattice**:

- The algorithm starts by embedding the geometric model within a 3D lattice of control points. This lattice is usually a parallelepiped (a 3D parallelogram).
- The lattice provides a flexible framework for manipulating the embedded model.

**Trivariate Bernstein Polynomials**:
- FFD uses trivariate Bernstein polynomials to define the deformation. These polynomials allow smooth and continuous deformation over the lattice.
- The Bernstein polynomials for a point $(s, t, u)$ in the parameter space are defined as:
  $$
  B_{i,j,k}(s,t,u) = B_i^l(s) B_j^m(t) B_k^n(u)
  $$
  where $B_i^l(s)$, $B_j^m(t)$, and $B_k^n(u)$ are the Bernstein polynomials of degrees $l$, $m$, and $n$ respectively.

**Control Points**:
- The position of a point $P$ in the deformed space is determined by the control points of the lattice. If $P_{i,j,k}$ are the control points, then the deformed position $P(s,t,u)$ is given by:
  $$
  P(s,t,u) = \sum_{i=0}^l \sum_{j=0}^m \sum_{k=0}^n P_{i,j,k} B_{i,j,k}(s,t,u)
  $$
- By moving the control points $P_{i,j,k}$, the embedded model is deformed accordingly.

### Algorithm Steps

**Initialization**:
- Embed the geometric model within a lattice of control points.
- Define the parameter space $(s, t, u)$ which maps the points in the geometric model to their corresponding positions in the lattice.

**Deformation Specification**:
- The user specifies the desired deformation by moving the control points of the lattice.
- The movement of these control points defines how the Bernstein polynomials modify the position of each point in the original model.

**Computing Deformed Positions**:
- For each point in the geometric model, compute its new position using the weighted sum of the control points and the Bernstein polynomials.
- The new position $P(s,t,u)$ is calculated as per the trivariate Bernstein polynomial equation mentioned earlier.

**Updating the Model**:
- Update the geometric model with the new positions of its points.
- The resulting deformed model reflects the changes specified by the control points' movement.
