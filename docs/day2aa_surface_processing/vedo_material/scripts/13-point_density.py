"""Density plot from a distribution of points in 3D"""
from vedo import *

n = 3000
p = np.random.normal(7, 0.3, (n,3))
p[:int(n*1/3) ] += [1,0,0]       # shift 1/3 of the points along x by 1
p[ int(n*2/3):] += [1.7,0.4,0.2]

pts = Points(p, alpha=0.5)

# Create a Volume from the points representing the points density
vol = pts.density(radius=0.25).cmap('Dark2').alpha([0.1,1])
vol.add_scalarbar3d(title='Density (counts in radius)', c='k')

show(pts, vol, __doc__, axes=1).close()

