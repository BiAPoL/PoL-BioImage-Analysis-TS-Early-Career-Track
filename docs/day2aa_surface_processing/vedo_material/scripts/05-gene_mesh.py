from vedo import *

# Gene expression data
gene_path = '../data/gene_data.npy'

# Mesh data
faces_path = '../data/mesh_faces.npy'
verts_path = '../data/mesh_nodes.npy'

# Read data
faces = np.load(faces_path)
verts = np.load(verts_path)

# Create the mesh 
msh = Mesh([verts, faces]).linewidth(1)
show(msh, bg="#282a36").close()

##############
# Adding scalar values
n = faces.shape[0] # number of faces
values = np.random.random(n)
msh.celldata["fake_data"] = values
msh.cmap("viridis")
msh.linewidth(0)
show(msh, bg="#282a36").close()

##############
values = np.load(gene_path)
msh.celldata["gene_data"] = values
msh.cmap("viridis")
show(msh, bg="#282a36", zoom='tight').close()
