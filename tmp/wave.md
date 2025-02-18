# Wave

[TOC]

## Wave Function

$$
\begin{align*}
\frac{\partial^2 u}{\partial t ^ 2} &= c^2 \Delta u \\
&= c^2 \sum_{i=1}^{\dim}\frac{\partial^2 u}{\partial x_i ^ 2}
\end{align*}
$$



## Monochromatic wave

$$
f(\boldsymbol x, t) = A e^{\mathrm i(\boldsymbol k \cdot \boldsymbol  x - \omega t + \varphi)}
$$

- $A$: the amplitude, which indicates the maximum displacement of the wave and reflects the intensity of the wave.
- $\lambda$: the wavelength.
- $\boldsymbol k$: the wave vector, wave number $|\boldsymbol k|$ indicates the number of cycles of the wave per unit length, the direction of the wave vector indicates the direction in which the wave propagates.
$$
|\boldsymbol k| = \frac{2\pi}{\lambda}
$$
- $\omega$: the angular frequency, indicates the phase change of the wave per unit time.
- $f$ is the frequency.
$$
\omega=2\pi f
$$
- $\varphi$: the initial phase, which determines the initial state of the wave at $t = 0$ and $x = 0$.

### Properties

#### Velocity

$$
\boldsymbol v = \frac{\omega}{|\boldsymbol k|} \hat {\boldsymbol k}
$$

> ***Proof***:
>$$
>\begin{align*}
>\boldsymbol k \cdot \boldsymbol  x - \omega t &= const. \\
>\Rightarrow \boldsymbol k \cdot \frac{\mathrm d \boldsymbol  x}{\mathrm d t} - \omega &= 0\\
>\frac{\mathrm d \boldsymbol x}{\mathrm d t} &=  \frac{\omega}{|\boldsymbol k|} \hat {\boldsymbol k}
>\end{align*}
>$$

## Polychromatic wave

$$
f(\boldsymbol x, t) = \int A(\boldsymbol k) e^{i(\boldsymbol k \cdot \boldsymbol x - \omega(\boldsymbol k) t)} d \boldsymbol k
$$




### Properties

#### Group velocity & Phase velocity

$$
v_g=\frac{d\omega}{dk}
$$

**Group velocity** refers to the propagation speed of the wave envelope, and is also the energy transmission speed associated with a group of forward waves composed of sinusoidal components. It can be understood as the overall propagation speed formed by the combined action of various frequency components in the wave packet. For example, in water waves, a group of water waves with a certain frequency range is regarded as a wave packet, and the speed at which this group of water waves moves forward as a whole is the group velocity. **Physical meaning**: Group velocity represents the propagation speed of the energy or information carried by the wave. In practical applications such as communication, the signal is usually composed of multiple frequency components, and the propagation speed of the signal is the group velocity, which determines the speed of information transmission in the medium.

![Wave_group](./assets/Wave_group.gif)

$$
v_p=\frac{\omega}{k}
$$


**Phase velocity** refers to the speed at which the equiphase surface (such as the crest surface or the trough surface) of a sinusoidal electromagnetic wave of a single frequency propagates in a medium. Simply put, it is the speed at which a certain phase (such as the crest or trough) of a wave moves in space. For example, for an ideal sinusoidal water wave, the speed at which a crest on the water wave moves forward is the phase velocity. **Physical meaning**: Phase velocity is mainly used to describe the propagation characteristics of the phase of a wave in space. It reflects the propagation speed of the periodic change of the wave in space. When studying wave interference, diffraction and other phenomena, phase velocity is an important parameter because these phenomena are closely related to the phase of the wave.


- $v_g$ is the group velocity
- $v_p$ is the phase velocity