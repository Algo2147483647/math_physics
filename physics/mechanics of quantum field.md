# Quantum Field

[TOC]



## Principles


### Heisenberg uncertainty principle

$$
\Delta A \Delta B \geq \frac{1}{2} \left| \langle [\hat{A}, \hat{B}] \rangle \right|
$$


The Heisenberg uncertainty describes if two observables $\hat{A}$ and $\hat{B}$ do not commute (i.e., if their commutator is non-zero), there is a fundamental limit to how precisely their values can be known or measured simultaneously. The Heisenberg uncertainty principle reflects the **fundamental nature of quantum mechanics**: the inability to simultaneously measure certain pairs of observables (like position and momentum) with arbitrary precision. This is not a limitation of measurement technology, but rather a consequence of the structure of quantum theory itself.

- $\Delta A$ and $\Delta B$: The standard deviation in the measurements of the observables $\hat{A}$ and $\hat{B}$. The standard deviation $\Delta A$ is defined as $\Delta A = \sqrt{\langle \hat{A}^2 \rangle - \langle \hat{A} \rangle^2}$.
- $[\hat{A}, \hat{B}]$: This is the **commutator** of the operators $\hat{A}$ and $\hat{B}$, defined as $[\hat{A}, \hat{B}] = \hat{A}\hat{B} - \hat{B}\hat{A}$.
- $\langle [\hat{A}, \hat{B}] \rangle$: The expectation value of the commutator $[\hat{A}, \hat{B}]$ in a given quantum state. It is a scalar quantity that indicates the strength of the non-commutativity between the two observables.

Special Cases: The uncertainty principle for position and momentum is

$$
\Delta x \Delta p \geq \frac{\hbar}{2}
$$

### Spin

Spin is an intrinsic form of angular momentum that particles carry with them, akin to angular momentum, but it does not correspond to physical rotation in space. Spin is quantized, meaning that particles can only have specific, discrete values of spin. The possible values of spin for a particle are given in terms of **spin quantum number** $s$, where the **spin** $S$ is related to this quantum number by $S = \hbar \sqrt{s(s + 1)}$. The number of possible spin states of a particle is $2s + 1$.

#### Fermions

**Fermions** are particles with **half-integer spin** (e.g., $s = \frac{1}{2}, \frac{3}{2}, \dots$). Fermions obey the **Pauli exclusion principle**, which states that no two fermions can occupy the same quantum state simultaneously (if they are in the same system). This is directly related to their half-integer spin. Most particles that make up matter are fermions, such as Electrons, Protons, Neutrons, Quarks. Every fermion has a corresponding antiparticle, called an **antifermion** (e.g., the positron is the antiparticle of the electron).

**Fermi-Dirac Distribution**
$$
f(E) = \frac{1}{e^{(E - \mu) / k_B T} + 1}
$$


#### Bosons

**Boson** are particles with **integer spin** (e.g., $s = 0, 1, 2, \dots$). Bosons do not follow the exclusion principle and can occupy the same state. This is why, bosons like photons can form phenomena like **Bose-Einstein condensates**. Many force-carrying particles are bosons, include Photons, Gluons, W and Z bosons, Higgs boson.

**Bose-Einstein Condensate (BEC)**: At low temperatures, a collection of bosons can condense into the same quantum state, forming a new phase of matter known as the **Bose-Einstein condensate**, where a large fraction of the particles occupy the lowest quantum state.

**Bose-Einstein Distribution**
$$
n(\epsilon) = \frac{1}{e^{(\epsilon - \mu) / k_B T} - 1}
$$


## Wave Function

**Wave function** represents the quantum state of a particle or system. It encodes information about the system's position, momentum, or other observable quantities, depending on the context. The wave function is typically complex, so $|\psi(x)|^2$ is used to extract real values representing the probability density. 
$$
\mathbb P = |\psi(x)|^2 \tag{Born Rule}\\
\int|\psi(x)|^2 \mathrm d^3 r= 1
$$

**Born Rule** provides a link between the wave function $\psi(x)$ of a quantum system and the probabilities of different outcomes in measurements. This states that the probability density $\mathbb{P}(x)$ of finding a particle at a particular position $x$ (or in a specific state) is proportional to the **square of the modulus** of the wave function $\psi(x)$.

- $\mathbb{P}(x)$ Probability Density: describes the likelihood of finding the particle at position $x$ in space at a particular time. $\mathbb{P}(x)$ is a real, non-negative quantity.

$$
\langle\hat{A}\rangle=\int \psi^{*}(\mathbf{r}, t) \hat{A} \psi(\mathbf{r}, t) \mathrm d^{3} r  \\
\langle A \rangle = \langle \psi | \hat{A} | \psi \rangle
$$

The expectation value $\langle \hat{A} \rangle$ is the average result of many measurements of the observable $A$ performed on a system described by the wave function $\psi(\mathbf{r}, t)$. It is computed by taking the integral of the wave function and its conjugate, applying the operator $\hat{A}$, and integrating over all space.

### Wave equation (spin 1/2): Dirac equation

$$
(i \hbar \gamma^\mu \partial_\mu - m c) \psi = 0
$$

Dirac equation describes a free, relativistic particle with mass $m$ in 4-dimensional spacetime. This equation is a relativistic generalization of the Schrödinger equation for spin-1/2 particles, consistent with special relativity. It's fundamental in quantum field theory and particle physics.

