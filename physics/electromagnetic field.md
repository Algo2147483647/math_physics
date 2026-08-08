# Electromagnetic Field

[TOC]

## Field

### Four-potential

The scalar potential $\phi$ and vector potential $\mathbf A$ combine into a four-potential $A^\mu$.

$$
A^\mu=\left(\frac{\phi}{c},\mathbf A\right).
$$

$$
\begin{empheq}[left=\empheqlbrace]{align}
\mathbf B &= \nabla\times\mathbf A, \\
\mathbf E &= -\nabla\phi-\frac{\partial\mathbf A}{\partial t}.
\end{empheq}
$$

### Field Tensor

The electromagnetic field tensor $F_{\mu\nu}$ is defined as

$$
F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu.
$$

It is antisymmetric:

$$
F_{\mu\nu}=-F_{\nu\mu}.
$$

One convenient matrix form is

$$
F^{\mu\nu} =
\begin{pmatrix}
0 & -\frac{E_x}{c} & -\frac{E_y}{c} & -\frac{E_z}{c} \\
\frac{E_x}{c} & 0 & -B_z & B_y \\
\frac{E_y}{c} & B_z & 0 & -B_x \\
\frac{E_z}{c} & -B_y & B_x & 0
\end{pmatrix}.
$$

The dual tensor is

$$
\tilde F^{\mu\nu}
=
\frac12\epsilon^{\mu\nu\rho\sigma}F_{\rho\sigma}.
$$

Lorentz invariants. Two scalar invariants can be formed from $F_{\mu\nu}$. These quantities are unchanged under Lorentz transformations.

$$
F_{\mu\nu}F^{\mu\nu}=2\left(B^2-\frac{E^2}{c^2}\right),
$$

$$
F_{\mu\nu}\tilde F^{\mu\nu}
=
-\frac{4}{c}\mathbf E\cdot\mathbf B .
$$

### Current

The four-current is

$$
J^\mu=(c\rho,\mathbf J),
$$

where $\rho$ is charge density and $\mathbf J$ is current density.

## Field Equations: Maxwell Equations

Fundamental Field Equations of Classical Electromagnetism, Maxwell's equations in vacuum are as follows. The first equation contains Gauss's law and the Ampere-Maxwell law. The second equation contains the absence of magnetic monopoles and Faraday's law.

(Covariant form)
$$
\begin{empheq}[left=\empheqlbrace]{align}
\partial_\mu F^{\mu\nu} &=\mu_0 J^\nu,\\
\partial_\lambda F_{\mu\nu} + \partial_\mu F_{\nu\lambda} + \partial_\nu F_{\mu\lambda} &=0.
\end{empheq}
$$

(Vector form)
$$
\begin{empheq}[left=\empheqlbrace]{align}
\nabla\cdot\mathbf E
    &= \frac{\rho}{\varepsilon_0}
    \tag{Gauss's law}\\
\nabla\cdot\mathbf B
    &= 0
    \tag{Gauss's law for magnetism}\\
\nabla\times\mathbf E
    &= -\frac{\partial\mathbf B}{\partial t}
    \tag{Faraday's law of induction}\\
\nabla\times\mathbf B
    &= \mu_0\mathbf J + \mu_0\varepsilon_0\frac{\partial\mathbf E}{\partial t}
    \tag{Ampère-Maxwell law}
\end{empheq}
$$

1. Electric charges are sources of the electric field.
2. No magnetic monopoles.
3. A changing magnetic field induces an electric field.
4. Currents and changing electric fields (displacement currents) generate magnetic fields.

The speed of electromagnetic waves in vacuum is
$$
c=\frac{1}{\sqrt{\mu_0\varepsilon_0}}.
$$

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




$$
K^\mu = q F^{\mu}{}_{\nu}U^\nu
$$


## Electromagnetic Waves