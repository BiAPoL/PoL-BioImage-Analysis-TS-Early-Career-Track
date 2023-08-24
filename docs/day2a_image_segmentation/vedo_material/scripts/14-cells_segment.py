from skimage import data
from vedo import Volume, show

cells = data.cells3d()[:,1,:,:]

vol = Volume(cells).permute_axes(2,1,0)
vol.smooth_gaussian((3,3,1))

iso = vol.isosurface(11000)

isos = iso.split()

show([vol, iso, isos], N=3, axes=1)
