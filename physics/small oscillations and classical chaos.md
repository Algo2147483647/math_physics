# Small Oscillations and Classical Chaos

[TOC]

## Purpose

Small-oscillation theory describes motion near stable equilibria by reducing coupled systems to independent normal modes. Classical chaos studies deterministic systems whose long-time behavior is highly sensitive to initial conditions.

This page expands the overview in [basic principles of mechanics](./basic%20principles%20of%20mechanics.md).

## Small Oscillations

### Equilibrium and quadratic expansion

Let $q_0$ be an equilibrium point:

$$
\left.\frac{\partial V}{\partial q^i}\right|_{q_0}=0.
$$

Define small displacements

$$
\eta^i=q^i-q_0^i.
$$

For a natural system,

$$
L=\frac12 M_{ij}(q)\dot q^i\dot q^j - V(q),
$$

the quadratic approximation near a stable equilibrium is

$$
L_2=
\frac12 M_{ij}\dot\eta^i\dot\eta^j
-
\frac12 K_{ij}\eta^i\eta^j,
$$

where

$$
M_{ij}=M_{ij}(q_0),\qquad
K_{ij}=
\left.
\frac{\partial^2 V}{\partial q^i\partial q^j}
\right|_{q_0}.
$$

### Normal mode equation

The equations of motion are

$$
M\ddot\eta+K\eta=0.
$$

Try

$$
\eta(t)=a e^{i\omega t}.
$$

Then

$$
K a = \omega^2 M a.
$$

This generalized eigenvalue problem gives the normal frequencies $\omega_\alpha$ and mode shapes $a_\alpha$.

### Decoupling

If the eigenvectors are normalized by

$$
a_\alpha^T M a_\beta=\delta_{\alpha\beta},
$$

then the normal coordinates $Q_\alpha$ diagonalize the quadratic Lagrangian:

$$
L_2 =
\sum_\alpha
\left(
\frac12 \dot Q_\alpha^2
-
\frac12\omega_\alpha^2Q_\alpha^2
\right).
$$

Each mode behaves as an independent harmonic oscillator.

## Coupled Oscillators

### Two equal masses and three springs

For two equal masses $m$ coupled by springs, a typical quadratic Lagrangian is

$$
L=
\frac12m(\dot x_1^2+\dot x_2^2)
-
\frac12k(x_1^2+x_2^2)
-
\frac12k_c(x_1-x_2)^2 .
$$

Use normal coordinates

$$
Q_+ = \frac{x_1+x_2}{\sqrt2},\qquad
Q_- = \frac{x_1-x_2}{\sqrt2}.
$$

The frequencies are

$$
\omega_+^2=\frac{k}{m},\qquad
\omega_-^2=\frac{k+2k_c}{m}.
$$

$Q_+$ is the in-phase mode, and $Q_-$ is the out-of-phase mode.

## From Normal Modes to Fields

A continuous string or elastic body has infinitely many coupled degrees of freedom. In the continuum limit, normal modes become field modes.

For a stretched string,

$$
\rho\,\partial_t^2 u = T\,\partial_x^2 u.
$$

With fixed endpoints $u(0,t)=u(L,t)=0$,

$$
u_n(x,t)=\sin\frac{n\pi x}{L}\,e^{i\omega_n t},
\qquad
\omega_n=\frac{n\pi}{L}\sqrt{\frac{T}{\rho}}.
$$

This mode decomposition is the classical ancestor of field quantization.

## Nonlinear Oscillations

Small oscillations describe only the quadratic part of the dynamics. Nonlinear corrections produce frequency shifts, mode coupling, resonances, and chaos.

A typical nonlinear oscillator is the Duffing oscillator:

$$
\ddot x+\delta\dot x+\alpha x+\beta x^3=\gamma\cos(\Omega t).
$$

Depending on parameters, it can show periodic, quasi-periodic, or chaotic behavior.

## Classical Chaos

### Sensitive dependence on initial conditions

Let $z=(q,p)$ be a phase-space point. A chaotic system has nearby trajectories whose separation grows as

$$
\|\delta z(t)\|\sim e^{\lambda t}\|\delta z(0)\|.
$$

The coefficient $\lambda$ is a Lyapunov exponent. A positive largest Lyapunov exponent is a common signature of chaos.

### Variational equation

For Hamiltonian flow

$$
\dot z = X_H(z),
$$

the linearized separation obeys

$$
\frac{\mathrm d}{\mathrm dt}\delta z
=
DX_H(z(t))\delta z .
$$

Lyapunov exponents are extracted from the long-time growth rates of solutions to this variational equation.

## Poincare Section

A Poincare section reduces continuous-time dynamics to an iterated map. Choose a hypersurface $\Sigma$ in phase space and record successive intersections:

$$
z_{n+1}=P(z_n).
$$

For Hamiltonian systems, the Poincare map preserves the induced symplectic area. Typical patterns:

- Fixed points correspond to periodic orbits.
- Closed curves indicate quasi-periodic motion on invariant tori.
- Scattered regions indicate chaotic motion.
- Island chains indicate resonances.

## Separatrix and Homoclinic Intersections

A separatrix divides qualitatively different types of motion. When stable and unstable manifolds of a hyperbolic periodic orbit intersect transversely, the repeated stretching and folding of phase space produces chaotic dynamics.

This mechanism appears in:

- driven pendulum.
- restricted three-body problem.
- magnetic field-line dynamics.
- standard map.

## Standard Map

The standard map is a basic area-preserving map:

$$
\begin{align*}
p_{n+1} &= p_n + K\sin\theta_n,\\
\theta_{n+1} &= \theta_n + p_{n+1}\pmod{2\pi}.
\end{align*}
$$

For small $K$, many invariant curves survive. As $K$ grows, resonances overlap and global chaos appears.

## Integrability versus Chaos

Integrable systems have enough conserved quantities to confine motion to invariant tori. Chaotic systems do not. A useful contrast:

$$
\text{integrable}
\quad\Longrightarrow\quad
\text{regular torus motion}
$$

$$
\text{non-integrable with resonance overlap}
\quad\Longrightarrow\quad
\text{chaotic layers and mixing}
$$

The transition from integrability to chaos is one of the main reasons action-angle variables and KAM theory are central in advanced classical mechanics.

## Connections

- [basic principles of mechanics](./basic%20principles%20of%20mechanics.md)
- [advanced hamiltonian mechanics](./advanced%20hamiltonian%20mechanics.md)
- [mechanics of absolute spacetime](./mechanics%20of%20absolute%20spacetime.md)
- [elasticity](./elasticity.md)
