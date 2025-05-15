import numpy as np # math functionality
import matplotlib.pyplot as plt # plotting

fig = plt.figure(figsize=(8,7))

ax = fig.add_subplot()
ax.set_title("Marching Squares")

# G holds some scalar values of a grid
G = np.array([[-1,-3,-3,-6,-9],
              [ 1, 1,-3,-6,-9],
              [ 2, 3, 3,-9,-9],
              [ 2, 3, 3,-9,-9],
              [ 9, 6, 6,-6,-9]])
G_rows = G.shape[0]
G_cols = G.shape[1]

# Build coordinates
x = np.linspace(0, 1, G_cols)
y = np.linspace(1, 0, G_rows)
X, Y = np.meshgrid(x,y)

####################
# Task 1           #
####################

# Marching Squares
for i in range(G_rows-1):
    for j in range(G_cols-1):
        # get the 4 corners of the cell
        p0 = G[i][j]
        p1 = G[i][j+1]
        p2 = G[i+1][j+1]
        p3 = G[i+1][j]

        # find zeros (if lambda is in [0,1])
        lambda_p0_p1 = p0 / (p0 - p1)
        lambda_p1_p2 = p1 / (p1 - p2)
        lambda_p2_p3 = p2 / (p2 - p3)
        lambda_p3_p0 = p3 / (p3 - p0)

        # if lambda is in [0,1], then the edge is crossed
        points = []
        
        # Check edge p0-p1
        if 0 <= lambda_p0_p1 <= 1:
            x_p0_p1 = x[j] + lambda_p0_p1 * (x[j+1] - x[j])
            y_p0_p1 = y[i]
            points.append((x_p0_p1, y_p0_p1))
        
        # Check edge p1-p2
        if 0 <= lambda_p1_p2 <= 1:
            x_p1_p2 = x[j+1]
            y_p1_p2 = y[i] - lambda_p1_p2 * (y[i] - y[i+1])
            points.append((x_p1_p2, y_p1_p2))
        
        # Check edge p2-p3
        if 0 <= lambda_p2_p3 <= 1:
            x_p2_p3 = x[j+1] - lambda_p2_p3 * (x[j+1] - x[j])
            y_p2_p3 = y[i+1]
            points.append((x_p2_p3, y_p2_p3))
        
        # Check edge p3-p0
        if 0 <= lambda_p3_p0 <= 1:
            x_p3_p0 = x[j]
            y_p3_p0 = y[i+1] + lambda_p3_p0 * (y[i] - y[i+1])
            points.append((x_p3_p0, y_p3_p0))
        
        # Draw the line segments if we found exactly 2 intersection points
        if len(points) == 2:
            ax.plot([points[0][0], points[1][0]], [points[0][1], points[1][1]], 'g-', linewidth=2)
        elif len(points) == 3:
            # ignore the case where 3 points are found
            continue
        elif len(points) == 4:
            # if 4 points are found, the corners are "crossed"
            # that means that top-left and bottom-right are connected
            # and top-right and bottom-left are connected
            # check which is positive and which is negative
            # and draw lines depending whether the middle point is positive or negative

            if p0 > 0:
                ax.plot([points[0][0], points[3][0]], [points[0][1], points[3][1]], 'g-', linewidth=2)
                ax.plot([points[1][0], points[2][0]], [points[1][1], points[2][1]], 'g-', linewidth=2)
            else:
                ax.plot([points[0][0], points[1][0]], [points[0][1], points[1][1]], 'g-', linewidth=2)
                ax.plot([points[2][0], points[3][0]], [points[2][1], points[3][1]], 'g-', linewidth=2)

####################
# Plot the grid    #
####################
# set XY-ticks to resemble grid lines
ax.set_xticks(np.linspace(0, 1, G_cols))
ax.set_yticks(np.linspace(0, 1, G_rows))
ax.grid(True)
ax.set_axisbelow(True)
ax.get_xaxis().set_ticklabels([])
ax.get_yaxis().set_ticklabels([])

# annotate each gridpoint with the scalar value in G
ax.scatter(X, Y, s=200)
for i in range(G_rows):
    for j in range(G_cols):
        ax.annotate(G[i][j], xy=(X[i][j], Y[i][j]), ha='center', va='center', c='white')

# Always run show, to make sure everything is displayed.
plt.show()