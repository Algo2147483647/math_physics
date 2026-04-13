# Quantum Mechanics

[TOC]

## Purpose

Quantum mechanics is the theory of physical states, observables, probabilities, and time evolution in Hilbert space. It replaces classical phase-space points by state vectors or density operators, and replaces classical observables by self-adjoint operators.

This page is the entry point for nonrelativistic quantum mechanics. Related specialized pages:

- [quantum angular momentum and spin](./quantum%20angular%20momentum%20and%20spin.md)
- [quantum approximation and scattering](./quantum%20approximation%20and%20scattering.md)
- [quantum information and open systems](./quantum%20information%20and%20open%20systems.md)
- [quantum statistical mechanics](./quantum%20statistical%20mechanics.md)
- [quantum field](./quantum%20field.md)

## Hilbert Space

### State space

The state space of an isolated quantum system is a complex Hilbert space $\mathcal H$ with inner product

$$
\langle \phi|\psi\rangle .
$$

A pure state is represented by a nonzero vector $|\psi\rangle\in\mathcal H$, with normalization

$$
\langle\psi|\psi\rangle=1.
$$

Vectors that differ only by a nonzero complex phase represent the same physical state:

$$
|\psi\rangle \sim e^{i\alpha}|\psi\rangle.
$$

### Bra-ket notation

Dirac notation uses:

- ket: $|\psi\rangle$, a vector in $\mathcal H$.
- bra: $\langle\psi|$, a dual vector in $\mathcal H^\ast$.
- inner product: $\langle\phi|\psi\rangle$.
- outer product: $|\phi\rangle\langle\psi|$.

For an orthonormal basis $\{|n\rangle\}$,

$$
\langle m|n\rangle=\delta_{mn},
$$

and completeness is

$$
\sum_n |n\rangle\langle n|=\mathbf 1.
$$

For a continuous basis such as position eigenstates,

$$
\langle x|x'\rangle=\delta(x-x'),
\qquad
\int |x\rangle\langle x|\,\mathrm dx=\mathbf 1.
$$

### Wave function as representation

The wave function is the coordinate representation of a state:

$$
\psi(x)=\langle x|\psi\rangle.
$$

The momentum-space wave function is

$$
\tilde\psi(p)=\langle p|\psi\rangle.
$$

The two are related by Fourier transform:

$$
\tilde\psi(p)
=
\frac{1}{\sqrt{2\pi\hbar}}
\int e^{-ipx/\hbar}\psi(x)\,\mathrm dx.
$$

## Postulates

### States

The physical state of a closed system is represented by a ray in Hilbert space, or more generally by a density operator $\hat\rho$.

### Observables

Observable quantities are represented by self-adjoint operators $\hat A$:

$$
\hat A^\dagger=\hat A.
$$

The possible measurement outcomes are eigenvalues of $\hat A$.

### Born rule

If

$$
\hat A|a_n\rangle=a_n|a_n\rangle,
$$

then the probability of measuring $a_n$ in state $|\psi\rangle$ is

$$
P(a_n)=|\langle a_n|\psi\rangle|^2.
$$

For a continuous position measurement,

$$
P(x\in [a,b])=\int_a^b|\psi(x)|^2\,\mathrm dx.
$$

### Projection postulate

For an ideal projective measurement with projector $\hat P_n$, the state after observing outcome $n$ is

$$
|\psi\rangle
\to
\frac{\hat P_n|\psi\rangle}
{\sqrt{\langle\psi|\hat P_n|\psi\rangle}}.
$$

For density matrices,

$$
\hat\rho
\to
\frac{\hat P_n\hat\rho\hat P_n}
{\operatorname{Tr}(\hat P_n\hat\rho)}.
$$

### Time evolution

Closed-system time evolution is unitary:

$$
|\psi(t)\rangle=\hat U(t,t_0)|\psi(t_0)\rangle,
$$

where

$$
\hat U^\dagger\hat U=\mathbf 1.
$$

The Schrodinger equation is

