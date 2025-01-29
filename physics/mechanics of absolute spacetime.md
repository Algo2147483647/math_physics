# Mechanics of absolute spacetime

[TOC]

## Absolute spacetime

### Absolute space & time

Absolute spacetime refers to the idea that space and time exist as independent, unchanging entities, separate from the matter and events that occur within them.

- **Space** is a fixed, uniform, infinite, three-dimensional backdrop where objects are located and distances are measured.
- **Time** is a continuous, one-dimensional flow that ticks the same for everyone, regardless of how they move.

### Coordinate transformation: Galileo's principle of relativity

Galileo's Principle of Relativity asserts the laws of physics are the same in all inertial reference frames. An **inertial reference frame** is one that is not accelerating, meaning it moves at a constant velocity (or is at rest). The transformation relationship between different inertial reference frames:

$$
\begin{align*}
t &= t' \tag{Time invariance}\\
\boldsymbol r &= \boldsymbol r' + \boldsymbol Vt  \tag{Position transformation}\\
\boldsymbol v &= \boldsymbol v' + \boldsymbol V  \tag{Velocity transformation}\\
\end{align*}
$$

- **Time invariance**: Time is absolute and does not change between inertial frames in Galilean relativity.
- **Position transformation**: the position in the original frame $\boldsymbol r$ is related to the position in the moving frame $\boldsymbol r'$ by adding the distance the moving frame has traveled during time $t$, which is $\boldsymbol V t$.
- **Velocity transformation**: the velocity of an object in the original frame $\boldsymbol v$ is the sum of its velocity in the moving frame $\boldsymbol v'$ and the velocity of the moving frame itself $\boldsymbol V$.

#### Coordinate transformation between non-inertial coordinate systems: Fictitious Force

Non-inertial reference frames accelerate relative to an inertial reference frame. In these systems, Newton's laws of motion do **not** hold without including fictitious forces. Transformations must account for relative acceleration and rotational effects. Let:
- $S$: Inertial frame (stationary or moving with constant velocity).
- $S'$: Non-inertial frame, accelerating or rotating relative to $S$.

The general transformation depends on **relative motion**:

