# Mechanics of curved spacetime

[TOC]

## Curved spacetime: differential geometry

### Metric & Metric tensor

A **metric** is a function that defines the distance between two points in a given space.

A **metric tensor** is a mathematical object that encodes the information about the metric of a space. It is a type of tensor that describes how distances are measured, taking into account both the curvature of space and the coordinate system in use. For a space with coordinates $x^1, x^2, \dots, x^n$, the metric tensor $g_{\mu \nu}$ is a symmetric matrix whose components define the inner product of the differential position vectors in the space. In local coordinates, the differential of distance squared (the square of the infinitesimal length) is written as:
$$
ds^2 = g_{\mu \nu} dx^\mu dx^\nu
$$


### Christoffel symbol
$$
\Gamma^{\lambda}_{\mu\nu} = \frac{1}{2} g^{\lambda\sigma} (\partial_{\mu}g_{\nu\sigma} + \partial_{\nu}g_{\mu\sigma} - \partial_{\sigma}g_{\mu\nu})
$$

The Christoffel symbols represent the connection coefficients that describe how the coordinate basis vectors change from point to point in a curved space or spacetime. The Christoffel symbols provide a way to compute how vectors change when they are parallel transported along a curve in a curved space or spacetime. They are not tensors themselves but are used to construct tensors.


### Equations of motion: Geodesic & Geodesic equation
$$
\frac{d^2 x^\mu}{d\lambda^2} + \Gamma^{\mu}_{\alpha\beta} \frac{dx^\alpha}{d\lambda} \frac{dx^\beta}{d\lambda} = 0
$$

Geodesic equation describes free-falling objects follow the straightest possible paths (geodesics) in curved spacetime.

- $x^\mu$ **four-position** of the particle, where $\mu$ is a spacetime index, running over the four spacetime dimensions: $\mu = 0, 1, 2, 3$. In four-dimensional spacetime, these correspond to the time coordinate $x^0$ (typically denoted as $t$) and three spatial coordinates $x^1, x^2, x^3$ (typically denoted as $x, y, z$).
- $\lambda$ **affine parameter** along the geodesic. For a massive particle, this is often taken to be the proper time $\tau$, while for massless particles, such as photons, $\lambda$ might represent an arbitrary parameter like the distance traveled along the path.
- $\frac{d^2 x^\mu}{d\lambda^2}$ represents the **second derivative** of the position with respect to the affine parameter, indicating the acceleration (change in velocity) along the geodesic.
- $\frac{dx^\alpha}{d\lambda}$ is the **first derivative** of the position with respect to the affine parameter $\lambda$, which represents the velocity (the rate of change of position) of the particle along the geodesic.

## Action

### Action of Gravitational field: Einstein-Hilbert action

$$
S=-\frac{1}{c}\int L_m \sqrt{-g} \mathrm d^4x + \frac{c^3}{16\pi G}\int R\sqrt{-g} \mathrm d^4x
$$

- $S_m = -\frac{1}{c}\int L_m \sqrt{-g} d^4x$ matter action.
- $S_g = \frac{c^3}{16\pi G}\int R\sqrt{-g} d^4x $ gravitational action.

### Einstein gravitational field equation

$$
\begin{align*}
G_{\mu\nu} &= \frac{8\pi G}{c^4} T_{\mu\nu}  \\
G_{\mu\nu} &= R_{\mu\nu} - \frac{1}{2} g_{\mu\nu} R  \tag{Einstein Tensor}\\
T_{\mu\nu} &= (\rho + p) u_\mu u_\nu + p g_{\mu\nu}   \tag{Stress-Energy Tensor} 
\end{align*}
$$

- $G_{\mu\nu}$ **Einstein Tensor**: The Einstein tensor encapsulates how spacetime curvature is influenced by the matter and energy content.
- $T_{\mu\nu}$ **Stress-Energy Tensor**: The stress-energy tensor describes the distribution and flow of energy and momentum in spacetime. It includes the energy density, pressure, and the flux of energy and momentum. In simpler terms, it represents the "matter content" of the universe, including everything from ordinary matter to radiation.
- $R_{\mu\nu}$ **Ricci tensor**: represents gravitational effects due to matter and energy.
- $R$ **Ricci scalar**: is the trace of the Ricci tensor, and it is related to the curvature of spacetime.
- $g_{\mu\nu}$ **metric tensor**: which describes the spacetime geometry.
- $\frac{8\pi G}{c^4}$ **Gravitational Constant and Units**: ensures that the units on both sides of the equation are consistent. It also determines the "strength" of the gravitational field in terms of the energy-momentum content of spacetime.
- $G$ **gravitational constant**, which quantifies the strength of gravitational interactions.
- $c$ **speed of light** in a vacuum.