$$
i\hbar\frac{\partial}{\partial t}|\psi(t)\rangle
=
\hat H|\psi(t)\rangle.
$$

For time-independent $\hat H$,

$$
\hat U(t,t_0)=e^{-i\hat H(t-t_0)/\hbar}.
$$

## Observables and Spectral Decomposition

### Expectation value and variance

The expectation value of observable $\hat A$ in pure state $|\psi\rangle$ is

$$
\langle A\rangle
=
\langle\psi|\hat A|\psi\rangle.
$$

The variance is

$$
(\Delta A)^2
=
\langle A^2\rangle-\langle A\rangle^2.
$$

For a density matrix,

$$
\langle A\rangle
=
\operatorname{Tr}(\hat\rho\hat A).
$$

### Spectral decomposition

For a discrete nondegenerate spectrum,

$$
\hat A=\sum_n a_n|a_n\rangle\langle a_n|.
$$

For degenerate eigenvalues, use projectors:

$$
\hat A=\sum_a a\,\hat P_a.
$$

For continuous spectra,

$$
\hat A=\int a\,|a\rangle\langle a|\,\mathrm da.
$$

The identity resolution is

$$
\mathbf 1=\sum_a\hat P_a
$$

or, for continuous spectra,

$$
\mathbf 1=\int |a\rangle\langle a|\,\mathrm da.
$$

## Commutation Relations

### Canonical commutation relation

Position and momentum obey

$$
[\hat x,\hat p]=i\hbar.
$$

In position representation,

$$
\hat x=x,\qquad
\hat p=-i\hbar\frac{\partial}{\partial x}.
$$

In momentum representation,

$$
\hat p=p,\qquad
\hat x=i\hbar\frac{\partial}{\partial p}.
$$

### Compatibility

If

$$
[\hat A,\hat B]=0,
$$

then $\hat A$ and $\hat B$ can be simultaneously diagonalized, up to degeneracy. A complete set of commuting observables labels a basis of states.

### Uncertainty relation

For any two observables,

$$
\Delta A\,\Delta B
\ge
\frac12
\left|
\langle[\hat A,\hat B]\rangle
\right|.
$$

For position and momentum,

$$
\Delta x\,\Delta p\ge\frac{\hbar}{2}.
$$

## Pictures of Time Evolution

### Schrodinger picture

States evolve and operators are usually time-independent:

$$
i\hbar\frac{\mathrm d}{\mathrm dt}|\psi_S(t)\rangle
=
\hat H|\psi_S(t)\rangle.
$$

### Heisenberg picture

Operators evolve and states are fixed:

$$
\hat A_H(t)=\hat U^\dagger(t)\hat A_S\hat U(t).
$$

The Heisenberg equation is

$$
\frac{\mathrm d\hat A_H}{\mathrm dt}
=
\frac{i}{\hbar}[\hat H,\hat A_H]
+
\left(\frac{\partial \hat A}{\partial t}\right)_H.
$$

### Interaction picture

If

$$
\hat H=\hat H_0+\hat V,
$$

then the interaction picture evolves states with $\hat V$ and operators with $\hat H_0$. It is the natural language of time-dependent perturbation theory and quantum field theory.

## Harmonic Oscillator

### Hamiltonian

The one-dimensional harmonic oscillator is

$$
\hat H
=
\frac{\hat p^2}{2m}
+\frac12m\omega^2\hat x^2.
$$

### Ladder operators

Define

$$
\hat a
=
\sqrt{\frac{m\omega}{2\hbar}}\hat x
+
\frac{i}{\sqrt{2m\hbar\omega}}\hat p,
$$

$$
\hat a^\dagger
=
\sqrt{\frac{m\omega}{2\hbar}}\hat x
-
\frac{i}{\sqrt{2m\hbar\omega}}\hat p.
$$

They satisfy

$$
[\hat a,\hat a^\dagger]=1.
$$

The Hamiltonian becomes