- Translational acceleration ($\vec{a}_\text{rel}$).
- Rotational motion (angular velocity $\vec{\omega}$ and angular acceleration $\vec{\alpha}$).
$$
\begin{align*}
\vec{r} &= \vec{r}' + \vec{R}(t)\\
\vec{v} &= \vec{v}' + \vec{V}(t) + \vec{\omega} \times \vec{r}' \\
\vec{a} &= \vec{a}' + \vec{A}(t) + 2 \vec{\omega} \times \vec{v}' + \vec{\omega} \times (\vec{\omega} \times \vec{r}') + \vec{\alpha} \times \vec{r}'
\end{align*}
$$

- $\vec{R}(t)$ is the time-dependent displacement of $S'$ relative to $S$.
- $\vec{v}'$: Velocity in the non-inertial frame.
- $\vec{V}(t)$: Velocity of $S'$ relative to $S$.
- $\vec{\omega} \times \vec{r}'$: Contribution due to rotation 
- $\vec{a}$: Acceleration in the inertial frame.
- $\vec{a}'$: Acceleration in the non-inertial frame.
- $\vec{A}(t)$: Acceleration of $S'$ relative to $S$.
- $2\vec{\omega} \times \vec{v}'$: **Coriolis force** term.
- $\vec{\omega} \times (\vec{\omega} \times \vec{r}')$: **Centrifugal force** term.
- $\vec{\alpha} \times \vec{r}'$: Contribution due to angular acceleration.

| **Fictitious Force**    | **Expression**                     | **Cause**                  |
|--------------------------|------------------------------------|----------------------------|
| Centrifugal Force        | $\vec{F}_\text{cent} = -m (\vec{\omega} \times (\vec{\omega} \times \vec{r}))$ | Rotation of $S'$       |
| Coriolis Force           | $\vec{F}_\text{cor} = -2m (\vec{\omega} \times \vec{v}')$ | Relative velocity in $S'$ |
| Linear Acceleration Force| $\vec{F}_\text{lin} = -m \vec{A}(t)$  | Translational acceleration |
| Angular Acceleration Force| $\vec{F}_\text{ang} = -m (\vec{\alpha} \times \vec{r}')$ | Angular acceleration       |

## Action

### Action of particles in absolute spacetime

$$
\begin{align*}
S = \int (T - V) \mathrm dt  \\
S = \int \left(\frac{m v^2}{2} - U(\boldsymbol r, t)\right) \mathrm dt  \tag{particle}\\
S = \int \sum\frac{m_i v_i^2}{2} \mathrm dt  \tag{Free particle system}
\end{align*}
$$

### Equations of motion

$$
\boldsymbol F = \frac{\mathrm{d} \boldsymbol P}{\mathrm{d}t} = m \frac{\mathrm{d} \boldsymbol v}{\mathrm{d}t}\\
\boldsymbol F = - \frac{\partial U(\boldsymbol r, t)}{\partial \boldsymbol r}
$$

An isolated particle remains stationary or moves in a uniform straight line without the action of an external force. For a particle with momentum $\boldsymbol P$, the rate of change of its momentum with time is proportional to the external force on the particle and has the same direction as the external force. 

The action and reaction forces between two interacting particles are always equal in magnitude, opposite in direction, and act on the same straight line.
$$
\boldsymbol F_{12} = - \boldsymbol F_{21}
$$

### Conserved quantity: Momentum, Angular momentum, Energy

$$
\begin{align*}
\boldsymbol P &= m \frac{\mathrm{d} \boldsymbol r}{\mathrm{d}t}  \tag{Momentum }\\
\boldsymbol L &= \boldsymbol r \times \boldsymbol P  \tag{Angular Momentum}\\
E &= \frac{1}{2} mv^2  \tag{Kinetic Energy}\\
\end{align*}
$$

- **Momentum** is a vector quantity that describes the motion of an object.
- **Angular momentum** is a vector quantity that describes the rotational motion of an object about a point or an axis.
- **Kinetic Energy**: The energy associated with an object's motion.

### Rigid body

#### Action of a rigid body

The motion of a rigid body is divided into two parts: translational motion and rotational motion
$$
S = \int_{t_1}^{t_2} \left( \frac{1}{2} m |\dot{\mathbf{r}}|^2 + \frac{1}{2} \dot{\boldsymbol{\boldsymbol{\theta}}}^\mathrm{T} \mathbf{I} \dot{\boldsymbol{\boldsymbol{\theta}}} - V(\mathbf{r}, \boldsymbol{\theta}) \right) \mathrm{d}t
$$

- **Translational Kinetic Energy** $\frac{1}{2} m |\dot{\mathbf{r}}|^2$: This term accounts for the motion of the center of mass.
- **Rotational Kinetic Energy** $\frac{1}{2} \dot{\boldsymbol{\boldsymbol{\theta}}}^\mathrm{T} \mathbf{I} \dot{\boldsymbol{\boldsymbol{\theta}}}$: This term accounts for the body's rotation about its center of mass.
- **Potential Energy** $V(\mathbf{r}, \boldsymbol{\theta})$: This term incorporates external forces such as gravity or fields acting on the rigid body.

#### Angular momentum: Inertia tensor

$$
\mathbf{L} = \mathbf{I} \boldsymbol{\omega} \\
\mathbf{I} =
\begin{bmatrix}
I_{xx} & -I_{xy} & -I_{xz} \\
-I_{xy} & I_{yy} & -I_{yz} \\
-I_{xz} & -I_{yz} & I_{zz}
\end{bmatrix}
$$

**Inertia tensor**: The inertia tensor $\mathbf{I}$ is a symmetric $3 \times 3$ matrix that relates the angular velocity $\boldsymbol{\omega}$ to the angular momentum $\mathbf{L}$. In a body-fixed coordinate system, the elements of the inertia tensor $\mathbf{I}$ are:
$$
I_{ij} = \int_V \rho(\mathbf{r}) \left( \delta_{ij} |\mathbf{r}|^2 - r_i r_j \right) \, dV  \\
$$

- $\rho(\mathbf{r})$: Mass density at point $\mathbf{r}$.
- $\mathbf{r} = (x, y, z)$: Position vector relative to the center of mass.
- $\delta_{ij}$: Kronecker delta ($1$ if $i = j$, otherwise $0$).
- $I_{ij}$: Element of the inertia tensor.
- $V$: Volume of the rigid body.
- $I_{xx} = \int_V \rho(y^2 + z^2) \, dV$: Moment of inertia about the $x$-axis. Similar definitions apply for $I_{xx}$ and $I_{yy}$.
- $I_{xy} = \int_V \rho(xy) \, dV$: Product of inertia for $x$ and $y$. Similar definitions apply for $I_{xz}$ and $I_{yz}$.

The inertia tensor can be diagonalized in a coordinate system aligned with the principal axes of rotation. If the rotation axis does not pass through the center of mass, the parallel axis theorem allows the calculation of the moment of inertia of a body about any axis, given its moment of inertia about a parallel axis passing through its center of mass.
$$
\begin{align*}
\mathbf{I} &=
\begin{bmatrix}
I_1 & 0 & 0 \\
0 & I_2 & 0 \\
0 & 0 & I_3
\end{bmatrix}  \\
I' &= I_{cm} + m d^2  \tag{parallel axis theorem}
\end{align*}
$$

- $I_1, I_2, I_3$: the principal moments of inertia
- $I_{cm}$: Moment of inertia about the axis through the center of mass.
- $d$: the distance between the center of mass and the new axis.

#### Equations of motion for a rigid body

$$
\begin{align*}
m \ddot{\mathbf{r}} &= - \nabla V(\mathbf{r})  \tag{Translational Motion}\\
\frac{d}{dt} \left( \mathbf{I} \boldsymbol{\omega} \right) + \boldsymbol{\omega} \times \left( \mathbf{I} \boldsymbol{\omega} \right) &= - \frac{\partial V}{\partial \boldsymbol{\theta}}  \tag{Rotational Motion}
\end{align*}
$$

- $\ddot{\mathbf{r}}$ is the acceleration vector (second time derivative of position).
- $\nabla V(\mathbf{r})$ is the gradient of the potential energy $V$ with respect to position, which represents the force acting on the particle due to the potential field.
- $\frac{d}{dt} \left( \mathbf{I} \boldsymbol{\omega} \right)$ represents the rate of change of angular momentum.
- $\boldsymbol{\omega} \times \left( \mathbf{I} \boldsymbol{\omega} \right)$ is the torque due to the rotational motion of the body.
- $\frac{\partial V}{\partial \boldsymbol{\theta}}$ is the gradient of the potential energy $V$ with respect to the generalized rotational coordinates $\boldsymbol{\theta}$, which represents the torque acting on the rigid body due to the potential.

## Gravitation

$$
\boldsymbol F = \frac{G m_1m_2}{r^2}\hat{\boldsymbol r} \\
U = \frac{G m_1m_2}{r}
$$

- $G$: Gravitational constant. $G = (6.67 \pm0.07) \times 10^{-11} \mathrm{m^3kg^{-1}s^{-2}}$

### Two-body gravitational system

When one particle is stationary as the origin, the trajectory equation of the other particle is as follows. Among them, the polar coordinate equation of the conic section, the $e$ eccentricity, and the $p$ semi-diameter. The two-body scenario can be abstracted as motion around the equivalent center of mass in an inertial system.
$$
\begin{align*}
  r &= \frac{p}{1 - e \sin(θ + θ_0)}  \\
  p &= \frac{L^2}{G M m^2}  \\
  e &= \sqrt{1 + 2 \frac{E}{m} \left(\frac{L}{G M m}\right)^2}
\end{align*}
$$

### Restricted three-body gravitational system
两个大质量天体 $M_1, M_2$, 选择以质心为原点且使其相对静止的旋转参考系, 则势能有, 
$$
\begin{align*}
U &= -\frac{GM_1}{r_1} -\frac{GM_1}{r_2} - \frac{1}{2} \omega^2 r^2\\
\omega &= \sqrt{\frac{G(M_1+M_2)}{d^3}}\\
r_1 &= \sqrt{(x + \frac{M_2}{M_1+M_2}d)^2 + y^2}\\
r_2 &= \sqrt{(x - \frac{M_1}{M_1+M_2}d)^2 + y^2}
\end{align*}
$$

#### Lagrange Points

Lagrange points are points of equilibrium for small-mass objects under the gravitational influence of two massive orbiting bodies. Mathematically, this involves the solution of the restricted three-body problem. 拉格朗日点的条件
$$
\nabla U = 0
$$

$$
\begin{align*}
L_1 &= \left(-\frac{M_2}{M_1 + M_2}d , 0\right)\\
L_2 &= \left(+\frac{M_1}{M_1 + M_2}d , 0\right)\\
L_3 &= \left(-\frac{M_1}{M_1 + M_2}d , 0\right)\\
L_4 &= \left(\frac{M_1 - M_2}{M_1 + M_2}d, +\frac{\sqrt{3}}{2} d\right)\\
L_5 &= \left(\frac{M_1 - M_2}{M_1 + M_2}d, -\frac{\sqrt{3}}{2} d\right)\\
\end{align*}
$$

## Appendix

### Proof of Two-body gravitational system

建立方程组。其中$L, E$是常量. $r, θ, v_r, v_θ$是变量. 3个方程4个变量.求出 $r-θ$ 关系式.
$$
\begin{align*}
L &= m r v_θ  \tag{角动量守恒}  \\
E &= \frac{1}{2} m (v_r^2 + v_θ^2) - G \frac{M m}{r}  \tag{能量守恒}  \\
\frac{\mathrm d r}{\mathrm d θ} &= r \frac{v_r}{v_θ}  \tag{$v_r = \frac{\mathrm d r}{\mathrm d t}, v_θ = r \frac{\mathrm d θ}{\mathrm d t}$}
\end{align*}
$$
解方程组
$$
\begin{align*}
v_θ &= \frac{L}{m r}  \tag{独立$v_θ$}  \\
v_r &= \sqrt{\frac{2 E}{m} + \frac{2 G M}{r} -\left(\frac{L}{m}\right)^2 \frac{1}{r^2}}  \tag{独立$v_r$}\\
\Rightarrow\quad  \frac{\mathrm d r}{\mathrm d θ} &= r \frac{v_r}{v_θ}  \\
&= r \frac{m r \sqrt{\frac{2 E}{m} + \frac{2 G M}{r} - \left(\frac{L}{m}\right)^2 \frac{1}{r^2}}}{L}  \tag{代入}
\end{align*}
$$
$$
\begin{align*}
\Rightarrow\quad  \int \frac{\mathrm d r}{r^2 \sqrt{\frac{2 E}{m} + \frac{2 G M}{r} - \left(\frac{L}{m}\right)^2 \frac{1}{r^2}}} &= \int \frac{m}{L} \mathrm d θ  \tag{两边独立$r,θ$,并积分}  \\
\Rightarrow\quad  - \int \frac{\mathrm d \left(\frac{1}{r}\right)}{\sqrt{\frac{2 E}{m} + 2 G M \frac{1}{r} - (\frac{L}{m})^2 \frac{1}{r^2}}} &= \frac{m}{L} θ + C_θ  \tag{换元}  \\
\Rightarrow\quad  - \left(\frac{m}{L} \arcsin \frac{\left(\frac{L}{m}\right)^2 \frac{1}{r} - G M}{\sqrt{G^2 M^2 + \frac{2 E}{m} \left(\frac{L}{m}\right)^2 }} + C_r\right) &= \frac{m}{L} θ + C_θ  \tag{$\int \frac{\mathrm d x}{\sqrt{c+b x-a x^2}} = \frac{1}{\sqrt{a}} \arcsin \frac{2 a x-b}{\sqrt{b^2 + 4 a c}} + C$}  \\
\Rightarrow\quad  - \left(\frac{1}{L_0} \arcsin \frac{L_0^2 \frac{1}{r} - G M}{\sqrt{G^2 M^2 + 2 E_0 L_0^2 }} + C_r\right) &= \frac{1}{L_0} θ + C_θ  \tag{$L_0 = \frac{L}{m}, E_0 = \frac{E}{m}$}
\end{align*}
$$

$$
\begin{align*}
\Rightarrow\quad  r &= \frac{L_0^2}{\sqrt{G^2 M^2 + 2 E_0 L_0^2 } \sin(-θ + θ_0) + G M}  \\
\Rightarrow\quad  r &= \frac{L_{00}^2 G M}{1 + \sqrt{1 + 2 E_0 L_{00}^2 } \sin(-θ + θ_0)}  \tag{$L_{00} = \frac{L_0}{G M} = \frac{L}{G M m}$}
\end{align*}
$$