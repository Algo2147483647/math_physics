# Mechanics of fluid

[TOC]

## Basic physical quantities

### Density & Pressure & Viscosity & Surface tension

- Density $\rho$: Mass per unit volume of a fluid.
- Pressure $P$: Force exerted per unit area by the fluid on a surface.
- Viscosity: A measure of a fluid's resistance to flow or deformation.
- Surface Tension: The force acting along the surface of a liquid due to cohesive forces among molecules.

## Action

### Action of fluid

$$
S = \int \left( \frac{1}{2} \rho \mathbf{v}^2 - p + \mu \left( \nabla \mathbf{v} + (\nabla \mathbf{v})^T \right) : \left( \nabla \mathbf{v} + (\nabla \mathbf{v})^T \right) \right) d^3x \, dt
$$

- $\rho$: the density of the fluid.
- $\mathbf{v}$: the velocity field.
- $p$: the pressure.
- $\mu$: the dynamic viscosity of the fluid.
- $\nabla \mathbf{v}$: the gradient of the velocity field.
- $\ :\ $: the double contraction of two tensors (in this case, the gradients of the velocity).
- $\frac{1}{2} \rho \mathbf{v}^2$ Kinetic energy density: Describes the motion of the fluid particles.
- $-p$ Pressure (or potential) energy density: Describes the internal energy of the fluid related to its compressibility.
- $\mu \left( \nabla \mathbf{v} + (\nabla \mathbf{v})^T \right) : \left( \nabla \mathbf{v} + (\nabla \mathbf{v})^T \right)$ Viscous dissipation: Describes the internal friction and the energy loss due to viscosity.

### Equation of motion: Navier Stokes Equations

$$
ρ \left(\frac{∂\boldsymbol v}{∂t} + (\boldsymbol v · ∇) \boldsymbol v \right) =  - ∇ P  + ρ \boldsymbol f + η ∇^2 \boldsymbol v + \left(ζ + \frac{η}{3} \right) ∇ (∇ · \boldsymbol v)
$$

(**component formula of Navier Stokes Equations**)
$$
ρ \left(\frac{∂ v_x}{∂t} + \sum_{i=1}^{\dim} v_i \frac{∂ v_d}{∂x_i}\right) =  - \frac{∂ P}{∂d}  + ρ  f_d + η \sum_{i=1}^{\dim} \left(\frac{∂^2 v_d}{∂ x_i^2}\right) + \left(ζ + \frac{η}{3} \right) \frac{∂\left(\sum\limits_{i=1}^{\dim} \frac{∂ v_d}{∂x_i}\right)}{∂x_i}
$$

#### Incompressible fluid $∇ ·\boldsymbol v ≡ 0$
For incompressible fluid, we have $∇ ·\boldsymbol v ≡ 0$ and
$$
\frac{∂\boldsymbol v}{∂t} + (\boldsymbol v·∇) \boldsymbol v = -\frac{1}{ρ} ∇ P  + \boldsymbol f + \frac{η}{ρ} ∇^2 \boldsymbol v  \tag{$∇ ·\boldsymbol v ≡ 0$}
$$
- $η$: Viscosity
- $ρ$: Density
- Pressure: $∇ ·∇ P = ∇ ·v·ρ/ dt$

#### Ideal fluid $∇^2 \boldsymbol v ≡ 0$: Eular equation

Ideal fluid is incompressible and has no viscosity, so there is no tangential force
$$
\begin{align*}
  \frac{∂ \boldsymbol v}{∂ t} + (\boldsymbol v · ∇)\boldsymbol v &= - \frac{1}{ρ} ∇ P + \boldsymbol f\tag{$∇^2 \boldsymbol v ≡ 0$}
\end{align*}
$$

#### Steady fluid $\frac{∂ \boldsymbol v}{∂ t} = 0$: Bernoulli equation
Steady fluid is a fluid in which the velocity of any point in the fluid region does not change with time.
$$
\begin{align*}
\frac{v^2}{2} + w &= const.  \\
\frac{v^2}{2} + w + g z &= const.  \tag{In gravity field}
\end{align*}
$$

#### Static fluid $v = 0$: Pascal's law

$$
\begin{align*}
\nabla P &= \rho \boldsymbol f  \\
v & = 0
\end{align*}
$$



### Continuity equation

$$
∇ · (ρ \boldsymbol v) + \frac{∂ ρ}{∂ t} = 0
$$
质量流流出速率 = 流体密度减少速率.
- 质量流密度 $\boldsymbol j = ρ \boldsymbol v$

### Equation of motion

$$
\begin{align*}
  -\oint p d \boldsymbol f &= -\int ∇ p\ dV  \\
  ρ \frac{d \boldsymbol v}{t} &= -∇ p
\end{align*}
$$



$- ∇ p$: 单位体积流体上的作用力.

## Appendix

### Proof of Eular Ideal fluid equation

$$
\begin{align*}
ρ \frac{\mathrm d \boldsymbol v}{\mathrm d t} &=  - ∇ p + ρ \boldsymbol g  \tag{微元运动方程}  \\
\mathrm d \boldsymbol v &= \frac{∂ \boldsymbol v}{∂t} \mathrm d t + (\mathrm d \boldsymbol r · ∇) \boldsymbol v    \tag{全导数}  \\
\Rightarrow\quad \frac{\mathrm d \boldsymbol v}{\mathrm d t} &= \frac{∂ \boldsymbol v}{∂t} + (\boldsymbol v · ∇) \boldsymbol v  \tag{除以$\mathrm d t$}  \\
\Rightarrow\quad \frac{∂ \boldsymbol v}{∂t} + (\boldsymbol v · ∇) \boldsymbol v &= - \frac{1}{ρ} ∇ p + \boldsymbol g  \tag{代入}
\end{align*}
$$

### Proof of Continuity equation
Mass Conservation. The outflow mass of the region body = the outflow mass of the region closed surface.
$$
\begin{align*}
  \oint ρ \boldsymbol v · d \boldsymbol f &= -\frac{∂}{∂ t}\int ρ dV   \\
  \Rightarrow\quad  \int ∇ · (ρ \boldsymbol v) dV  &= -\frac{∂}{∂ t}\int ρ dV  \\
  \Rightarrow\quad  \int \left(∇ · (ρ \boldsymbol v) + \frac{∂ ρ}{∂ t} \right) dV  &= 0  
\end{align*}
$$
