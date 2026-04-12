# Basic principles of mechanics

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

## Canonical Transformations

Canonical transformations are coordinate changes $(q,p)\mapsto(Q,P)$ that preserve the Poisson bracket or, equivalently, the symplectic form:

$$
\omega = \sum_i \mathrm d q^i\wedge \mathrm d p_i
=
\sum_i \mathrm d Q^i\wedge \mathrm d P_i .
$$

They preserve the form of Hamilton's equations. A common way to construct them is by a generating function. For example, if $F_2(q,P,t)$ is used, then

$$
p_i = \frac{\partial F_2}{\partial q^i},\qquad
Q^i = \frac{\partial F_2}{\partial P_i},\qquad
K(Q,P,t)=H(q,p,t)+\frac{\partial F_2}{\partial t}.
$$

Canonical transformations are the classical counterpart of unitary transformations in quantum mechanics.

More details: [advanced hamiltonian mechanics](./advanced%20hamiltonian%20mechanics.md).

## Hamilton-Jacobi Theory

Hamilton-Jacobi theory seeks a canonical transformation to constants of motion. The principal function $S(q,t)$ satisfies

$$
H\left(q,\frac{\partial S}{\partial q},t\right)
+\frac{\partial S}{\partial t}=0 .
\tag{Hamilton-Jacobi equation}
$$

For a time-independent Hamiltonian one often writes

$$
S(q,t)=W(q)-Et,
$$

and obtains the time-independent Hamilton-Jacobi equation

$$
H\left(q,\frac{\partial W}{\partial q}\right)=E .
$$

The gradient of the action generates the momentum:

$$
p_i = \frac{\partial S}{\partial q^i}.
$$

This formulation connects classical mechanics with wave optics and semiclassical quantum mechanics.

More details: [advanced hamiltonian mechanics](./advanced%20hamiltonian%20mechanics.md).

## Action-Angle Variables and Integrability

For a completely integrable Hamiltonian system with $s$ degrees of freedom, there exist $s$ independent conserved quantities $F_i$ in involution:

$$
\{F_i,F_j\}=0 .
$$

On compact invariant tori one can introduce action-angle variables $(I_i,\theta^i)$:

$$
I_i=\frac{1}{2\pi}\oint_{\gamma_i} p\,\mathrm dq,\qquad
\dot I_i=0,\qquad
\dot\theta^i=\omega^i(I).
$$

The Hamiltonian depends only on the actions:

$$
H=H(I).
$$

Small perturbations of integrable systems lead to KAM theory: many invariant tori survive if the perturbation is small and the frequency vector satisfies a non-resonance condition, while resonant tori can break and produce chaotic layers.

More details: [advanced hamiltonian mechanics](./advanced%20hamiltonian%20mechanics.md).

## Constrained Hamiltonian Systems

If the Legendre transform is singular, the system has constraints in phase space:

$$
\phi_a(q,p)=0 .
$$

Dirac's theory classifies constraints as:

- **First-class constraints**: constraints whose Poisson brackets with all constraints vanish on the constraint surface; they usually generate gauge transformations.
- **Second-class constraints**: constraints whose Poisson bracket matrix is invertible on the constraint surface; they remove true phase-space degrees of freedom.

The total Hamiltonian has the form

$$
H_T = H_c + u^a\phi_a ,
$$

where $u^a$ are undetermined multipliers. Second-class constraints are handled by the Dirac bracket:

$$
\{f,g\}_D
=
\{f,g\}
-
\{f,\chi_a\}C^{ab}\{\chi_b,g\},
$$

where $C^{ab}$ is the inverse of $C_{ab}=\{\chi_a,\chi_b\}$.

More details: [advanced hamiltonian mechanics](./advanced%20hamiltonian%20mechanics.md).

## Small Oscillations and Normal Modes

Near a stable equilibrium $q_0$, expand the Lagrangian to quadratic order:

$$
L \approx
\frac12 M_{ij}\dot\eta^i\dot\eta^j
-
\frac12 K_{ij}\eta^i\eta^j,\qquad
\eta^i=q^i-q_0^i .
$$

The normal modes solve the generalized eigenvalue problem

$$
K a = \omega^2 M a .
$$

