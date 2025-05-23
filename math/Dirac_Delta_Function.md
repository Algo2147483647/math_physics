# Dirac Delta Function

[TOC]

## Define

Dirac delta function $\delta(x)$ is a type of [generalized function](./Function.md). 
$$
\delta(x) = \left\{\begin{matrix}+\infty,& x = 0\\0, & x \neq 0\end{matrix}\right.\\
\int_{-\infty}^{\infty}\delta(x) \mathrm{d} x = 1
$$
<img src="assets/Dirac_distribution_PDF.svg" alt="Dirac_distribution_PDF" style="zoom:15%;" />

## Properties

### sampling property  

$$
\int_{-\infty}^{\infty} f(t) \delta(t-T) \mathrm{d} t = f(T)
$$

## Include

## Parents

- [Function](./Function.md): is-a

