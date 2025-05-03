import numpy as np  # math functionality
import matplotlib.pyplot as plt  # plotting
import matplotlib.image as mpimg  # loading images
from scipy.interpolate import griddata

fig = plt.figure(figsize=(8, 7))

# show the first chart
ax1 = fig.add_subplot(1, 2, 1)
ax1.set_title("Skalarfeld kontinuierlich\n" + r'$f(x,y) = 3x^2 - 4y^2$')

# build and show the function f(x,y) = 3x^2 - 4y^2
delta = 0.025
x = y = np.arange(-3.0, 3.0, delta)
X, Y = np.meshgrid(x, y)
Z = 3 * np.power(X, 2) - 4 * np.power(Y, 2)
dxZ = 6 * X
dyZ = -8 * Y

# Create a coarser grid for the quiver plot (every 0.5 units)
x_quiver = y_quiver = np.arange(-3.0, 3.0, 0.5)
X_quiver, Y_quiver = np.meshgrid(x_quiver, y_quiver)

# Interpolate gradient values at the quiver positions
points = np.column_stack([X.flatten(), Y.flatten()])
dxZ_quiver = griddata(points, dxZ.flatten(), (X_quiver, Y_quiver))
dyZ_quiver = griddata(points, dyZ.flatten(), (X_quiver, Y_quiver))

img1 = ax1.imshow(Z, extent=[-3, 3, -3, 3], vmin=-30, vmax=30, cmap='coolwarm')
ax1.quiver(X_quiver, Y_quiver, dxZ_quiver, dyZ_quiver)

# Mark point (0,0) with a greed dot
ax1.plot(0, 0, 'go', markersize=3)

### Second chart ###

# show the second chart
ax2 = fig.add_subplot(1, 2, 2)
ax2.set_title("Skalarfeld diskret")

# load the test image
circle_png = mpimg.imread('circle.png')
circle_bw = circle_png[:, :, 0]
img2 = ax2.imshow(circle_bw, cmap="gray", vmin="0", vmax="1")

# forward derivative in x direction
circle_forward_x = np.zeros(circle_bw.shape)
circle_forward_x[:, 1:] = circle_bw[:, 1:] - circle_bw[:, :-1]
# forward derivative in y direction
circle_forward_y = np.zeros(circle_bw.shape)
circle_forward_y[1:, :] = circle_bw[1:, :] - circle_bw[:-1, :]

# build full-pixel coordinate grid for interpolation
height_img, width_img = circle_bw.shape
x_img = np.arange(width_img)
y_img = np.arange(height_img)
X_img, Y_img = np.meshgrid(x_img, y_img)
points_img = np.column_stack([X_img.flatten(), Y_img.flatten()])

# coarse quiver grid
circle_quiver_x = np.arange(0, width_img, 10)
circle_quiver_y = np.arange(0, height_img, 10)
circle_quiver_x, circle_quiver_y = np.meshgrid(
    circle_quiver_x, circle_quiver_y)

# now interpolate from full grid → quiver grid
circle_dxZ_quiver = griddata(points_img,
                             circle_forward_x.flatten(),
                             (circle_quiver_x, circle_quiver_y))
circle_dyZ_quiver = griddata(points_img,
                             circle_forward_y.flatten(),
                             (circle_quiver_x, circle_quiver_y))

# add quiver plot to the second chart with true lengths
ax2.quiver(
    circle_quiver_x, circle_quiver_y,
    circle_dxZ_quiver, circle_dyZ_quiver,
    angles='xy', scale_units='xy', pivot='mid', scale=0.005,
)

# add colorbars
fig.colorbar(img1, ax=ax1, orientation='horizontal', pad=0.06)
fig.colorbar(img2, ax=ax2, orientation='horizontal', pad=0.06)

# Always run show, to make sure everything is displayed.
plt.show()
