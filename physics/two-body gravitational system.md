# Two-body gravitational system

Under Newton's classical theory of gravitation. When one particle is stationary as the origin, the trajectory equation of the other particle is as follows. Among them, the polar coordinate equation of the conic section, the $e$ eccentricity, and the $p$ semi-diameter. The two-body scenario can be abstracted as motion around the equivalent center of mass in an inertial system.
$$
\begin{align*}
  r &= \frac{p}{1 - e \sin(θ + θ_0)}  \\
  p &= \frac{L^2}{G M m^2}  \\
  e &= \sqrt{1 + 2 \frac{E}{m} \left(\frac{L}{G M m}\right)^2}
\end{align*}
$$


> ***Proof of Two-body gravitational system***
>
> Formulate a system of equations, where $L$ and $E$ are constants, and $r, \theta, v_r, v_\theta$ are variables. There are three equations and four variables. Determine the relationship between $r$ and $\theta$.
> $$
> \begin{align*}
> L &= m r v_θ  \tag{Conservation of angular momentum}  \\
> E &= \frac{1}{2} m (v_r^2 + v_θ^2) - G \frac{M m}{r}  \tag{Conservation of energy}  \\
> \frac{\mathrm d r}{\mathrm d θ} &= r \frac{v_r}{v_θ}  \tag{$v_r = \frac{\mathrm d r}{\mathrm d t}, v_θ = r \frac{\mathrm d θ}{\mathrm d t}$}
> \end{align*}
> $$
> Solve the system of equations.
> $$
> \begin{align*}
> v_θ &= \frac{L}{m r}\\
> v_r &= \sqrt{\frac{2 E}{m} + \frac{2 G M}{r} -\left(\frac{L}{m}\right)^2 \frac{1}{r^2}}\\
> \Rightarrow\quad  \frac{\mathrm d r}{\mathrm d θ} &= r \frac{v_r}{v_θ}  \\
> &= r \frac{m r \sqrt{\frac{2 E}{m} + \frac{2 G M}{r} - \left(\frac{L}{m}\right)^2 \frac{1}{r^2}}}{L}
> \end{align*}
> $$
>
> $$
> \begin{align*}
> \int \frac{\mathrm d r}{r^2 \sqrt{\frac{2 E}{m} + \frac{2 G M}{r} - \left(\frac{L}{m}\right)^2 \frac{1}{r^2}}} &= \int \frac{m}{L} \mathrm d θ \\
> - \int \frac{\mathrm d \left(\frac{1}{r}\right)}{\sqrt{\frac{2 E}{m} + 2 G M \frac{1}{r} - (\frac{L}{m})^2 \frac{1}{r^2}}} &= \frac{m}{L} θ + C_θ \\
> - \left(\frac{m}{L} \arcsin \frac{\left(\frac{L}{m}\right)^2 \frac{1}{r} - G M}{\sqrt{G^2 M^2 + \frac{2 E}{m} \left(\frac{L}{m}\right)^2 }} + C_r\right) &= \frac{m}{L} θ + C_θ   \\
> - \left(\frac{1}{L_0} \arcsin \frac{L_0^2 \frac{1}{r} - G M}{\sqrt{G^2 M^2 + 2 E_0 L_0^2 }} + C_r\right) &= \frac{1}{L_0} θ + C_θ  \tag{$L_0 = \frac{L}{m}, E_0 = \frac{E}{m}$}
> \end{align*}
> $$
>
> $$
> \begin{align*}
> \Rightarrow\quad  r &= \frac{L_0^2}{\sqrt{G^2 M^2 + 2 E_0 L_0^2 } \sin(-θ + θ_0) + G M}  \\
> r &= \frac{L_{00}^2 G M}{1 + \sqrt{1 + 2 E_0 L_{00}^2 } \sin(-θ + θ_0)}  \tag{$L_{00} = \frac{L_0}{G M} = \frac{L}{G M m}$}
> \end{align*}
> $$
>


For two massive celestial bodies $M_1, M_2$, choosing a rotating frame of reference with its center of mass as the origin and kept relatively stationary, then the potential energy is:
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
