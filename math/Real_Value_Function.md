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

### Basic properties

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

$$
\lim_{x\rightarrow a}f(x)=L\Leftrightarrow\forall\epsilon > 0,\exists\delta > 0,\text{ s.t. }0 < |x - a|<\delta\Rightarrow|f(x)-L|<\epsilon
$$

For a function $f: \mathbb R \to \mathbb R$ defined on some open interval that contains the number $a$, except possibly at $a$ itself. We say that the limit of $f(x)$ as $x$ approaches $a$ is equal to $L$: If and only if for any given positive number $\epsilon > 0$ there exists a number $\delta > 0$ such that whenever $0 < |x- a|< \delta$ (which means $x$ is within $\delta$ units of $a$ but not equal to a), it follows that $| f(a) - L|< \epsilon$.

#### Property

- **Uniqueness**: If $\lim\limits_{x\rightarrow a}f(x)$ exists, then this limit value is unique. 

- **Local Boundedness**: If $\lim\limits_{x\rightarrow a}f(x)=L$, then there exist constants $M>0$, $\delta>0$ and a deleted neighborhood of $a$ such that when $0 < |x - a|<\delta$, $f(x)$ is bounded in this neighborhood $|f(x)|\leq M$.

- **Local Sign Preservation**: If $\lim\limits_{x\rightarrow a}f(x)=L>0$ (or $L < 0$), then there exists a constant $\delta>0$ and a deleted neighborhood of $a$ such that in this neighborhood $0 < |x - a|<\delta$, $f(x)>0$ (or $f(x)<0$). If the function limit is greater than $0$, the function value is also greater than $0$ near the limit point; vice versa. 

- **Squeeze theorem**: Let $I$ be an interval containing the point $a$. Let $g, f, h$ be functions defined on $I$, except possibly at a itself. Suppose that for every $x$ in $I$ not equal to $a$, we have $g(x) \le f(x) \le h(x)$, and also suppose that
  $$
  \lim\limits_{x\to a} g(x) = \lim\limits_{x\to a} h(x) = L \quad \Rightarrow\quad \lim\limits_{x\to a} f(x) = L
  $$

- **Heine's Theorem (Resolution Principle)**: The necessary and sufficient condition for the existence of the limit of the function $f(x)$ as $x\to x_0$ is that for any sequence $\{x_n\}$ with $x_0$ as the limit ($x_n\neq x_0$), $\lim_{n\to\infty}f(x_n)$ exists and is equal.

**Equivalent Infinitesimal Formulas**: When $x \to 0$

$$
\begin{align*}
\sin x &\sim x\\
\tan x &\sim x\\
1 - \cos x &\sim\frac{1}{2}x^2\\
e^x - 1 &\sim x\\
\ln(1 + x) &\sim x
\end{align*}
$$


#### Limit Operation Rules

**Arithmetic rules of limits**: 

- Addition & Subtraction: $\lim\limits_{x\rightarrow a}(f(x)\pm g(x))=\lim\limits_{x\rightarrow a}f(x)\pm \lim\limits_{x\rightarrow a}g(x)$
- Multiplication: $\lim\limits_{x\rightarrow a}(f(x)\cdot g(x))=\lim\limits_{x\rightarrow a}f(x)\cdot\lim\limits_{x\rightarrow a}g(x)$
- Division: $\lim\limits_{x\rightarrow a}\frac{f(x)}{g(x)}=\frac{\lim\limits_{x\rightarrow a}f(x)}{\lim\limits_{x\rightarrow a}g(x)},B\neq0$

**Infinitesimal Operation Rules**: The sum of two infinitesimals is an infinitesimal; the product of a bounded function and an infinitesimal is an infinitesimal. The corollaries include that the product of a constant and an infinitesimal is an infinitesimal, and the product of a finite number of infinitesimals is an infinitesimal.

**Limit Operation Rules of Composite Functions**: Let the function $y = f(g(x))$ be composed of the function $u = g(x)$ and $y = f(u)$. $f(g(x))$ is defined in a deleted neighborhood of the point $x_0$. If $\lim\limits_{x \to x_0}g(x)=u_0$ and there exists $\delta_0>0$ such that when $x\in U^{\circ}(x_0,\delta_0)$, $g(x)\neq u_0$. If $\lim\limits_{u \to u_0}f(u)=A$, then $\lim\limits_{x \to x_0}f(g(x))=\lim\limits_{u \to u_0}f(u)=A$.



### Derivative & Partial derivative

$$
\begin{align*}
  \frac{\mathrm df}{\mathrm dx} &= \lim_{Δx \to 0}  \frac{ f(x + Δx) - f(x - Δx) }{ 2 Δx }  \tag{First derivative}\\
  \frac{\mathrm d^n f}{\mathrm dx^n} &= \lim_{Δx \to 0} \frac{ f^{(n - 1)}(x + Δx) - f^{(n - 1)}(x - Δx)} { 2 Δx }  \tag{$n$-order derivative}
