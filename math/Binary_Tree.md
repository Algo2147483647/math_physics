# Binary Tree

[TOC]

## Define

A tree in which each node has at most two children, which are referred to as the left child and the right child.

## Properties

### Special Binary Tree

- Full Binary Tree: Every node has either 0 or 2 children. All leaf nodes are at the same level.
- Complete Binary Tree: All levels are completely filled except possibly the last level, and all nodes are as far left as possible.
- Balanced Binary Tree: The heights of the left and right subtrees of every node differ by at most 1.

For Complete Binary Tree,
A binary tree in which all leaf nodes have the same height.
Number of nodes with depth $h$: $2^h$
Number of nodes in a complete binary tree with depth $h$: $2^{h+1} - 1$ 
Number of non leaf nodes: $2^h - 1$
Number of leaf nodes: $2^h$  

Proof: 
$$
  \sum\limits_{i=0}^h 2^i = \frac{1 - 2^h}{1 - 2} = 2^h - 1  \tag{geometric sequence summation}
$$

### Traversal
Pre-order Traversal: The root node is visited first, then the left subtree, and finally the right subtree.
In-order Traversal: The left subtree is visited first, then the root node, and finally the right subtree. For a binary search tree, in-order traversal visits the nodes in ascending order.
Post-order Traversal: The left subtree is visited first, then the right subtree, and finally the root node.

## Include

## Parents

- [Tree](./Tree.md): 

