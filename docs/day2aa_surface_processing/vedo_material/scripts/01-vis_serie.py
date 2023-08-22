from vedo import load
from vedo.applications import Browser

meshes = load("../data/meshed_*.stl")

for i in range(len(meshes)):
    meshes[i].color(i).linewidth(1)

bro = Browser(meshes, size=(1600,800))
bro.show()
bro.close()
