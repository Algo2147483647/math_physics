# Hilbert Transform

[TOC]

## Define

[**Hilbert transform**](./Function.md) of $u(t)$ can be thought of as the convolution of $u(t)$ with the function $h(t) = \frac{1}{\pi t}$, known as the Cauchy kernel. Because $1/t$ is not integrable across $t = 0$, the integral defining the convolution does not always converge. Instead, the Hilbert transform is defined using the Cauchy principal value (denoted here by $p.v.$).
$$
H(u)(t) = p.v.\frac{1}{\pi}\int_{-\infty}^{+\infty} \frac{u(\tau)}{t-\tau}\mathrm{d}\tau
$$

## Properties

- $H(H(u))(t) = u(-t)$
- $H(\omega) = (-i \cdot \text{sgn}(\omega))\cdot \mathcal F_h(\omega)$

## Include

## Parents

- [Function](./Function.md): 

