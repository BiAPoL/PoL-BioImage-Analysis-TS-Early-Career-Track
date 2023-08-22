import numpy as np
import matplotlib.pyplot as matplt
import vedo

############################################
# # matplotlib
# Create some points
x = np.array([1, 2, 3, 4, 5])
y = np.array([4, 5, 2, 5, 4])
pts = np.c_[x, y]  # Convert to 2D array

# Show with matplotlib
matplt.scatter(x, y)
matplt.show()

# If you want to change the style of the points
# we have to modify the `scatter` plot.
matplt.scatter(x, y, color="#b22222")
matplt.show()
matplt.close()

############################################
# In Vedo, we create an object for the points
# and we add the ✨aesthetics✨ on the points object
points = vedo.Points(pts).color("#b22222").point_size(20)

# This shows any object and returns a Plotter object
plt = vedo.show(points, axes=1)  # axes style 1
plt.close()

#############################################
# 🔥 Can you add a line through the points?
# Hint: don't hesitate to check the documentation!
# line = vedo.Line(pts).c("#22b2b2")
# plt = vedo.show(points, line, axes=1)
# plt.close()
