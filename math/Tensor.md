# Tensor

[TOC]

## Define

$$
T:\underbrace{V^*\times\cdots\times V^*}_{k\text{ times}}\times\underbrace{V\times\cdots\times V}_{l\text{ times}}\to\mathbb{R}
$$

A $(k,l)$-type tensor $T$ is a multilinear map on an $n$-dimensional [vector space](./Linear_Space.md) $V$ and its dual space $V^*$.

In abstract index notation, tensors $T_{a_1,\cdots, a_l}^{a_{l+1}, \cdot, a_{l+k}}$ are denoted by letters with indices, but the indices do not refer to specific components in a particular basis as in the traditional component-based index notation. Instead, they represent the abstract algebraic and geometric roles that the tensors play in a given context.

## Properties

### Basic Operations

- Addition: 

$$
(T + S)(\alpha_1,\cdots,\alpha_k,v_1,\cdots,v_l)=T(\alpha_1,\cdots,\alpha_k,v_1,\cdots,v_l)+S(\alpha_1,\cdots,\alpha_k,v_1,\cdots,v_l)
$$

- Tensor Product

$$
(T S)(\alpha_1,\cdots,\alpha_{k_1 + k_2},v_1,\cdots,v_{l_1 + l_2})=T(\alpha_1,\cdots,\alpha_{k_1},v_1,\cdots,v_{l_1})S(\alpha_{k_1+1},\cdots,\alpha_{k_1 + k_2},v_{l_1 + 1},\cdots,v_{l_1 + l_2})
$$


- $\alpha_1,\cdots,\alpha_k\in V^*$
- $v_1,\cdots,v_l\in V$.

### Contraction

$$
C(T)^{i_1\cdots i_{k - 1}i_{k + 1}\cdots i_m}_{j_1\cdots j_{l - 1}j_{l + 1}\cdots j_n}=\sum_{r = 1}^{N}T^{i_1\cdots r\cdots i_m}_{j_1\cdots r\cdots j_n}
$$

The contraction of a tensor is an operation that reduces the rank of a tensor by summing over a pair of indices. For a tensor $T^{i_1i_2\cdots i_m}_{j_1j_2\cdots j_n}$, if we contract over the indices $i_k$ and $j_l$, we sum over the values of these indices.

- $N$ is the dimension of the vector space on which the tensor is defined.

## Include

## Parents

- [Linear_Space](./Linear_Space.md): 

