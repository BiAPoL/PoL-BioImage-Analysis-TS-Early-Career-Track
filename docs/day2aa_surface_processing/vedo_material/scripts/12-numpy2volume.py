"""Create a Volume from a numpy.mgrid array
and then create a mesh from it."""
import numpy as np
from vedo import Volume, show

# Get the numpy mesh grid
X, Y, Z = np.mgrid[:30, :30, :30]

# Create a scalar field: the distance from (15, 15, 15)
scalar_field = ((X - 15) ** 2 + (Y - 15) ** 2 + (Z - 15) ** 2) / 225

# Create a Volume from the scalar field
vol = Volume(scalar_field)
print("numpy array from Volume:", vol.tonumpy().shape)

# Create a surface mesh from the Volume
lego = vol.legosurface(vmin=1, vmax=2)
lego.cmap("hot_r", vmin=1, vmax=2).add_scalarbar3d()

# show the Volume and the mesh
show(vol, lego, N=2, axes=1).close()
