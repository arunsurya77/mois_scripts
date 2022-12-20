import matplotlib.pyplot as plt
import numpy as np
det_fov=9.1
spec_fov=3.1
imag_mod_fov=5.4
#imag_mod_fov=3.1

imag_fov_r=np.sqrt((det_fov/2)**2+(det_fov/2)**2)
spec_fov_r=np.sqrt((det_fov/2)**2+(spec_fov/2)**2)
spec_fov_r=np.sqrt((imag_mod_fov/2)**2+(spec_fov/2)**2)
circle1 = plt.Circle((0, 0),spec_fov_r , color='green',alpha=.8)
square1 = plt.Rectangle((-det_fov /2, -det_fov/2 ),det_fov ,det_fov, color='black',alpha=.3)
fig, ax = plt.subplots()

plt.xlim(-7,7)
plt.ylim(-7,7)

#plt.grid(linestyle='--')

ax.set_aspect(1)

ax.add_artist(circle1)

ax.add_artist(square1)

plt.xlabel('arcminute')
plt.ylabel('arcminute')
plt.show()
