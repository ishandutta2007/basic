# run with lcpfct.py in same folder

import numpy as np
from lcpfct import lcpfct

nx = 5
dt = 0.1
xint = np.sin(np.linspace(0, 1, nx+1))
vint = np.cos(np.pi * np.linspace(0, 1, nx+1))
rho = np.array([0.1, 0.3, 0.5, 0.4, 0.2])
d = np.array([0.3, 0.1, -0.1, 0.1, 0.3])
c = np.cos(d)
print(rho)

lh = lcpfct(nx+1)
lh.residiff(0.9)
lh.makegrid(xint, xint, 0, nx, 2)
lh.velocity(vint, 0, nx, dt)
lh.sources(0, nx-1, dt, 1, c, d, 0.4, 0.4)
lh.sources(0, nx-1, dt, 3, c, d, 0.4, 0.4)
for it in range(1, 6):
    tym = it * dt
    rho = lh.lcpfct(rho, 0, nx-1, 0.1, 0.05, 0.2, -0.03, False)
    print(rho)

