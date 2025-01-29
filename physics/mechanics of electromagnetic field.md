# Electromagnetic Field

[TOC]

## Principles

### Electromagnetic four-potential

$$
A^i = \left(\begin{matrix}\varphi \\ \boldsymbol A \end{matrix}\right)
$$

The electromagnetic field is described by the electromagnetic four-potential $A^i$, it combines the electric potential $\varphi$ and magnetic vector potential $\boldsymbol A$ into a single four-vector. The electromagnetic four-potential are related to the observable quantities $\boldsymbol E, \boldsymbol B$ between the electric field and the magnetic field as follows:
$$
\begin{align*}
\mathbf{B} &= \nabla \times \mathbf{A}\\
\mathbf{E} &= -\nabla \varphi - \frac{\partial \mathbf{A}}{\partial t}
\end{align*}
$$

### Electromagnetic field tensor

$$
F^{ik} = \frac{\partial A_k}{\partial x^i}-\frac{\partial A_i}{\partial x^k}
$$

$$
F_{\mu\nu} =
\begin{pmatrix}
0 & -E_x & -E_y & -E_z \\
E_x & 0 & B_z & -B_y \\
E_y & -B_z & 0 & B_x \\
E_z & B_y & -B_x & 0
\end{pmatrix}
$$

The field tensor provides a unified description of the electric and magnetic fields. The components of the tensor are antisymmetric, meaning $F_{\mu\nu} = -F_{\nu\mu}$, so the diagonal elements are always zero.

### Reference frame transformation

$$
E= E+ \frac{1}{c}H'\times V\\
H = H' - \frac{1}{c}E'\times V\\
$$

## Action

###  Action of Electromagnetic field

$$
S = \sum\int mc \mathrm ds - \sum \int \frac{e}{c} A_k \mathrm dx^k - \frac{1}{16 \pi c} \int F_{ik}F^{ik} \mathrm d \Omega
$$

This action combines the dynamics of charged particles interacting with the electromagnetic field and the field itself.

- $\sum\int mc \mathrm ds$: The total action for a system of particles with mass $m$.
- $- \sum \int \frac{e}{c} A_k \mathrm dx^k$: interaction of the charged particles with the electromagnetic field.
- $- \frac{1}{16 \pi c} \int F_{ik}F^{ik} \mathrm d \Omega$: The action of electromagnetic field itself.


### Equation of motion: Lorentz force law

$$
m c \frac{\mathrm{d} u^i}{\mathrm{d} s} = \frac{e}{c} F^{ik} u_k
$$

The **Lorentz force law** describing the motion of a charged particle in an electromagnetic field. The electromagnetic field tensor $F^{ik}$ acts on the four-dimensional velocity $u_k$ of the particle, producing acceleration (i.e., the rate of change of the four-dimensional velocity). The result, multiplied by the charge $e$ and the speed of light $c$, is equal to the mass $m$ of the particle and the speed of light $c$ multiplied by the rate of change of the four-dimensional velocity.

(**Vector form of Lorentz force law**)
$$
\frac{\mathrm{d} \boldsymbol p}{\mathrm{d} t} = e \boldsymbol E + \frac{e}{c} \boldsymbol v \times \boldsymbol H \\
\frac{\mathrm{d} \mathrm E_{kin}}{\mathrm{d} t} = e \boldsymbol E \cdot \boldsymbol v
$$


### Maxwell’s equations

$$
\partial _\mu F^{\mu\nu}=\frac{4\pi}{c}J^{\nu}\\
\partial _\mu \bar F^{\mu\nu}=0
$$

The first equation that relates the divergence of the field strength tensor to the current density. The change in the electromagnetic field is caused by the presence of charges and currents. 

The second equation expresses the **absence of magnetic monopoles**. It states that the divergence of the dual field strength tensor is zero, meaning that there are no isolated sources of the magnetic field, which is a key assumption in classical electromagnetism

(**Vector form of Maxwell’s equations**)
$$
\begin{align*}
\nabla \cdot \mathbf{E} &= \frac{\rho}{\varepsilon_0}\\
\nabla \cdot \mathbf{B} &= 0 \\
\nabla \times \mathbf{E} + \frac{\partial \mathbf{B}}{\partial t}&= 0\\
\nabla \times \mathbf{B} - \mu_0 \varepsilon_0 \frac{\partial \mathbf{E}}{\partial t}&=  \mu_0 \mathbf{J} 
\end{align*}
$$

- **Gauss's law for electricity**: Electric fields are produced by electric charges.
- **Gauss's law for magnetism**: There are no magnetic monopoles; magnetic fields always form closed loops.
- **Faraday's law of induction**: A changing magnetic field induces an electric field.
- **Ampère's law (with Maxwell's correction)**: Electric currents and changing electric fields generate magnetic fields.

