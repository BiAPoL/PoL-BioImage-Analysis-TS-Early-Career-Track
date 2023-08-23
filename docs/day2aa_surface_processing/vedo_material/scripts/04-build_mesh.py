# This code demonstrates how to create and display a 3D Mesh object.
# The Mesh object is created from a list of vertices and a list of faces.
# The backface color is set to violet, and vertex labels are generated for each vertex.
# The mesh object's vertices and faces are printed to the console,
# and the mesh is displayed in a 3D visualization window along with
# the vertex labels and coordinate axes.

from vedo import Mesh, show

# Define a list of vertices and a list of faces to represent a 3D mesh:
# The vertices are 3D points defined by their (x, y, z) coordinates
# The faces are defined by the indices of the vertices that form each triangle
# For example, the first triangle face is formed by vertex 0, 1, and 2
verts = [(50, 50, 50), (70, 40, 50), (50, 40, 80), (80, 70, 50)]
faces = [(0, 1, 2), (2, 1, 3), (1, 0, 3)]

# Create a polygonal Mesh object using the vertices and faces lists
mesh = Mesh([verts, faces])

# Set the backface color of the mesh to violet
mesh.backcolor("violet")

# Assign numerical labels (vertex indices) to the vertices of the mesh
# These labels are displayed as text next to the vertices in the visualization
labels = mesh.labels2d("id")

# Print information about the mesh:
# points(): returns the list of vertices (points) of the mesh
# faces() : returns the list of faces (triangles) of the mesh
print("points():", mesh.points())
print("faces() :", mesh.faces())

# Display the mesh and the vertex labels in a 3D visualization window
# axes=1 enables automatic display of the cartesian axes
show(mesh, labels, axes=1).close()
