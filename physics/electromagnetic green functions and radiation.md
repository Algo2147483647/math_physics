# Electromagnetic Green Functions and Radiation

[TOC]

## Purpose

This note develops the source-to-field side of classical electromagnetism: Green functions, retarded and advanced potentials, Lienard-Wiechert potentials, dipole radiation, and multipole expansion.

It expands the overview in [electromagnetic field](./electromagnetic%20field.md).

## Wave Equations for Potentials

In Lorenz gauge,

$$
\nabla\cdot\mathbf A+\frac{1}{c^2}\frac{\partial\phi}{\partial t}=0,
$$

the potentials satisfy

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

Define the wave operator

$$
\Box=\frac{1}{c^2}\frac{\partial^2}{\partial t^2}-\nabla^2.
$$

Then the covariant equation is

$$
\Box A^\mu=\mu_0J^\mu.
$$

## Green Function Method

### Definition

A Green function for the wave equation satisfies

$$
\left(\nabla^2-\frac{1}{c^2}\frac{\partial^2}{\partial t^2}\right)
G(\mathbf r,t;\mathbf r',t')
=
-\delta^3(\mathbf r-\mathbf r')\delta(t-t').
$$

Once $G$ is known, the scalar potential is

$$
\phi(\mathbf r,t)
=
\frac{1}{\varepsilon_0}
\int G(\mathbf r,t;\mathbf r',t')\rho(\mathbf r',t')\,\mathrm d^3r'\,\mathrm dt',
$$

and the vector potential is

$$
\mathbf A(\mathbf r,t)
=
\mu_0
\int G(\mathbf r,t;\mathbf r',t')\mathbf J(\mathbf r',t')\,\mathrm d^3r'\,\mathrm dt'.
$$

### Retarded Green function

Let

$$
R=|\mathbf r-\mathbf r'|.
$$

The retarded Green function is

