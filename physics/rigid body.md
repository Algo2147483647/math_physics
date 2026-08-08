# Rigid body

## Action of a rigid body

The motion of a rigid body is divided into two parts: translational motion and rotational motion
$$
S = \int_{t_1}^{t_2} \left( \frac{1}{2} m |\dot{\mathbf{r}}|^2 + \frac{1}{2} \dot{\boldsymbol{\boldsymbol{\theta}}}^\mathrm{T} \mathbf{I} \dot{\boldsymbol{\boldsymbol{\theta}}} - V(\mathbf{r}, \boldsymbol{\theta}) \right) \mathrm{d}t
$$

- **Translational Kinetic Energy** $\frac{1}{2} m |\dot{\mathbf{r}}|^2$: This term accounts for the motion of the center of mass.
- **Rotational Kinetic Energy** $\frac{1}{2} \dot{\boldsymbol{\boldsymbol{\theta}}}^\mathrm{T} \mathbf{I} \dot{\boldsymbol{\boldsymbol{\theta}}}$: This term accounts for the body's rotation about its center of mass.
- **Potential Energy** $V(\mathbf{r}, \boldsymbol{\theta})$: This term incorporates external forces such as gravity or fields acting on the rigid body.

### Angular momentum: Inertia tensor

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

### Equations of motion for a rigid body

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