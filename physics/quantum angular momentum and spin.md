# Quantum Angular Momentum and Spin

[TOC]

## Purpose

Angular momentum is the quantum theory of rotations. It connects operator algebra, representation theory of $SO(3)$ and $SU(2)$, orbital motion, spin, and addition of angular momenta through Clebsch-Gordan coefficients.

This page expands [quantum mechanics](./quantum%20mechanics.md).

## Rotation Operators

A rotation by angle $\theta$ around unit vector $\mathbf n$ is represented by a unitary operator

$$
\hat U(R)=e^{-i\theta\mathbf n\cdot\hat{\mathbf J}/\hbar}.
$$

$\hat{\mathbf J}$ is the generator of rotations.

For a vector operator $\hat{\mathbf V}$,

$$
\hat U^\dagger(R)\hat V_i\hat U(R)=R_{ij}\hat V_j.
$$

Infinitesimal rotations imply the angular momentum algebra

$$
[\hat J_i,\hat J_j]=i\hbar\epsilon_{ijk}\hat J_k.
$$

## SO(3) and SU(2)

$SO(3)$ is the group of three-dimensional rotations. $SU(2)$ is its double cover:

$$
SU(2)/\mathbb Z_2\simeq SO(3).
$$

This double cover is why quantum states can have half-integer angular momentum. A spin-$1/2$ state changes sign under a $2\pi$ rotation and returns to itself under a $4\pi$ rotation.

Irreducible representations are labeled by

$$
j=0,\frac12,1,\frac32,\dots
$$

with dimension

$$
\dim \mathcal H_j=2j+1.
$$

## Angular Momentum Eigenstates

The Casimir operator is

$$
\hat J^2=\hat J_x^2+\hat J_y^2+\hat J_z^2.
$$

It commutes with all components:

$$
[\hat J^2,\hat J_i]=0.
$$

Use simultaneous eigenstates $|j,m\rangle$:

$$
\hat J^2|j,m\rangle
=
\hbar^2j(j+1)|j,m\rangle,
$$

$$
\hat J_z|j,m\rangle
=
\hbar m|j,m\rangle.
$$

The magnetic quantum number takes values

$$
m=-j,-j+1,\dots,j-1,j.
$$

## Ladder Operators

Define

$$
\hat J_\pm=\hat J_x\pm i\hat J_y.
$$

They obey

$$
[\hat J_z,\hat J_\pm]=\pm\hbar\hat J_\pm,
$$

$$
[\hat J_+,\hat J_-]=2\hbar\hat J_z.
$$

Their action is

$$
\hat J_\pm|j,m\rangle
=
\hbar
\sqrt{j(j+1)-m(m\pm1)}
\,|j,m\pm1\rangle.
$$

The ladder stops at $m=\pm j$, which forces $j$ to be integer or half-integer.

## Orbital Angular Momentum

For a particle in three dimensions,

$$
\hat{\mathbf L}=\hat{\mathbf r}\times\hat{\mathbf p}.
$$

In position representation,

$$
\hat{\mathbf p}=-i\hbar\nabla.
$$

The eigenfunctions of $\hat L^2$ and $\hat L_z$ are spherical harmonics:

$$
\hat L^2Y_{\ell m}(\theta,\phi)
=
\hbar^2\ell(\ell+1)Y_{\ell m}(\theta,\phi),
$$

$$
\hat L_zY_{\ell m}(\theta,\phi)
=
\hbar mY_{\ell m}(\theta,\phi).
$$

Here

$$
\ell=0,1,2,\dots,\qquad
m=-\ell,\dots,\ell.
$$

Orbital angular momentum only has integer $\ell$ because wave functions on ordinary space must be single-valued.

## Spin

Spin is intrinsic angular momentum. For spin $1/2$,

$$
\hat{\mathbf S}=\frac{\hbar}{2}\boldsymbol\sigma,
$$

where the Pauli matrices are

$$
\sigma_x=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix},
\quad
\sigma_y=
\begin{pmatrix}
0&-i\\
i&0
\end{pmatrix},
\quad
\sigma_z=
\begin{pmatrix}
1&0\\
0&-1
\end{pmatrix}.
$$

They satisfy

$$
[\sigma_i,\sigma_j]=2i\epsilon_{ijk}\sigma_k,
$$

$$
\{\sigma_i,\sigma_j\}=2\delta_{ij}\mathbf 1.
$$

A general spin-$1/2$ state is

$$
|\psi\rangle
=
\alpha|\uparrow\rangle+\beta|\downarrow\rangle,
\qquad
|\alpha|^2+|\beta|^2=1.
$$

Modulo global phase, pure spin-$1/2$ states are points on the Bloch sphere.

## Addition of Angular Momentum

For two systems,

$$
\hat{\mathbf J}=\hat{\mathbf J}_1+\hat{\mathbf J}_2.
$$

There are two natural bases:

$$
|j_1,m_1\rangle|j_2,m_2\rangle
$$

and

$$
|j_1,j_2;j,m\rangle.
$$

The allowed total angular momenta are

$$
j=|j_1-j_2|,\ |j_1-j_2|+1,\dots,j_1+j_2.
$$

The magnetic quantum number is

$$
m=m_1+m_2.
$$

## Clebsch-Gordan Coefficients

The basis transformation is

$$
|j_1,j_2;j,m\rangle
=
\sum_{m_1,m_2}
C^{jm}_{j_1m_1,j_2m_2}
|j_1,m_1\rangle|j_2,m_2\rangle.
$$

$C^{jm}_{j_1m_1,j_2m_2}$ are Clebsch-Gordan coefficients. They vanish unless

$$
m=m_1+m_2.
$$

They encode angular momentum selection rules in atoms, molecules, nuclei, and particle physics.

## Example: Two Spin-1/2 Particles

Two spin-$1/2$ particles combine as

$$
\frac12\otimes\frac12=1\oplus0.
$$

The triplet states are

$$
|1,1\rangle=|\uparrow\uparrow\rangle,
$$

$$
|1,0\rangle=
\frac{1}{\sqrt2}
\left(
|\uparrow\downarrow\rangle+
|\downarrow\uparrow\rangle
\right),
$$

$$
|1,-1\rangle=|\downarrow\downarrow\rangle.
$$

The singlet state is

$$
|0,0\rangle=
\frac{1}{\sqrt2}
\left(
|\uparrow\downarrow\rangle-
|\downarrow\uparrow\rangle
\right).
$$

The singlet is rotationally invariant and maximally entangled.

## Spin-Orbit Coupling

In atoms, spin and orbital angular momentum couple:

$$
\hat{\mathbf J}=\hat{\mathbf L}+\hat{\mathbf S}.
$$

A common spin-orbit term is

$$
\hat H_{SO}=\xi(r)\hat{\mathbf L}\cdot\hat{\mathbf S}.
$$

Using

$$
\hat{\mathbf L}\cdot\hat{\mathbf S}
=
\frac12
\left(
\hat J^2-\hat L^2-\hat S^2
\right),
$$

the energy shifts are labeled by $j,\ell,s$.

## Selection Rules

Angular momentum algebra constrains transitions. For electric dipole transitions in atoms, common selection rules are

$$
\Delta \ell=\pm1,
\qquad
\Delta m=0,\pm1.
$$

These rules come from the tensor transformation properties of the dipole operator under rotations.

## Connections

- [quantum mechanics](./quantum%20mechanics.md)
- [quantum approximation and scattering](./quantum%20approximation%20and%20scattering.md)
- [quantum information and open systems](./quantum%20information%20and%20open%20systems.md)
- [quantum field](./quantum%20field.md)
