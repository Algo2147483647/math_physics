# Phase Transitions and Critical Phenomena

[TOC]

## Purpose

Phase transition theory studies qualitative changes of macroscopic states in the thermodynamic limit. Critical phenomena reveal universal behavior controlled by symmetry, dimensionality, fluctuations, and renormalization group fixed points.

This page expands [mechanics of statistics](./mechanics%20of%20statistics.md).

## Phase Transitions

### Thermodynamic limit

True phase transitions require the thermodynamic limit:

$$
N\to\infty,\qquad
V\to\infty,\qquad
\frac{N}{V}=\mathrm{const}.
$$

In this limit, the free energy can become nonanalytic.

### First-order and continuous transitions

A first-order transition has discontinuity in a first derivative of the free energy, such as entropy or density:

$$
S=-\left(\frac{\partial F}{\partial T}\right)_{V,N}.
$$

A continuous transition has continuous first derivatives but singular higher derivatives, such as heat capacity or susceptibility.

## Order Parameter

An order parameter distinguishes phases. Examples:

- Magnetization $m$ for a ferromagnet.
- Density difference for a liquid-gas transition.
- Condensate amplitude for a superfluid or superconductor.
- Staggered magnetization for an antiferromagnet.

For the Ising ferromagnet,

$$
m=\frac{1}{N}\sum_i\langle s_i\rangle.
$$

In the disordered phase, $m=0$. In the ordered phase, $m\ne0$.

## Spontaneous Symmetry Breaking

Spontaneous symmetry breaking occurs when the Hamiltonian has a symmetry but the chosen equilibrium state does not.

For the Ising model with no external field,

$$
s_i\to -s_i
$$

is a symmetry. Below the critical temperature, the system chooses either $m>0$ or $m<0$, breaking the symmetry.

In systems with continuous symmetry, spontaneous symmetry breaking usually produces gapless Goldstone modes.

## Ising Model

The Ising model has spin variables

$$
s_i=\pm1
$$

and Hamiltonian

$$
H=-J\sum_{\langle ij\rangle}s_is_j-h\sum_i s_i.
$$

- $J>0$: ferromagnetic interaction.
- $J<0$: antiferromagnetic interaction.
- $h$: external magnetic field.

The partition function is

$$
Z=\sum_{\{s_i\}}e^{-\beta H}.
$$

The Ising model is a minimal model of symmetry breaking, phase transition, and universality.

## Mean-Field Theory

Mean-field theory replaces neighboring spins by their average magnetization:

$$
s_j\to \langle s_j\rangle=m.
$$

For coordination number $z$, the effective field is

$$
h_{\mathrm{eff}}=h+Jzm.
$$

The self-consistency equation is

$$
m=\tanh\left[\beta(Jzm+h)\right].
$$

At $h=0$, the critical temperature is

$$
k_BT_c=Jz.
$$

Mean-field theory captures symmetry breaking but often gives incorrect critical exponents in low dimensions because it underestimates fluctuations.

## Landau Theory

Landau theory expands the free energy in powers of the order parameter:

$$
F[m]
=
F_0+\frac12a(T)m^2+\frac14bm^4-hm+\cdots,
$$

with

$$
a(T)=a_0(T-T_c),\qquad b>0.
$$

At $h=0$:

$$
m=0 \quad (T>T_c),
$$

$$
m^2=\frac{-a(T)}{b}\quad (T<T_c).
$$

Landau theory explains spontaneous symmetry breaking through the shape of the free-energy landscape.

## Ginzburg-Landau Functional

For a spatially varying order parameter,

$$
\mathcal F[\phi]
=
\int \mathrm d^dx
\left[
\frac12r\phi^2
+\frac12K(\nabla\phi)^2
+\frac14u\phi^4
-h\phi
\right].
$$

The gradient term penalizes spatial variation. This functional is the classical statistical-field-theory form of many critical systems.

## Correlation Functions

The connected two-point correlation function is

$$
G(\mathbf r)
=
\langle\phi(\mathbf r)\phi(\mathbf 0)\rangle
-\langle\phi\rangle^2.
$$

Away from criticality,

$$
G(r)\sim \frac{e^{-r/\xi}}{r^{d-2+\eta}}.
$$

$\xi$ is the correlation length. At a continuous phase transition,

$$
\xi\to\infty.
$$

This divergence explains why microscopic details become less important near criticality.

## Critical Exponents

Near reduced temperature

$$
t=\frac{T-T_c}{T_c},
$$

critical behavior is described by power laws:

$$
C\sim |t|^{-\alpha},
$$

$$
m\sim (-t)^\beta \quad (t<0),
$$

$$
\chi\sim |t|^{-\gamma},
$$

$$
\xi\sim |t|^{-\nu},
$$

$$
G(r)\sim \frac{1}{r^{d-2+\eta}}\quad (t=0),
$$

$$
m\sim h^{1/\delta}\quad (t=0).
$$

The exponents are $\alpha,\beta,\gamma,\delta,\nu,\eta$.

## Scaling Relations

Critical exponents are not independent. Common scaling relations include

$$
\alpha+2\beta+\gamma=2,
$$

$$
\gamma=\beta(\delta-1),
$$

$$
\gamma=\nu(2-\eta),
$$

$$
2-\alpha=d\nu.
$$

The last relation is hyperscaling and can fail above the upper critical dimension.

## Universality

Different microscopic systems can share the same critical exponents and scaling functions. A universality class is mainly determined by:

- spatial dimension $d$.
- order-parameter symmetry.
- range of interactions.
- conservation laws and dynamics.

Examples:

- Ising universality class: scalar order parameter with $Z_2$ symmetry.
- XY universality class: two-component order parameter with $O(2)$ symmetry.
- Heisenberg universality class: three-component order parameter with $O(3)$ symmetry.

## Renormalization Group

The renormalization group studies how a theory changes under coarse-graining. A schematic transformation is

$$
\mathcal H[\phi]\to \mathcal H'[\phi']
$$

after integrating out short-wavelength fluctuations and rescaling lengths:

$$
\mathbf x'=b^{-1}\mathbf x.
$$

Couplings $g_i$ flow with scale:

$$
\frac{\mathrm dg_i}{\mathrm d\ln b}=\beta_i(g).
$$

Fixed points satisfy

$$
\beta_i(g^\star)=0.
$$

Relevant, irrelevant, and marginal directions determine which perturbations matter at long distances.

### Wilsonian picture

For a momentum cutoff $\Lambda$, split field modes into slow and fast parts:

$$
\phi=\phi_<+\phi_>,
$$

where $\phi_>$ contains momenta in the shell

$$
\Lambda/b<|\mathbf k|<\Lambda.
$$

The effective Hamiltonian is defined by

$$
e^{-\beta\mathcal H_{\mathrm{eff}}[\phi_<]}
=
\int \mathcal D\phi_>\,
e^{-\beta\mathcal H[\phi_<+\phi_>]}.
$$

This is the statistical mechanics version of renormalization. It is directly related to effective field theory in quantum field theory.

## Connections

- [mechanics of statistics](./mechanics%20of%20statistics.md)
- [quantum statistical mechanics](./quantum%20statistical%20mechanics.md)
- [nonequilibrium statistical mechanics](./nonequilibrium%20statistical%20mechanics.md)
- [quantum field](./quantum%20field.md)
