# Electromagnetic Field

[TOC]

## Conventions

Unless stated otherwise, this note uses SI units, metric signature $(+,-,-,-)$, and spacetime coordinates

$$
x^\mu=(ct,x,y,z).
$$

The four-current is

$$
J^\mu=(c\rho,\mathbf J),
$$

where $\rho$ is charge density and $\mathbf J$ is current density.

## Potentials and Gauge Structure

### Scalar and vector potentials

The electromagnetic field can be described by a scalar potential $\phi$ and a vector potential $\mathbf A$:

$$
\mathbf B = \nabla\times\mathbf A,\qquad
\mathbf E = -\nabla\phi-\frac{\partial\mathbf A}{\partial t}.
$$

These equations automatically imply the homogeneous Maxwell equations:

$$
\nabla\cdot\mathbf B=0,\qquad
\nabla\times\mathbf E+\frac{\partial\mathbf B}{\partial t}=0.
$$

### Four-potential

The scalar and vector potentials combine into a four-potential

$$
A^\mu=\left(\frac{\phi}{c},\mathbf A\right).
$$

The potential is not unique. The physical fields are unchanged by the three-vector gauge transformation

$$
\mathbf A\to \mathbf A+\nabla\chi,\qquad
\phi\to\phi-\frac{\partial\chi}{\partial t}.
$$

Equivalently, after the conventional sign choice for the gauge function is fixed, the covariant statement may be written as

$$
A_\mu \to A_\mu+\partial_\mu\chi .
$$

Gauge freedom means that $A_\mu$ contains redundant description. The observable object is the field strength.

## Field Tensor

### Definition

The electromagnetic field tensor is

$$
F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu.
$$

It is antisymmetric:

$$
F_{\mu\nu}=-F_{\nu\mu}.
$$

With the convention above, one convenient matrix form is

$$
F^{\mu\nu} =
\begin{pmatrix}
0 & -E_x/c & -E_y/c & -E_z/c \\
E_x/c & 0 & -B_z & B_y \\
E_y/c & B_z & 0 & -B_x \\
E_z/c & -B_y & B_x & 0
\end{pmatrix}.
$$

The dual tensor is

$$
\tilde F^{\mu\nu}
=
\frac12\epsilon^{\mu\nu\rho\sigma}F_{\rho\sigma}.
$$

### Lorentz invariants

Two scalar invariants can be formed from $F_{\mu\nu}$:

$$
F_{\mu\nu}F^{\mu\nu}=2\left(B^2-\frac{E^2}{c^2}\right),
$$

$$
F_{\mu\nu}\tilde F^{\mu\nu}
=
-\frac{4}{c}\mathbf E\cdot\mathbf B .
$$

These quantities are unchanged under Lorentz transformations.

## Maxwell Equations

### Covariant form

Maxwell's equations in vacuum are

$$
\partial_\mu F^{\mu\nu}=\mu_0 J^\nu,
$$

$$
\partial_\mu \tilde F^{\mu\nu}=0.
$$

The first equation contains Gauss's law and the Ampere-Maxwell law. The second equation contains the absence of magnetic monopoles and Faraday's law.

### Vector form

$$
\begin{align*}
\nabla\cdot\mathbf E &= \frac{\rho}{\varepsilon_0},\\
\nabla\cdot\mathbf B &= 0,\\
\nabla\times\mathbf E+\frac{\partial\mathbf B}{\partial t} &= 0,\\
\nabla\times\mathbf B-\mu_0\varepsilon_0\frac{\partial\mathbf E}{\partial t} &= \mu_0\mathbf J.
\end{align*}
$$

The speed of electromagnetic waves in vacuum is

$$
c=\frac{1}{\sqrt{\mu_0\varepsilon_0}}.
$$

### Charge conservation

Taking $\partial_\nu$ of $\partial_\mu F^{\mu\nu}=\mu_0J^\nu$ gives

$$
\partial_\nu J^\nu=0,
$$

because $F^{\mu\nu}$ is antisymmetric. In vector form,

$$
\frac{\partial\rho}{\partial t}+\nabla\cdot\mathbf J=0.
$$

This is the local conservation law for charge.

## Gauge Choices

Gauge conditions choose one representative from the equivalence class of potentials.

### Lorenz gauge

The Lorenz gauge is

$$
\partial_\mu A^\mu=0,
$$

or

$$
\nabla\cdot\mathbf A+\frac{1}{c^2}\frac{\partial\phi}{\partial t}=0.
$$

In Lorenz gauge, the potentials satisfy decoupled wave equations:

$$
\left(\nabla^2-\frac{1}{c^2}\frac{\partial^2}{\partial t^2}\right)\phi
=
-\frac{\rho}{\varepsilon_0},
$$

$$
\left(\nabla^2-\frac{1}{c^2}\frac{\partial^2}{\partial t^2}\right)\mathbf A
=
-\mu_0\mathbf J.
$$

Lorenz gauge is manifestly Lorentz covariant and is the natural gauge for retarded potentials and relativistic field theory.

### Coulomb gauge

The Coulomb gauge is

$$
\nabla\cdot\mathbf A=0.
$$

Then the scalar potential satisfies the instantaneous Poisson equation

$$
\nabla^2\phi=-\frac{\rho}{\varepsilon_0},
$$

