import numpy as np  # math functionality
import matplotlib.pyplot as plt  # plotting
import matplotlib.image as mpimg  # loading images

# Using subplots allows several plots to be displayed at once.
# First, a figure is created. The figsize determines default size.
fig = plt.figure(figsize=(8, 7))


########################################################
# Plot 1
########################################################

# This loads an image as a numpy matrix.
# Actually, its three stacked matrices (or a 3D array).
# Each dimension corresponds with one component: red, green and blue.
img = mpimg.imread('circle.png')

# As this is a black and white image and rgb components are more or less equal,
# we can select the first component (red) to get a simple 2D matrix.
# This is done by using numpy's array slicing operations.
# [:, :, 0] means: Select all from dimensions 1 and 2 and only the first entry from 3.
bw_img = img[:, :, 0]

# Add a subplot to our image at position 1. The subplot-grid is 2x2
axs1 = fig.add_subplot(2, 2, 1)

# A 2D matrix can be displayed using 'imshow', rendering each entry as a pixel.
image1 = axs1.imshow(bw_img)

# Why is the image not black and white? -> Because the default colormap is applied.
# When reading in the image, all values were scaled to floats between [0,1].
# We can see this by adding a colorbar to the view:
axs1.set_title('Viridis Colormap (circle.png)')

# ADDED: Arrow from (0,0) to (width//2, height//2)
height, width = bw_img.shape
axs1.annotate("", xytext=(0, 0), xy=(width//2, height//2),
              arrowprops=dict(arrowstyle="->", color="black", lw=1.5))

fig.colorbar(image1, ax=axs1)


########################################################
# Plot 2
########################################################

# To display an image with gray levels, we can use the 'gray' colormap.
axs2 = fig.add_subplot(2, 2, 2)
axs2.set_title('Gray Colormap (circle.png)')

# ADDED: Scatterplot blue dots on the image for every 10 coordinates
x_coords = np.arange(10, width, 10)
y_coords = np.arange(10, height, 10)
x_grid, y_grid = np.meshgrid(x_coords, y_coords)
axs2.scatter(x_grid.flatten(), y_grid.flatten(), color='blue', s=10, alpha=1)

image2 = axs2.imshow(bw_img, cmap='gray')
fig.colorbar(image2, ax=axs2)


########################################################
# Plot 3
########################################################

# This creates two arrays (x and y) with values between -3 and 3 in 0.025 increments.
delta = 0.025
x = y = np.arange(-3.0, 3.0, delta)

# Meshgrid builds a matrix from two given axes.
# X is a 2D array containing all row indices.
# Y is a 2D array containing all column indices.
X, Y = np.meshgrid(x, y)

# This way, the distance to the center (0,0) can be computed for each 'pixel'.
Radius = np.sqrt(X**2 + Y**2)

# From the radius, a 2D-Sin function could be derived.
# We use 'Z' to indicate a third coordinate (next to X and Y)
Z = np.sin(Radius)

# The result can be mapped to an image using a colormap
axs3 = fig.add_subplot(2, 2, 3)

# ADDED contours to the plot
contours_3 = axs3.contour(X, Y, Z, 4, colors='black')
axs3.clabel(contours_3, inline=True, fontsize=8)

axs3.set_title('2D sin')
image3 = axs3.imshow(Z, extent=[-3, 3, -3, 3], cmap='coolwarm')
fig.colorbar(image3, ax=axs3)


########################################################
# Plot 4
########################################################

# The result can also be displayed in a 3D plot
axs4 = fig.add_subplot(2, 2, 4, projection='3d')

# ADDED: 3D Contours to the plot
contours_4_3D = axs4.contour3D(X, Y, Z, 4, colors='black')
axs4.clabel(contours_4_3D, inline=True, fontsize=8)

contours_4 = axs4.contour(X, Y, Z, 4, colors='black', offset=-1, zdir='z')
axs4.clabel(contours_4, inline=True, fontsize=8)

axs4.set_title('3D plot of 2D sin')
plot1 = axs4.plot_surface(X, Y, Z, cmap='coolwarm')  # shows a surface
# plot1 = axs4.plot_wireframe(X,Y,Z, cmap='coolwarm') # shows a wireframe
# plot1 = axs4.contour3D(X,Y,Z, 80, cmap='coolwarm') # shows 3D contours
fig.colorbar(plot1, ax=axs4)


# Always run this, to make sure everything is displayed.
# Calling the program with the console allows you to rotate the 3D plot.
plt.show()
