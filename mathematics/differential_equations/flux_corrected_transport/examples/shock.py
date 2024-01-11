# Last Updated: 2019-Jul-08
# Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
# Source: https://github.com/udy11, https://gitlab.com/udy11

# This program runs a simple 1D gasdynamic shock through a uniform grid using lcpfct and its utility routines. The fluid is ideal and inviscid with constant gamma0 = 1.4. The boundary conditions are specified external values on both ends of the system.

# Tested with Python 3.6.4, Numpy 1.13.3, Matplotlib 2.1.1

import numpy as np
from lcpfct import lcpfct
from gasdyn import gasdyn
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# The Progressing Shock test run control parameters are specified here...
mach = 5.0    # mach number of the incoming ambient flow
v0 = 3.0    # shock speed in lab frame
deltax = 1.0    # cell size
deltat = 0.05    # timestep for the calculation
alpha = 0    # (0 = Cartesian, 1 = Cylindrical, 2 = Spherical)
nx = 50    # number of cells in the computational domain
mx = 10    # number of cells initialized behind the shock
maxstp = 200    # maximum number of timesteps of length deltat

# Initialize the variables for use in gasdyn...
gamma0 = 1.4    # gas constant
preamb = 1.0    # ambient (unshocked) pressure on the right
rhoamb = 1.0    # density of the unshocked fluid on the right
relax = 0.0    # relaxation rate, not used when bc0, bc1 = 1
gammam = gamma0 - 1.0

# The Rankine-Hugoniot conditions are set for boundaries...
csamb = np.sqrt(gamma0 * preamb / rhoamb)
velamb = -mach * csamb
vel_in = velamb * (gammam + 2.0 / mach**2) / (gamma0 + 1.0)
rho_in = rhoamb * velamb / vel_in
pre_in = preamb - rho_in * vel_in**2 + rhoamb * velamb**2
velamb += v0
vel_in += v0
ergamb = preamb / (gamma0 - 1.0) + 0.5 * rhoamb * velamb**2
erg_in = pre_in / (gamma0 - 1.0) + 0.5 * rho_in * vel_in**2

# Define the cell interface locations and physical variables...
rhon = np.empty(nx)
rvxn = np.empty(nx)
rvtn = np.empty(nx)
ergn = np.empty(nx)
nxp = nx + 1
xint = np.linspace(0, nx * deltax, nxp)
for i in range(mx, nx):
    rhon[i] = rhoamb
    rvxn[i] = rhoamb * velamb
    rvtn[i] = 0.0
    ergn[i] = ergamb
for i in range(mx):
    rhon[i] = rho_in
    rvxn[i] = rho_in * vel_in
    rvtn[i] = 0.0
    ergn[i] = erg_in

# Set up plotting...
plots = []
fig, ((ax1, ax2, ax3), (ax4, ax5, ax6)) = plt.subplots(2, 3)
vnew = rvxn / rhon
pnew = gammam * (ergn - 0.5 * rvxn * vnew)
tnew = pnew / rhon
ax1.set_title('Density')
pl1, = ax1.plot(xint[:nx], rhon, 'k')
ax2.set_title('Temperature')
pl2, = ax2.plot(xint[:nx], tnew, 'k')
ax3.set_title('Pressure')
pl3, = ax3.plot(xint[:nx], pnew, 'k')
ax4.set_title('Velocity')
pl4, = ax4.plot(xint[:nx], vnew, 'k')
ax5.set_title('Energy')
pl5, = ax5.plot(xint[:nx], ergn, 'k')
plots.append([pl1, pl2, pl3, pl4, pl5])

# Begin loop over timesteps...
bc0 = 3
bc1 = 3
lh = lcpfct(nxp)
lh.residiff(1.0)
lh.makegrid(xint, xint, 0, nx, alpha)
gs = gasdyn(nxp)
gs.setvars(gammam = gammam, relax = relax, pre_in = pre_in, vel_in = vel_in, preamb = preamb, velamb = velamb, rho_in = rho_in, rhoamb = rhoamb)
for i in range(maxstp):
    rhon, rvxn, rvtn, ergn = gs.gasdyn(0, nx-1, bc0, bc1, deltat, rhon, rvxn, rvtn, ergn, lh)
    vnew = rvxn / rhon
    pnew = gammam * (ergn - 0.5 * rvxn * vnew)
    tnew = pnew / rhon
    pl1, = ax1.plot(xint[:nx], rhon[:nx], 'k')
    pl2, = ax2.plot(xint[:nx], tnew[:nx], 'k')
    pl3, = ax3.plot(xint[:nx], pnew[:nx], 'k')
    pl4, = ax4.plot(xint[:nx], vnew[:nx], 'k')
    pl5, = ax5.plot(xint[:nx], ergn[:nx], 'k')
    plots.append([pl1, pl2, pl3, pl4, pl5])
vid = animation.ArtistAnimation(fig, plots, interval = 20, repeat = True, repeat_delay = 0, blit = True)
#vidwriter = animation.FFMpegWriter(fps = 30, codec ='libx264', extra_args=['-tune', 'animation'])
#vid.save('vids.mp4', writer = vidwriter)
plt.show()

