# Statistical Mechanics

[TOC]

## Purpose

Statistical mechanics connects microscopic states with macroscopic thermodynamics. Its central objects are entropy, ensembles, partition functions, fluctuations, correlation functions, and the thermodynamic limit.

This page is the entry point. More specialized topics are covered in:

- [quantum statistical mechanics](./quantum%20statistical%20mechanics.md)
- [phase transitions and critical phenomena](./phase%20transitions%20and%20critical%20phenomena.md)
- [nonequilibrium statistical mechanics](./nonequilibrium%20statistical%20mechanics.md)

## Thermodynamic Quantities

### Entropy

For an isolated macrostate with $\Omega$ compatible microstates,

$$
S=k_B\ln\Omega.
$$

More generally, for probabilities $p_i$,

$$
S=-k_B\sum_i p_i\ln p_i.
$$

For a quantum density matrix $\rho$,

$$
S=-k_B\operatorname{Tr}(\rho\ln\rho).
$$

### Temperature

For a simple system,

$$
\frac{1}{T}=
\left(\frac{\partial S}{\partial U}\right)_{V,N}.
$$

Temperature measures how entropy changes with internal energy.

### Chemical potential

The chemical potential is

$$
\mu=
\left(\frac{\partial U}{\partial N}\right)_{S,V}.
$$

It measures the free-energy cost of adding one particle. It controls particle exchange in the grand canonical ensemble.

### Thermodynamic identity

For a simple compressible system,

$$
\mathrm dU=T\,\mathrm dS-P\,\mathrm dV+\mu\,\mathrm dN.
$$

Useful thermodynamic potentials are

$$
F=U-TS,\qquad
G=U-TS+PV,\qquad
\Omega_G=U-TS-\mu N.
$$

Natural variables:

$$
F=F(T,V,N),\qquad
G=G(T,P,N),\qquad
\Omega_G=\Omega_G(T,V,\mu).
$$

## Ensembles

An ensemble is a probability distribution over microscopic states. The common equilibrium ensembles differ by which macroscopic variables are fixed.

| Ensemble | Fixed variables | Fluctuating variables | Partition function |
| --- | --- | --- | --- |
| Microcanonical | $E,V,N$ | none | $\Omega(E,V,N)$ |
| Canonical | $T,V,N$ | $E$ | $Z(T,V,N)$ |
| Grand canonical | $T,V,\mu$ | $E,N$ | $\Xi(T,V,\mu)$ |
| Isothermal-isobaric | $T,P,N$ | $E,V$ | $\Delta(T,P,N)$ |

### Microcanonical ensemble

For an isolated system, all accessible states with fixed energy are equally probable:

$$
p_i=\frac{1}{\Omega(E,V,N)}.
$$

Entropy is

$$
S(E,V,N)=k_B\ln\Omega(E,V,N).
$$

Thermodynamics follows from derivatives of $S$:

$$
\frac{1}{T}=\left(\frac{\partial S}{\partial E}\right)_{V,N},
\qquad
\frac{P}{T}=\left(\frac{\partial S}{\partial V}\right)_{E,N},
\qquad
-\frac{\mu}{T}=\left(\frac{\partial S}{\partial N}\right)_{E,V}.
$$

### Canonical ensemble

For fixed $T,V,N$,

$$
p_i=\frac{e^{-\beta E_i}}{Z},
\qquad
\beta=\frac{1}{k_BT},
$$

with

$$
Z(T,V,N)=\sum_i e^{-\beta E_i}.
$$

The Helmholtz free energy is

$$
F=-k_BT\ln Z.
$$

Average energy and heat capacity are

$$
\langle E\rangle=-\frac{\partial\ln Z}{\partial\beta},
$$

$$
C_V=
\left(\frac{\partial\langle E\rangle}{\partial T}\right)_{V,N}
=
\frac{\langle E^2\rangle-\langle E\rangle^2}{k_BT^2}.
$$

Energy fluctuations are therefore thermodynamic response functions.

### Grand canonical ensemble

For fixed $T,V,\mu$, both energy and particle number fluctuate:

$$
p_{i,N}
=
\frac{e^{-\beta(E_{i,N}-\mu N)}}{\Xi}.
$$

The grand partition function is

$$
\Xi(T,V,\mu)
=
\sum_{N=0}^{\infty}
\sum_i
e^{-\beta(E_{i,N}-\mu N)}.
$$

The grand potential is

$$
\Omega_G=-k_BT\ln\Xi.
$$

For a homogeneous system,

