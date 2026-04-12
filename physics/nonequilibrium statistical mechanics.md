# Nonequilibrium Statistical Mechanics

[TOC]

## Purpose

Nonequilibrium statistical mechanics studies relaxation, transport, dissipation, noise, and entropy production away from thermal equilibrium. It connects microscopic dynamics to macroscopic irreversible behavior.

This page expands [mechanics of statistics](./mechanics%20of%20statistics.md).

## Correlation Functions

For observables $A(t)$ and $B(t')$, the equilibrium correlation function is

$$
C_{AB}(t-t')
=
\langle A(t)B(t')\rangle.
$$

The connected correlation function is

$$
C^c_{AB}(t)
=
\langle A(t)B(0)\rangle
-\langle A\rangle\langle B\rangle.
$$

Time correlation functions measure memory and relaxation.

## Response Functions

Suppose a perturbation couples to observable $B$:

$$
H\to H-f(t)B.
$$

The linear response of $A$ is

$$
\delta\langle A(t)\rangle
=
\int_{-\infty}^{t}\chi_{AB}(t-t')f(t')\,\mathrm dt'.
$$

$\chi_{AB}$ is the response function. Causality requires

$$
\chi_{AB}(t)=0\qquad t<0.
$$

## Fluctuation-Dissipation Theorem

The fluctuation-dissipation theorem relates equilibrium fluctuations to linear response.

In a classical system, a common form is

$$
\chi_{AB}(t)
=
\beta\,\Theta(t)\frac{\mathrm d}{\mathrm dt}
\langle B(0)A(t)\rangle
$$

up to sign conventions depending on how the perturbation is defined.

In frequency space, dissipative response is related to noise power. Schematically,

$$
S_{AA}(\omega)
\propto
\coth\left(\frac{\beta\hbar\omega}{2}\right)
\operatorname{Im}\chi_{AA}(\omega)
$$

in the quantum case. The classical limit gives a factor proportional to $k_BT/\omega$.

The theorem states that the same microscopic processes that produce dissipation also produce equilibrium fluctuations.

## Brownian Motion

Brownian motion is random motion caused by many microscopic collisions.

For one-dimensional diffusion, the probability density satisfies

$$
\frac{\partial P(x,t)}{\partial t}
=
D\frac{\partial^2P(x,t)}{\partial x^2}.
$$

The mean-square displacement is

$$
\langle x^2(t)\rangle=2Dt.
$$

In $d$ dimensions,

$$
\langle |\mathbf x(t)-\mathbf x(0)|^2\rangle=2dDt.
$$

## Langevin Equation

For a particle of mass $m$ in a fluid, a simple Langevin equation is

$$
m\dot v=-\gamma v+\eta(t).
$$

$\gamma$ is the friction coefficient and $\eta(t)$ is random force. For thermal equilibrium,

$$
\langle\eta(t)\rangle=0,
$$

$$
\langle\eta(t)\eta(t')\rangle
=
2\gamma k_BT\,\delta(t-t').
$$

This noise strength is fixed by fluctuation-dissipation balance.

In the overdamped limit,

$$
\gamma\dot x=-\frac{\partial U}{\partial x}+\eta(t).
$$

## Fokker-Planck Equation

The Fokker-Planck equation gives the time evolution of a probability density. For the overdamped Langevin equation

$$
\gamma\dot x=-\partial_xU+\eta(t),
$$

the probability density satisfies

$$
\frac{\partial P}{\partial t}
=
\frac{1}{\gamma}
\frac{\partial}{\partial x}
\left[
(\partial_xU)P
+k_BT\frac{\partial P}{\partial x}
\right].
$$

The stationary equilibrium solution is the Boltzmann distribution:

$$
P_{\mathrm{eq}}(x)
=
\frac{1}{Z}e^{-\beta U(x)}.
$$

For a general diffusion process,

$$
\frac{\partial P}{\partial t}
=
-\partial_i[A_i(\mathbf x)P]
+\frac12\partial_i\partial_j[B_{ij}(\mathbf x)P].
$$

$A_i$ is drift and $B_{ij}$ is the diffusion matrix.

## Master Equation

For discrete states with probabilities $P_i(t)$ and transition rates $W_{ij}$ from $j$ to $i$,

$$
\frac{\mathrm dP_i}{\mathrm dt}
=
\sum_j\left(W_{ij}P_j-W_{ji}P_i\right).
$$

Detailed balance is

$$
W_{ij}P_j^{\mathrm{eq}}
=
W_{ji}P_i^{\mathrm{eq}}.
$$

Detailed balance is sufficient for equilibrium but not required for a nonequilibrium steady state.

## Boltzmann Equation

Let $f(\mathbf r,\mathbf p,t)$ be the single-particle distribution function. The Boltzmann equation is

$$
\frac{\partial f}{\partial t}
+\mathbf v\cdot\nabla_{\mathbf r}f
+\mathbf F\cdot\nabla_{\mathbf p}f
=
\left(\frac{\partial f}{\partial t}\right)_{\mathrm{coll}}.
$$

The left side is streaming in phase space. The right side is the collision integral.

For binary collisions,

$$
\left(\frac{\partial f_1}{\partial t}\right)_{\mathrm{coll}}
=
\int
\left(f_1'f_2'-f_1f_2\right)
W(12\to1'2')\,\mathrm d\Gamma_2\,\mathrm d\Gamma_{1'}\,\mathrm d\Gamma_{2'}.
$$

This form assumes molecular chaos: two-particle distributions factorize before collision.

## H-Theorem

Define Boltzmann's $H$ functional:

$$
H(t)=\int f\ln f\,\mathrm d^3r\,\mathrm d^3p.
$$

For the Boltzmann equation with suitable collision assumptions,

$$
\frac{\mathrm dH}{\mathrm dt}\le0.
$$

Since entropy is

$$
S=-k_BH+\mathrm{const},
$$

the H-theorem gives

$$
\frac{\mathrm dS}{\mathrm dt}\ge0.
$$

This is a kinetic explanation of irreversibility, based on probabilistic assumptions about collisions.

## Transport Coefficients

Transport coefficients measure response to gradients:

$$
\mathbf J_N=-D\nabla n
\tag{diffusion}
$$

$$
\mathbf J_Q=-\kappa\nabla T
\tag{heat conduction}
$$

$$
\sigma_{ij}=2\eta u_{ij}+\zeta\delta_{ij}\nabla\cdot\mathbf v
\tag{viscosity}
$$

Kinetic theory and linear response both provide ways to calculate these coefficients.

Green-Kubo relations express transport coefficients as time integrals of equilibrium correlation functions. For example,

$$
D=\frac{1}{d}\int_0^\infty
\langle\mathbf v(t)\cdot\mathbf v(0)\rangle\,\mathrm dt.
$$

## Entropy Production

Nonequilibrium thermodynamics writes local entropy production as fluxes times thermodynamic forces:

$$
\dot S_{\mathrm{prod}}
=
\sum_a J_aX_a\ge0.
$$

Examples:

- heat flux times temperature gradient.
- particle flux times chemical-potential gradient.
- viscous stress times velocity gradient.

Near equilibrium, linear laws are used:

$$
J_a=\sum_b L_{ab}X_b.
$$

Onsager reciprocity gives

$$
L_{ab}=L_{ba}
$$

when the corresponding variables have the same time-reversal parity.

## Connections

- [mechanics of statistics](./mechanics%20of%20statistics.md)
- [phase transitions and critical phenomena](./phase%20transitions%20and%20critical%20phenomena.md)
- [quantum statistical mechanics](./quantum%20statistical%20mechanics.md)
- [fluid](./fluid.md)
