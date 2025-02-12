# Real Value Function

[TOC]

## Define

$$
f: \mathbb R \to \mathbb R
$$

A real function $f: \mathbb R \to \mathbb R$ is a [function](./Function.md) from [real numbers](./Real_Field.md) to real numbers.

For multi-variate real functions:
$$
f: \mathbb R^n \to \mathbb R
$$

## Properties

- Continuity: A function $f$ with variable $x$ is continuous at the real number $c$, if the limit of $f(a)$, as $x$ tends to $c$, is equal to $f(c)$. More formally, for any positive number $\epsilon > 0$, if there exists a positive number $\delta > 0$ such that whenever $|x - a| < \delta$, $|f(x) - f(a)| < \epsilon$, the function is said to be continuous at $a$.
- Monotonicity
- Boundedness
- Differentiability: A function is said to be differentiable at a point $x = a$ if the following limit exists:
$$
f'(a) = \lim_{{h \to 0}} \frac{f(a + h) - f(a)}{h}
$$
- Periodicity: $f(x + T) = f(x)$.  The number $T$ is referred to as its period.
- Odd and Even Properties
  - Odd function: $f(-x) = -f(x)$
  - Even function: $f(-x) = f(x)$

### Limitation

- Define

for a function $f: R \to R$ defined on some open interval that contains the number $a$, except possibly at $a$ itself. We say that the limit of $f(x)$ as $x$ approaches $a$ is equal to $L$: If and only if for any given positive number $\epsilon > 0$ there exists a number $\delta > 0$ such that whenever $0 < |x- a|< \delta$ (which means $x$ is within $\delta$ units of $a$ but not equal to a), it follows that $| f(a) - L|< \epsilon$.
$$
\lim\limits_{x\to a} f(x) = L
$$

- Property
  - Uniqueness
  
  - Boundedness
  
  - 保号性
  
  - Squeeze theorem
  
    Let $I$ be an interval containing the point $a$. Let $g, f, h$ be functions defined on $I$, except possibly at a itself. Suppose that for every $x$ in $I$ not equal to $a$, we have $g(x) \le f(x) \le h(x)$, and also suppose that
    $$
    \lim\limits_{x\to a} g(x) = \lim\limits_{x\to a} h(x) = L \quad \Rightarrow\quad \lim\limits_{x\to a} f(x) = L
    $$
    

### Derivative & Partial derivative

- Define
  $$
  \begin{align*}
    \frac{\mathrm df}{\mathrm dx} &= \lim_{Δx \to 0}  \frac{ f(x + Δx) - f(x - Δx) }{ 2 Δx }  \tag{First derivative}\\
    \frac{\mathrm d^n f}{\mathrm dx^n} &= \lim_{Δx \to 0} \frac{ f^{(n - 1)}(x + Δx) - f^{(n - 1)}(x - Δx)} { 2 Δx }  \tag{$n$-order derivative}
  \end{align*}
  $$

Let $f: \mathbb{R} \to \mathbb{R}$ be a function. The derivative of $f$ at a point $x$ in its domain, if it exists, is given by the limit as mentioned above . If this limit exists, we say that $f$ is differentiable at $x$. The function $f'$ that assigns to each $x$ the value $f'(x)$ (where it exists) is called the derivative of $f$.

For multi-variate functions, the partial derivative is

$$
\begin{align*}
  \frac{∂f}{∂x_i} &= \frac{f(...,x_i + Δx_i,...) -  f(..., x_i - Δx_i, ...)}{2 Δx_i}  \\
  \frac{∂^2 f}{∂x_i^2}  
  &= \frac{f'(..,x_i+Δx_i,..) -  f'(..,x_i-Δx_i,..)}{Δx_i}   \\
  &= \frac{f(..,x_i+Δx_i) - 2·f(..,x) + f(..,x_i-Δx_i)}{Δx_i^2}  \\
  \frac{∂^2 f}{∂x_j ∂x_i}  
  &= \frac{\partial}{\partial x_j} \left(\frac{\partial f}{\partial x_i} \right)
\end{align*}
$$