- $\psi$: The Dirac spinor field representing a particle. It is a function of spacetime coordinates.
- $\gamma^\mu$: The gamma matrices, which are 4x4 matrices that satisfy the **Clifford algebra** relations $\{ \gamma^\mu, \gamma^\nu \} = 2g^{\mu\nu}$, where $\eta^{\mu\nu}$ is the Minkowski metric (typically $\text{diag}(1, -1, -1, -1)$) and $I$ is the identity matrix. These matrices encode information about spacetime symmetries and the spin of the particle.
- $m$: The mass of the particle, which is a scalar constant. It corresponds to the rest mass of the particle.
- $\partial_\mu$: The partial derivative with respect to the spacetime coordinate $x^\mu$, where $\mu = 0, 1, 2, 3$ corresponds to time and the three spatial directions.
- $i$: The imaginary unit, ensuring that the equation remains consistent with quantum mechanics and relativistic invariance.
- $i \gamma^\mu \partial_\mu$ involves the interaction between the spinor field $\psi$ and the spacetime derivative, leading to the particle's dynamics.


#### Wave equation ($v \ll c$): Schrödinger equation

$$
i\hbar \frac{\partial}{\partial t} \psi(\mathbf{r}, t) = \hat{H} \psi(\mathbf{r}, t)
$$
The time-dependent Schrödinger equation, describes how the quantum state evolves over time for a given Hamiltonian. The wave function $\psi(\mathbf{r}, t)$ contains all the information about the system, and the Hamiltonian operator governs the dynamics of the system.

- $\psi(\mathbf{r}, t)$ is the wave function, which encodes the quantum state of a particle or system.
- $\hbar$ is the reduced Planck's constant
- $\hat{H}$ is the Hamiltonian operator, which represents the total energy (kinetic + potential) of the system.

(**Time-independent Schrödinger equation**)

$$
\hat{H} \psi(\mathbf{r}) = E \psi(\mathbf{r})
$$
$$
\nabla^{2} \psi-\frac{8 \pi^{2}}{h^{2}} V \psi \mp \frac{4 \pi i}{h} \frac{\partial \psi}{\partial t}=0
$$

$$
\nabla^2 \psi + \frac{8 \pi^2}{h^2} (E-V) \psi = 0
$$

#### Matrix form: Heisenberg equation

$$
\frac{d\hat{A}}{dt} = \frac{i}{\hbar} [\hat{H}, \hat{A}] + \left( \frac{\partial \hat{A}}{\partial t} \right)
$$

In matrix mechanics, the state of a particle is not described by a wave function, but rather by the action of an operator. Matrix mechanics and the Schrödinger equation are essentially equivalent. They are both expressions of quantum mechanics, but they use different mathematical languages and tools.

## Hydrogen Atom

### Hamiltonian of the hydrogen atom

$$
H = -\frac{\hbar^2}{2m} \nabla^2 - \frac{e^2}{4 \pi \epsilon_0 r}
$$

- $-\frac{\hbar^2}{2m} \nabla^2$: **Kinetic Energy**. This term accounts for the kinetic energy of the particle due to its motion through space.
- $-\frac{e^2}{4 \pi \epsilon_0 r}$: **Potential Energy**. This term represents the Coulomb potential energy between two charged particles, such as the attraction between the negatively charged electron and the positively charged proton in a hydrogen atom. The negative sign indicates that this is an attractive force.

### Wave function solution for the hydrogen atom

$$
\begin{align*}
\psi_{n,l,m_l}(r, \theta, \phi) &= R_{n,l}(r) \cdot \Theta(\theta) \cdot \Phi(\phi)  \\
R_{n,l}(r) &= \sqrt{\frac{2}{a_0}} \cdot \frac{1}{\sqrt{n^2}} \left( \frac{r}{a_0} \right)^l e^{-\frac{r}{n a_0}} L_{n-l-1}^{2l+1} \left( \frac{2r}{n a_0} \right)  \tag{Radial}\\
\Theta(\theta) &= P_l^{m_l}(\cos \theta)  \tag{Angular}  \\
\Phi(\phi) &= \frac{1}{\sqrt{2\pi}} e^{i m_l \phi}  \tag{Azimuthal angle}
\end{align*}
$$

- $n$: principal quantum number (for energy levels). $n = 1, 2, 3, \dots$.
- $l$: angular momentum quantum number (determines the orbital shape).
- $m_l$: magnetic quantum number (determines the orientation of the orbital in space).
- $\psi_{n,l,m_l}(r, \theta, \phi)$: the wavefunction of the system, which depends on three quantum numbers.
- $R_{n,l}(r)$: the radial part of the wavefunction, which describes how the wavefunction depends on the radial distance $r$ from the nucleus.
- $\Theta(\theta)$: the angular part of the wavefunction. $P_l^{m_l}(\cos \theta)$ is the associated Legendre polynomial.
- $\Phi(\phi)$: the angular dependence on the azimuthal angle $\phi$, which is periodic with period $2\pi$. The factor $e^{i m_l \phi}$ reflects the azimuthal dependence of the wavefunction. The quantum number $m_l$ determines how the wavefunction rotates in the $xy$-plane. The factor $\frac{1}{\sqrt{2\pi}}$ is a normalization factor to ensure that the wavefunction is properly normalized over the angular coordinate $\phi$, such that $\int_0^{2\pi} e^{i m_l \phi} e^{-i m_l' \phi} d\phi = 2\pi \delta_{m_l,m_l'}$.

$$
E_n = - \frac{13.6 \, \text{eV}}{n^2}
$$
