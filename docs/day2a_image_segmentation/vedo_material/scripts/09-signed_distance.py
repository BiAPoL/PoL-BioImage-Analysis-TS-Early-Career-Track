from vedo import Mesh, dataurl, Plotter

msh = Mesh(dataurl + "panther.stl")

vol = msh.signed_distance(dims=[25, 125, 25])
iso = vol.isosurface(0.0)

plt = Plotter()
plt += iso.wireframe()

for i in range(0, 25, 5):
    plt += vol.xslice(i).cmap("jet")

# vol.write("panther.tif")
plt.show(axes=1)
plt.close()
