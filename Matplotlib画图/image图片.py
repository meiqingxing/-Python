import matplotlib.pyplot as plt
import numpy as np

# image data
a = np.array([0.313660827978, 0.365348418405, 0.423733120134,
              0.365348418405, 0.439599930621, 0.525083754405,
              0.423733120134, 0.525083754405, 0.651536351379]).reshape(3, 3)

"""
for the value of "interpolation", check this:
http://matplotlib.org/examples/images_contours_and_fields/interpolation_methods.html
"""

plt.imshow(a, interpolation='nearest', cmap='bone', origin='lower')  # origin='upper'：颜色相反
plt.colorbar(shrink=0.6)

plt.xticks(())
plt.yticks(())

plt.show()