$$
G_{\mathrm{ret}}
=
\frac{\delta(t'-t+R/c)}{4\pi R}.
$$

It gives causal fields: the field at $(\mathbf r,t)$ depends on the source at the earlier time

$$
t_{\mathrm{ret}}=t-\frac{R}{c}.
$$

The retarded potentials are

$$
\phi(\mathbf r,t)
=
\frac{1}{4\pi\varepsilon_0}
\int
\frac{\rho(\mathbf r',t-R/c)}{R}\,\mathrm d^3r',
$$

$$
\mathbf A(\mathbf r,t)
=
\frac{\mu_0}{4\pi}
\int
\frac{\mathbf J(\mathbf r',t-R/c)}{R}\,\mathrm d^3r'.
$$

### Advanced Green function

The advanced Green function is

$$
G_{\mathrm{adv}}
=
\frac{\delta(t'-t-R/c)}{4\pi R}.
$$

It depends on the source at

$$
t_{\mathrm{adv}}=t+\frac{R}{c}.
$$

Advanced solutions are usually not used as physical boundary conditions for ordinary radiation problems, but they are useful in formal scattering theory and time-symmetric formulations.

## Static Limits

For time-independent sources, the retarded potentials reduce to the Coulomb and Biot-Savart potentials:

$$
\phi(\mathbf r)
=
\frac{1}{4\pi\varepsilon_0}
\int\frac{\rho(\mathbf r')}{|\mathbf r-\mathbf r'|}\,\mathrm d^3r',
$$

$$
\mathbf A(\mathbf r)
=
\frac{\mu_0}{4\pi}
\int\frac{\mathbf J(\mathbf r')}{|\mathbf r-\mathbf r'|}\,\mathrm d^3r'.
$$

## Lienard-Wiechert Potentials

For a point charge $q$ moving on trajectory $\mathbf r_q(t)$, define retarded time $t_r$ by

$$
t_r=t-\frac{|\mathbf r-\mathbf r_q(t_r)|}{c}.
$$

Let

$$
\mathbf R=\mathbf r-\mathbf r_q(t_r),\qquad
R=|\mathbf R|,\qquad
\mathbf n=\frac{\mathbf R}{R},\qquad
\boldsymbol\beta=\frac{\mathbf v(t_r)}{c}.
$$

The Lienard-Wiechert potentials are

$$
\phi(\mathbf r,t)
=
\frac{q}{4\pi\varepsilon_0}
\left[
\frac{1}{(1-\mathbf n\cdot\boldsymbol\beta)R}
\right]_{\mathrm{ret}},
$$

$$
\mathbf A(\mathbf r,t)
=
\frac{\mu_0 q}{4\pi}
\left[
\frac{\mathbf v}{(1-\mathbf n\cdot\boldsymbol\beta)R}
\right]_{\mathrm{ret}}.
$$

Equivalently,

$$
\mathbf A=\frac{\mathbf v}{c^2}\phi
$$

evaluated at retarded time.

## Fields of an Accelerated Charge

The electric field of a moving point charge separates into a velocity field and an acceleration field:

$$
\mathbf E
=
\frac{q}{4\pi\varepsilon_0}
\left[
\frac{\mathbf n-\boldsymbol\beta}
{\gamma^2(1-\mathbf n\cdot\boldsymbol\beta)^3R^2}
+
\frac{\mathbf n\times\left((\mathbf n-\boldsymbol\beta)\times\dot{\boldsymbol\beta}\right)}
{c(1-\mathbf n\cdot\boldsymbol\beta)^3R}
\right]_{\mathrm{ret}}.
$$

The magnetic field is

$$
\mathbf B=\frac{1}{c}\left[\mathbf n\times\mathbf E\right]_{\mathrm{ret}}.
$$

The first term scales as $1/R^2$ and dominates near the charge. The second term scales as $1/R$ and is the radiation field.

## Radiation Power

### Larmor formula

For a nonrelativistic accelerated charge,

$$
P=\frac{q^2a^2}{6\pi\varepsilon_0c^3}.
$$

This is the Larmor formula.

### Relativistic generalization

For relativistic motion,

$$
P
=
\frac{q^2\gamma^6}{6\pi\varepsilon_0c^3}
\left(
a^2-|\boldsymbol\beta\times\mathbf a|^2
\right).
$$

Radiation is strongly beamed in the forward direction when $\gamma\gg1$.

## Electric Dipole Radiation

For a localized source whose size $a$ is much smaller than the wavelength $\lambda$, the leading radiation is often electric dipole radiation.

The electric dipole moment is

$$
\mathbf p(t)=\int \rho(\mathbf r,t)\mathbf r\,\mathrm d^3r.
$$

In the far zone,

$$
\mathbf E_{\mathrm{rad}}
=
\frac{\mu_0}{4\pi r}
\left[
\mathbf n\times(\mathbf n\times\ddot{\mathbf p})
\right]_{t-r/c},
$$

$$
\mathbf B_{\mathrm{rad}}
=
\frac{1}{c}\mathbf n\times\mathbf E_{\mathrm{rad}}.
$$

The instantaneous radiated power is

$$
P
=
\frac{\mu_0}{6\pi c}|\ddot{\mathbf p}|^2
=
\frac{|\ddot{\mathbf p}|^2}{6\pi\varepsilon_0c^3}.
$$

For harmonic dipole moment $\mathbf p(t)=\mathbf p_0\cos\omega t$, the time-averaged power is

$$
\langle P\rangle
=
\frac{\omega^4|\mathbf p_0|^2}{12\pi\varepsilon_0c^3}.
$$

## Multipole Expansion

For a localized source observed far away, expand the fields in powers of

$$
ka=\frac{2\pi a}{\lambda}.
$$

When $ka\ll1$, the hierarchy is usually:

1. electric dipole radiation.
2. magnetic dipole radiation.
3. electric quadrupole radiation.
4. higher electric and magnetic multipoles.

For static electrostatics, the scalar potential outside a localized charge distribution is

$$
\phi(\mathbf r)
=
\frac{1}{4\pi\varepsilon_0}
\left[
\frac{Q}{r}
+
\frac{\mathbf p\cdot\mathbf n}{r^2}
+
\frac{1}{2r^3}Q_{ij}n_in_j
+\cdots
\right],
$$

where

$$
Q=\int\rho\,\mathrm d^3r,\qquad
\mathbf p=\int\rho\mathbf r\,\mathrm d^3r.
$$

The multipole expansion separates source geometry from observation distance and is central in radiation, antenna theory, atomic transitions, and scattering.

## Radiation Zones

For a source of size $a$ and wavelength $\lambda$, the regions are:

- Near zone: $r\ll\lambda$; quasistatic fields dominate.
- Induction zone: $r\sim\lambda$; mixed reactive and radiative behavior.
- Radiation zone: $r\gg\lambda$ and $r\gg a$; fields scale as $1/r$ and carry power outward.

In the radiation zone,

$$
\mathbf E\perp\mathbf B\perp\mathbf n,\qquad
|\mathbf E|=c|\mathbf B|.
$$

## Connections

- [electromagnetic field](./electromagnetic%20field.md)
- [electromagnetic waves waveguides and antennas](./electromagnetic%20waves%20waveguides%20and%20antennas.md)
- [electromagnetic field in media](./electromagnetic%20field%20in%20media.md)
- [mechanics of flat spacetime](./mechanics%20of%20flat%20spacetime.md)
