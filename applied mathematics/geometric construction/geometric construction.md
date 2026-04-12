# Geometric Construction

[TOC]

## Problem

Geometric construction studies how to build usable geometric objects from mathematical descriptions, samples, or editing operations. A construction pipeline usually answers four questions:

1. **Representation**: how is the object stored or described?
2. **Generation**: how is the object created from primitives, equations, or operations?
3. **Discretization**: how is a continuous object converted into samples, polygons, meshes, or voxels?
4. **Editing and detail**: how is the object deformed, refined, simplified, or enriched?

Typical inputs include analytic equations, curves, surfaces, point clouds, images, scalar fields, polygonal boundaries, and control points. Typical outputs include point sets, polylines, triangle meshes, tetrahedral meshes, implicit fields, parametric surfaces, and solid models.

## Geometric Representations

Different algorithms become natural under different representations. A good construction method usually starts by choosing the representation that makes the desired operation simple.

| Representation | Form | Good for | Common operations |
| :--- | :--- | :--- | :--- |
| Explicit graph | $z = f(x, y)$ | height fields, terrain | sampling, interpolation, displacement |
| Implicit equation | $f(\boldsymbol{x}) = 0$ | closed curves and surfaces | inside-outside test, boolean operations, contouring |
| Signed distance field | $\phi(\boldsymbol{x})$ | robust solids, level sets | offset, blending, collision, ray marching |
| Parametric curve | $\gamma(t): I \to \mathbb{R}^n$ | curves, trajectories | evaluation, subdivision, arc-length sampling |
| Parametric surface | $\boldsymbol{x}(u, v): \Omega \to \mathbb{R}^3$ | smooth surfaces | tessellation, texture coordinates, differential geometry |
| Point cloud | $\{p_i\}_{i=1}^n$ | scanned or sampled geometry | reconstruction, normal estimation, registration |
| Polygon / mesh | $(V, E, F)$ | rendering, simulation, fabrication | triangulation, smoothing, simplification, remeshing |
| Voxel grid | $V[i, j, k]$ | volumetric data | morphology, marching cubes, flood fill |
| Boundary representation | faces, edges, vertices with topology | CAD solids | trimming, sewing, boolean operations |
| Constructive solid geometry | expression tree of primitives and boolean operations | procedural solids | union, intersection, difference |

### Representation Conversion

Many geometric construction problems are conversion problems:

- implicit field $\to$ mesh: contour extraction, e.g. Marching Cubes.
- point cloud $\to$ mesh: surface reconstruction.
- polygon $\to$ triangles: polygon triangulation.
- parametric surface $\to$ mesh: tessellation.
- mesh $\to$ implicit field: distance transform or volumetric rasterization.
- curve/surface control points $\to$ sampled geometry: spline evaluation.

## Construction Pipeline

A practical geometric construction pipeline often has this shape:

1. **Define geometry** using primitives, equations, input samples, or control points.
2. **Choose representation** according to the operation: implicit, parametric, mesh, point cloud, voxel, or solid model.
3. **Generate base shape** through primitive construction, sweep, extrusion, revolution, lofting, or boolean composition.
4. **Discretize** the continuous shape into samples, polylines, triangles, tetrahedra, or voxels.
5. **Repair and validate** topology, orientation, intersections, degeneracies, and boundary conditions.
6. **Edit or deform** the shape using control handles, lattices, physical models, or differential coordinates.
7. **Add detail** with procedural noise, displacement, subdivision, or texture-driven geometry.

## Primitive Construction

Primitive construction builds objects from elementary geometric entities.

### Analytic Primitives

Common primitives include:

- line, ray, segment, plane.
- circle, ellipse, sphere, cylinder, cone, torus.
- quadric surfaces:
  $$
  \boldsymbol{x}^{T} A \boldsymbol{x} + \boldsymbol{b}^{T}\boldsymbol{x} + c = 0
  $$
- superquadrics and other generalized implicit primitives.

