# Statistical Mechanics

[TOC]

## Thermodynamic Quantities

### Entropy


$$
S = k \ln(\Omega)
$$

Entropy is a measure of the number of available microstates.

- $S$: entropy of the system.
- $k$: Boltzmann constant, $1.380649 \times 10^{-23} \, \text{J/K}$.
- $\Omega$: the number of microstates (distinct ways the system can be arranged) corresponding to a particular macrostate (state defined by macroscopic variables such as energy, volume, etc.).


### Temperature

$$
\frac{\mathrm{d}S}{\mathrm{d}U} = \frac{1}{T}
$$

If two systems are each in thermal equilibrium with a third, they are also in thermal equilibrium with each other.
$$
\mathrm{d}U = \mathrm{d}Q - \mathrm{d}W
$$

In a process without transfer of matter, the change in internal energy, $\Delta U$, of a thermodynamic system is equal to the energy gained as heat, $Q$, less the thermodynamic work, $W$, done by the system on its surroundings.
$$
\Delta U = Q-W
$$

As the temperature of a system approaches absolute zero, all processes cease and the entropy of the system approaches a minimum value.

### Maxwell-Boltzmann Distribution

$$
f(v) = \left( \frac{m}{2\pi k_B T} \right)^{3/2} 4\pi v^2 \exp\left(-\frac{mv^2}{2k_B T}\right)
$$

### Boltzmann Distribution

$$
N_i \propto \exp\left(-\frac{E_i}{k_B T}\right)
$$

## Collection of microscopic systems: Ensemble

An ensemble in statistical mechanics is a large collection of virtual copies of a system, considered in different possible states. Each member of the ensemble represents a possible configuration (or microstate) of the system under certain conditions. The introduction of the ensemble is to describe the macroscopic thermodynamic behavior from a microscopic perspective, providing a bridge connecting the macroscopic and microscopic aspects through statistical methods.

### Microcanonical ensemble

Microcanonical ensemble is used for isolated systems, where energy, volume, and particle number are fixed. All microstates have the same energy, and the system is isolated from its surroundings.

- Isolated System: The system does not exchange energy, particles, or volume with the environment. 
- Fixed Energy (E): All microstates in the ensemble have the same energy. 
- Fixed Volume (V): The volume of the system is constant. 
- Fixed Number of Particles (N): The number of particles in the system remains constant. 
- All Microstates are Equally Probable: In the microcanonical ensemble, all possible configurations of the system that satisfy the constraints of energy, volume, and number of particles are considered equally probable.

#### Entropy

$$
S = k \ln(\Omega)
$$

Entropy is a measure of the number of available microstates.

- $S$: entropy of the system.
- $k$: Boltzmann constant, $1.380649 \times 10^{-23} \, \text{J/K}$.
- $\Omega$: the number of microstates (distinct ways the system can be arranged) corresponding to a particular macrostate (state defined by macroscopic variables such as energy, volume, etc.).


Heat does not spontaneously flow from a colder body to a hotter body.
$$
\mathrm{d}S \ge \frac{\mathrm{d}Q}{T}
$$

### Canonical ensemble

Canonical ensemble describes a system in thermal equilibrium with a heat reservoir at a constant temperature $T$. The system can exchange energy with the reservoir but the number of particles and volume remain fixed.

- System in Thermal Contact: The system can exchange energy with a large external reservoir (heat bath), so the energy of the system is not fixed.
- Fixed Temperature (T): The system is maintained at a constant temperature by exchanging energy with the reservoir.
- Fixed Volume (V): The volume of the system is constant.
- Fixed Number of Particles (N): The number of particles in the system is constant.
- Energy Fluctuations: The system can have fluctuating energy, but on average, it is determined by the temperature of the reservoir.

#### Partition function

$$
Z = \sum_i e^{-\beta E_i}
$$

The canonical partition function $Z$ is the sum over all possible microstates of the system, weighted by their respective Boltzmann factors.

- $\beta = \frac{1}{k_B T}$ is the inverse temperature
- $E_i$ is the energy of the $i$-th microstate

#### Free Energy

$$
F = -k_B T \ln Z
$$

The Helmholtz free energy $F$ is a central thermodynamic quantity that determines the equilibrium properties of the system at constant temperature and volume.

#### Average Energy

$$
\langle E \rangle = -\frac{\partial \ln Z}{\partial \beta}
$$

The average energy $\langle E \rangle$ of the system.

#### Entropy

$$
S = -\left( \frac{\partial F}{\partial T} \right)_V = k_B \ln Z + \frac{\langle E \rangle}{T}
$$

The entropy $S$ of the system.

#### Pressure

$$
P = -\left( \frac{\partial F}{\partial V} \right)_T
$$

#### Specific heat

$$
\begin{align*}
C_V &= \frac{\partial \langle E \rangle}{\partial T}\\
&= \frac{\beta^2}{Z} \sum_i e^{-\beta E_i} (E_i - \langle E \rangle)^2
\end{align*}
$$

#### Gibbs Distribution

$$
P(E_i) = \frac{e^{-\frac{E_i}{k_B T}}}{Z}
$$

### Grand canonical ensemble

Grand canonical ensemble is used for systems that can exchange both energy and particles with a reservoir. This is useful for systems where both the number of particles and the energy can fluctuate, such as gases in a container.

- System in Contact with a Reservoir: The system can exchange both energy and particles with a large reservoir or bath. This implies that the system's energy and particle number can fluctuate, but the temperature $T$ and chemical potential $\mu$ of the system are fixed.
- Fixed Temperature (T): The system is maintained at a constant temperature by exchanging heat with the reservoir.
- Fixed Chemical Potential ($\mu$): The chemical potential, which controls the exchange of particles between the system and the reservoir, is fixed.
- Energy and Particle Number Fluctuate: Unlike the microcanonical and canonical ensembles, both the energy and the number of particles of the system are allowed to fluctuate.
- System Size: The number of particles in the system is not fixed and can change, which is different from the canonical ensemble, where the number of particles is constant.

### Isothermal-Isobaric Ensemble

Isothermal-isobaric ensemble describes a system at a constant temperature and pressure. This ensemble is often used in simulations where both temperature and pressure are controlled, such as in a thermodynamic system immersed in a reservoir with both thermal and mechanical exchange.

- Energy: Fluctuates
- Volume: Fluctuates (due to pressure)
- Particle number: Fixed
- Temperature: Fixed
- Pressure: Fixed

### Isoenthalpic-isobaric ensemble

Isoenthalpic-isobaric ensemble is a statistical ensemble that describes a system at constant enthalpy (H) and constant pressure (P). This ensemble is less commonly discussed in traditional statistical mechanics compared to the more well-known canonical or grand canonical ensembles, but it has specific applications, particularly in the study of thermodynamic systems where both enthalpy and pressure are controlled.

### Isothermal-Isovolumetric Ensemble

Isothermal-isovolumetric ensemble describes a system with a fixed temperature and volume, but with the number of particles allowed to fluctuate. It is useful for studying systems like chemical reactions in a closed volume, where the volume is held constant but particles can be added or removed.

- Energy: Fluctuates
- Volume: Fixed
- Particle number: Fluctuates
- Temperature: Fixed


## Ideal Gas

$$
PV=nRT
$$

- $P$: pressure
- $V$: volume
- $T$: temperature
- $n$: the amount of substance
- $R$: the ideal gas constant.