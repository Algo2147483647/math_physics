# Graph

[TOC]

## Define

$$
\begin{align*}
G &= (V, E)  \tag{Graph} \\
E &= \{(v_i, v_j)\ |\ v_i, v_j \in V\}  \tag{Edge set}
\end{align*}
$$

Graph is a pair consist of vertex set $V$ and edge set $E$ with weights of edges $w: E \to \mathbb R$.

- $V$: Vertex set
- $E$: Edge set, a set of paired vertices
- $w: E \to \mathbb R$: weight of edge

### Undirected Graph & Directed Graph

$$
\begin{align*}
E &= \{\{v_i, v_j\}\ |\ v_i, v_j \in V\}  \tag{Undirected Graph}\\
E &= \{(v_i, v_j)\ |\ v_i, v_j \in V\}  \tag{Directed Graph}
\end{align*}
$$

Undirected Graph, is a type of graph that does not distinguish the direction of edges.

Directed Graph, is a type of graph that distinguish the direction of edges and its edge set is a set of ordered pairs.

## Properties

### Representation by Adjacency Matrix
Due to the discreteness of vertices, we can represent the weight of edge $w: E \to \mathbb R$ by Matrix $\boldsymbol G \in \mathbb R^{n \times n}$.

$$
\boldsymbol G = \left(\begin{matrix} w(v_1, v_1) & \cdots & w(v_1, v_n) \\ \vdots&\ddots &\vdots \\ w(v_n, v_1) & \cdots & w(v_n, v_n) \end{matrix}\right)
$$


### Degree
Degree of a node refers to the number of edges connecting this node. 

### Connectivity

In an undirected graph $G=(V, E)$, the graph is said to be connected if there is a path between every pair of vertices. A path is a sequence of vertices where consecutive vertices are adjacent (connected by an edge).

In a directed graph $G=(V, E)$, the graph is strongly connected if for every pair of vertices $u$ and $v$, there is a directed path from $u$ to $v$ and a directed path from $v$ to $u$.

### Directivity

### Acyclicity

### Euler Path & Euler Graph

Euler path is a path in a graph that passes through every edge exactly once. If the path starts and ends at the same vertex, it is called an Euler circuit. A graph that has an Euler circuit is called an Eulerian graph, while a graph that has an Euler path but not an Euler circuit is called a semi-Eulerian graph. 

<img src="./assets/48727417-28c3d500-ec58-11e8-9715-33b168a50b7c.png" alt="theory1" style="zoom:20%;" />

#### Property
The existence of an Euler path or circuit in a connected undirected graph depends on the degree of the vertices. For a graph to have an Euler circuit, every vertex must have an even degree. For a connected undirected graph to have an Euler path, exactly two vertices must have an odd degree (all other vertices must have even degree).


### Matching of Graph

$$
\forall e_i, e_j \in M \subseteq E, e_i \neq e_j \quad\Rightarrow\quad v(e_i, 1) \neq v(e_i, 2) \neq v(e_j, 1) \neq v(e_j, 2)  \tag{Matching}
$$
Matching of a graph is a set of edges $M \subseteq E$ that have no common points between any two edges.

#### Maximum Matching

$$
M^* = \arg\max_{M} \quad \text{number}(M) \tag{Maximum Matching}
$$
Maximum Matching is a matching with the largest number of matching edges among all matches in a graph.

#### Perfect Matching

$$
V^{(G)} = v(M^*)
$$
Perfect Matching is a matching that all vertices of the graph are in it.

## Include

- [Bipartite_Graph](./Bipartite_Graph.md): 

- [Complete_Graph](./Complete_Graph.md): 

- [Directed_Acyclic_Graph](./Directed_Acyclic_Graph.md): 

- [Tree](./Tree.md): 

## Parents

- [Set](./Set.md): 