These primitives are useful because they support exact formulas for evaluation, intersection, normals, curvature, and distance.

### Parametric Primitives

Parametric curves and surfaces describe geometry by mapping low-dimensional parameters into space:

$$
\gamma(t): [0, 1] \to \mathbb{R}^n
$$

$$
\boldsymbol{x}(u, v): \Omega \subset \mathbb{R}^2 \to \mathbb{R}^3
$$

Important families include:

- polynomial curves.
- Bézier curves and surfaces.
- B-spline curves and surfaces.
- NURBS.
- subdivision surfaces.

Related note:

- [Bézier Curve](./Bezier_Curve.md)

## Solid Construction Operations

Solid construction creates 3D objects from lower-dimensional geometry or from other solids.

### Extrusion

Extrusion moves a planar region along a direction vector:

$$
S = \{p + t\boldsymbol{d} \mid p \in R,\ t \in [0, h]\}
$$

If the path is a straight line and the cross section is fixed, the result is a prismatic body.

### Revolution

A solid or surface of revolution is produced by rotating a curve or planar region around an axis.

<img src="./assets/Rotationskoerper_animation.gif" alt="Solid of revolution" style="zoom: 25%;" />

For a profile curve $(r(t), z(t))$ around the $z$-axis:

$$
\boldsymbol{x}(t, \theta) =
\begin{bmatrix}
r(t)\cos\theta \\
r(t)\sin\theta \\
z(t)
\end{bmatrix}
$$

### Sweep

A sweep moves a cross section along a spatial path. The cross section may remain rigid, rotate along a moving frame, or change scale along the path.

Common issues:

- frame twisting.
- self-intersection.
- cross-section orientation.
- smooth connection at path corners.

### Loft

Lofting constructs a surface or solid that interpolates several cross sections. It is common in CAD and shape modeling.

### Offset and Thickening

An offset surface moves points along the normal direction:

$$
\boldsymbol{x}_{offset}(u, v) = \boldsymbol{x}(u, v) + d\boldsymbol{n}(u, v)
$$

Offsets are simple conceptually but difficult near high curvature, sharp features, and self-intersections.

### Boolean Operations

Boolean operations combine solids:

- union: $A \cup B$.
- intersection: $A \cap B$.
- difference: $A \setminus B$.

They are especially natural for implicit representations and CSG trees, but require robust intersection and topology handling for meshes and B-rep solids.

## Sampling

Sampling converts continuous geometry into a finite set of points. The main difficulty is that uniform sampling in parameter space is often not uniform on the geometric object.

For a parametric manifold $\gamma : \Omega \subset \mathbb{R}^n \to M \subset \mathbb{R}^m$, the intrinsic volume element is:

$$
dV_M = \sqrt{\det(J_\gamma^T J_\gamma)}\, d\boldsymbol{x}
$$

Therefore, uniform sampling should account for the local metric distortion:

$$
p(\boldsymbol{x}) \propto \sqrt{\det(J_\gamma^T J_\gamma)}
$$

Related note:

- [Uniform sampling on manifolds](./uniform%20sampling%20on%20manifolds.md)

## Discretization and Meshing

Meshing converts geometric descriptions into combinatorial structures such as polylines, triangle meshes, quad meshes, or tetrahedral meshes.

### Polygon Triangulation

Polygon triangulation decomposes a simple polygon into non-overlapping triangles. It is useful for rendering, finite element methods, and geometric decomposition.

Related note:

- [Triangulating a simple polygon](./triangulating%20a%20simple%20polygon.md)

### Point Set Triangulation

Delaunay triangulation constructs a triangulation of a point set such that no input point lies inside the circumcircle of any triangle, under the usual 2D general-position assumption. It is a basic tool for meshing, interpolation, nearest-neighbor structures, and Voronoi diagrams.

Related note:

- [Triangulation of point set in Euclidean space](./triangulation%20of%20point%20set%20in%20euclidean%20space.md)

### Convex Hull

