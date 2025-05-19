import numpy as np
import matplotlib.pyplot as plt
import vtk
from vtk.util.numpy_support import vtk_to_numpy

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
fig = plt.figure(figsize=(16,5))


####################
# Task 1a 
####################
# Maximum intensity projection

# create a figure
ax2 = fig.add_subplot(1,3,1)
ax2.set_title("Maximum Intensity Projection")

# compute maximum intensity projection along z-axis
mip = np.max(image, axis=2)

# plot the result
ax2.imshow(mip, cmap='gray')



####################
# Task 1b 
####################

# simulate ortographic x-ray

ax3 = fig.add_subplot(1,3,2)
ax3.set_title("Ortho X-ray")

# compute ortographic x-ray along z-axis
ortho = np.zeros((x_dim, y_dim))
for i in range(x_dim):
    for j in range(y_dim):
        ortho[i,j] = np.sum(image[i,j,:])

ax3.imshow(ortho, cmap='gray')

####################
# Task 1c 
####################
gamma = 0.0
alpha = 0.06

# Maximum intensity Difference Accumulation

ax4 = fig.add_subplot(1,3,3)
ax4.set_title("Maximum Intensity Difference Accumulation")

# Maximum Intensity Difference Accumulation (MIDA)
gamma = 0.0
alpha = 0.06

# init intermediate buffers (per ray over z)
C_out = np.ones((x_dim, y_dim), dtype=float)   # accumulated color
alpha = np.zeros((x_dim, y_dim), dtype=float)  # accumulated alpha

# march along z only
for k in range(z_dim):
    I = image[:, :, k]
    maximum = np.max(I)

    if I.all() > maximum:
        delta = I - maximum
    else:
        delta = 0
        
    if gamma <= 0.0:
        beta = 1- delta * (1.0 + gamma)
    else:
        beta = 1 - delta
    w = alpha * beta
    # accumulate weighted intensity
    C_out = beta * C_out + (1.0 - beta * alpha) * C_out
    alpha = alpha * beta + (1.0 - beta * alpha) * alpha

ax4.imshow(C_out, cmap='gray')

# Always run show, to make sure everything is displayed.
plt.show()