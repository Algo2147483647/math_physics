# Electromagnetic Waves, Waveguides, and Antennas

[TOC]

## Purpose

This note collects wave phenomena that follow from Maxwell's equations: plane waves, polarization, Stokes parameters, waveguides, resonant cavities, and basic antenna radiation.

It expands the overview in [electromagnetic field](./electromagnetic%20field.md).

## Plane Waves in Vacuum

In source-free vacuum,

$$
\nabla^2\mathbf E-\frac{1}{c^2}\frac{\partial^2\mathbf E}{\partial t^2}=0,
\qquad
\nabla^2\mathbf B-\frac{1}{c^2}\frac{\partial^2\mathbf B}{\partial t^2}=0.
$$

A monochromatic plane wave has the form

$$
\mathbf E(\mathbf r,t)=\mathrm{Re}\left(\mathbf E_0e^{i(\mathbf k\cdot\mathbf r-\omega t)}\right),
$$

$$
\mathbf B(\mathbf r,t)=\mathrm{Re}\left(\mathbf B_0e^{i(\mathbf k\cdot\mathbf r-\omega t)}\right).
$$

Maxwell's equations imply

$$
\omega=c|\mathbf k|,
\qquad
\mathbf k\cdot\mathbf E_0=0,
\qquad
\mathbf k\cdot\mathbf B_0=0,
$$

$$
\mathbf B_0=\frac{1}{\omega}\mathbf k\times\mathbf E_0.
$$

The vacuum impedance is

$$
Z_0=\sqrt{\frac{\mu_0}{\varepsilon_0}}=\mu_0c.
$$

For a plane wave,

$$
|\mathbf E|=Z_0|\mathbf H|.
$$

## Polarization

### Jones vector

For a wave propagating in the $z$ direction, the transverse electric field can be written as

$$
\mathbf E_\perp(t)
=
\mathrm{Re}
\left[
\begin{pmatrix}
E_x\\
E_y
\end{pmatrix}
e^{i(kz-\omega t)}
\right].
$$

The complex vector

$$
\mathbf J=
\begin{pmatrix}
E_x\\
E_y
\end{pmatrix}
$$

is the Jones vector.

Common polarization states:

- Linear polarization: $E_x$ and $E_y$ have phase difference $0$ or $\pi$.
- Circular polarization: $|E_x|=|E_y|$ with phase difference $\pm\pi/2$.
- Elliptical polarization: the general case.

### Stokes parameters

The Stokes parameters describe intensity and polarization without requiring phase coherence:

$$
I=|E_x|^2+|E_y|^2,
$$

$$
Q=|E_x|^2-|E_y|^2,
$$

$$
U=2\mathrm{Re}(E_xE_y^*),
$$

$$
V=2\mathrm{Im}(E_xE_y^*).
$$

Interpretation:

- $I$: total intensity.
- $Q$: horizontal versus vertical linear polarization.
- $U$: $45^\circ$ versus $-45^\circ$ linear polarization.
- $V$: right versus left circular polarization, with sign depending on convention.

For fully polarized light,

$$
I^2=Q^2+U^2+V^2.
$$

The normalized vector $(Q/I,U/I,V/I)$ lies on the Poincare sphere.

## Reflection and Boundary Conditions

At a perfect electric conductor,

$$
\mathbf n\times\mathbf E=0,\qquad
\mathbf n\cdot\mathbf B=0
$$

on the surface. These boundary conditions shape standing waves in cavities and guided modes in waveguides.

At an interface between ordinary media without free surface charge or current,

$$
\mathbf n\cdot(\mathbf D_2-\mathbf D_1)=0,
\qquad
\mathbf n\cdot(\mathbf B_2-\mathbf B_1)=0,
$$

$$
\mathbf n\times(\mathbf E_2-\mathbf E_1)=0,
\qquad
\mathbf n\times(\mathbf H_2-\mathbf H_1)=0.
$$

## Waveguides

### Modes