$$
\hat H=\hbar\omega\left(\hat a^\dagger\hat a+\frac12\right).
$$

The number operator is

$$
\hat N=\hat a^\dagger\hat a,
$$

with eigenstates

$$
\hat N|n\rangle=n|n\rangle.
$$

The ladder action is

$$
\hat a|n\rangle=\sqrt n\,|n-1\rangle,
\qquad
\hat a^\dagger|n\rangle=\sqrt{n+1}\,|n+1\rangle.
$$

The energy levels are

$$
E_n=\hbar\omega\left(n+\frac12\right).
$$

The oscillator is the local normal form of many quantum systems and the building block of field quantization.

## Angular Momentum and Spin

Angular momentum operators obey

$$
[\hat J_i,\hat J_j]=i\hbar\epsilon_{ijk}\hat J_k.
$$

The simultaneous eigenstates of $\hat J^2$ and $\hat J_z$ are

$$
\hat J^2|j,m\rangle=\hbar^2j(j+1)|j,m\rangle,
$$

$$
\hat J_z|j,m\rangle=\hbar m|j,m\rangle.
$$

The ladder operators

$$
\hat J_\pm=\hat J_x\pm i\hat J_y
$$

raise or lower $m$.

Spin is intrinsic angular momentum. For spin $1/2$,

$$
\hat{\mathbf S}=\frac{\hbar}{2}\boldsymbol\sigma,
$$

where $\boldsymbol\sigma$ are the Pauli matrices.

More details: [quantum angular momentum and spin](./quantum%20angular%20momentum%20and%20spin.md).

## Approximation Methods

Most quantum systems cannot be solved exactly. Core approximation tools are:

- time-independent perturbation theory.
- degenerate perturbation theory.
- time-dependent perturbation theory.
- variational method.
- WKB approximation.

More details: [quantum approximation and scattering](./quantum%20approximation%20and%20scattering.md).

## Scattering Theory

Scattering theory studies how incoming asymptotic states evolve into outgoing asymptotic states. Central objects include:

- scattering amplitude.
- differential cross section.
- Born approximation.
- partial waves and phase shifts.
- $S$-matrix.

More details: [quantum approximation and scattering](./quantum%20approximation%20and%20scattering.md).

## Density Matrices and Mixed States

A mixed state is described by a density operator

$$
\hat\rho=\sum_i p_i|\psi_i\rangle\langle\psi_i|,
\qquad
p_i\ge0,\qquad
\sum_i p_i=1.
$$

Pure states satisfy

$$
\hat\rho^2=\hat\rho,
\qquad
\operatorname{Tr}\hat\rho^2=1.
$$

Mixed states satisfy

$$
\operatorname{Tr}\hat\rho^2<1.
$$

The density matrix is essential for quantum statistics, decoherence, measurement theory, and open quantum systems.

More details:

- [quantum information and open systems](./quantum%20information%20and%20open%20systems.md)
- [quantum statistical mechanics](./quantum%20statistical%20mechanics.md)

## Entanglement and Quantum Information

A bipartite pure state in $\mathcal H_A\otimes\mathcal H_B$ is entangled if it cannot be written as

$$
|\psi\rangle_{AB}=|\alpha\rangle_A\otimes|\beta\rangle_B.
$$

Entanglement has no classical probabilistic analogue. It leads to Bell inequality violations and is a resource for quantum information processing.

More details: [quantum information and open systems](./quantum%20information%20and%20open%20systems.md).

## Connections

- [quantum angular momentum and spin](./quantum%20angular%20momentum%20and%20spin.md)
- [quantum approximation and scattering](./quantum%20approximation%20and%20scattering.md)
- [quantum information and open systems](./quantum%20information%20and%20open%20systems.md)
- [quantum statistical mechanics](./quantum%20statistical%20mechanics.md)
- [quantum field](./quantum%20field.md)
- [advanced hamiltonian mechanics](./advanced%20hamiltonian%20mechanics.md)
- [mechanics of statistics](./mechanics%20of%20statistics.md)
