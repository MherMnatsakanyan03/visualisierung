import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# compute a 2D function f(x,y) = sin(x^2 + y^2)
x = y = np.linspace(-2, 2, 200)
X, Y = np.meshgrid(x, y)
Z = np.sin(X**2 + Y**2)

# Note that the function can be expressed as sin(x^2 + y^2) - z = 0.
# This allows to derive the normal and the Hessian.

####################
# Task 1a          #
####################
def hessian(x,y,z):

    return 0


####################
# Task 1b          #
####################
def get_P(x,y,z):

    return 0


####################
# Task 1c          #
####################
def get_abs_nabla(x,y,z):

    return 0

def get_G(P, H, abs_nabla):

    return 0


####################
# Task 1d          #
####################
def get_T(G):

    return 0


####################
# Task 1e          #
####################
def get_F(G):

    return 0


####################
# Task 1f          #
####################
def get_kappa(T,F):

    return 0

def mean_kappa(i,j):
    # get sample values
    x = X[i,j]
    y = Y[i,j]
    z = Z[i,j]

    # TODO: put everything together



    return 0


####################
# Display Result   #
####################
fig = plt.figure(figsize=(9,7))
ax = fig.add_subplot(projection='3d')

# matrix that will hold mean kappa values for each point
mean_kappa_matrix = np.zeros(np.shape(X))

# probe each sample point of the function
# calculate mean kappa value and save
for i in range(np.shape(X)[0]):
    for j in range(np.shape(X)[1]):
        mean_kappa_matrix[i,j] = mean_kappa(i,j)

# normalize mean kappa_matrix from [minval,maxval] to [0,1]
minval = -1
maxval = 1
kappa_normalized = (mean_kappa_matrix - minval) / (maxval - minval)

# plot result
surface = ax.plot_surface(X,Y,Z,
    rcount=100,
    ccount=100,
    facecolors=mpl.cm.cool(kappa_normalized))

# add a colorbar
cmap = mpl.cm.cool
norm = mpl.colors.Normalize(vmin=minval, vmax=maxval)
fig.colorbar(mpl.cm.ScalarMappable(norm=norm, cmap=cmap),
    ax=ax,
    orientation='horizontal',
    label=r'$(\kappa_1 + \kappa_2)/2$',
    extend='both')

plt.show()