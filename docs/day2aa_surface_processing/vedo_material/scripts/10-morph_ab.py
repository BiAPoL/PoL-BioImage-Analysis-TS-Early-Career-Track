from vedo import Mesh, show, Lines

mesh_a = Mesh("../data/mouse_limb_a.stl").c("red5")
mesh_b = Mesh("../data/mouse_limb_b.stl").c("green5")

# Here user clicks on mesh A and then B to pick 5+5 landmarks
show("Click meshes & press i", mesh_a, mesh_b).clear()

# This shows that automatic alignment may be not good enough:
# make a copy and align it to mesh B with ICP
# mesh_fail = mesh_a.clone().align_to(mesh_b, rigid=True)
# show("ICP alignment is not good enough!", mesh_fail, mesh_b).clear()

# Warp A to match B using the manually picked landmarks:
pts_a = [
    (490.395, 145.306, 891.946),
    (290.923, 913.594, 279.837),
    (651.440, 836.449, 775.404),
    (771.368, 310.359, 465.300),
    (266.866, 390.811, 941.395),
]

pts_b = [
    (1735.77, 538.276, 524.379),
    (1680.17, 1468.45, 644.959),
    (1693.76, 1164.16, 140.946),
    (1297.26, 904.027, 415.989),
    (2036.56, 763.552, 477.475),
]

if len(pts_a) > 3:
    # Make a copy and warp it
    aligned_mesh = mesh_a.clone().warp(pts_a, pts_b)

    # Create arrows to show the displacement
    arrows = Lines(pts_a, pts_b)

    # Compute the distance between the two meshes
    mesh_b.distance_to(mesh_a)
    mesh_b.cmap("coolwarm").add_scalarbar()
    mesh_a.alpha(0.2)  # make mesh A very transparent

    # Show all the objects in one go
    show("Warping Result", mesh_a, aligned_mesh, mesh_b, arrows)
