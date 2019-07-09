# Last Updated: 2019-Jul-08

# This program runs periodic convection problems using lcpfct and utility routines. The profile is a semicircular hump. The velocity is constant in space and time and the grid is kept stationary.

# Tested with Python 3.6.4, Numpy 1.13.3, Matplotlib 2.1.1

import numpy as np
from lcpfct import lcpfct
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def prof(t, x, n, v):
    width = 10.0
    height = 1.0
    x0 = 20.0
    n1 = n + 1

    # Compute the profile of the semicircular hump...
    xleft = (x0 - width) + v * t
    while xleft > x[n]:
        xleft -= x[n]
    while xleft < 0.0:
        xleft += x[n]
    xright = xleft + 2.0 * width

    # Loop over the cells in the numerical profile to be determined...
    a = np.zeros(n)
    for i in range(n):
        for k in range(10):
            xk = x[i] + 0.1 * (k + 0.5) * (x[i+1] - x[i])
            if xk > xleft and xk < xright:
                xcent = xleft + width
                a[i] += 0.1 * height * np.sqrt(1 - ((xk - xcent) / width)**2)
            else:
                xk += x[n]
                if xk > xleft and xk < xright:
                    xcent = xleft + width
                    a[i] += 0.1 * height * np.sqrt(1 - ((xk - xcent) / width)**2)
    return a

# The Constant Velocity Convection control parameters are initialized...
nx = 50
dx = 1.0
dt = 0.2
vx = 1.0
mxstp = 501
tym = 0.0

# The grid, velocity and the density profile are initialized...
nxp = nx + 1
xint = np.linspace(0, dx * nx, nxp)
vint = vx * np.ones(nxp)
scr = prof(tym, xint, nx, vx)

# Set up plotting...
fig = plt.figure()
plt.title('Semicircular Wave Convection')
plt.ylabel('Density')
plt.xlabel('X')
plots = []
plots.append(plt.plot(scr, 'k'))

# Set residual diffusion, grid, and velocity factors in lcpfct...
lh = lcpfct(nxp)
lh.residiff(1.0)
lh.makegrid(xint, xint, 0, nx, 0)
lh.velocity(vint, 0, nx, dt)

# Begin loop over timesteps...
for it in range(1, mxstp):
    tym = it * dt
    scr = lh.lcpfct(scr, 0, nx-1, 0.0, 0.0, 0.0, 0.0, True)
    if it % 1 == 0:
        plots.append(plt.plot(scr, 'k'))
vid = animation.ArtistAnimation(fig, plots, interval = 20, repeat = True, repeat_delay = 0, blit = True)
#vidwriter = animation.FFMpegWriter(fps = 30, codec ='libx264', extra_args=['-tune', 'animation'])
#vid.save('vid_scr.mp4', writer = vidwriter)
plt.show()

