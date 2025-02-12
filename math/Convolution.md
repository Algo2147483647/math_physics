# Convolution

[TOC]

## Define

Cross Correlation and Convolution, are a measure of similarity (through [inner product](./Inner_Poduct_Space.md)) of two functions $f, g$ of the displacement $t \in \mathbb R$ of one relative to the other.
$$
\begin{align*}
Corr(f(t), g(t)) 
&= \sum_{t = -\infty}^{\infty} f(\tau) g(t + \tau)  \tag{Cross Correlation}  \\
&= \sum_{t = -\infty}^{\infty} f(-t+\tau) g(\tau)  \\
&= \int_{-\infty}^{\infty} f(\tau) g(t + \tau) \mathrm d \tau   \\
&= \int_{-\infty}^{\infty} f(-t+\tau) g(\tau) \mathrm d \tau  \\
Conv(f(t), g(t)) 
&= \sum_{t = -\infty}^{\infty} f(\tau) g(t - \tau)  \tag{Convolution}  \\
&= \sum_{t = -\infty}^{\infty} f(t-\tau) g(\tau)  \\
&= \int_{-\infty}^{\infty} f(\tau) g(t - \tau) \mathrm d \tau   \\
&= \int_{-\infty}^{\infty} f(t-\tau) g(\tau) \mathrm d \tau  \\
\end{align*}
$$

## Properties

- Commutativity & Associativity & Distributivity
$$
\begin{align*}
Conv(f, g)  &= Conv(g, f)  \tag{Commutativity}  \\
Conv(f, Conv(g, h))  &= Conv(Conv(f, g), h)  \tag{Associativity}  \\
Conv(f, g+h)  &= Conv(f, g) + Conv(f, h)  \tag{Distributivity}  \\
a·Conv(f, g)  &= Conv(a·f, g)  \tag{Associativity with scalar multiplication}  \\
\end{align*}
$$
- Differential 
$$
\frac{\mathrm{d}(f_1(t) * f_2(t))}{\mathrm{d} t} = \mathrm{d}(f_1(t) * \frac{\mathrm{d} f_2(t)}{\mathrm{d} t} = \mathrm{d}(f_2(t) * \frac{\mathrm{d} f_1(t)}{\mathrm{d} t}
$$
- Integral 
$$
\int^t_{-\infty} f_1(λ) * f_2(λ) \mathrm{d} λ = f_1(t) * \int^t_{-\infty} f_2(λ) \mathrm{d} λ =  f_2(t) * \int^t_{-\infty} f_1(λ) \mathrm{d} λ
$$
- Relation with impulse function
$$
f(t) * δ^{(k)}(t - t_0) = f^{(k)}(t - t_0)
$$
$$
\begin{align*}
\mathrm{d}f(t) * δ(t) &= f(t)\\
\mathrm{d}f(t) * δ(t - t_0) &= f(t - t_0)\\
\mathrm{d}f(t) * δ'(t - t_0) &= f'(t - t_0)\\
\mathrm{d}f(t) * u(t - t_0) &= f(t) * \int^t_{-\infty} δ(λ - t_0) \mathrm{d} λ = \int^t_{-\infty} f(λ - t_0) \mathrm{d} λ\\
\end{align*}
$$

### Convolution Theorem
$$
\mathcal F(f_1(t) * f_2(t)) = F_1(ω) · F_2(ω)
$$
$$
\mathcal F(F_1(ω) * F_2(ω)) = \frac{1}{2 π} f_1(t) · f_2(t)
$$

## Include

## Parents

- [Inner_Poduct_Space](./Inner_Poduct_Space.md): 

