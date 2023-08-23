from vedo import *

points = np.random.rand(2000, 3)

pts = Points(points)
pln = Plane(pos=(0.5, 0.5, 0.6), normal=(1, 0, 0), s=(1.5, 1.5))
pln.alpha(0.5)
show(pts, pln, axes=1).close()

pts = Points(points)
pts.cut_with_plane((0.5, 0.5, 0.6))
show(pts, pln, axes=1).close()
