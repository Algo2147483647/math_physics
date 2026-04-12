# Math & Physics Notes

[TOC]

## Introduction

This library is a concept-oriented notebook for mathematics, applied mathematics, and physics.

- **Mathematics** is treated as a formal language built from axioms, definitions, structures, and logical consequences.
- **Applied mathematics** records reusable mathematical tools for computation, modeling, information, optimization, geometry, statistics, and algorithms.
- **Physics** records models of natural phenomena through observation, experiment, symmetry, variational principles, and mathematical fields.
- **Engineering** uses proven knowledge to build systems that serve human society.

The goal of this repository is not to collect isolated formulas. It is to keep concepts connected: each note should make clear what the object is, what it depends on, what it contains, and how it is used.

## Map

| Path | Role |
| --- | --- |
| [`math/`](./math/) | Pure mathematical concepts organized as a directed knowledge graph. |
| [`applied mathematics/`](./applied%20mathematics/) | Problem-oriented mathematical tools: algorithms, cryptography, differential equations, geometry, information, language, optimization, and statistics. |
| [`physics/`](./physics/) | Physical theories, core principles, fields, spacetime models, fluids, statistical mechanics, and experiments. |
| [`history/`](./history/) | Historical graph/data snapshots and conversion scripts. |
| [`tmp/`](./tmp/) | Draft notes waiting to be refined or moved into the main structure. |

## Reading Order

1. Start from [`math/Set.md`](./math/Set.md), [`math/Logic.md`](./math/Logic.md), and [`math/Relation.md`](./math/Relation.md) to enter the mathematical graph.
2. Move through algebra, topology, measure/probability, functions, transformations, manifolds, and tensors as needed.
3. Use [`applied mathematics/`](./applied%20mathematics/) when the question is problem-driven rather than structure-driven.
4. For physics, begin with [`physics/basic principles of mechanics.md`](./physics/basic%20principles%20of%20mechanics.md), then read the spacetime and field notes.

## Mathematics

![](./math/assets/math.svg)

The math folder is maintained as a concept graph. Each Markdown file is a node; links in `Include` and `Parents` define directed edges between nodes.

### Note Format

Each mathematical concept should use the following structure:

```markdown
# Concept Name

[TOC]

## Define

The definition of the concept.

## Properties

Important theorems, equivalent characterizations, operations, examples, and counterexamples.

## Include

- [Child_Concept](./Child_Concept.md): edge_label

## Parents

- [Parent_Concept](./Parent_Concept.md): edge_label
```

### Edge Labels

- **is-a**: Inheritance. The child concept inherits the definition, properties, or behavior of the parent concept.
- **has-a**: Composition. The parent concept is built from, or contains, child concepts.
- **defined_on**: The concept is defined on another structure.
- **subtype_of**: The concept is a more specific version of another concept.

Use short edge labels. The label should explain the relation, not repeat the file name.

### Graph Rules

- A note should focus on one mathematical entity.
- `Define` should contain the minimal definition and the notation needed to identify the entity.
- `Properties` should hold the working knowledge: identities, closure properties, constructions, canonical examples, and important theorems.
- `Include` lists lower-level or contained concepts.
- `Parents` lists higher-level or prerequisite concepts.
- Together, the notes are intended to form a directed acyclic graph.

## Graph Synchronization

The graph tools live in [`math/src/`](./math/src/). Start the local Flask service first:

```powershell
cd D:/Algo/Notes/math_physics/math/src
python service.py
```

### Markdown To Graph JSON

Build a graph JSON snapshot from the Markdown notes:

```bash
curl --location 'http://localhost:5000/function' \
--header 'Content-Type: application/json' \
--data '{
  "function": "build_graph_json_from_markdown_folder",
  "params": {
    "folder_path": "D:/Algo/Notes/math_physics/math/"
  }
}'
```

### Graph JSON To Markdown

Regenerate Markdown notes from the graph JSON:

```bash
curl --location 'http://localhost:5000/function' \
--header 'Content-Type: application/json' \
--data '{
  "function": "build_markdown_from_graph_json",
  "params": {
    "json_file": "D:/Algo/Notes/math_physics/math/lib/math.json"
  }
}'
```

### Add A Child Node

Add an edge in the graph and rebuild the Markdown files:

