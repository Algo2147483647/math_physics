# $Mathematic\ Library$

[TOC]

## Note Format

- **Entity / Concept**: Take a mathematical entity as a note.
- **Define**: The definition of this concept.
- **Property**: The important properties of this concept.
- **Include**: Subsets of this concept.
- **Problem**: The classic problem derived from this concept.

### Knowledge Graph of Nodes

- If a hyperlink appears in the definition `Definie`, it indicates that it is the parent node of this concept.
- Other hyperlinks that appear are child nodes of this concept.
- All concepts together form a directed acyclic graph.
- Specific implementation reference `./admin/`

## Physics

- Basic principles of mechanics

  - The Principle of Least Action
  - Symmetry: Noether's theorem

- Spacetime
  - Absolute spacetime

    $S = \int \left(\frac{m v^2}{2} - U(\boldsymbol r, t)\right) \mathrm dt  \tag{particle}$

  - Flat spacetime

  - Curved spacetime

    $S=-\frac{1}{c}\int L_m \sqrt{-g} \mathrm d^4x + \frac{c^3}{16\pi G}\int R\sqrt{-g} \mathrm d^4x$
  
- Field
  - Electromagnetic field

    $S = \sum\int mc \mathrm ds - \sum \int \frac{e}{c} A_k \mathrm dx^k - \frac{1}{16 \pi c} \int F_{ik}F^{ik} \mathrm d \Omega$

  - Quantum field

  - Gravitational field

- Complex System
  - Fluid

    $ρ \left(\frac{∂\boldsymbol v}{∂t} + (\boldsymbol v · ∇) \boldsymbol v \right) =  - ∇ P  + ρ \boldsymbol f + η ∇^2 \boldsymbol v + \left(ζ + \frac{η}{3} \right) ∇ (∇ · \boldsymbol v)$

  - Statistics
