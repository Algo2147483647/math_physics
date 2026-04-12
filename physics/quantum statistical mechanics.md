# Quantum Statistical Mechanics

[TOC]

## Purpose

Quantum statistical mechanics applies statistical mechanics to systems whose microscopic states obey quantum mechanics. It explains Bose and Fermi gases, degeneracy pressure, blackbody radiation, phonons, and many condensed matter systems.

This page expands [mechanics of statistics](./mechanics%20of%20statistics.md).

## Density Operator

The statistical state of a quantum system is a density operator $\hat\rho$:

$$
\hat\rho\ge0,\qquad
\operatorname{Tr}\hat\rho=1.
$$

The expectation value of an observable $\hat A$ is

$$
\langle A\rangle=\operatorname{Tr}(\hat\rho\hat A).
$$

The von Neumann entropy is

$$
S=-k_B\operatorname{Tr}(\hat\rho\ln\hat\rho).
$$

For the canonical ensemble,

$$
\hat\rho
=
\frac{e^{-\beta\hat H}}{Z},
\qquad
Z=\operatorname{Tr}e^{-\beta\hat H}.
$$

For the grand canonical ensemble,

$$
\hat\rho
=
\frac{e^{-\beta(\hat H-\mu\hat N)}}{\Xi},
\qquad
\Xi=\operatorname{Tr}e^{-\beta(\hat H-\mu\hat N)}.
$$

## Identical Particles

Identical quantum particles are not labeled individually.

- Bosons have symmetric many-body wave functions.
- Fermions have antisymmetric many-body wave functions.

The occupation number of a one-particle energy level $\epsilon$ is

$$
\bar n(\epsilon)
=
\frac{1}{e^{\beta(\epsilon-\mu)}\mp1},
$$

where the minus sign is for bosons and the plus sign is for fermions:

$$
\bar n_B(\epsilon)
=
\frac{1}{e^{\beta(\epsilon-\mu)}-1},
\qquad
\bar n_F(\epsilon)
=
\frac{1}{e^{\beta(\epsilon-\mu)}+1}.
$$

The classical Maxwell-Boltzmann limit is recovered when

$$
e^{\beta(\epsilon-\mu)}\gg1.
$$

## Ideal Quantum Gases

For noninteracting particles, the grand partition function factorizes over single-particle states:

$$
\Xi_B=\prod_\alpha \frac{1}{1-ze^{-\beta\epsilon_\alpha}},
\qquad
\Xi_F=\prod_\alpha \left(1+ze^{-\beta\epsilon_\alpha}\right),
$$

where

$$
z=e^{\beta\mu}
$$

is the fugacity.

The average occupation number is

$$
\bar n_\alpha
=
z\frac{\partial}{\partial z}\ln\Xi_\alpha.
$$

## Density of States

For free particles in three dimensions with spin degeneracy $g$,

$$
D(\epsilon)\,\mathrm d\epsilon
=
g\frac{V}{4\pi^2}
\left(\frac{2m}{\hbar^2}\right)^{3/2}
\epsilon^{1/2}\,\mathrm d\epsilon.
$$

Thermodynamic quantities are obtained by replacing sums with integrals:

$$
\sum_\alpha f(\epsilon_\alpha)
\to
\int_0^\infty D(\epsilon)f(\epsilon)\,\mathrm d\epsilon.
$$

## Fermi Gas

At zero temperature, fermion states fill up to the Fermi energy $\epsilon_F$:

$$
\bar n_F(\epsilon)=
\begin{cases}
1,&\epsilon<\epsilon_F,\\
0,&\epsilon>\epsilon_F.
\end{cases}
$$

For a spin-$1/2$ free Fermi gas,

$$
\epsilon_F
=
\frac{\hbar^2}{2m}(3\pi^2n)^{2/3},
\qquad
n=\frac{N}{V}.
$$

The Fermi temperature is

$$
T_F=\frac{\epsilon_F}{k_B}.
$$

At $T=0$ the pressure is nonzero:

$$
P
=
\frac{2}{5}n\epsilon_F.
$$

This is **degeneracy pressure**. It arises from the Pauli exclusion principle, not from thermal motion. It supports white dwarfs and neutron stars against gravitational collapse in appropriate regimes.

## Bose Gas

For ideal bosons,

$$
\bar n_B(\epsilon)
=
\frac{1}{e^{\beta(\epsilon-\mu)}-1}.
$$

The chemical potential must satisfy

$$
\mu\le\epsilon_0.
$$

For a free Bose gas, Bose-Einstein condensation occurs when the excited states cannot hold all particles. In three dimensions,

$$
T_c
=
\frac{2\pi\hbar^2}{mk_B}
\left(
\frac{n}{\zeta(3/2)}
\right)^{2/3}.
$$

Below $T_c$,

$$
\frac{N_0}{N}
=
1-\left(\frac{T}{T_c}\right)^{3/2}.
$$

The condensate is a macroscopic occupation of a single quantum state.

## Photon Gas and Blackbody Radiation

Photons are bosons with chemical potential

$$
\mu=0,
$$

because photon number is not conserved in thermal equilibrium.

The number of photon modes per volume with angular frequency between $\omega$ and $\omega+\mathrm d\omega$ is

$$
g(\omega)\,\mathrm d\omega
=
\frac{\omega^2}{\pi^2c^3}\,\mathrm d\omega,
$$

including the two polarization states.

The average energy per mode is

$$
\bar E(\omega)
=
\frac{\hbar\omega}{e^{\beta\hbar\omega}-1}.
$$

Therefore the spectral energy density is

$$
u(\omega)\,\mathrm d\omega
=
\frac{\hbar\omega^3}{\pi^2c^3}
\frac{1}{e^{\beta\hbar\omega}-1}\,\mathrm d\omega.
$$

This is Planck's law. Integrating over frequency gives

$$
u=aT^4,
$$

where

$$
a=\frac{\pi^2k_B^4}{15\hbar^3c^3}.
$$

The pressure of photon gas is

$$
P=\frac{u}{3}.
$$

The Stefan-Boltzmann law for emitted power per area is

$$
j^\star=\sigma T^4,
\qquad
\sigma=\frac{ac}{4}.
$$

## Phonons

Phonons are quantized normal modes of lattice vibrations. In the Debye approximation, low-frequency acoustic phonons have

$$
\omega=c_s k.
$$

The low-temperature heat capacity of a three-dimensional crystal scales as

$$
C_V\propto T^3.
$$

This is the Debye $T^3$ law.

## Connections

- [mechanics of statistics](./mechanics%20of%20statistics.md)
- [phase transitions and critical phenomena](./phase%20transitions%20and%20critical%20phenomena.md)
- [quantum field](./quantum%20field.md)
- [electromagnetic field](./electromagnetic%20field.md)
