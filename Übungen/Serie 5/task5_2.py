import vtk # the visualization toolkit

# Data structures for point field
gridSize = 16
points = vtk.vtkPoints()

# Create point geometry (the coordinates)
for i in range(gridSize):
    for j in range(gridSize):
        # calculate coordinates
        x = i / (gridSize - 1.0) * 3.0 - 1.0
        y = j / (gridSize - 1.0) * 3.0 - 2.0
        z = x * x**2 / 3.0 + y * y**2 / 3.0 - x * x / 2.0 + y * y / 2.0
        
        # insert the point (geometry)
        points.InsertNextPoint(x,y,z)

# Create a polydata object
polyData = vtk.vtkPolyData()
polyData.SetPoints(points)

# Create a vertex glyph filter to visualize the points
vertexFilter = vtk.vtkVertexGlyphFilter()
vertexFilter.SetInputData(polyData)
vertexFilter.Update()
delaunayFilter = vtk.vtkDelaunay2D()
delaunayFilter.SetInputConnection(vertexFilter.GetOutputPort())


# Create a mapper for the vertex data
vertexMapper = vtk.vtkPolyDataMapper()
vertexMapper.SetInputConnection(vertexFilter.GetOutputPort())
delaunayMapper = vtk.vtkPolyDataMapper()
delaunayMapper.SetInputConnection(delaunayFilter.GetOutputPort())

# Create an actor for the vertex data
vertexActor = vtk.vtkActor()
vertexActor.SetMapper(vertexMapper)
vertexActor.GetProperty().SetPointSize(8) # set point size
vertexActor.GetProperty().SetRenderPointsAsSpheres(True)
vertexActor.GetProperty().SetColor(1.0, 0.0, 0.0) # red (r, g, b)

# Create an actor for the Delaunay triangulation
delaunayActor = vtk.vtkActor()
delaunayActor.SetMapper(delaunayMapper)
delaunayActor.GetProperty().SetColor(1.0, 1.0, 1.0)  # White surface color
delaunayActor.GetProperty().SetEdgeVisibility(True)  # Enable edge visibility
delaunayActor.GetProperty().SetEdgeColor(0.0, 0.0, 0.0)  # Black edges
delaunayActor.GetProperty().SetLineWidth(1)  # Set line width

# Create a renderer, render window, and interactor
renderer = vtk.vtkRenderer()
renderWindow = vtk.vtkRenderWindow()
renderWindow.AddRenderer(renderer)
renderWindowInteractor = vtk.vtkRenderWindowInteractor()
renderWindowInteractor.SetRenderWindow(renderWindow)

# Add the actors to the scene
renderer.AddActor(vertexActor)
renderer.AddActor(delaunayActor)
renderer.SetBackground(0.5, 0.5, 0.5) # Background color dark gray (r, g, b)

# Render and interact
renderWindow.Render()
renderWindowInteractor.Start()