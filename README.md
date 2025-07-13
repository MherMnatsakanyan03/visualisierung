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

Data reconstruction: get continuous data from discrete data

- set constant boxes based on the data
- interpolate the data in the boxes

`Radial Basis Function`: $RBF(x) = \sum_{i=1}^n f_i \cdot \phi(||x - x_i||)$ with $\phi(x) = \exp(-x^2)$

Better: $RBF(x_i) = \sum_{i=1}^n w_i \cdot \phi(||x - x_i||) = f_i$, that is: solve equation system so that line goes through all points

- drawbacks: every sample point is used, so it is slow, new points need to be recalculated

One solution: $\phi(x) = \frac{1}{x^2} / \sum_{i=1}^N \frac{1}{||x - x_i||^2}$

New formula: $RBF(x) = \sum_{i=1}^n \frac{f_i}{||x_i - x||^2} / \sum_{i=1}^N \frac{1}{||x_i - x||^2}$

- still have to calculate all again for new points

`Triangulation`: connect points with triangles, then interpolate the data in the triangles

- avoid long, thin triangles -> use Delaunay triangulation
- make circle around triangle, if another triangle has line inside, flip the line

`Line-interpolation`: $f(y) = x \cdot p_1 + (1-x) \cdot p_2$ with $p_1$ and $p_2$ are the two points of the line

Triangle-interpolation: $f(x) = p_1 \cdot \frac{A_1}{A} + p_2 \cdot \frac{A_2}{A} + p_3 \cdot \frac{A_3}{A}$ with $A$ is the area of the triangle and $A_i$ is the area of the triangle with point $p_i$ and the two other points

Grid-interpolation:

- **linear**: $f(x,y)$ calculate 1D on x axis for value x, then use the result to calculate 1D on y axis for value y
- **bilinear**: f(x,y) calculate area of quadrangle $xy$, $(1-x)y$, $x(1-y)$, $(1-x)(1-y)$, then use the areas to calculate the value with values $f_{ij}$ of opposite corners

## Chapter 6

Marching cubes: distinguish which way diagonal is cut by calculating middle value $\frac{sum\_of\_corners}{4}$

`Connected Component Analysis`: find connected components in a binary image and only keep the largest one

Smoothing:

- Iterative smoothing: average the points with their neighbors
- $x_i \leftarrow x_i + \lambda\sum_j \omega_{ij}(x_j - x_i)$ with $\omega_{ij}$ is the weight of point $j$ to point $i$ and $\lambda$ is the smoothing factor
- Combinatorial: $\omega_{ij} = 1$ if $i$ and $j$ are neighbors, else 0
- Laplace-Smoothing: $\omega_{ij} = \frac{1}{N(i)}$ -> loses volume
- Laplace-Smoothing + HC: Add correction term to Laplace-Smoothing to keep volume
- LowPass Filter: implementation of two laplace smoothing steps, with $\lambda_1 > 0$ and $\lambda_2 < 0$

- Mean value filter: average the normal vector of surfaces in the neighborhood
- Median filter: average the normal vector of surfaces in the neighborhood, but only use the median value

Distance aware smoothing: Smooth more the further away from a certain point -> use distance as scaling factor

## Chapter 7

`Maximum Intensity Projection`: project the maximum value of a volume onto a 2D plane

- Interpolation: use linear interpolation to get the value from inside the voxel
- nearest neighbor: use the value of the nearest voxel
- Nyquist-Shannon Sampling Theorem: to avoid aliasing, sample at least twice the highest frequency of the signal -> $< 0.5$ voxel size

Transfer function: map data values to colors and opacities

Gradients:

- forward difference: $\nabla f(x,y) = \begin{pmatrix} f(x + 1) - f(x) \\ f(y+1) - f(y) \end{pmatrix}$
- backward difference: $\nabla f(x,y) = \begin{pmatrix} f(x) - f(x - 1) \\ f(y) - f(y - 1) \end{pmatrix}$
- central difference: $\nabla f(x,y) = \frac{1}{2} \begin{pmatrix} f(x + 1) - f(x - 1) \\ f(y + 1) - f(y - 1) \end{pmatrix}$

Types of projections:

- First-hit: only the first voxel that is hit by the ray is used
- average: average all voxels that are hit by the ray
- maximum intensity: use the maximum value of all voxels that are hit by the ray
- cvp, threshold: use first voxel that is above a certain threshold
- mida: local maximum of change of intensity along the ray

## Chapter 8

Surface normal: $n = -\frac{\nabla f}{||\nabla f||}$

Curvature Information: $\nabla n^\top = -\nabla \frac{\nabla f}{||\nabla f||} = - \frac{1}{|\nabla f^\top|}(I - nn^\top)H$

$P = I - nn^\top$ porjects all points to the plane orthogonal to the normal vector

- $T=trace(G)$ sum of the diagonal elements of the matrix
- $F = |G|_F = \sqrt{G_{11}^2 + \dots + G_{nn}^2}$
- $\kappa_{1/2} = \frac{T \pm \sqrt{2F^2 - T^2}}{2}$

Isolines on triangles: on side $e_2$: $\frac{\varphi_1}{\varphi_1-\varphi_3}\cdot e_2$

Covariant Derivative: $D_{v(x)}f(x) = <\nabla\f(x), v(x)>$

Contours vs crease lines:

- differences:
  - view dependent: contours are view dependent, crease lines are view independent
  - sharp edges: creases show sharp edges
  - contours: crease lines are not contours
- similarities:
  - order 1
  - both no round edges
  - both no bumps
  - both show deformations

Evaluation: Schulze method, pairwise comparison, rank order

## Chapter 9
