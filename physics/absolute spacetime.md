# Absolute spacetime

Absolute spacetime refers to the idea that space and time exist as independent, unchanging entities, separate from the matter and events that occur within them.

- **Space** is a fixed, uniform, infinite, three-dimensional backdrop where objects are located and distances are measured.
- **Time** is a continuous, one-dimensional flow that ticks the same for everyone, regardless of how they move.

## Coordinate transformation: Galileo's principle of relativity

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

### Coordinate transformation between non-inertial coordinate systems: Fictitious Force

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

| **Fictitious Force**       | **Expression**                                               | **Cause**                  |
| -------------------------- | ------------------------------------------------------------ | -------------------------- |
| Centrifugal Force          | $\vec{F}_\text{cent} = -m (\vec{\omega} \times (\vec{\omega} \times \vec{r}))$ | Rotation of $S'$           |
| Coriolis Force             | $\vec{F}_\text{cor} = -2m (\vec{\omega} \times \vec{v}')$    | Relative velocity in $S'$  |
| Linear Acceleration Force  | $\vec{F}_\text{lin} = -m \vec{A}(t)$                         | Translational acceleration |
| Angular Acceleration Force | $\vec{F}_\text{ang} = -m (\vec{\alpha} \times \vec{r}')$     | Angular acceleration       |
