# Directed Acyclic Graph

[TOC]

## Define

A directed graph without loops.

## Properties

### Topological Sort  

- Purpose  
  Linear ordering of point sets of directed acyclic graphs, and satisfying:
  - Each point appears only once
  - If there is an edge from point A to point B, point A appears before point B in the sequence.

- Application  
  - Help determine whether a graph is a directed acyclic graph.  

- Algorithm  
  Iterate and delete points with 0 incoming edge on the Graph, put these points into the output sequence in turn, until all points are removed from the graph.  

  If there are no more nodes in the graph that can be delete, but the number of remaining points is not 0, then the graph has loops and is not a directed acyclic graph.
  
  ```python
  def topological_sort(graph):
      in_degree = dict(int)
      for node in graph:
          for neighbor in graph[node]:
              in_degree[neighbor] += 1
  
      queue = [node for node, degree in in_degree.items() if degree == 0]
      result = []
      
      while not queue.empty():
          node = queue.pop()
          result.append(node)
          
          for neighbor in graph[node]:
              in_degree[neighbor] -= 1
              if in_degree[neighbor] == 0:
                  queue.append(neighbor)
                  
      if result.size() == graph.size():
          return result
      else:
          return None
  ```

## Include

## Parents

- [Graph](./Graph.md): 