\end{align*}
$$

**Derivative**: Let $f: \mathbb{R} \to \mathbb{R}$ be a function. The derivative of $f$ at a point $x$ in its domain, if it exists, is given by the limit as mentioned above . If this limit exists, we say that $f$ is differentiable at $x$. The function $f'$ that assigns to each $x$ the value $f'(x)$ (where it exists) is called the derivative of $f$.
$$
\begin{align*}
\frac{∂f}{∂x_i} &= \lim\limits_{\Delta x_i\to0}\frac{f(...,x_{i, 0} + \Delta x_i,...) -  f(..., x_{i, 0} - \Delta x_i, ...)}{2 Δx_i}  \\
\frac{∂^2 f}{∂x_i^2}  
&= \lim\limits_{\Delta x_i\to0} \frac{f'(..,x_{i, 0}+\Delta x_i,..) -  f'(..,x_{i, 0}-\Delta x_i,..)}{\Delta x_i}   \\
&= \lim\limits_{\Delta x_i\to0}\frac{f(..,x_{i, 0}+\Delta x_i) - 2·f(..,x_{i, 0}) + f(..,x_{i, 0}-Δx_i)}{\Delta x_i^2}  \\
\frac{∂^2 f}{∂x_j ∂x_i} &= \frac{\partial}{\partial x_j} \left(\frac{\partial f}{\partial x_i} \right)
\end{align*}
$$

**Partial derivative**: For multi-variate functions, let the function $z = f(x_{1}, \cdots,x_{i}, \cdots)$ be defined in a certain neighborhood of the point $(x_{1, 0}, \cdots,x_{i, 0}, \cdots)$. The partial derivative of $f$ with respect to $x$ at the point $(x_{1, 0}, \cdots,x_{i, 0}, \cdots)$ is list as above.

#### Property

- **Necessary Condition for Differentiability**: If the function $z = f(x,y)$ is differentiable at the point $(x_0,y_0)$, then the partial derivatives $f_x(x_0,y_0)$ and $f_y(x_0,y_0)$ must exist.
- **Sufficient Condition for Differentiability**: If the partial derivatives $f_x(x,y)$ and $f_y(x,y)$ of the function $z = f(x,y)$ are continuous in a certain neighborhood of the point $(x_0,y_0)$, then the function $z = f(x,y)$ is differentiable at the point $(x_0,y_0)$.

- **Arithmetic rules**: Let $u = u(x)$ and $v = v(x)$ be differentiable at point $x$. 

$$
\begin{align*}
(u\pm v)'&=u'\pm v'\\
(uv)' &= u'v + uv'\\
(cu)'&=cu'\\
\left(\frac{u}{v}\right)'&=\frac{u'v - uv'}{v^{2}} \quad (v\neq0)
\end{align*}
$$

- **Chain Rule**: for the function $z(x) = z(y(x))$, then 
$$
\frac{\mathrm d z}{\mathrm d x} = \frac{\mathrm d z}{\mathrm d y} \cdot \frac{\mathrm d y}{\mathrm d x}
$$

- **Chain Rule for Partial Derivatives**: If $z = f(u,v)$, $u = u(x,y)$, $v = v(x,y)$, then 

$$
\begin{align*}
\frac{\partial z}{\partial x}&=\frac{\partial z}{\partial u}\frac{\partial u}{\partial x}+\frac{\partial z}{\partial v}\frac{\partial v}{\partial x}\\
\frac{\partial z}{\partial y}&=\frac{\partial z}{\partial u}\frac{\partial u}{\partial y}+\frac{\partial z}{\partial v}\frac{\partial v}{\partial y}
\end{align*}
$$

- **Derivative Rule of Inverse Functions**: If the function $x = f(y)$ is monotonic, differentiable in the interval $I_y$ and $f'(y)\neq0$, then its inverse function $y = f^{-1}(x)$ is also differentiable in the interval $I_x=\{x|x = f(y),y\in I_y\}$, and 

$$
(f^{-1})'(x)=\frac{1}{f'(y)}
$$

- **Derivative Rule of Composite Functions**: If $u = g(x)$ is differentiable at point $x$, and $y = f(u)$ is differentiable at point $u = g(x)$, then the composite function $y = f(g(x))$ is differentiable at point $x$, and its derivative is 
$$
y'=f'(u)\cdot g'(x)
$$

