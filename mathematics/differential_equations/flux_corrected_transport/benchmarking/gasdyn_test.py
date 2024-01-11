# run with lcpfct.py and gasdyn.py in same folder

import numpy as np
from lcpfct import lcpfct
from gasdyn import gasdyn

gammam = 1.0
relax = 0.1
pre_in = 0.1
vel_in = 0.2
preamb = 1.0
velamb = 0.5
rho_in = 0.4
rhoamb = 0.6

nx = 5
xint = np.sin(np.linspace(0, 1.0, nx+1))
vint = np.cos(np.pi * np.linspace(0, 1, nx+1))
dt = 0.01

rhon = np.array([0.4, 0.2, 0.1, 0.3, 0.6])
rvxn = np.array([0.08, 0.1, 0.17, 0.26, 0.3])
rvtn = np.array([0.1, 0.2, 0.5, 0.6, 0.8])
ergn = np.array([0.4, 0.3, 0.2, 0.4, 0.6])

print(rhon)
print(rvxn)
print(rvtn)
print(ergn)
print()

bc0 = 1
bc1 = 1
lh = lcpfct(nx+1)
lh.residiff(0.9)
lh.makegrid(xint, xint, 0, nx, 0)
gs = gasdyn(nx+1)
gs.setvars(gammam = gammam, relax = relax, pre_in = pre_in, vel_in = vel_in, preamb = preamb, velamb = velamb, rho_in = rho_in, rhoamb = rhoamb)
for i in range(1, 6):
    rhon, rvxn, rvtn, ergn = gs.gasdyn(0, nx-1, bc0, bc1, dt, rhon, rvxn, rvtn, ergn, lh)
    print(rhon)
    print(rvxn)
    print(rvtn)
    print(ergn)
    print()
