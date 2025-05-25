import numpy as np
import matplotlib.pyplot as plt
import vtk
from vtk.util.numpy_support import vtk_to_numpy
import time

# ── install a DummyController so the parallel NRRD reader will run in single‐process mode ──
dummy = vtk.vtkDummyController()
vtk.vtkMultiProcessController.SetGlobalController(dummy)
# ────────────────────────────────────────────────────────────────────────────────

# read a volume image
reader = vtk.vtkNrrdReader()
reader.SetFileName("MRHead.nrrd")
reader.Update()
imageData = reader.GetOutput()

# convert from vtkImageData to numpy array
x_dim, y_dim, z_dim = imageData.GetDimensions()
sc = imageData.GetPointData().GetScalars()
image = vtk_to_numpy(sc)
image = image.reshape(x_dim, y_dim, z_dim, order='F')
image = np.rot90(np.flip(image, axis=1))

# normalize image values
image = np.divide(image, float(np.max(image)))

# create a figure
fig = plt.figure(figsize=(16, 5))


####################
# Task 1a
####################
# Maximum intensity projection

# create a figure
ax2 = fig.add_subplot(1, 3, 1)
ax2.set_title("Maximum Intensity Projection")

# compute maximum intensity projection along z-axis
mip = np.max(image, axis=2)

# plot the result
ax2.imshow(mip, cmap='gray')


####################
# Task 1b
####################

# simulate ortographic x-ray

ax3 = fig.add_subplot(1, 3, 2)
ax3.set_title("Ortho X-ray")

# compute ortographic x-ray along z-axis

start = time.time()
ortho_z = np.zeros((x_dim, y_dim))
for k in range(z_dim):
    ortho_z += image[:, :, k]
stop = time.time()
print("Time for ortho projection: z-loop ", stop - start)

""" start = time.time()
ortho_x_y = np.zeros((x_dim, y_dim))
for i in range(x_dim):
    for j in range(y_dim):
        ortho_x_y[i,j] = np.sum(image[i,j,:])
stop = time.time()
print("Time for ortho projection x-y-loop: ", stop - start) """

ax3.imshow(ortho_z, cmap='gray')

####################
# Task 1c
####################
gamma = 0.0
alpha_out = 0.06

# Maximum intensity Difference Accumulation

ax4 = fig.add_subplot(1, 3, 3)
ax4.set_title("Maximum Intensity Difference Accumulation")

# Maximum Intensity Difference Accumulation (MIDA)
gamma = 0.0
alpha_out = 0.06            # per‐slice opacity

# accumulation buffers
C_mida = np.zeros((x_dim, y_dim), dtype=float)   # color
A_mida = np.zeros((x_dim, y_dim), dtype=float)   # opacity
I_max = image[:, :, 0].copy()                    # initial max‐intensity

# loop over slices
for k in range(z_dim):
    I = image[:, :, k]

    # delta = max(I - I_max, 0)
    delta = np.maximum(I - I_max, 0.0)
    # update running max
    I_max = np.maximum(I_max, I)

    # beta depending on gamma
    if gamma <= 0:
        beta = 1.0 - delta * (1.0 + gamma)
    else:
        beta = 1.0 - delta

    # accumulate color & opacity
    C_mida = beta * C_mida + (1.0 - beta * A_mida) * I
    A_mida = beta * A_mida + (1.0 - beta * A_mida) * alpha_out

ax4.imshow(C_mida, cmap='gray')

# Always run show, to make sure everything is displayed.
plt.show()
