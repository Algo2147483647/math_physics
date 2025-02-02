# $Tensor$

[TOC]

## Define

A $(k,l)$-type tensor $T$ on an $n$-dimensional vector space $V$ is a multilinear map,
$$
T:\underbrace{V^*\times\cdots\times V^*}_{k\text{ times}}\times\underbrace{V\times\cdots\times V}_{l\text{ times}}\to\mathbb{R}
$$

## Property

### Operations

Addition: 

$$
(T + S)(\alpha_1,\cdots,\alpha_k,v_1,\cdots,v_l)=T(\alpha_1,\cdots,\alpha_k,v_1,\cdots,v_l)+S(\alpha_1,\cdots,\alpha_k,v_1,\cdots,v_l)
$$

Tensor Product

$$
(T S)(\alpha_1,\cdots,\alpha_{k_1 + k_2},v_1,\cdots,v_{l_1 + l_2})=T(\alpha_1,\cdots,\alpha_{k_1},v_1,\cdots,v_{l_1})S(\alpha_{k_1+1},\cdots,\alpha_{k_1 + k_2},v_{l_1 + 1},\cdots,v_{l_1 + l_2})
$$




- $\alpha_1,\cdots,\alpha_k\in V^*$
- $v_1,\cdots,v_l\in V$.