while the vector potential carries the transverse radiative degrees of freedom. Coulomb gauge is useful in radiation theory, nonrelativistic quantum mechanics, and canonical quantization.

## Action

### Field and source action

The electromagnetic field action with external current is

$$
S[A]
=
\int
\left(
-\frac{1}{4\mu_0}F_{\mu\nu}F^{\mu\nu}
-J_\mu A^\mu
\right)\mathrm d^4x .
$$

Varying $A_\mu$ gives

$$
\partial_\mu F^{\mu\nu}=\mu_0J^\nu.
$$

Gauge invariance of the source term requires charge conservation:

$$
\partial_\mu J^\mu=0.
$$

### Charged particle action

For a point charge $q$ moving on a worldline $x^\mu(\tau)$,

$$
S
=
-mc^2\int\mathrm d\tau
+q\int A_\mu\,\mathrm d x^\mu .
$$

In three-vector form the Lagrangian is

$$
L
=
-mc^2\sqrt{1-\frac{v^2}{c^2}}
+q\mathbf A\cdot\mathbf v
-q\phi .
$$

## Lorentz Force

The covariant Lorentz force law is

$$
\frac{\mathrm d p^\mu}{\mathrm d\tau}
=
qF^{\mu\nu}u_\nu.
$$

The spatial part is

$$
\frac{\mathrm d\mathbf p}{\mathrm dt}
=
q(\mathbf E+\mathbf v\times\mathbf B).
$$

The power delivered to the charge is

$$
\frac{\mathrm dE}{\mathrm dt}=q\mathbf E\cdot\mathbf v.
$$

## Energy, Momentum, and Stress

### Poynting theorem

The electromagnetic energy density is

$$
u
=
\frac12\varepsilon_0E^2+\frac{1}{2\mu_0}B^2.
$$

The Poynting vector is

$$
\mathbf S=\frac{1}{\mu_0}\mathbf E\times\mathbf B.
$$

Poynting's theorem is

$$
\frac{\partial u}{\partial t}
+\nabla\cdot\mathbf S
=
-\mathbf J\cdot\mathbf E.
$$

The right-hand side is the rate at which the field does work on charges.

### Momentum density and Maxwell stress tensor

The electromagnetic momentum density is

$$
\mathbf g=\frac{\mathbf S}{c^2}=\varepsilon_0\mathbf E\times\mathbf B.
$$

The Maxwell stress tensor is

$$
T_{ij}
=
\varepsilon_0\left(E_iE_j-\frac12\delta_{ij}E^2\right)
+
\frac{1}{\mu_0}
\left(B_iB_j-\frac12\delta_{ij}B^2\right).
$$

It expresses the flux of electromagnetic momentum.

## Green Functions and Radiation

In Lorenz gauge, the potentials obey wave equations. Their solutions can be written using Green functions:

$$
\left(\nabla^2-\frac{1}{c^2}\frac{\partial^2}{\partial t^2}\right)G(\mathbf r,t;\mathbf r',t')
=
-\delta^3(\mathbf r-\mathbf r')\delta(t-t').
$$

The retarded Green function gives causal potentials; the advanced Green function gives acausal mathematical solutions useful in formal theory.

More details: [electromagnetic green functions and radiation](./electromagnetic%20green%20functions%20and%20radiation.md).

## Electromagnetic Waves

In vacuum without sources,

$$
\nabla^2\mathbf E-\frac{1}{c^2}\frac{\partial^2\mathbf E}{\partial t^2}=0,
\qquad
\nabla^2\mathbf B-\frac{1}{c^2}\frac{\partial^2\mathbf B}{\partial t^2}=0.
$$

Plane waves are transverse:

$$
\mathbf k\cdot\mathbf E=0,\qquad
\mathbf k\cdot\mathbf B=0,\qquad
\mathbf B=\frac{1}{\omega}\mathbf k\times\mathbf E.
$$

Polarization, Stokes parameters, waveguides, resonant cavities, and antennas are covered in:

- [electromagnetic waves waveguides and antennas](./electromagnetic%20waves%20waveguides%20and%20antennas.md)
- [electromagnetic field in media](./electromagnetic%20field%20in%20media.md)

## Differential Forms

Electromagnetism has a compact coordinate-free form. Let

$$
A=A_\mu\,\mathrm d x^\mu
$$

be the electromagnetic potential one-form. The field strength two-form is

$$
F=\mathrm dA.
$$

Gauge transformation is

$$
A\to A+\mathrm d\chi.
$$

Since $\mathrm d^2=0$,

$$
\mathrm dF=0.
$$

This is the homogeneous Maxwell equation. The inhomogeneous equation is

$$
\mathrm d\star F=\mu_0\mathcal J,
$$

where $\star$ is the Hodge star and $\mathcal J$ is the current three-form. In this language, magnetic flux conservation and Faraday induction are both consequences of $F=\mathrm dA$.

## Connections

- [electromagnetic green functions and radiation](./electromagnetic%20green%20functions%20and%20radiation.md)
- [electromagnetic waves waveguides and antennas](./electromagnetic%20waves%20waveguides%20and%20antennas.md)
- [electromagnetic field in media](./electromagnetic%20field%20in%20media.md)
- [basic principles of mechanics](./basic%20principles%20of%20mechanics.md)
- [mechanics of flat spacetime](./mechanics%20of%20flat%20spacetime.md)
