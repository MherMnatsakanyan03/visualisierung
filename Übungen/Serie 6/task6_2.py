import vtk
import numpy as np

# Returns vertex-ids in a mesh, which share
# an edge with the vertex at a specified seed id,
# i.e., finds the one-ring neighborhood
def getConnectedVertices(mesh, seed_id):
    # use a set to avoid multiple references to the same point
    connected_vertex_ids = set()

    # retrieve all cells containing the seed point
    # (cells are commonly polygons, edges and vertices)
    cellIdList = vtk.vtkIdList()
    mesh.GetPointCells(seed_id, cellIdList)

    # iterate these cells
    for i in range(cellIdList.GetNumberOfIds()):
        cell = mesh.GetCell(cellIdList.GetId(i))
        if cell.GetNumberOfEdges() <= 0:
            # cell has no edges, so it's a line or a point
            line = vtk.vtkLine.SafeDownCast(cell)
            if not line: # it's a point
                continue
            else: # it's a line
                p0 = line.GetPointId(0)
                p1 = line.GetPointId(1)
                if p0 == seed_id:
                    connected_vertex_ids.add(p1)
                else:
                    connected_vertex_ids.add(p0)
            continue

        # if we get to here, the cell is a polygon, so extract its border edges
        for e in range(cell.GetNumberOfEdges()):
            edge = cell.GetEdge(e)
            pointIdList = edge.GetPointIds()

            if(pointIdList.GetId(0) == seed_id or pointIdList.GetId(1) == seed_id):
                if pointIdList.GetId(0) == seed_id:
                    connected_vertex_ids.add(pointIdList.GetId(1))
                else:
                    connected_vertex_ids.add(pointIdList.GetId(0))
    return connected_vertex_ids

# Create a sphere
sphere = vtk.vtkSphereSource()
sphere.SetPhiResolution(12)
sphere.SetThetaResolution(12)
sphere.Update()

# retrieve the mesh
mesh = sphere.GetOutput()

# apply random noise on top of sphere points
np.random.seed(19640804)
for i in range(mesh.GetNumberOfPoints()):
    displacement = np.random.rand(3) * 0.09
    p = np.array(mesh.GetPoint(i))
    p += displacement
    mesh.GetPoints().SetPoint(i, p)

# copy the mesh to create the smoothed geometries
mesh_laplace = vtk.vtkPolyData()
mesh_low_pass = vtk.vtkPolyData()
mesh_laplace.DeepCopy(mesh)
mesh_low_pass.DeepCopy(mesh)


####################
# Task 2           #
####################

# Laplace smoothing
k_laplace = 5
lambda_laplace = 0.5
for _ in range(k_laplace):
    points = mesh_laplace.GetPoints()
    for j in range(points.GetNumberOfPoints()):
        neighbors = getConnectedVertices(mesh_laplace, j)
        if not neighbors:
            continue
        print(neighbors)
        # old position
        old_pos = np.array(points.GetPoint(j))
        # average of neighbor positions
        avg_pos = np.zeros(3)
        for neighbor_ids in neighbors:
            avg_pos += np.array(points.GetPoint(neighbor_ids))
        avg_pos /= len(neighbors)
        # Laplace step with lambda
        new_pos = old_pos + lambda_laplace * (avg_pos - old_pos)
        points.SetPoint(j, new_pos)
    

# Low-pass filter

k_low_pass = 10
λ = 0.5
μ = -1.02 * λ
n = mesh_low_pass.GetNumberOfPoints()

for _ in range(k_low_pass):
    points = mesh_low_pass.GetPoints()
    # 1) read into a numpy array
    P0 = np.array([points.GetPoint(i) for i in range(n)])
    P1 = P0.copy()

    # 2) λ-step (pure Laplace) into P1
    for j in range(n):
        neighbors = getConnectedVertices(mesh_low_pass, j)
        if not neighbors: continue
        L = np.mean(P0[list(neighbors)], axis=0)
        P1[j] = P0[j] + λ * (L - P0[j])

    # 3) μ-step (inverse Laplace) into P2
    P2 = P1.copy()
    for j in range(n):
        neighbors = getConnectedVertices(mesh_low_pass, j)
        if not neighbors: continue
        L1 = np.mean(P1[list(neighbors)], axis=0)
        P2[j] = P1[j] + μ * (L1 - P1[j])

    # 4) write back
    for j in range(n):
        points.SetPoint(j, P2[j])
    mesh_low_pass.Modified()









####################
# Scene            #
####################
mapper_orig = vtk.vtkPolyDataMapper()
mapper_orig.SetInputData(mesh)
actor_orig = vtk.vtkActor()
actor_orig.SetMapper(mapper_orig)
actor_orig.GetProperty().SetInterpolationToFlat()

mapper_laplace = vtk.vtkPolyDataMapper()
mapper_laplace.SetInputData(mesh_laplace)
actor_laplace = vtk.vtkActor()
actor_laplace.SetMapper(mapper_laplace)
actor_laplace.GetProperty().SetInterpolationToFlat()
actor_laplace.SetPosition(1.5, 0, 0)

mapper_low_pass = vtk.vtkPolyDataMapper()
mapper_low_pass.SetInputData(mesh_low_pass)
actor_low_pass = vtk.vtkActor()
actor_low_pass.SetMapper(mapper_low_pass)
actor_low_pass.GetProperty().SetInterpolationToFlat()
actor_low_pass.SetPosition(3.0, 0, 0)


####################
# Renderpipeline   #
####################
# Create the renderer, add actors
renderer = vtk.vtkRenderer()
renderer.AddActor(actor_orig)
renderer.AddActor(actor_laplace)
renderer.AddActor(actor_low_pass)
renderer.SetBackground(1.0, 1.0, 1.0)

# Create the render window
renderWindow = vtk.vtkRenderWindow()
renderWindow.SetSize(1280, 720)
renderWindow.AddRenderer(renderer)

# Create the interactor
renderWindowInteractor = vtk.vtkRenderWindowInteractor()
renderWindowInteractor.SetRenderWindow(renderWindow)
renderWindowInteractor.SetInteractorStyle(vtk.vtkInteractorStyleTrackballCamera())

# This starts the event loop.
renderWindowInteractor.Start()