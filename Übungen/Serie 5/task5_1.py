import numpy as np # math functionality
import matplotlib.pyplot as plt # plotting

def phi(r):
    return np.exp(-r**2)

points = np.array([[-2,-2], [2,0], [0,-1], [-1,2]])
values = np.array( [0.2,     0.6,   0.3,    0.5])

fig = plt.figure(figsize=(8,7))

# 3D scatter plot
ax = fig.add_subplot(111, projection='3d')
ax.scatter(points[:,0], points[:,1], values + 0.01, c='r', depthshade=False, zorder=10)
# + 0.01 to avoid overlap with the surface, not actually correct

# Create a grid of points
x = np.linspace(-4, 4, 100)
y = np.linspace(-4, 4, 100)
X, Y = np.meshgrid(x, y)

# Interpolate the values on the grid
Z = np.zeros(X.shape)
for i in range(len(points)):
    r = np.sqrt((X - points[i,0])**2 + (Y - points[i,1])**2)
    Z += values[i] * phi(r)

# Plot the interpolated surface and hide the grid
ax.plot_surface(X, Y, Z, cmap='viridis', alpha=1, edgecolor='none')

# Always run show, to make sure everything is displayed.
plt.show()