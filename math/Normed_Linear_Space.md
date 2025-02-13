# Normed Linear Space

[TOC]

## Define

$$
(X, ||·||)
$$
The [Linear Space](./Linear_Space.md) of Norm is defined.

Symbol:
- $X$: linear space
- $||·||$:  Norm

## Properties

### Norm

#### Include

##### Vector Norm 

- Define   
  A class of functions$f: X \to \mathbb R$ that satisfy:
  
  - Nonnegativity, $||A|| ≥ 0 ; ||A|| = 0 <=> A = 0$
  - Homogeneity, $||k A|| = |k| ||A||$
  - Trigonometric Inequality, $||A + B|| ≤ ||A|| + ||B||$
  
- Example 
  - $p$-Norm
    $$
    \begin{align*}
      ||x||_{p} &= \left(\sum_{i=1}^n |x_i|^p \right)^{1 / p}  \tag{p-Norm}\\
      ||x||_0 &= number(x_i ≠ 0 |_{i=1:n})  \tag{0-Norm}\\
      ||x||_1 &= \sum_{i=1}^n |x_i|  \tag{1-Norm}\\
      ||x||_2 &= \sqrt{\sum_{i=1}^n x_i^2}  \tag{2-Norm}\\
      ||x||_∞ &= \max |x_i|  \tag{$∞$-Norm}\\
    \end{align*}
    $$

  - Ellipse Norm 
    $$||x||_A = (x^T A x)^{1/2}$$

##### Matrix Norm 

- Define   
  A class of functions that satisfy:
  - Nonnegativity, $||A|| ≥ 0$, if and only if $A = 0, ||A|| = 0$
  - Homogeneity, $||k A|| = |k| ||A||$
  - Trigonometric Inequality, $||A + B|| ≤ ||A|| + ||B||$
  - Consistency, $||A B|| ≤ ||A||\ ||B||$

- Example 
  - simple
    $$
    \begin{align*}
      ||A||_{m_1} &= \sum_{i,j} |a_{ij}|  \\
      ||A||_{m_2} &= \left(\sum_{i,j} a_{ij}^2 \right)^{1/2}  \\
      ||A||_{m_∞} &= n·\max_{i,j}|a_{ij}|  \\
      ||A||_1    &= \max_j \sum_i |a_{ij}|  \tag{列和 Norm}\\
      ||A||_∞ &= \max_i \sum_j |a_{ij}|  \tag{行和 Norm}\\
    \end{align*}
    $$
  - Spectral Norm   
    $$
    ||A||_2 = \sqrt{\max\ λ_i}
    $$
    $(λ_i)$ is eigenvalue of $A^H A$ .

  - Frobenius Norm 
    $$
    ||\.A||_F = \sqrt{\sum_i \sum_j |a_{ij}|^2}
    $$

#### Property

- Matrix & Vector Norm Consistency
  $$
  ||A x||_V ≤ ||A||_M ||x||_V
  $$

## Include

- [Inner_Product_Space](./Inner_Product_Space.md): 

## Parents

- [Linear_Space](./Linear_Space.md): 

