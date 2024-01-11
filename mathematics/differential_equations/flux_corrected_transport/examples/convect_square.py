# Last Updated: 2019-Jul-08
# Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
# Source: https://github.com/udy11, https://gitlab.com/udy11

# This program runs periodic convection problems using lcpfct and utility routines. The profile is a square wave. The velocity is constant in space and time and the grid is kept stationary.

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

    # Compute the profile of the square wave...
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
                a[i] += 0.1 * height
            else:
                xk += x[n]
                if xk > xleft and xk < xright:
                    a[i] += 0.1 * height
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
sqr = prof(tym, xint, nx, vx)

# Set up plotting...
fig = plt.figure()
plots = []
plt.title('Square Wave Convection')
plt.ylabel('Density')
plt.xlabel('X')
plots.append(plt.plot(sqr, 'k'))

# Set residual diffusion, grid, and velocity factors in lcpfct...
lh = lcpfct(nxp)
lh.residiff(1.0)
lh.makegrid(xint, xint, 0, nx, 0)
lh.velocity(vint, 0, nx, dt)

# Begin loop over timesteps...
for it in range(1, mxstp):
    tym = it * dt
    sqr = lh.lcpfct(sqr, 0, nx-1, 0.0, 0.0, 0.0, 0.0, True)
    if it % 1 == 0:
        plots.append(plt.plot(sqr, 'k'))
vid = animation.ArtistAnimation(fig, plots, interval = 20, repeat = True, repeat_delay = 0, blit = True)
#vidwriter = animation.FFMpegWriter(fps = 30, codec ='libx264', extra_args=['-tune', 'animation'])
#vid.save('vid_sqr.mp4', writer = vidwriter)
plt.show()

