# Relation

[TOC]

## Define

$$
R(A_1, A_2, \cdots, A_n) \subseteq A_1 \times A_2 \times \cdots \times A_n  \tag{Relation}
$$

A $n$-ary **relation** $R$ in sets $A_1, A_2, \cdots, A_n$ is a [subset](./Set.md) of their Cartesian product $A_1 \times A_2 \times \cdots \times A_n$. Relation is like a table, consists of a set of tuples (rows) and attributes (columns).

- $n$ Degree: The number of attributes (columns) in a relation.
- Cardinality: The number of tuples (rows) in a relation.

## Property

### Operations

#### Set operations

A relation is essentially a set, so it possesses the same operations as a set.

- **Intersection** (∩): returns the rows that are common to both relations.

$$
R\cap S=\{t|t\in R\land t\in S\} \text{ and } R\cap S = R-(R - S)
$$

- **Union** (∪): combines the results of two relations. The relations must be union-compatible (i.e., they have the same number of columns with the same domains).

$$
R\cup S = \{t|t\in R \lor t\in S\}
$$

- **Set Difference** (−): returns the rows that are in the first relation but not in the second.

$$
R - S = \{t|t\in R \land t\notin S\}
$$

- **Cartesian Product** (×): combines each row of the first relation with every row of the second relation.

$$
R\times S=\{(r_1,r_2,\cdots,r_m,s_1,s_2,\cdots,s_n)|(r_1,r_2,\cdots,r_m)\in R\land(s_1,s_2,\cdots,s_n)\in S\}
$$


#### Select & Projection

**Select** (σ): filters rows based on a specified condition (predicate).
$$
\sigma_\text{condition}(R)=\{t|t\in R\land F(t)=\text{True}\}
$$

**Projection** (π): selects specific columns from a relation.
$$
\pi_{A}(R)=\{t[A]|t\in R\}
$$

#### Join

**Join** ($\Join$): combines related tuples from two relations based on a condition, typically a common attribute. Where A and B are groups of attributes of equal and comparable degree on R and S respectively, and $\theta$ is a comparison operator.
$$
R\Join_{A\theta B}S=\sigma_{A\theta B}(R\times S)
$$

## Include

### Binary Relation

#### Define  

$$
X \ R\ Y \subseteq X \times Y  \tag{Binary Relation}
$$
Binary Relation $R$ over set $X, Y$ is a subset of the Cartesian product $X \times Y$. The set $X$ is called the domain, and set $Y$ the codomain.

