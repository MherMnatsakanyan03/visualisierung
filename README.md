# Visualisierung

## Chapter 1

$size\_of\_effect = \frac{difference}{first\_value}$

$lie\_factor = \frac{size\_of\_effect\_graph}{size\_of\_effect\_data}$

`Change blindness`: significant changes are not noticed by the observer

goals: visual exploration, analysis and presentation

**pipeline**: `data acquisition` -> `filtering` -> `visualization/mapping` -> `rendering/interaction`

## Chapter 2

`Sensory memory`: Preattentive processing, "instinctive" perception

`Short-term memory`: seconds to minutes, limited capacity

`Long-term memory`: days to years, unlimited capacity

`Weber's law`: linear increase in subjective perception with logarithmic increase in stimulus intensity

Distinguish 200 colors (H), 500 gradations (S), 20 variation (V)

Two stages of visual perception:

1. `Preattentive`: automatic, parallel processing of visual features
2. `Attentive`: serial processing, requires focus

Preatentive attributes: < 8 hues, <= 4 orientations, <= 4 sizes, <= 10 else

non-preatentive attributes: parallelism, juncture

Color: use high luminance contrast, avoid red-green combinations, only use max 5 colors

## Chapter 3

Best to worst mapping: `position` -> `length` -> `angle/slope` -> `area` -> `luminance/saturation` -> `volume/curvature`

Steven's area judgment scale: $I = \alpha r^{1.4}$

Rule: map most important data to the most accurate visual attribute

`Simple line Graphs`: direct comparison, fine details **BUT** clutter, hard to distinguish time series

`Stacked Graphs`: time series destinguish **BUT** less vertivcal resolution, hard to compare time series

`Small multiples`: easy time series destinguish, easy to compare **BUT** less resolution per time, difficult to compare across time

`Horiton Graphs`: vertical resolution, quick min/max **BUT** steep learning curve, hard to compare

Quartils: $Q_1 = (n+1)/4$, $Q_2 = (n+1)/2$, $Q_3 = 3(n+1)/4$

Parallel Coordinates: crossing lines -> negative correlation, parallel lines -> positive correlation

## Chapter 4

Derivative to a point $u$: derive $\frac{\delta f(x_0 + t\cdot u)}{\delta t}$

$f(x,y) = \exp(-0.2 \cdot (x^2 + y^2)) \Rightarrow f(x_0 + t\cdot u) = \exp(-0.2 \cdot ((x_0 + t\cdot u_x)^2 + (y_0 + t\cdot u_y)^2))$

On Image:

- `forward derivative`: $f'\rightarrow_x(x,y)=f(x,y) - f(x-1,y)$
- backward derivative: $f'\leftarrow_x(x,y)=f(x,y) - f(x+1,y)$

Gradient: $\nabla f(x,y) = \left(\frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}\right)$

Derivative to a point $u$: $D_u f = \nabla f\cdot u$

On Image:

- forward derivative: $\nabla f(x,y) = \left(f(x,y) - f(x-1,y), f(x,y) - f(x,y-1)\right)$

`Hessian Matrix`: First row is derivative to x then x y z, second row is derivative to y then x y z, third row is derivative to z then x y z

Type of critical point ($\lambda$ are eigenvalues of Hessian matrix):

- local minimum: $0 < \lambda_1 \leq \lambda_2 \leq \lambda_3$
- saddle point: $\lambda_1 < 0 < \lambda_3$
- local maximum: $\lambda_1 \leq \lambda_2 \leq \lambda_3 < 0$

Calculate eigenvalues:

- $A - \lambda E$
- $det(A - \lambda E) = 0$
- $det(M_{2x2}) = a_{11}a_{22} - a_{12}a_{21}$
- $det(M_{3x3}) = m_{11}m_{22}m_{33} + m_{12}m_{23}m_{31} + m_{13}m_{21}m_{32} - m_{13}m_{22}m_{31} - m_{12}m_{21}m_{33} - m_{11}m_{23}m_{32}$

Quadrangle Lemma: minimum, saddle, maximum, saddle

`Jacobian Matrix`: first row is derivative of u to x, y and z, second row is derivative of v to x, y and z and third row is derivative of w to x, y and z

Critical points:

- inflow behavior: $Re(\lambda_i) < 0$
- outflow behavior: $Re(\lambda_i) > 0$
- swirling behavior: $Im(\lambda_1) = -Im(\lambda_2) \neq 0$

`Poincaré Index`: counterclockwise rotation of a vector, number of counterclockwise rotation of that vector

`Divergence`: sum of the diagonal elements of the Jacobian matrix

`Laplacian`: zweite ableitung nach x + zweite ableitung nach y + zweite ableitung nach z

Estemated divergence: $\div f(x,y) = f_x(x,y) - f_x(x-1,y) + f_y(x,y) - f_y(x,y-1)$

`Curl`: $(w_y - v_z, u_z - w_x, v_x - u_y)$

## Chapter 5
