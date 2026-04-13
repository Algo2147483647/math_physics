# Quantum Information and Open Systems

[TOC]

## Purpose

Quantum information studies states, measurements, entanglement, and information processing in quantum theory. Open quantum systems study subsystems that interact with an environment, producing decoherence, dissipation, and noise.

This page expands [quantum mechanics](./quantum%20mechanics.md).

## Density Matrices

A general quantum state is described by a density operator

$$
\hat\rho
=
\sum_i p_i|\psi_i\rangle\langle\psi_i|,
\qquad
p_i\ge0,
\qquad
\sum_i p_i=1.
$$

It satisfies

$$
\hat\rho^\dagger=\hat\rho,
\qquad
\hat\rho\ge0,
\qquad
\operatorname{Tr}\hat\rho=1.
$$

Expectation values are

$$
\langle A\rangle=\operatorname{Tr}(\hat\rho\hat A).
$$

A state is pure if

$$
\operatorname{Tr}\hat\rho^2=1.
$$

It is mixed if

$$
\operatorname{Tr}\hat\rho^2<1.
$$

The von Neumann entropy is

$$
S(\hat\rho)
=
-\operatorname{Tr}(\hat\rho\ln\hat\rho).
$$

## Composite Systems

For systems $A$ and $B$, the joint Hilbert space is

$$
\mathcal H_{AB}=\mathcal H_A\otimes\mathcal H_B.
$$

If the joint state is $\hat\rho_{AB}$, the reduced state of $A$ is obtained by tracing out $B$:

$$
\hat\rho_A=\operatorname{Tr}_B\hat\rho_{AB}.
$$

The partial trace is the mathematical operation that turns inaccessible degrees of freedom into a mixed state.

## Entanglement

A pure bipartite state is separable if

$$
|\psi\rangle_{AB}=|\alpha\rangle_A\otimes|\beta\rangle_B.
$$

If it cannot be written in this form, it is entangled.

The Schmidt decomposition states that any bipartite pure state can be written as

$$
|\psi\rangle_{AB}
=
\sum_i\sqrt{\lambda_i}
|i\rangle_A|i\rangle_B,
$$

where

$$
\lambda_i\ge0,
\qquad
\sum_i\lambda_i=1.
$$

The entanglement entropy is

$$
S_A=-\operatorname{Tr}(\hat\rho_A\ln\hat\rho_A)
=
-\sum_i\lambda_i\ln\lambda_i.
$$

For a pure product state, only one Schmidt coefficient is nonzero. For an entangled state, more than one Schmidt coefficient is nonzero.

## Bell States

Two-qubit maximally entangled Bell states are

$$
|\Phi^\pm\rangle
=
\frac{1}{\sqrt2}
\left(|00\rangle\pm|11\rangle\right),
$$

$$
|\Psi^\pm\rangle
=
\frac{1}{\sqrt2}
\left(|01\rangle\pm|10\rangle\right).
$$

They form an orthonormal basis of two-qubit Hilbert space.

## Bell Inequality

Bell inequalities constrain correlations in local hidden-variable theories. In the CHSH form, define observables

$$
A,A',B,B'
$$

with outcomes $\pm1$. Local hidden-variable theories imply

$$
|E(A,B)+E(A,B')+E(A',B)-E(A',B')|\le2.
$$

Quantum mechanics can violate this bound. The maximal quantum value is Tsirelson's bound:

$$
2\sqrt2.
$$

Bell inequality violation shows that quantum correlations cannot be explained by local hidden variables.

## Qubits and Bloch Sphere

A qubit pure state is

$$
|\psi\rangle
=
\alpha|0\rangle+\beta|1\rangle,
\qquad
|\alpha|^2+|\beta|^2=1.
$$

Modulo global phase, it can be written as

$$
|\psi\rangle
=
\cos\frac{\theta}{2}|0\rangle
+e^{i\phi}\sin\frac{\theta}{2}|1\rangle.
$$

The density matrix is

$$
\hat\rho
=
\frac12
\left(
\mathbf 1+\mathbf r\cdot\boldsymbol\sigma
\right),
$$

where $\mathbf r$ is the Bloch vector. Pure states have