$$
\Omega_G=-PV.
$$

Average particle number is

$$
\langle N\rangle
=
\frac{1}{\beta}\frac{\partial\ln\Xi}{\partial\mu}.
$$

Number fluctuations are

$$
\langle(\Delta N)^2\rangle
=
k_BT
\left(\frac{\partial\langle N\rangle}{\partial\mu}\right)_{T,V}.
$$

### Isothermal-isobaric ensemble

For fixed $T,P,N$, the volume fluctuates. The partition function is

$$
\Delta(T,P,N)
=
\int_0^\infty \mathrm dV\,e^{-\beta PV}Z(T,V,N).
$$

The Gibbs free energy is

$$
G=-k_BT\ln\Delta.
$$

This ensemble is common in simulations and phase equilibrium.

## Classical Ideal Gas

For a classical monatomic ideal gas,

$$
PV=Nk_BT.
$$

The thermal de Broglie wavelength is

$$
\lambda_T=\frac{h}{\sqrt{2\pi mk_BT}}.
$$

The canonical partition function is

$$
Z_N
=
\frac{1}{N!}
\left(\frac{V}{\lambda_T^3}\right)^N.
$$

The Helmholtz free energy is

$$
F
=
-Nk_BT
\left[
\ln\left(\frac{V}{N\lambda_T^3}\right)+1
\right].
$$

The chemical potential is

$$
\mu
=
k_BT\ln(n\lambda_T^3),
\qquad
n=\frac{N}{V}.
$$

The classical regime requires

$$
n\lambda_T^3\ll1.
$$

When this condition fails, quantum statistics becomes important.

## Maxwell-Boltzmann Distribution

The speed distribution of a classical ideal gas is

$$
f(v)
=
4\pi v^2
\left(\frac{m}{2\pi k_BT}\right)^{3/2}
\exp\left(-\frac{mv^2}{2k_BT}\right).
$$

The Boltzmann weight for a state of energy $E_i$ is

$$
p_i\propto e^{-\beta E_i}.
$$

## Fluctuations and Correlations

Statistical mechanics relates fluctuations to response. For an observable $A$,

$$
\langle A\rangle=\sum_i p_iA_i.
$$

The connected correlation function of two observables is

$$
\langle AB\rangle_c
=
\langle AB\rangle-\langle A\rangle\langle B\rangle.
$$

For a field $\phi(\mathbf x)$,

$$
G(\mathbf x-\mathbf y)
=
\langle\phi(\mathbf x)\phi(\mathbf y)\rangle_c.
$$

Correlation functions measure how microscopic fluctuations at different points are statistically linked. Near a continuous phase transition they often take the scaling form

$$
G(r)\sim \frac{e^{-r/\xi}}{r^{d-2+\eta}},
$$

where $\xi$ is the correlation length.

More details:

- [phase transitions and critical phenomena](./phase%20transitions%20and%20critical%20phenomena.md)
- [nonequilibrium statistical mechanics](./nonequilibrium%20statistical%20mechanics.md)

## Equilibrium, Phase Transitions, and Fields

The thermodynamic limit

$$
N\to\infty,\qquad
V\to\infty,\qquad
\frac{N}{V}=n
$$

is essential because true nonanalytic phase transitions occur only in this limit.

Modern statistical mechanics often rewrites the partition function as a functional integral:

$$
Z=\int \mathcal D\phi\,e^{-\beta \mathcal H[\phi]}.
$$

This is the bridge to statistical field theory, condensed matter theory, and Euclidean quantum field theory.

More details: [phase transitions and critical phenomena](./phase%20transitions%20and%20critical%20phenomena.md).

## Nonequilibrium Statistical Mechanics

Equilibrium ensembles describe stationary distributions. Nonequilibrium theory studies relaxation, transport, noise, and entropy production.

Core tools include:

- Brownian motion.
- Langevin equation.
- Fokker-Planck equation.
- Linear response and fluctuation-dissipation theorem.
- Boltzmann equation and H-theorem.

More details: [nonequilibrium statistical mechanics](./nonequilibrium%20statistical%20mechanics.md).

## Connections

- [quantum statistical mechanics](./quantum%20statistical%20mechanics.md)
- [phase transitions and critical phenomena](./phase%20transitions%20and%20critical%20phenomena.md)
- [nonequilibrium statistical mechanics](./nonequilibrium%20statistical%20mechanics.md)
- [quantum field](./quantum%20field.md)
- [electromagnetic field](./electromagnetic%20field.md)
