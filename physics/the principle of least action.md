# The Principle of Least Action

[TOC]

## The Principle of Least Action

### Action & Lagrangian

$$
S[q] = \int_{t_1}^{t_2} L(q,\dot q,t)\,\mathrm{d}t
\tag{Action}
$$

**Action** $S$ is a functional of the path $q(t)$. **Lagrangian** $L(q,\dot q,t)$ is a function on the tangent bundle of configuration space, usually written as

$$
L = T - V
$$

for a natural mechanical system. Different Lagrangians that differ by a total time derivative,

$$
L' = L + \frac{\mathrm d F(q,t)}{\mathrm d t},
$$

give the same equations of motion because they change the action only by a boundary term.

### The Principle of Stationary Action

$$
\delta S = 0
\tag{Hamilton's principle}
$$

The physical path between two fixed endpoints is a stationary point of the action. "Stationary" means that the first-order variation vanishes; the action need not be a minimum.

### Equations of motion: Euler-Lagrange equations

$$
\frac{\mathrm d}{\mathrm dt} \left( \frac{\partial L}{\partial \dot{q}^i} \right) - \frac{\partial L}{\partial q^i} = 0
\tag{Euler-Lagrange}
$$

- $q^i$: generalized coordinates.
- $\dot q^i$: generalized velocities.
- $p_i = \partial L / \partial \dot q^i$: canonical momenta.

> ***Proof of Euler-Lagrange equations***
>
> Let $q(t)\to q(t)+\epsilon\eta(t)$ with fixed endpoints $\eta(t_1)=\eta(t_2)=0$. Then
>
> $$
> \begin{align*}
> \delta S
> &=
> \delta \int_{t_1}^{t_2} L(q,\dot q,t)\,\mathrm dt\\
> &=
> \int_{t_1}^{t_2}
> \left(
> \frac{\partial L}{\partial q^i}\delta q^i
> +
> \frac{\partial L}{\partial \dot q^i}\delta \dot q^i
> \right)\mathrm dt\\
> &=
> \left.
> \frac{\partial L}{\partial \dot q^i}\delta q^i
> \right|_{t_1}^{t_2}
> +
> \int_{t_1}^{t_2}
> \left(
> \frac{\partial L}{\partial q^i}
> -
> \frac{\mathrm d}{\mathrm dt}
> \frac{\partial L}{\partial \dot q^i}
> \right)
> \delta q^i\,\mathrm dt .
> \end{align*}
> $$
>
> The boundary term vanishes. Since $\delta q^i$ is arbitrary,
>
> $$
> \frac{\mathrm d}{\mathrm dt}
> \left(
> \frac{\partial L}{\partial \dot q^i}
> \right)
> -
> \frac{\partial L}{\partial q^i}
> =0 .
> $$
>

### Generalized forces and constraints

For non-conservative generalized forces $Q_i$, the equations become

$$
\frac{\mathrm d}{\mathrm dt} \left( \frac{\partial L}{\partial \dot{q}^i} \right) - \frac{\partial L}{\partial q^i} = Q_i .
$$

For holonomic constraints $f_a(q,t)=0$, one may introduce Lagrange multipliers:

$$
L_c(q,\dot q,t,\lambda)=L(q,\dot q,t)+\lambda^a f_a(q,t).
$$

The multipliers $\lambda^a$ encode the constraint forces.

## Phase Space

$$
(q^1,\cdots,q^s,p_1,\cdots,p_s)
$$

**Phase space** is the $2s$-dimensional space of generalized coordinates and canonical momenta. A point in phase space represents a complete instantaneous state of a Hamiltonian system.

### Hamiltonian function

If the Legendre transform from $\dot q$ to $p$ is nonsingular, the Hamiltonian is

$$
\begin{align*}
H(q,p,t) &= \sum_i p_i \dot q^i - L(q,\dot q,t),\\
p_i &= \frac{\partial L}{\partial \dot q^i}.
\end{align*}
$$

Hamilton's equations are

$$
\begin{align*}
\dot q^i &= \frac{\partial H}{\partial p_i},\\
\dot p_i &= -\frac{\partial H}{\partial q^i}.
\end{align*}
\tag{Hamilton's equations}
$$

The Hamiltonian method rewrites $s$ second-order equations as $2s$ first-order equations on phase space.

### Poisson bracket

$$
\{f,g\} =
\sum_k \left(
\frac{\partial f}{\partial q^k}\frac{\partial g}{\partial p_k}
-
\frac{\partial f}{\partial p_k}\frac{\partial g}{\partial q^k}
\right)
\tag{Poisson bracket}
$$

The time evolution of any phase-space function $f(q,p,t)$ is

$$
\frac{\mathrm df}{\mathrm dt}
=
\frac{\partial f}{\partial t}+\{f,H\}.
$$

The fundamental Poisson brackets are

$$
\{q^i,q^j\}=0,\qquad
\{p_i,p_j\}=0,\qquad
\{q^i,p_j\}=\delta^i_j .
$$

### Symplectic form

The canonical one-form and symplectic two-form are

$$
\theta = \sum_i p_i\,\mathrm d q^i,\qquad
\omega = -\mathrm d\theta = \sum_i \mathrm d q^i \wedge \mathrm d p_i .
$$

The Hamiltonian vector field $X_H$ is defined by

$$
\iota_{X_H}\omega = \mathrm dH .
$$

In canonical coordinates this definition is equivalent to Hamilton's equations. The pair $(M,\omega)$, where $M$ is phase space and $\omega$ is a closed non-degenerate two-form, is a **symplectic manifold**.

### Liouville's Theorem

Hamiltonian flow preserves the symplectic volume:

$$
\Omega = \frac{\omega^s}{s!},\qquad
\mathcal L_{X_H}\Omega = 0 .
$$

Equivalently, the phase-space volume of a transported region is invariant:

$$
\int_{\Gamma_t}\mathrm d\Gamma = \mathrm{const}.
$$

This is the geometric basis of the microcanonical ensemble in statistical mechanics.

### Maupertuis Principle

For a time-independent natural system with fixed energy $H=E$, the trajectory in configuration space extremizes the abbreviated action

$$
W = \int p_i\,\mathrm d q^i .
$$

This is **Maupertuis' principle**. It is useful for relating mechanics to geometry because the motion can be regarded as geodesic motion under the Jacobi metric.