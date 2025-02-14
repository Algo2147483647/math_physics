# Directed Acyclic Graph

[TOC]

## Define

Directed acyclic graph is directed graph without loops.

## Properties

### Topological Sort  

Topological Sort aims to linear ordering of point sets of directed acyclic graphs, and satisfying as follows. Topological Sort can help determine whether a graph is a directed acyclic graph.  
- Each point appears only once
- If there is an edge from point A to point B, point A appears before point B in the sequence.

#### Solution

Iterate and delete points with 0 incoming edge on the Graph, put these points into the output sequence in turn, until all points are removed from the graph. If there are no more nodes in the graph that can be delete, but the number of remaining points is not 0, then the graph has loops and is not a directed acyclic graph.

## Include

## Parents

- [Graph](./Graph.md): directed, acyclic