```bash
curl --location 'http://localhost:5000/function' \
--header 'Content-Type: application/json' \
--data '{
  "function": "add_kid_for_graph",
  "params": {
    "json_file": "D:/Algo/Notes/math_physics/math/lib/math.json",
    "key": "Set",
    "kid_key": "Relation"
  }
}'
```

## Applied Mathematics

Applied mathematics is organized by problem type:

- [`algorithm/`](./applied%20mathematics/algorithm/) records data structures, graph problems, sequence problems, sorting, hashing, trees, heaps, and related algorithmic patterns.
- [`cryptography/`](./applied%20mathematics/cryptography/) records symmetric encryption, asymmetric encryption, hash algorithms, RSA, ECC, DES, AES, MD5, and SHA.
- [`differential equation/`](./applied%20mathematics/differential%20equation/) records ODEs, PDEs, and second-order linear PDEs.
- [`geometric construction/`](./applied%20mathematics/geometric%20construction/) records Bezier curves, triangulation, convex hulls, sampling, deformation, contour surfaces, and noise generation.
- [`geometric problem/`](./applied%20mathematics/geometric%20problem/) records intersection problems in flat and curved spaces.
- [`information/`](./applied%20mathematics/information/) records communication, compressed sensing, error correction, and measurement of information.
- [`language/`](./applied%20mathematics/language/) records formal language and abstract syntax trees.
- [`optimization problem/`](./applied%20mathematics/optimization%20problem/) records linear programming, integer programming, convex optimization, descent methods, ADMM, proximal gradient, interior point methods, and knapsack problems.
- [`statistics/`](./applied%20mathematics/statistics/) records regression, classification, interpolation, Gaussian processes, time series, unit-root tests, hypothesis testing, and stochastic differential equations.

## Physics

Physics notes are organized around action, symmetry, spacetime, fields, and complex systems.

### Mechanics

The basic principle is stationary action:

$$
\delta S = 0
$$

with

$$
S = \int L(q, \dot q, t)\,\mathrm dt.
$$

The Euler-Lagrange equation follows from this principle:

$$
\frac{\mathrm d}{\mathrm dt}\left(\frac{\partial L}{\partial \dot q}\right) - \frac{\partial L}{\partial q} = 0.
$$

Symmetry gives conservation laws through Noether's theorem:

- time translation symmetry gives conservation of energy;
- spatial translation symmetry gives conservation of momentum;
- rotational symmetry gives conservation of angular momentum.

### Spacetime

- **Absolute spacetime**: classical particle mechanics.

  $$
  S = \int \left(\frac{m v^2}{2} - U(\boldsymbol r, t)\right)\mathrm dt
  $$

- **Flat spacetime**: special-relativistic mechanics and field theory.
- **Curved spacetime**: general relativity and gravitational dynamics.

  $$
  S = -\frac{1}{c}\int L_m\sqrt{-g}\,\mathrm d^4x
  + \frac{c^3}{16\pi G}\int R\sqrt{-g}\,\mathrm d^4x
  $$

### Fields

- **Electromagnetic field**

  $$
  S = \sum\int mc\,\mathrm ds
  - \sum \int \frac{e}{c} A_k\,\mathrm dx^k
  - \frac{1}{16 \pi c}\int F_{ik}F^{ik}\,\mathrm d\Omega
  $$

- **Quantum field**: fields become the fundamental degrees of freedom.
- **Gravitational field**: spacetime geometry becomes dynamical.

### Complex Systems

- **Fluid**

  $$
  \rho \left(\frac{\partial\boldsymbol v}{\partial t}
  + (\boldsymbol v \cdot \nabla)\boldsymbol v \right)
  =
  - \nabla P
  + \rho \boldsymbol f
  + \eta \nabla^2 \boldsymbol v
  + \left(\zeta + \frac{\eta}{3}\right)\nabla(\nabla \cdot \boldsymbol v)
  $$

- **Statistics**: macroscopic behavior from microscopic states and probability distributions.

## Maintenance Principles

- Keep each note centered on one concept.
- Prefer structural links over loose references.
- Put definitions before examples and formulas before interpretation when that improves precision.
- Move mature drafts out of [`tmp/`](./tmp/) into the appropriate folder.
- When changing graph structure, keep Markdown files and `math/lib/math.json` synchronized.