- **L'Hôpital's Rule**: if $\lim\limits_{x \to a} f(x) =  \lim\limits_{x \to a} g(x) = 0  \text{ or } \infty$ and $g'(x) \neq 0, \forall x \in I \text{ with } x \neq a$, and $\lim\limits_{x \to a} \frac{f'(x)}{g'(x)}$ exists, then
$$
\lim\limits_{x \to a} \frac{f(x)}{g(x)} = \lim\limits_{x \to a} \frac{f'(x)}{g'(x)}
$$

- **Taylor's theorem**: If a real-valued function $f(x)$ is differentiable at the point $x = a$, then 

$$
f(x) = f(a) + \sum_{i=1}^k \frac{f^{(i)}(a)}{i!}(x-a)^i + o(|x-a|^k)
$$

**Lagrange's Mean Value Theorem**: If the function $y = f(x)$ satisfies: (1) continuous on the closed interval $[a,b]$; (2) differentiable on the open interval $(a,b)$, then there exists at least one point $\xi\in(a,b)$ such that 

$$
f(b)-f(a)=f'(\xi)(b - a)
$$

- **Rolle's Theorem**: If the function $y = f(x)$ satisfies: (1) continuous on the closed interval $[a,b]$; (2) differentiable on the open interval $(a,b)$; (3) $f(a)=f(b)$, then there exists at least one point $\xi\in(a,b)$ such that $f'(\xi)=0$.

- **Fermat's Theorem**: If the function $y = f(x)$ has a local extremum at the point $x_0$ and is differentiable at this point, then $f'(x_0)=0$.

- **Cauchy's Mean Value Theorem**: If the functions $f(x)$ and $g(x)$ satisfy: (1) continuous on the closed interval $[a,b]$; (2) differentiable on the open interval $(a,b)$; (3) $g'(x)\neq0$ for any $x\in(a,b)$, then there exists at least one point $\xi\in(a,b)$ such that 

$$
\frac{f(b)-f(a)}{g(b)-g(a)}=\frac{f'(\xi)}{g'(\xi)}
$$

### Gradient & Divergence & Curl

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

#### Property

- $\nabla \times (\nabla \phi) = 0$, for any scalar field $\phi$.
- $\nabla \cdot (\nabla \times \boldsymbol F) = 0$, for any vector field (in three dimensions) $\boldsymbol F$. 
- $\nabla \cdot (\phi \boldsymbol F) = (\nabla \phi) \cdot \boldsymbol F + \phi (\nabla \cdot \boldsymbol F)$
- $\nabla \times (\phi \boldsymbol F) = (\nabla \phi) \times \boldsymbol F + \phi (\nabla \times \boldsymbol F)$

### Integral

$$
\int f(x) \mathrm d x  = F(x)  + const. \tag{Integral}
$$
Integral $f: (f: \mathbb R \to \mathbb R) \to (f: \mathbb R \to \mathbb R)$ represents the anti-derivative of a function $f(x)$. The indefinite integral of a function $f$ is a family of functions $F$ such that for all $x$ in the domain of $f$, $F'(x) = f(x)$. Where $const.$ is an arbitrary constant, reflecting the fact that the process of differentiation loses constant information.

#### Integral of multivariate functions

$$
\begin{align*}
\iint\limits_{D}f(x,y)d\sigma&=\int_{a}^{b}dx\int_{c}^{d}f(x,y)dy=\int_{c}^{d}dy\int_{a}^{b}f(x,y)dx\\
&=\iint\limits_{D}f(r\cos\theta,r\sin\theta)rdrd\theta=\int_{\alpha}^{\beta}d\theta\int_{r_1(\theta)}^{r_2(\theta)}f(r\cos\theta,r\sin\theta)rdr
\end{align*}
$$

Double Integral Conversion Formula

$$
\begin{align*}
\iiint\limits_{\Omega}f(x,y,z)dV&=\int_{a}^{b}dx\int_{c}^{d}dy\int_{e}^{f}f(x,y,z)dz\\
&=\iiint\limits_{\Omega}f(r\cos\theta,r\sin\theta,z)rdrd\theta dz\\
\end{align*}
$$

Triple Integral Conversion Formula

#### Property

- Integration by part: for two continuously differentiable functions $u, v$, 
  $$
  \int u \mathrm d v = uv - \int v \mathrm d u
  $$
  

**Substitution Integration Formula**:
- **First Substitution**: If $x=\varphi(t)$ is differentiable, and $\varphi^\prime(t)$ is continuous, and $f(x)$ is continuous on the corresponding interval, then 

$$
\int f(x)dx=\int f[\varphi(t)]\varphi^\prime(t)dt
$$

- **Second Substitution**: If $x=\varphi(t)$ has an inverse function $t=\varphi^{-1}(x)$, and $\varphi^\prime(t)$ is continuous and $\varphi^\prime(t)\neq0$, and $f[\varphi(t)]\varphi^\prime(t)$ has an antiderivative $F(t)$, then 

$$
\int f(x)dx = F[\varphi^{-1}(x)]+C
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

