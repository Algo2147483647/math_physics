# Heat Conduction

[TOC]

### Heat Conduction Equation

$$
\frac{\partial T}{\partial t} = \alpha \nabla^2 T
$$

The heat conduction equation describes how temperature changes over time within a material.

- $T$ is the temperature,
- $t$ is time,
- $\alpha = \frac{k}{\rho c_p}$ is the thermal diffusivity (where $k$ is thermal conductivity, $\rho$ is density, and $c_p$ is specific heat capacity),
- $\nabla^2 T$ is the Laplacian operator, which represents the spatial second derivative of the temperature in 3D (for 1D, it simplifies to $\frac{\partial^2 T}{\partial x^2}$).