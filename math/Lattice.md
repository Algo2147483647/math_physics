# Lattice

[TOC]

## Define

$$
(L, \wedge, \vee)
$$

Lattice is a concept of partially ordered sets, which is a special type of [algebraic structure](./Algebra_Structure.md) that can define minimum upper and maximum lower bounds on certain sets.一个格 $L$ 是一个集合，配合两个二元运算meet $\wedge$和 join $\vee$，满足以下公理：

1. **交换律**：$\forall a, b \in L$，有 $a \wedge b = b \wedge a$ 和 $a \vee b = b \vee a$
2. **结合律**：$\forall a, b, c \in L$，有 $a \wedge (b \wedge c) = (a \wedge b) \wedge c$ 和 $a \vee (b \vee c) = (a \vee b) \vee c$
3. **吸收律**：$\forall a, b \in L$，有 $a \wedge (a \vee b) = a$ 和 $a \vee (a \wedge b) = a$
4. **幂等律**：$\forall a \in L$，有 $a \wedge a = a$ 和 $a \vee a = a$

在格中，任意两个元素 $a$ 和 $b$ 的“meet” $a \wedge b$ 是它们所有下界的最大者，而它们的“join” $a \vee b$ 是它们所有上界的最小者。

## Properties



## Include

- [Boolean_Algebra](./Boolean_Algebra.md): 

## Parents

- [Algebra_Structure](./Algebra_Structure.md): 