A waveguide confines electromagnetic waves by boundary conditions. Modes are classified by longitudinal components:

- TEM mode: $E_z=0$ and $B_z=0$.
- TE mode: $E_z=0$ and $B_z\ne0$.
- TM mode: $B_z=0$ and $E_z\ne0$.

Single-conductor hollow metallic waveguides support TE and TM modes but not TEM modes. Two-conductor structures, such as coaxial cables, can support TEM modes.

### Cutoff

For a guide with propagation direction $z$,

$$
\beta^2=k^2-k_c^2,
\qquad
k=\frac{\omega}{c}.
$$

$k_c$ is the cutoff wavenumber. Propagation requires

$$
\omega>\omega_c=ck_c.
$$

Below cutoff, $\beta$ is imaginary and the mode is evanescent.

### Rectangular waveguide

For a rectangular metallic waveguide with sides $a$ and $b$,

$$
k_c^2=
\left(\frac{m\pi}{a}\right)^2
+
\left(\frac{n\pi}{b}\right)^2.
$$

The cutoff frequency is

$$
f_c=\frac{c}{2}
\sqrt{
\left(\frac{m}{a}\right)^2+
\left(\frac{n}{b}\right)^2
}.
$$

The dominant mode for $a>b$ is usually $\mathrm{TE}_{10}$.

The phase and group velocities are

$$
v_p=\frac{\omega}{\beta},
\qquad
v_g=\frac{\mathrm d\omega}{\mathrm d\beta},
\qquad
v_pv_g=c^2
$$

for an ideal hollow guide.

## Resonant Cavities

A resonant cavity traps electromagnetic standing waves. Resonant frequencies are selected by boundary conditions.

For a rectangular cavity with side lengths $a,b,d$,

$$
\omega_{mnp}
=
c\sqrt{
\left(\frac{m\pi}{a}\right)^2
+
\left(\frac{n\pi}{b}\right)^2
+
\left(\frac{p\pi}{d}\right)^2
}.
$$

The quality factor is

$$
Q=\omega\frac{U}{P_{\mathrm{loss}}},
$$

where $U$ is stored energy and $P_{\mathrm{loss}}$ is power dissipated per unit time.

Large $Q$ means narrow bandwidth and slow energy decay:

$$
U(t)\sim U_0e^{-\omega t/Q}.
$$

## Antenna Basics

### Radiation pattern

An antenna converts guided currents into radiating fields. In the far zone,

$$
\mathbf E,\mathbf H\propto\frac{1}{r},
$$

and the angular dependence defines the radiation pattern.

The time-averaged radiated power per solid angle is

$$
\frac{\mathrm dP}{\mathrm d\Omega}
=
r^2\langle\mathbf S\rangle\cdot\mathbf n.
$$

The directivity is

$$
D(\theta,\phi)
=
\frac{4\pi\,\mathrm dP/\mathrm d\Omega}{P_{\mathrm{rad}}}.
$$

### Short dipole

For a short current element of length $l\ll\lambda$ with current amplitude $I_0$, the far-zone electric field is approximately

$$
E_\theta
=
iZ_0\frac{kI_0l}{4\pi r}\sin\theta\,e^{i(kr-\omega t)}.
$$

The magnetic field is

$$
H_\phi=\frac{E_\theta}{Z_0}.
$$

The radiation resistance is

$$
R_r=80\pi^2\left(\frac{l}{\lambda}\right)^2.
$$

### Effective aperture and gain

A receiving antenna has effective aperture $A_e$ related to gain $G$ by

$$
A_e=\frac{\lambda^2G}{4\pi}.
$$

Gain includes directivity and efficiency:

$$
G=\eta D.
$$

## Connections

- [electromagnetic field](./electromagnetic%20field.md)
- [electromagnetic green functions and radiation](./electromagnetic%20green%20functions%20and%20radiation.md)
- [electromagnetic field in media](./electromagnetic%20field%20in%20media.md)