$$
|\mathbf r|=1,
$$

and mixed states have

$$
|\mathbf r|<1.
$$

## Quantum Gates

Closed-system gates are unitary operators. Common one-qubit gates include

$$
X=\sigma_x,\qquad
Y=\sigma_y,\qquad
Z=\sigma_z,
$$

$$
H=\frac{1}{\sqrt2}
\begin{pmatrix}
1&1\\
1&-1
\end{pmatrix}.
$$

A common two-qubit entangling gate is CNOT:

$$
|a,b\rangle\to|a,b\oplus a\rangle.
$$

Universal quantum computation can be built from arbitrary one-qubit rotations plus one entangling two-qubit gate.

## General Measurements

A projective measurement is described by projectors $\hat P_i$ satisfying

$$
\hat P_i\hat P_j=\delta_{ij}\hat P_i,
\qquad
\sum_i\hat P_i=\mathbf 1.
$$

More general measurements are described by POVM elements $\hat E_i$:

$$
\hat E_i\ge0,
\qquad
\sum_i\hat E_i=\mathbf 1.
$$

The probability of outcome $i$ is

$$
p_i=\operatorname{Tr}(\hat\rho\hat E_i).
$$

## Open Quantum Systems

A subsystem $S$ interacting with environment $E$ evolves jointly by a unitary operation:

$$
\hat\rho_{SE}(t)
=
\hat U(t)\hat\rho_{SE}(0)\hat U^\dagger(t).
$$

The reduced state is

$$
\hat\rho_S(t)=\operatorname{Tr}_E\hat\rho_{SE}(t).
$$

This reduced evolution is generally not unitary.

## Quantum Channels

A general physical evolution of a density matrix is a completely positive trace-preserving map:

$$
\hat\rho\to\mathcal E(\hat\rho).
$$

It can be written in Kraus form:

$$
\mathcal E(\hat\rho)
=
\sum_k\hat K_k\hat\rho\hat K_k^\dagger,
$$

with

$$
\sum_k\hat K_k^\dagger\hat K_k=\mathbf 1.
$$

Examples:

- dephasing channel.
- depolarizing channel.
- amplitude damping channel.
- measurement channel.

## Decoherence

Decoherence is the loss of phase coherence in a subsystem due to entanglement with the environment.

For a simple pure dephasing process in basis $\{|i\rangle\}$,

$$
\rho_{ij}(t)\sim \rho_{ij}(0)e^{-\Gamma t}
\qquad
(i\ne j).
$$

The diagonal elements may remain nearly unchanged while off-diagonal coherences decay. This explains why classical-looking mixtures emerge from quantum superpositions in a preferred pointer basis.

## Lindblad Equation

For Markovian open-system evolution, the density matrix often obeys a Lindblad master equation:

$$
\frac{\mathrm d\hat\rho}{\mathrm dt}
=
-\frac{i}{\hbar}[\hat H,\hat\rho]
+
\sum_k
\left(
\hat L_k\hat\rho\hat L_k^\dagger
-
\frac12
\{\hat L_k^\dagger\hat L_k,\hat\rho\}
\right).
$$

$\hat L_k$ are jump operators describing dissipative channels.

## Quantum Statistics

Quantum statistical mechanics uses density matrices with thermal weights:

$$
\hat\rho
=
\frac{e^{-\beta\hat H}}{Z}
$$

or, when particle number fluctuates,

$$
\hat\rho
=
\frac{e^{-\beta(\hat H-\mu\hat N)}}{\Xi}.
$$

Identical particles require symmetric or antisymmetric state spaces, producing Bose-Einstein and Fermi-Dirac statistics.

More details: [quantum statistical mechanics](./quantum%20statistical%20mechanics.md).

## Connections

- [quantum mechanics](./quantum%20mechanics.md)
- [quantum angular momentum and spin](./quantum%20angular%20momentum%20and%20spin.md)
- [quantum statistical mechanics](./quantum%20statistical%20mechanics.md)
- [nonequilibrium statistical mechanics](./nonequilibrium%20statistical%20mechanics.md)
- [quantum field](./quantum%20field.md)
