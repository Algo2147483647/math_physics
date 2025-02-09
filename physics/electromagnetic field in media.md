# Electromagnetic field in media

[TOC]

## Principles

### Polarization: Induce dipoles

$$
\begin{align*}
\boldsymbol P &= \frac{\sum \boldsymbol p}{V}  \tag{polarization intensity}\\
\boldsymbol D &= \epsilon_0 \boldsymbol E + \boldsymbol P  \tag{electric displacement vector}
\end{align*}
$$

Under the action of the electric field, the positive and negative charge centers of the molecules or atoms in the dielectric are relatively displaced to form electric dipoles. This phenomenon is called polarization of the medium. Polarization intensity $\boldsymbol P$ is a physical quantity used to describe the degree and direction of polarization of a dielectric in an electric field, defined as the vector sum of the electric dipole moments of all molecules within a unit volume of the dielectric, represents the overall polarization state of the dielectric under the action of an external electric field.
$$
\begin{align*}
\rho_p &= -\nabla\cdot\boldsymbol{P}  \tag{volume density of polarization charge}\\
\sigma_p &=\boldsymbol{P}\cdot\boldsymbol{n} \tag{surface density of polarization charge}
\end{align*}
$$
Volume Density of Polarization Charge represents the volume distribution of polarization charges within the medium. At the interface between two media, the surface density of polarization charge is $\sigma_p=\boldsymbol{P}\cdot\boldsymbol{n}$.

- $\boldsymbol{P}$ represents the polarization intensity vector
- $\sum \boldsymbol{p}$ is the vector sum of the electric dipole moments of all molecules within the volume $V$. 
- $\chi_e$ is the electric susceptibility
- $\epsilon_0$ is the permittivity of free space
- $\epsilon$ is the permittivity of the medium.
- $\boldsymbol{E}$ is the electric field strength.
- $\boldsymbol{n}$ is the unit normal vector of the interface, pointing from medium 1 to medium 2.

#### Polarization in isotropic linear dielectrics

$$
\begin{align*}
\boldsymbol{P} &=\epsilon_0\chi_e\boldsymbol{E}  \\
\boldsymbol D &= \epsilon \boldsymbol E\\
\epsilon &= \epsilon_0 (1 + \chi_e)
\end{align*}
$$

Isotropic linear dielectrics refer to a class of dielectric materials that have the same dielectric properties in all directions and exhibit a linear relationship between $\boldsymbol D, \boldsymbol  P, \boldsymbol E$.


### Magnetization

$$
\begin{align*}
\boldsymbol{M} &= \frac{\sum \boldsymbol{m}}{V}    \tag{magnetization intensity}\\
\boldsymbol{B} &= \mu_0(\boldsymbol{H}+\boldsymbol{M})  \tag{magnetic induction intensity}
\end{align*}
$$

Under the action of a magnetic field, the molecular magnetic moments or atomic magnetic moments in the magnetic medium will tend to align along the direction of the magnetic field, forming macroscopic magnetic dipoles, causing the medium to be magnetized.  Magnetization intensity $\boldsymbol M$ is a physical quantity that characterizes the degree and direction of magnetization of a magnetic medium in a magnetic field, defined as the vector sum of the magnetic moments of all molecules within a unit volume of the magnetic medium, reflects the overall magnetic moment distribution of the magnetic medium under the action of an external magnetic field.
$$
\begin{align*}
\boldsymbol{J}_m &= \nabla\times\boldsymbol{M}  \tag{volume density of magnetization current}\\
\boldsymbol{K}_m &=\boldsymbol{M}\times\boldsymbol{n}  \tag{surface density of magnetization current}\\
\end{align*}
$$
Volume Density of Magnetization Current reflects the equivalent current distribution generated inside the medium during the magnetization process. On the surface of the medium, the surface density of magnetization current.

- $\boldsymbol{M}$ is the magnetization intensity vector
- $\sum \boldsymbol{m}$ is the vector sum of the magnetic moments of all molecules within the volume $V$
- $\chi_m$ is the magnetic susceptibility
- $\boldsymbol{H}$ is the magnetic field strength.
- $\mu$ is the permeability of the medium
- $\mu_0$ is the permeability of free space.

#### Magnetized in isotropic linear dielectrics

$$
\begin{align*}
\boldsymbol{M}&=\chi_m\boldsymbol{H}\\
\boldsymbol{B}&=\mu\boldsymbol{H}\\
\mu&=\mu_0(1 + \chi_m)
\end{align*}
$$

Isotropic linear dielectrics refer to a class of dielectric materials that have the same dielectric properties in all directions and exhibit a linear relationship between $\boldsymbol M, \boldsymbol B, \boldsymbol H$.

### Maxwell's equations in media

$$
\begin{align*}
\nabla \cdot \boldsymbol D &= \rho_f  \\
\nabla \cdot \boldsymbol B &= 0  \\
\nabla \times \boldsymbol E &= -\frac{\partial \boldsymbol B}{\partial t}  \\
\nabla \times \boldsymbol H &= J_f + \frac{\partial \boldsymbol D}{\partial t}
\end{align*}
$$

Maxwell's equations in media describe the behavior of electromagnetic fields in the presence of matter.

#### Boundary conditions

$$
\begin{align*}
D_1^{\perp} - D_2^{\perp} &= \sigma_f \\
B_1^{\perp} - B_2^{\perp} &= 0  \\
E_1^{\parallel} - E_2^{\parallel} &= 0 \\
H_1^{\parallel} - H_2^{\parallel} &= \boldsymbol K_f \times \hat n
\end{align*}
$$

The boundary conditions can be deduced form the Maxwell's equations.

## Conductors

## Insulators

