# Quantum Approximation and Scattering

[TOC]

## Purpose

Most quantum systems cannot be solved exactly. Approximation methods extract spectra, states, transition rates, and scattering cross sections from Hamiltonians that are close to solvable limits.

This page expands [quantum mechanics](./quantum%20mechanics.md).

## Time-Independent Perturbation Theory

Let

$$
\hat H=\hat H_0+\lambda\hat V,
$$

where $\hat H_0$ has known eigenstates:

$$
\hat H_0|n^{(0)}\rangle=E_n^{(0)}|n^{(0)}\rangle.
$$

For a nondegenerate level, expand

$$
E_n=E_n^{(0)}+\lambda E_n^{(1)}+\lambda^2E_n^{(2)}+\cdots,
$$

$$
|n\rangle=|n^{(0)}\rangle+\lambda|n^{(1)}\rangle+\cdots.
$$

The first-order energy shift is

$$
E_n^{(1)}
=
\langle n^{(0)}|\hat V|n^{(0)}\rangle.
$$

The second-order energy shift is

$$
E_n^{(2)}
=
\sum_{m\ne n}
\frac{|\langle m^{(0)}|\hat V|n^{(0)}\rangle|^2}
{E_n^{(0)}-E_m^{(0)}}.
$$

The first-order state correction is

$$
|n^{(1)}\rangle
=
\sum_{m\ne n}
\frac{\langle m^{(0)}|\hat V|n^{(0)}\rangle}
{E_n^{(0)}-E_m^{(0)}}
|m^{(0)}\rangle.
$$

## Degenerate Perturbation Theory

If several states share the same unperturbed energy, ordinary perturbation theory fails. Restrict $\hat V$ to the degenerate subspace:

$$
V_{ab}=\langle a|\hat V|b\rangle.
$$

Diagonalize $V_{ab}$ inside this subspace. Its eigenvectors give the correct zeroth-order combinations, and its eigenvalues give the first-order energy shifts.

This is essential for fine structure, Stark effect, Zeeman effect, and symmetry-breaking perturbations.

## Time-Dependent Perturbation Theory

Let

$$
\hat H(t)=\hat H_0+\hat V(t).
$$

In the interaction picture,

$$
i\hbar\frac{\mathrm d}{\mathrm dt}|\psi_I(t)\rangle
=
\hat V_I(t)|\psi_I(t)\rangle.
$$

The first-order transition amplitude from $|i\rangle$ to $|f\rangle$ is