Each normal coordinate behaves like an independent harmonic oscillator. This is the classical origin of phonons, field modes, and many perturbative expansions.

More details: [small oscillations and classical chaos](./small%20oscillations%20and%20classical%20chaos.md).

## Classical Chaos

A deterministic Hamiltonian system can be chaotic when nearby initial conditions separate exponentially:

$$
\|\delta z(t)\| \sim e^{\lambda t}\|\delta z(0)\| .
$$

Here $\lambda$ is a Lyapunov exponent. Hamiltonian chaos is usually studied through:

- Poincare sections.
- Periodic orbits and their stability.
- Separatrices and homoclinic intersections.
- Resonance overlap.
- Area-preserving maps such as the standard map.

More details: [small oscillations and classical chaos](./small%20oscillations%20and%20classical%20chaos.md).

## Continuum Mechanics and Elasticity

For continuous media, the finite-dimensional coordinates $q^i(t)$ are replaced by fields such as a displacement field $u_i(x,t)$. For small deformations,

$$
\varepsilon_{ij}
=
\frac12(\partial_i u_j+\partial_j u_i)
\tag{strain tensor}
$$

and the stress tensor of a linear isotropic elastic solid is

$$
\sigma_{ij}
=
\lambda\,\delta_{ij}\varepsilon_{kk}
+2\mu\,\varepsilon_{ij}.
\tag{Hooke's law}
$$

The equation of motion is

$$
\rho\,\partial_t^2 u_i = \partial_j\sigma_{ij}+f_i .
$$

This is the solid counterpart of fluid mechanics and the classical basis for sound waves, elastic waves, phonons, and continuum field theory.

More details: [elasticity](./elasticity.md).

## Field

A **field** assigns a value to every point of space or spacetime. Fields may be scalar, vector, spinor, or tensor-valued. The Lagrangian formalism generalizes from particles to fields by replacing

$$
q^i(t)\quad\longrightarrow\quad \phi^a(x^\mu),
$$

and the action becomes

$$
S[\phi]=\int \mathcal L(\phi^a,\partial_\mu\phi^a,x^\mu)\,\mathrm d^n x .
$$

The Euler-Lagrange equation for fields is

$$
\frac{\partial \mathcal L}{\partial \phi^a}
-
\partial_\mu
\left(
\frac{\partial \mathcal L}{\partial(\partial_\mu\phi^a)}
\right)
=0 .
$$

## Symmetry: Noether's theorem

### Symmetry and conserved quantity

For every differentiable continuous symmetry of the action, there exists a corresponding conserved quantity.

- Time translation symmetry -> conservation of energy.
- Spatial translation symmetry -> conservation of linear momentum.
- Rotational symmetry -> conservation of angular momentum.
- Internal symmetry -> conservation of charge.
- Gauge symmetry -> constraint and redundancy of description.

For fields, Noether's theorem gives a conserved current:

$$
\partial_\mu j^\mu = 0 .
$$

## Appendix

### Proof of Euler-Lagrange equations

Let $q(t)\to q(t)+\epsilon\eta(t)$ with fixed endpoints $\eta(t_1)=\eta(t_2)=0$. Then

$$
\begin{align*}
\delta S
&=
\delta \int_{t_1}^{t_2} L(q,\dot q,t)\,\mathrm dt\\
&=
\int_{t_1}^{t_2}
\left(
\frac{\partial L}{\partial q^i}\delta q^i
+
\frac{\partial L}{\partial \dot q^i}\delta \dot q^i
\right)\mathrm dt\\
&=
\left.
\frac{\partial L}{\partial \dot q^i}\delta q^i
\right|_{t_1}^{t_2}
+
\int_{t_1}^{t_2}
\left(
\frac{\partial L}{\partial q^i}
-
\frac{\mathrm d}{\mathrm dt}
\frac{\partial L}{\partial \dot q^i}
\right)
\delta q^i\,\mathrm dt .
\end{align*}
$$

The boundary term vanishes. Since $\delta q^i$ is arbitrary,

$$
\frac{\mathrm d}{\mathrm dt}
\left(
\frac{\partial L}{\partial \dot q^i}
\right)
-
\frac{\partial L}{\partial q^i}
=0 .
$$