#### Wave Equation: d'Alembert's equations

$$
\begin{align*}
\nabla^2 \mathbf{A} - \frac{1}{c^2} \frac{\partial \mathbf{A}}{\partial t^2} &= - \mu_0 \mathbf{J} \\
\nabla^2 \Phi - \frac{1}{c^2} \frac{\partial^2 \Phi}{\partial t^2} &= -\frac{\rho}{\varepsilon_0}
\end{align*}
$$

d'Alembert's equation describes the propagation of electromagnetic waves. 

#### Speed of electromagnetic waves in vacuum: Speed of Light

$$
\begin{align*}
c &= \frac{1}{\sqrt{\mu_0 \epsilon_0}} \\
&\approx \frac{1}{\sqrt{(4\pi \times 10^{-7} \, \text{N/A}^2)(8.854 \times 10^{-12} \, \text{F/m})}} \\
&\approx 2.99792458 \times 10^8 \, \text{m/s}
\end{align*}
$$




## Appendix

### Proof of Lorentz force law
Action of a charged particle moving in electromagnetic field: The action of a charged particle moving in an electromagnetic field, 描述粒子的自由运动 + 粒子与电磁场的相互作用.
$$
S = \int_a^b (-mc \mathrm{d} s - \frac{e}{c}A_i\mathrm{d}x^i)
$$

**Lagrangian**
$$
\begin{align*}
L &= -mc^2\sqrt{1 - \frac{v^2}{c^2}} + \frac{e}{c}A\cdot v - e \varphi\\
P &= \frac{mv}{\sqrt{1 - \frac{v^2}{c^2}}}+\frac{e}{c}A\\
H &= \sqrt{m^2c^4 + c^2 (P-\frac{e}{c}A)^2}+e\varphi
\end{align*}
$$

最小作用量原理, 
$$
\begin{align*}
δ S &= 0\\
δ\int_a^b (-mc \mathrm{d} s - \frac{e}{c}A_i\mathrm{d}x^i) &= 0\\
δ\int_a^b (mc \sqrt{\mathrm{d} x_i\mathrm{d} x^i} + \frac{e}{c}A_i\mathrm{d}x^i) &= 0   \tag{$\mathrm{d} s = \sqrt{\mathrm{d} x_i\mathrm{d} x^i}$}\\
\int_a^b (mc \frac{\mathrm{d} x_i\mathrm{d} δ x^i}{\mathrm{d} s} + \frac{e}{c}(A_iδ\mathrm{d}x^i + δA_i\mathrm{d}x^i)) &= 0\\
\int_a^b \left(mc u_i \mathrm{d} δ x^i + \frac{e}{c}(A_iδ\mathrm{d}x^i + δA_i\mathrm{d}x^i)\right) &= 0 \tag{$u_i = \frac{\mathrm{d} x_i}{\mathrm{d} s}$}\\
(mc u_i+\frac{e}{c}A_i)δ x^i - \int \left(mc \mathrm{d} u_i  δ x^i + \frac{e}{c}(\mathrm{d}A_iδx^i -  δA_i\mathrm{d}x^i) \right) &= 0 \tag{$\int u \mathrm{d} v = uv - \int v \mathrm{d} u$}\\
\end{align*}
$$

因为$(mc u_i + \frac{e}{c}A_i)  δ x^i = 0$
$$
δA_i = \frac{\partial A_i}{\partial x^k} δ x^k\\
\mathrm{d}A_i = \frac{\partial A_i}{\partial x^k} \mathrm{d}x^k\\
$$

$$
\begin{align*}
\Rightarrow\quad \int \left(mc \mathrm{d} u_i - \frac{e}{c}\mathrm{d}x^k(\frac{\partial A_k}{\partial x^i}-\frac{\partial A_i}{\partial x^k}) \right)δ x^i &= 0 \\
\end{align*}
$$

因为$δ x^i$ 任意, 所以被积函数为零
$$
\begin{align*}
\Rightarrow\quad mc \mathrm{d} u_i&=\frac{e}{c}\mathrm{d}x^k(\frac{\partial A_k}{\partial x^i}-\frac{\partial A_i}{\partial x^k}) \\
mc \mathrm{d} u_i&=\frac{e}{c}\mathrm{d}x^kF_{ik} \tag{$F_{ik} = (\frac{\partial A_k}{\partial x^i}-\frac{\partial A_i}{\partial x^k})$}\\
mc \mathrm{d} \frac{\mathrm{d}u_i}{\mathrm{d}s}&=\frac{e}{c}u_kF_{ik}\\
\end{align*}
$$
Q.E.D.