- Property
  - 线性性
  
  - 乘法法则
  
  - **Chain Rule**: for the function $z(x) = z(y(x))$, then 
    $$
    \frac{\mathrm d z}{\mathrm d x} = \frac{\mathrm d z}{\mathrm d y} \cdot \frac{\mathrm d y}{\mathrm d x}
    $$
  
  - **L'Hôpital's Rule**: if $\lim\limits_{x \to a} f(x) =  \lim\limits_{x \to a} g(x) = 0  \text{ or } \infty$ and $g'(x) \neq 0, \forall x \in I \text{ with } x \neq a$, and $\lim\limits_{x \to a} \frac{f'(x)}{g'(x)}$ exists, then
    $$
    \lim\limits_{x \to a} \frac{f(x)}{g(x)} = \lim\limits_{x \to a} \frac{f'(x)}{g'(x)}
    $$
  
  - **Taylor's theorem**: If a real-valued function $f(x)$ is differentiable at the point $x = a$, then 
    $$
    f(x) = f(a) + \sum_{i=1}^k \frac{f^{(i)}(a)}{i!}(x-a)^i + o(|x-a|^k)
    $$
  


### Gradient & Divergence & Curl

- Define
  Gradient $\nabla (\cdot): (f: \mathbb R^{\dim} \to \mathbb R) \to (f: \mathbb R^{\dim} \to \mathbb R^{\dim})$, reflects the direction of the maximum rate of change for function $f$ at point $\boldsymbol x_0$.
  $$
  \nabla f = \sum_{i=1}^{\dim} \frac{∂f}{∂x_i} \hat{\boldsymbol x_i} = \left(\begin{matrix}\frac{∂f}{∂x_1} \\ \vdots \\ \frac{∂f}{∂x_{\dim}}\end{matrix}\right)  \tag{Gradient}
  $$
  
  Divergence $\nabla \cdot (\cdot): (f: \mathbb R^{\dim} \to \mathbb R^{\dim}) \to (f: \mathbb R^{\dim} \to \mathbb R)$. For a vector field $\boldsymbol f(\boldsymbol x)$, the divergence is defined as the limit of the redio of the surface integral of $\boldsymbol f$ out of the closed surface $S$ of a valume $V$ enclosing point $\boldsymbol x_0$, as $V$ shrinks to $0$. The divergence represents the volume density of the outward flux of a vector field from an infinitesimal volume around a given point.
  $$
  \nabla · \boldsymbol f = \lim_{|V| \to 0} \frac{1}{|V|} \oint_{S(V)} \boldsymbol f \cdot \hat {\boldsymbol n} \mathrm d S \tag{Divergence}
  $$
  $$
  \nabla · \boldsymbol f = \sum_{i=1}^{\dim} \frac{∂f_{i}}{∂x_i}  \tag{Cartesian coordinates}
  $$
  
  Curl $\nabla \times (\cdot): (f: \mathbb R^{3} \to \mathbb R^{3}) \to (f: \mathbb R^{3} \to \mathbb R)$. For a vector field in three-dimensional $\boldsymbol f(\boldsymbol x)$, the curl is defined as the limit of the redio of the line integral of $\boldsymbol f$ along the boundary $C$ of a area $A$ enclosing point $\boldsymbol x_0$, as $A$ shrinks to $0$. The curl represents the circulation density at each point of the field. 方向是旋转度最大的环量的旋转轴, 旋转的方向满足右手定则, 大小是绕该旋转轴旋转的环量与旋转路径围成的面元面积之比.
  $$
  \nabla \times \boldsymbol f = \lim_{A \to 0} \frac{1}{|A|} \oint_{C} \boldsymbol f \cdot \mathrm d \boldsymbol r \tag{Curl}
  $$
  $$
  \begin{align*}
    \nabla \times \boldsymbol f =& \left(\frac{∂f_z}{∂y} - \frac{∂f_y}{∂z} \right) \hat{\boldsymbol x} + \\
    & \left(\frac{∂f_x}{∂z} - \frac{∂f_z}{∂x} \right) \hat{\boldsymbol y}  +\\
    & \left(\frac{∂f_y}{∂x} - \frac{∂f_x}{∂y} \right) \hat{\boldsymbol z}  \tag{3D Cartesian coordinates}
  \end{align*}
  $$
  
- Property
  - $\nabla \times (\nabla \phi) = 0$, for any scalar field $\phi$.
  - $\nabla \cdot (\nabla \times \boldsymbol F) = 0$, for any vector field (in three dimensions) $\boldsymbol F$. 
  - $\nabla \cdot (\phi \boldsymbol F) = (\nabla \phi) \cdot \boldsymbol F + \phi (\nabla \cdot \boldsymbol F)$
  - $\nabla \times (\phi \boldsymbol F) = (\nabla \phi) \times \boldsymbol F + \phi (\nabla \times \boldsymbol F)$

### Integral

- Define

$$
\int f(x) \mathrm d x  = F(x)  + const. \tag{Integral}
$$
Integral $f: (f: \mathbb R \to \mathbb R) \to (f: \mathbb R \to \mathbb R)$ represents the anti-derivative of a function $f(x)$. The indefinite integral of a function $f$ is a family of functions $F$ such that for all $x$ in the domain of $f$, $F'(x) = f(x)$. Where $const.$ is an arbitrary constant, reflecting the fact that the process of differentiation loses constant information.

- Property

  - Integration by part: for two continuously differentiable functions $u, v$, 
    $$
    \int u \mathrm d v = uv - \int v \mathrm d u
    $$
    
### Riemann Integra

$$
\int_a^b f(x) \mathrm d x = F(b) - F(a) \tag{Definite Integral}
$$

Definite Integral $f: (\mathbb R, \mathbb R, f: \mathbb R \to \mathbb R) \to \mathbb R$ of a function f(x) over an interval $[a, b]$ is the limit of a sum of rectangular areas as the width of the rectangles approaches zero. 


### Kolmogorov-Arnold Representation Theorem  

$$
f(\boldsymbol x) = f(x_1, ..., x_n) = \sum_{q=0}^{2n} \Phi_q\left( \sum_{p=1}^n \phi_{q, p}(x_p) \right)
$$
Kolmogorov-Arnold representation theorem states that every multivariate continuous function can be represented as a superposition of the two-argument addition of continuous functions of one variable.


### Differential Equation

#### Define
$$
f \left(x, y, \frac{\mathrm d y}{\mathrm d x}, \frac{\mathrm d^2 y}{\mathrm dx^2}, ..., \frac{\mathrm d^n y}{\mathrm d x^n} \right) = 0  \tag{ODE}
$$
Ordinary differential equation (ODE) is an equation that relates an unknown function $y$ to its derivatives with respect to a single independent variable $x$.  

$$
f \left(D^k u(x), ... , D^2 u(x), u(x), x \right) = 0  \tag{PDE}
$$
$$
f: \mathbb R^{n^k} \times \mathbb R^{n^{k-1}} \times \mathbb R^n \times \mathbb R \times \Omega \to \mathbb R \quad; x \in \Omega; u: \Omega \to \mathbb R
$$
Partial differential equation (PDE) is an equation that relates an unknown function $u$ of two or more variables to its partial derivatives with respect to those variables.

#### Include

##### Linear Differential Equation

- Define
  $$
  \sum_{k=0}^K a_k(x) u^{(k)}(x) = f(x)  \tag{Linear ODE}
  $$
  $$
  \sum_{k=0}^K a_k(x) D^k u(x) = f(x)  \tag{Linear PDE}
  $$

- Property
  - The solution set of a linear differential equation constitutes a linear space.

##### Second Order Nonlinear Partial Differential Equation

- Define
  $$
  \sum_{ij} a_{ij}(x) \frac{∂^2 u}{∂ x_i ∂ x_j} + \sum_i b_i(x) \frac{∂ u}{∂ x_i} + c(x) u(x) = f(x)
  $$
  coefficient matrix $A(x) = (a_{ij}(x))_{m \times m}$

- Include
  * Elliptic Partial Differential Equation
    - Define  
      $A(x)$ is negative definite.

    - Include
      * Poisson's Equations
        - Define
          $$
          -\nabla^2 \phi = f
          $$
        * Laplace's Equations
          $$
          \nabla^2 \phi = 0
          $$

  * Hyperbolic Partial Differential Equation
    - Define  
      eigenvalue of $A(x)$ consists of a $0$ and other negative numbers

    - Include
      * Diffusion equation
        - Define
          $$
          \frac{∂u}{∂t} - a \nabla^2 u = f(x,t)
          $$

  * Parabolic Partial Differential Equation
    - Define
      eigenvalue of $A(x)$ consists of of a positive number and other negative numbers.

    - Include
      * Wave equation
        - Define
          $$
          \frac{∂^2 u}{∂t^2} - a \nabla^2 u = f(x,t)
          $$

##### Semi-linear Partial Differential Equation

##### Quasi-linear Partial Differential Equation

##### Fully Nonlinear Partial Differential Equation

## Include

## Parents

- [Function](./Function.md): 

- [Real_Field](./Real_Field.md): 