The convex hull is the smallest convex set containing a point set. It is often used as a preprocessing step, a bounding approximation, or a dual structure related to Delaunay triangulation.

Related note:

- [Convex Hull](./convex%20hull.md)

### Iso-Surface Extraction

For a scalar field $f: \mathbb{R}^3 \to \mathbb{R}$, an iso-surface is:

$$
S_c = \{\boldsymbol{x} \mid f(\boldsymbol{x}) = c\}
$$

Iso-surface extraction constructs a polygonal approximation of $S_c$. Marching Cubes is the standard grid-based algorithm for extracting triangle meshes from volumetric scalar fields.

Related note:

- [Contour Surface](./contour%20surface.md)

### Tetrahedralization

Tetrahedralization decomposes a 3D domain into tetrahedra. It is important for finite element simulation, volumetric meshing, and physical modeling.

Important variants:

- constrained Delaunay tetrahedralization.
- quality tetrahedral meshing.
- adaptive tetrahedralization.
- boundary-conforming tetrahedralization.

## Surface Reconstruction

Surface reconstruction builds a continuous or discrete surface from samples. It is different from ordinary 2D triangulation because the input may be noisy, incomplete, nonuniform, and embedded in 3D.

Typical inputs:

- point positions.
- estimated normals.
- scanner confidence or density.
- known boundary curves.

Common methods:

| Method | Input | Idea | Notes |
| :--- | :--- | :--- | :--- |
| Delaunay-based reconstruction | points | infer surface from tetrahedral or triangular complexes | strong theory, sensitive to assumptions |
| Alpha shape | points and scale $\alpha$ | keep simplices selected by radius threshold | exposes multi-scale structure |
| Ball Pivoting | oriented points and radius | roll a ball over samples to create triangles | good for dense scans |
| Poisson reconstruction | oriented points | solve an implicit indicator-function problem | robust and smooth, may close holes |
| Moving Least Squares | points | locally fit smooth approximating surfaces | useful for denoising and resampling |

Key difficulties:

- normal estimation.
- boundary detection.
- hole filling.
- noise and outliers.
- nonuniform sample density.
- preserving sharp features.

## Free-Form Geometric Modeling

Free-form modeling represents shapes with control structures rather than simple analytic equations.

### Bézier Modeling

Bézier curves use Bernstein basis functions:

$$
C(t) = \sum_{i=0}^{n} P_i B_{i,n}(t), \quad t \in [0, 1]
$$

$$
B_{i,n}(t) = {n \choose i} t^i(1-t)^{n-i}
$$

Related note:

- [Bézier Curve](./Bezier_Curve.md)

### B-Spline and NURBS

B-splines provide local control and better continuity management than a single high-degree Bézier curve. NURBS extend B-splines with rational weights, making exact conics and many CAD shapes possible.

Core concepts:

- knot vector.
- basis function support.
- degree and continuity.
- control polygon.
- rational weights.

### Subdivision Surfaces

Subdivision surfaces generate smooth surfaces by repeatedly refining a control mesh. They are useful for arbitrary topology, especially in animation and modeling.

Common schemes:

- Catmull-Clark subdivision.
- Loop subdivision.
- Doo-Sabin subdivision.

### Free-Form Deformation

FFD embeds a shape inside a control lattice and deforms the embedded geometry by moving lattice control points.

Related note:

- [Free-Form Deformation](./free-form%20deformation.md)

## Deformation and Physical Modeling

Geometric deformation changes shape while trying to preserve selected properties such as volume, local rigidity, smoothness, or boundary constraints.

Common deformation models:

- lattice-based deformation.
- skeleton-based skinning.
- Laplacian surface editing.
- as-rigid-as-possible deformation.
- elastic deformation.
- mass-spring and finite element models.

Related note:

- [Elastically Deformable Models](./elastically%20deformable%20models.md)

## Procedural Detail Generation

Procedural methods add structure without manually modeling every detail.

Examples:

- gradient noise for textures and displacement.
- fractal noise for terrain and natural surfaces.
- L-systems for branching structures.
- reaction-diffusion patterns.
- displacement mapping.
- procedural cracks, wrinkles, pores, and erosion.

Related note:

- [Noise Generation](./noise%20generation.md)

## Geometric Queries

Construction algorithms often depend on low-level geometric predicates and queries.

Important queries:

- orientation test.
- point-in-polygon and point-in-polyhedron.
- segment, ray, triangle, and surface intersection.
- nearest point and distance query.
- bounding volume overlap.
- normal and curvature estimation.
- connected components and boundary loops.

Related notes:

- [Intersection](../geometric%20problem/Intersection.md)
- [Intersection of Ray and Surface in Flat Space](../geometric%20problem/Intersection_of_Ray_Surface_in_Flat_Space.md)
- [Intersection of Ray and Surface in Curvature Space](../geometric%20problem/Intersection_of_Ray_Surface_in_Curvature_Space.md)

## Numerical Robustness

Geometric construction is sensitive to degeneracy and floating-point error.

Common failure cases:

- nearly collinear or coplanar points.
- duplicate vertices.
- tiny edges and sliver triangles.
- self-intersections.
- inconsistent face orientation.
- non-manifold edges and vertices.
- holes and open boundaries.
- ambiguous inside-outside classification.

Typical remedies:

- exact or adaptive geometric predicates.
- epsilon policies tied to model scale.
- symbolic perturbation.
- snapping and welding.
- topology validation.
- robust boolean and intersection kernels.
- post-processing repair passes.

## Topic Map

| Task | Input | Output | Typical algorithms |
| :--- | :--- | :--- | :--- |
| Uniform sampling | curve, surface, manifold | point set | metric correction, rejection sampling, low-discrepancy sequences |
| Polygon triangulation | simple polygon | triangle set | ear clipping, monotone partition |
| Point set triangulation | planar point set | triangle mesh | Delaunay triangulation |
| Convex enclosure | point set | convex polygon/polytope | Graham scan, Quickhull |
| Iso-surface extraction | scalar field | triangle mesh | Marching Squares, Marching Cubes, Dual Contouring |
| Surface reconstruction | point cloud | mesh or implicit surface | Alpha Shape, Ball Pivoting, Poisson reconstruction |
| Smooth curve modeling | control points | parametric curve | Bézier, B-spline, NURBS |
| Free-form editing | mesh or solid | deformed geometry | FFD, Laplacian editing, ARAP |
| Procedural detail | coordinates, seed, parameters | scalar or displacement field | Perlin noise, Simplex noise, Diamond-Square |
| Solid modeling | primitives and operations | solid | extrusion, revolution, sweep, loft, CSG |

## Existing Notes

- [Uniform sampling on manifolds](./uniform%20sampling%20on%20manifolds.md)
- [Triangulating a simple polygon](./triangulating%20a%20simple%20polygon.md)
- [Triangulation of point set in Euclidean space](./triangulation%20of%20point%20set%20in%20euclidean%20space.md)
- [Convex Hull](./convex%20hull.md)
- [Contour Surface](./contour%20surface.md)
- [Bézier Curve](./Bezier_Curve.md)
- [Free-Form Deformation](./free-form%20deformation.md)
- [Noise Generation](./noise%20generation.md)
- [Elastically Deformable Models](./elastically%20deformable%20models.md)

## Missing Notes

The following topics are referenced by the structure above but do not yet have dedicated notes in this folder:

- Signed distance fields.
- Constructive solid geometry.
- Sweep, loft, offset, and thickening.
- Marching Squares.
- Dual Contouring.
- Tetrahedral meshing.
- Surface reconstruction from point clouds.
- Normal and curvature estimation.
- Mesh smoothing, subdivision, simplification, and remeshing.
- B-spline and NURBS.
- Subdivision surfaces.
- Laplacian deformation and ARAP deformation.
- Robust geometric predicates.
