# Elasticity

[TOC]

## Purpose

Elasticity is the continuum mechanics of deformable solids. It extends finite-dimensional mechanics by replacing particle coordinates with displacement fields and by replacing forces with stress.

## Kinematics

### Displacement field

Let $X$ be the material coordinate of a point in the reference configuration. The deformed position is

$$
x(X,t)=X+u(X,t),
$$

where $u(X,t)$ is the displacement field.

### Deformation gradient

$$
F_{iJ}=\frac{\partial x_i}{\partial X_J}
=
\delta_{iJ}+\frac{\partial u_i}{\partial X_J}.
$$

$F$ maps material line elements to spatial line elements.

### Small strain tensor

For small displacement gradients, use the infinitesimal strain tensor

$$
\varepsilon_{ij}
=
\frac12(\partial_i u_j+\partial_j u_i).
$$

It measures local stretching and shear. Rigid translations and infinitesimal rotations do not contribute to $\varepsilon_{ij}$.

## Stress

### Cauchy stress tensor

The traction $t_i$ on a surface with unit normal $n_j$ is

$$
t_i=\sigma_{ij}n_j.
$$

$\sigma_{ij}$ is the Cauchy stress tensor. Angular momentum conservation implies

$$
\sigma_{ij}=\sigma_{ji}.
$$

### Balance of linear momentum

For mass density $\rho$ and body force $f_i$,

$$
\rho\,\partial_t^2 u_i = \partial_j\sigma_{ij}+f_i .
$$

Static equilibrium is

$$
\partial_j\sigma_{ij}+f_i=0.
$$

## Linear Isotropic Elasticity

### Hooke's law

For a homogeneous isotropic solid,

$$
\sigma_{ij}
=
\lambda\,\delta_{ij}\varepsilon_{kk}
+2\mu\,\varepsilon_{ij}.
$$

$\lambda$ and $\mu$ are the Lame parameters. $\mu$ is the shear modulus.

Other common elastic constants are

$$
K=\lambda+\frac{2}{3}\mu,\qquad
E=\frac{\mu(3\lambda+2\mu)}{\lambda+\mu},\qquad
\nu=\frac{\lambda}{2(\lambda+\mu)}.
$$

- $K$: bulk modulus.
- $E$: Young's modulus.
- $\nu$: Poisson ratio.

### Elastic energy density

The strain energy density is

$$
W(\varepsilon)=
\frac12\lambda(\varepsilon_{kk})^2
+\mu\,\varepsilon_{ij}\varepsilon_{ij}.
$$

The stress is obtained by differentiation:

$$
\sigma_{ij}=\frac{\partial W}{\partial\varepsilon_{ij}}.
$$

## Elastic Wave Equation

Substitute Hooke's law into momentum balance:

$$
\rho\,\partial_t^2 u_i
=
(\lambda+\mu)\partial_i(\partial_j u_j)
+\mu\nabla^2u_i+f_i.
$$

Without body forces:

$$
\rho\,\partial_t^2 \mathbf u
=
(\lambda+\mu)\nabla(\nabla\cdot\mathbf u)
+\mu\nabla^2\mathbf u .
$$

Decompose the displacement into longitudinal and transverse parts:

$$
\mathbf u=\mathbf u_L+\mathbf u_T,\qquad
\nabla\times\mathbf u_L=0,\qquad
\nabla\cdot\mathbf u_T=0.
$$

The wave speeds are

$$
c_L=\sqrt{\frac{\lambda+2\mu}{\rho}},\qquad
c_T=\sqrt{\frac{\mu}{\rho}}.
$$

Longitudinal waves are compression waves; transverse waves are shear waves.

## Variational Formulation

The action for linear elasticity is

$$
S[u]=
\int
\left[
\frac12\rho\,\partial_t u_i\partial_t u_i
-
W(\varepsilon)
+
f_i u_i
\right]
\mathrm d^3x\,\mathrm dt .
$$

Stationary action gives

$$
\rho\,\partial_t^2 u_i = \partial_j\sigma_{ij}+f_i.
$$

This makes elasticity a classical field theory.

## Boundary Conditions

Common boundary conditions are:

- Displacement boundary condition: $u_i=\bar u_i$ on a fixed boundary.
- Traction boundary condition: $\sigma_{ij}n_j=\bar t_i$ on a loaded boundary.
- Free surface: $\sigma_{ij}n_j=0$.

## Normal Modes of Elastic Bodies

For a free elastic body, normal modes solve

$$
-\rho\omega^2 u_i
=
(\lambda+\mu)\partial_i(\partial_j u_j)
+\mu\nabla^2u_i .
$$

Boundary conditions select a discrete set of frequencies for bounded bodies. In crystals, elastic waves become acoustic phonons after quantization.

## Beyond Linear Elasticity

Linear elasticity assumes small strain and linear stress-strain response. More general theories include:

- finite elasticity: nonlinear strain measures and large deformation.
- viscoelasticity: stress depends on strain history.
- plasticity: irreversible deformation.
- fracture mechanics: cracks and singular stress fields.
- defects: dislocations and disclinations.

## Connections

- [basic principles of mechanics](./basic%20principles%20of%20mechanics.md)
- [small oscillations and classical chaos](./small%20oscillations%20and%20classical%20chaos.md)
- [fluid](./fluid.md)
