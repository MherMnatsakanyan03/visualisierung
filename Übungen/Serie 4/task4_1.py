import numpy as np  # math functionality
import matplotlib.pyplot as plt  # plotting
import matplotlib.image as mpimg  # loading images
from scipy.interpolate import griddata

fig = plt.figure(figsize=(8, 7))

### First chart ###
# show the first chart
ax1 = fig.add_subplot(1, 2, 1)
ax1.set_title("Skalarfeld kontinuierlich\n" + r'$f(x,y) = 3x^2 - 4y^2$')

# build and show the function f(x,y) = 3x^2 - 4y^2
delta = 0.025
x = y = np.arange(-3.0, 3.0, delta)
X, Y = np.meshgrid(x, y)
Z = 3 * np.power(X, 2) - 4 * np.power(Y, 2)

for i in np.arange(-3, 3.5, 0.5):
    for j in np.arange(-3, 3.5, 0.5):
        dxCircle = 6 * i
        dyCircle = -8 * j
        ax1.quiver(i, j, dxCircle, dyCircle, angles='xy',
                   scale_units='xy', color='black', scale=60, width=0.005)

        if i == 0 and j == 0:
            # Mark the special point with a green dot
            ax1.plot(i, j, 'go', markersize=3)

### Second chart ###
# show the second chart
ax2 = fig.add_subplot(1, 2, 2)
ax2.set_title("Skalarfeld diskret")

# load the test image
circle_png = mpimg.imread('circle.png')
circle_bw = circle_png[:, :, 0]

width, height = circle_bw.shape

for i in range(0, width, 10):
    for j in range(0, height, 10):
        # get forward derivative
        dxCircle = (circle_bw[i, j] - circle_bw[i - 1, j])
        dyCircle = (circle_bw[i, j] - circle_bw[i, j - 1])
        ax2.quiver(i, j, dxCircle, dyCircle, angles='xy',
                   scale_units='xy', pivot="mid", scale=0.005, width=0.006)


img1 = ax1.imshow(Z, extent=[-3, 3, -3, 3], vmin=-30, vmax=30, cmap='coolwarm')
img2 = ax2.imshow(circle_bw, cmap="gray", vmin="0", vmax="1")

# add colorbars
fig.colorbar(img1, ax=ax1, orientation='horizontal', pad=0.06)
fig.colorbar(img2, ax=ax2, orientation='horizontal', pad=0.06)

# Always run show, to make sure everything is displayed.
plt.show()