$$
c_f^{(1)}(t)
=
-\frac{i}{\hbar}
\int_{t_0}^{t}
\langle f|\hat V_I(t')|i\rangle\,\mathrm dt'.
$$

For a weak periodic perturbation, the long-time transition rate is given by Fermi's golden rule:

$$
\Gamma_{i\to f}
=
\frac{2\pi}{\hbar}
|\langle f|\hat V|i\rangle|^2
\rho(E_f).
$$

$\rho(E_f)$ is the density of final states.

## Variational Method

For any normalized trial state $|\psi_T\rangle$,

$$
E_0\le
\langle\psi_T|\hat H|\psi_T\rangle.
$$

The variational method chooses trial states depending on parameters $\alpha_i$ and minimizes

$$
E[\alpha_i]
=
\frac{\langle\psi_T(\alpha_i)|\hat H|\psi_T(\alpha_i)\rangle}
{\langle\psi_T(\alpha_i)|\psi_T(\alpha_i)\rangle}.
$$

It gives an upper bound on the ground-state energy and a practical approximation to the ground-state wave function.

## WKB Approximation

For one-dimensional stationary states,

$$
-\frac{\hbar^2}{2m}\frac{\mathrm d^2\psi}{\mathrm dx^2}
+V(x)\psi=E\psi.
$$

Assume the semiclassical form

$$
\psi(x)=A(x)e^{iS(x)/\hbar}.
$$

In a classically allowed region $E>V(x)$, define

$$
p(x)=\sqrt{2m(E-V(x))}.
$$

The WKB wave function is

$$
\psi(x)
\approx
\frac{C}{\sqrt{p(x)}}
\exp\left(\pm\frac{i}{\hbar}\int^x p(x')\,\mathrm dx'\right).
$$

In a forbidden region $E<V(x)$, define

$$
\kappa(x)=\sqrt{2m(V(x)-E)}.
$$

Then

$$
\psi(x)
\approx
\frac{C}{\sqrt{\kappa(x)}}
\exp\left(\pm\frac{1}{\hbar}\int^x \kappa(x')\,\mathrm dx'\right).
$$

For a bound state between two turning points,

$$
\int_{x_1}^{x_2}p(x)\,\mathrm dx
=
\left(n+\frac12\right)\pi\hbar.
$$

This is the Bohr-Sommerfeld quantization rule with the WKB turning-point correction.

## Tunneling

For a barrier where $V(x)>E$ between $x_1$ and $x_2$, the WKB transmission probability is approximately

$$
T
\sim
\exp\left[
-\frac{2}{\hbar}
\int_{x_1}^{x_2}
\sqrt{2m(V(x)-E)}\,\mathrm dx
\right].
$$

This describes alpha decay, field emission, and many semiclassical barrier processes.

## Scattering Theory

### Asymptotic form

For a particle incident with wave vector $\mathbf k$, the large-distance wave function has the form

$$
\psi(\mathbf r)
\sim
e^{i\mathbf k\cdot\mathbf r}
+
f(\theta,\phi)\frac{e^{ikr}}{r}.
$$

$f(\theta,\phi)$ is the scattering amplitude.

The differential cross section is

$$
\frac{\mathrm d\sigma}{\mathrm d\Omega}
=
|f(\theta,\phi)|^2.
$$

### Lippmann-Schwinger equation

For

$$
\hat H=\hat H_0+\hat V,
$$

the scattering state satisfies

$$
|\psi^{(+)}\rangle
=
|\phi\rangle
+
\frac{1}{E-\hat H_0+i0^+}
\hat V|\psi^{(+)}\rangle.
$$

The $+i0^+$ prescription enforces outgoing boundary conditions.

## Born Approximation

The first Born approximation replaces $|\psi^{(+)}\rangle$ by the incoming plane wave. For potential $V(\mathbf r)$,

$$
f_{\mathrm B}(\mathbf q)
=
-\frac{m}{2\pi\hbar^2}
\int e^{-i\mathbf q\cdot\mathbf r}
V(\mathbf r)\,\mathrm d^3r,
$$

where

$$
\mathbf q=\mathbf k_f-\mathbf k_i.
$$

The Born approximation is useful for weak potentials and high incident energies.

## Partial Waves and Phase Shifts

For a central potential $V(r)$, expand the scattering amplitude in partial waves:

$$
f(\theta)
=
\frac{1}{k}
\sum_{\ell=0}^{\infty}
(2\ell+1)e^{i\delta_\ell}\sin\delta_\ell
P_\ell(\cos\theta).
$$

$\delta_\ell$ is the phase shift of the $\ell$-th partial wave.

The total cross section is

$$
\sigma_{\mathrm{tot}}
=
\frac{4\pi}{k^2}
\sum_{\ell=0}^{\infty}
(2\ell+1)\sin^2\delta_\ell.
$$

At low energy, the $s$-wave often dominates:

$$
\ell=0.
$$

## S-Matrix

The scattering matrix relates incoming and outgoing asymptotic states:

$$
|{\mathrm{out}}\rangle=\hat S|{\mathrm{in}}\rangle.
$$

Unitarity,

$$
\hat S^\dagger\hat S=\mathbf 1,
$$

expresses probability conservation. In field theory, the $S$-matrix becomes the central object for particle scattering.

## Connections

- [quantum mechanics](./quantum%20mechanics.md)
- [quantum angular momentum and spin](./quantum%20angular%20momentum%20and%20spin.md)
- [quantum field](./quantum%20field.md)
- [advanced hamiltonian mechanics](./advanced%20hamiltonian%20mechanics.md)
