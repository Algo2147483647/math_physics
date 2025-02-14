# Tree

[TOC]

## Define

Tree is a class of connected undirected graphs without loops.

### Rooted Tree

- root node: A node without forward nodes, and a tree has only one root node.
- leaf node: A node that has no children.
- depth: Number of edges in the simple path from node to root node. The depth of the tree is the maximum node depth in the tree.

## Properties

- There exists and only exists one single simple path between any two points of the tree.
- $number(E) = number(V) - 1$
- Delete an edge, the Tree will become disconnected;  
  Add an edge, the Tree will have a loop.

## Include

- [Binary_Tree](./Binary_Tree.md): 

## Parents

- [Graph](./Graph.md): undirected, connected, acyclic

