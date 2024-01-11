# Last Updated: 2019-Jul-10
# Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
# Source: https://github.com/udy11, https://gitlab.com/udy11

# Flux Corrected Transport algorithm to solve Generalized Continuity Equations
# Based on the LCPFCT version by Lab. for Computational Physics and Fluid Dynamics (NRL/MR/6410-93-7192 (April 1993))
# Original: J.P. Boris; Code 4400, NRL, Feb. 1987

# Tested with Python 3.6.4, Numpy 1.13.3

# NOTE:
# Indices passed to all the functions are both inclusive, unlike usual python conventions
# All modes (like in makegrid(), sources(), copygrid(), new_grid()) are one less than what they are in original code. So if you are using alpha=2 in original LCPFCT's MAKEGRID(), use alpha=1 in this makegrid()

import numpy as np
import sys

class lcpfct:
    bignum = sys.float_info.max
    ftpi = 4.0 * np.pi / 3.0
    nindmax = 150

    def __init__(s, npt):
        # holds scratch arrays for use by lcpfct() and cnvfct()
        s.scrh = np.empty(npt)
        s.scr1 = np.empty(npt)
        s.diff = np.empty(npt)
        s.flxh = np.empty(npt)
        s.fabs = np.empty(npt)
        s.fsgn = np.empty(npt)
        s.term = np.empty(npt)
        s.terp = np.empty(npt)
        s.lnrhot = np.empty(npt)
        s.lorhot = np.empty(npt)
        s.rhot = np.empty(npt)
        s.rhotd = np.empty(npt)

        # holds OLD geometry, grid, area and volume information
        s.lop = np.empty(npt)
        s.lnp = np.empty(npt)
        s.ahp = np.empty(npt)
        s.rlnp = np.empty(npt)
        s.lhp = np.empty(npt)
        s.rlhp = np.empty(npt)
        s.rohp = np.empty(npt)
        s.rnhp = np.empty(npt)
        s.adugthp = np.empty(npt)

        # holds FCT geometry, grid, area and volume information
        s.lo = np.empty(npt)
        s.ln = np.empty(npt)
        s.ah = np.empty(npt)
        s.rln = np.empty(npt)
        s.lh = np.empty(npt)
        s.rlh = np.empty(npt)
        s.roh = np.empty(npt)
        s.rnh = np.empty(npt)
        s.adugth = np.empty(npt)
        s.rlo = np.empty(npt)

        # holds velocity-dependent flux coefficients
        s.hadudth = np.empty(npt)
        s.nulh = np.empty(npt)
        s.mulh = np.empty(npt)
        s.epsh = np.empty(npt)
        s.vdtodr = np.empty(npt)

        # holds the source array and diffusion coefficient
        s.source = np.zeros(npt)
        s.diff1 = 0.999

        # holds a scalar list of special cell information
        s.nind = 0
        s.index = 0
        s.scalars = 0

    def lcpfct(s, rhoo, i0, i1, srho0, vrho0, srho1, vrho1, pbc):
        ''' This function solves generalized continuity equations of the form: d(RHO)/dt = -div(rho*v) + SOURCES in the users's choice of cartesian, cylindrical or spherical coordinates. A facility is included to allow definition of other coordinates. The grid can be Eulerian, sliding rezone, or Lagrangian, and can be arbitrarily spaced. The algorithm is a low phase-error FCT algorithm, vectorized and optimized for a combination of speed and flexibility. A complete description appears in the NRL Memorandum Report: "LCPFCT - A Flux-Corrected Transport Algorithm for Solving Generalized Continuity Equations", NRL/MR/6410-93-7192 (April 1993).

        INPUT:
        rhoo = I/P real array: grid point densities at start of step (1d float array)
        i0, i1 = first and last grid points of integration (both inclusive) (int)
        srho0 = boundary guard cell factor at cell (i0-1) (1d float array)
        vrho0 = boundary value added to guard cell (i0-1) (1d float array)
        srho1 = boundary guard cell factor at cell (i1+1) (1d float array)
        vrho1 = boundary value added to guard cell (i1+1) (1d float array)
        pbc = uses periodic boundaries if True (bool)

        OUTPUT:
        rhon = grid point densities at end of step (1d float array of same size as rhoo)

        In this routine, the last interface at radhn[i1p] is the outer boundary of the last cell indexed i1. The first interface at radhn[i0] is the outer boundary of the integration domain before the first cell indexed i0.
        
        Underflows can occur when the function being transported has a region of zeros. The calculations misconserve by one or two bits per cycle. Relative phase and amplitude errors (for smooth functions) are typically a few percent for characteristic lengths of 1-2 cells (wavelengths of order 10 cells). The jump conditions for shocks are generally accurate to better than 1 percent.
        
        Auxiliary Functions: cnvfct(), conserve(), copygrid(), makegrid(), new_grid(), residiff(), set_grid(), sources(), velocity(), zerodiff(), zeroflux().
        The detailed documentation report provided (or the listing below) explains the definitions and use of the arguments to these other routines. These routines are not called from lcpfct() itself but are controlled by calls from the user. Routines makegrid(), velocity() and sources() must first be called to set the grid geometry, velocity-dependent flux and diffusion coefficients, and external source arrays used by lcpfct(). The other routines may be called to perform other functions such as to modify boundary conditions, to perform special grid operations, or compute conservation sums.
        '''
        i0p = i0 + 1
        i1p = i1 + 1

        # calculate convective and diffusive fluxes
        if pbc:
            rho0m = rhoo[i1]
            rho1p = rhoo[i0]
        else:
            rho0m = srho0 * rhoo[i0] + vrho0
            rho1p = srho1 * rhoo[i1] + vrho1

        s.diff[i0] = s.nulh[i0] * (rhoo[i0] - rho0m)
        s.flxh[i0] = s.hadudth[i0] * (rhoo[i0] + rho0m)
        for i in range(i0p, i1p):
            s.diff[i] = s.nulh[i] * (rhoo[i] - rhoo[i-1])
            s.flxh[i] = s.hadudth[i] * (rhoo[i] + rhoo[i-1])
        s.diff[i1p] = s.nulh[i1p] * (rho1p - rhoo[i1])
        s.flxh[i1p] = s.hadudth[i1p] * (rho1p + rhoo[i1])

        # calculate lorhot (the transported mass elements) and lnrhot (the transported & diffused mass elements)
        for i in range(i0, i1p):
            s.lorhot[i] = s.lo[i] * rhoo[i] + s.source[i] + (s.flxh[i] - s.flxh[i+1])
            s.lnrhot[i] = s.lorhot[i] + (s.diff[i+1] - s.diff[i])
            s.rhot[i] = s.lorhot[i] * s.rlo[i]
            s.rhotd[i] = s.lnrhot[i] * s.rln[i]

        # evaluate the boundary conditions for (rhot, rhotd)
        if pbc:
            rhot0m = s.rhot[i1]
            rhot1p = s.rhot[i0]
            rhotd0m = s.rhotd[i1]
            rhotd1p = s.rhotd[i0]
        else:
            rhot0m = srho0 * s.rhot[i0] + vrho0
            rhot1p = srho1 * s.rhot[i1] + vrho1
            rhotd0m = srho0 * s.rhotd[i0] + vrho0
            rhotd1p = srho1 * s.rhotd[i1] + vrho1

        # calculate the transported antidiffusive fluxes and transported and diffused density differences
        s.flxh[i0] = s.mulh[i0] * (s.rhot[i0] - rhot0m)
        s.diff[i0] = s.rhotd[i0] - rhotd0m
        s.fabs[i0] = np.abs(s.flxh[i0])
        s.fsgn[i0] = np.sign(s.diff[i0]) * np.abs(s.diff1)
        for i in range(i0p, i1p):
            s.flxh[i] = s.mulh[i] * (s.rhot[i] - s.rhot[i-1])
            s.diff[i] = s.rhotd[i] - s.rhotd[i-1]
        s.flxh[i1p] = s.mulh[i1p] * (rhot1p - s.rhot[i1])
        s.diff[i1p] = rhotd1p - s.rhotd[i1]

        # calculate the magnitude & sign of the antidiffusive flux followed by the flux-limiting changes on the right and left
        for i in range(i0, i1p):
            s.fabs[i+1] = np.abs(s.flxh[i+1])
            s.fsgn[i+1] = np.sign(s.diff[i+1]) * np.abs(s.diff1)
            s.term[i+1] = s.fsgn[i+1] * s.ln[i] * s.diff[i]
            s.terp[i] = s.fsgn[i] * s.ln[i] * s.diff[i+1]
        if pbc:
            s.terp[i1p] = s.terp[i0]
            s.term[i0] = s.term[i1p]
        else:
            s.terp[i1p] = s.bignum
            s.term[i0] = s.bignum

        # correct the transported fluxes completely and then calculate the new flux-corrected transport densities
        rhon = np.array(rhoo)
        s.flxh[i0] = s.fsgn[i0] * max(0.0, min(s.term[i0], s.fabs[i0], s.terp[i0]))
        for i in range(i0, i1p):
            s.flxh[i+1] = s.fsgn[i+1] * max(0.0, min(s.term[i+1], s.fabs[i+1], s.terp[i+1]))
            rhon[i] = s.rln[i] * (s.lnrhot[i] + (s.flxh[i] - s.flxh[i+1]))
            s.source[i] = 0.0

        return rhon

    def makegrid(s, radho, radhn, i0, i1p, alpha):
        ''' Initializes geometry variables and coefficients. It should be called first to initialize the grid. The grid must be defined for all of the grid interfaces from i0 to i1p. Subsequent calls to velocity() and lcpfct() can work on only portions of the grid, however, to perform restricted integrations on separate line segments.
        
        INPUT:
        radho = old cell interface positions (1d float array)
        radhn = new cell interface positions (1d float array)
        i0, i1p = first and last cell interfaces (both inclusive) (int)
        alpha = decides geometry
            = 0 cartesian
            = 1 cylindrical
            = 2 spherical
            = 3 user supplied
        '''
        i0p = i0 + 1
        i1 = i1p - 1

        # store the old and new grid interface locations from input and then update the new and average interface and grid coefficients
        for i in range(i0, i1p+1):
            s.roh[i] = radho[i]
            s.rnh[i] = radhn[i]

        # cartesian coordinates
        if alpha == 0:
            s.ah[i1p] = 1
            for i in range(i0, i1p):
                s.ah[i] = 1.0
                s.lo[i] = s.roh[i+1] - s.roh[i]
                s.ln[i] = s.rnh[i+1] - s.rnh[i]
        # cylindrical coordinates (radial)
        elif alpha == 1:
            s.diff[i0] = s.rnh[i0] * s.rnh[i0]
            s.scrh[i0] = s.roh[i0] * s.roh[i0]
            s.ah[i1p] = np.pi * (s.roh[i1p] + s.rnh[i1p])
            for i in range(i0, i1p):
                s.ah[i] = np.pi * (s.roh[i] + s.rnh[i])
                s.scrh[i+1] = s.roh[i+1] * s.roh[i+1]
                s.lo[i] = np.pi * (s.scrh[i+1] - s.scrh[i])
                s.diff[i+1] = s.rnh[i+1] * s.rnh[i+1]
                s.ln[i] = np.pi * (s.diff[i+1] - s.diff[i])
        # spherical coordinates (radial)
        elif alpha == 2:
            s.scr1[i0] = s.roh[i0]**3
            s.diff[i0] = s.rnh[i0]**3
            s.scrh[i1p] = (s.roh[i1p] + s.rnh[i1p]) * s.roh[i1p]
            s.ah[i1p] = s.ftpi * (s.scrh[i1p] + s.rnh[i1p] * s.rnh[i1p])
            for i in range(i0, i1p):
                s.scr1[i+1] = s.roh[i+1]**3
                s.diff[i+1] = s.rnh[i+1]**3
                s.scrh[i] = (s.roh[i] + s.rnh[i]) * s.roh[i]
                s.ah[i] = s.ftpi * (s.scrh[i] + s.rnh[i] * s.rnh[i])
                s.lo[i] = s.ftpi * (s.scr1[i+1] - s.scr1[i])
                s.ln[i] = s.ftpi * (s.diff[i+1] - s.diff[i])
        # user supplied (define below)
        elif alpha == 3:
            pass
            
        # additional system-independent geometric variables
        for i in range(i0, i1p):
            s.rlo[i] = 1.0 / s.lo[i]
            s.rln[i] = 1.0 / s.ln[i]
        s.lh[i0] = s.ln[i0]
        s.rlh[i0] = s.rln[i0]
        for i in range(i0p, i1p):
            s.lh[i] = 0.5 * (s.ln[i] + s.ln[i-1])
            s.rlh[i] = 0.5 * (s.rln[i] + s.rln[i-1])
        s.lh[i1p] = s.ln[i1]
        s.rlh[i1p] = s.rln[i1]
        for i in range(i0, i1p+1):
            s.adugth[i] = s.ah[i] * (s.rnh[i] - s.roh[i])

    def velocity(s, uh, i0, i1p, dt):
        ''' Calculates all velocity-dependent coefficients for the lcpfct() & cnvfct() routines. This routine must be called before either lcpfct() or cnvfct() is called. makegrid() must be called earlier to set grid and geometry data used here.

        INPUT:
        uh = flow velocity at cell interfaces (1d float array of size npt)
        i0 = first cell interface of integration (inclusive) (int)
        i1p = last cell interface (inclusive) (int)
        dt = stepsize for the time integration (float)

        Calculate 0.5 * interface area * velocity difference * dt (hadudth). Next, calculate the interface epsilon (epsh = uh*dt/dx). Then find the diffusion nulh and antidiffusion mulh coefficients. The variation with epsilon gives fourth-order accurate phases when the grid is uniform, the velocity constant, and scrh is set to zero. With scrh nonzero (as below) slightly better results are obtained in some of the tests. Optimal performance, of course, depends on the application.
        '''
        i0p = i0 + 1
        i1 = i1p - 1
        rdt = 1.0 / dt
        dth = 0.5 * dt
        dt2 = 2.0 * dt
        dt4 = 4.0 * dt
        r3 = 1.0 / 3.0
        r6 = 1.0 / 6.0
        for i in range(i0, i1p+1):
            s.hadudth[i] = dt * s.ah[i] * uh[i] - s.adugth[i]
            s.epsh[i] = s.hadudth[i] * s.rlh[i]
            s.scrh[i] = min(r6, np.abs(s.epsh[i]))
            s.scrh[i] = s.scrh[i]**2 * r3
            s.hadudth[i] = 0.5 * s.hadudth[i]
            s.nulh[i] = r6 + (s.epsh[i] + s.scrh[i]) * (s.epsh[i] - s.scrh[i]) * r3
            s.mulh[i] = 0.25 - 0.5 * s.nulh[i]
            s.nulh[i] = s.lh[i] * (s.nulh[i] + s.scrh[i])
            s.mulh[i] = s.lh[i] * (s.mulh[i] + s.scrh[i])
            s.diff[i] = uh[i] - rdt * (s.rnh[i] - s.roh[i])
        # calculate vdtodr for cnvfct()
        s.vdtodr[i0] = dt2 * s.diff[i0] / (s.rnh[i0p] - s.rnh[i0] +  s.roh[i0p] - s.roh[i0])
        for i in range(i0p, i1p):
            s.vdtodr[i] = dt4 * s.diff[i] / (s.rnh[i+1] - s.rnh[i-1] + s.roh[i+1] - s.roh[i-1])
        s.vdtodr[i1p] = dt2 * s.diff[i1p] / (s.rnh[i1p] - s.rnh[i1] + s.roh[i1p] - s.roh[i1])

    def sources(s, i0, i1, dt, mode, c, d, d0, d1):
        ''' Accumulates different source terms.

        INPUT:
        i0, i1 = first and last cells to be integrated (both inclusive) (int)
        dt = stepsize for time integration (float)
        mode = decides how to add sources (int)
             = 0 computes  +DIV(D)
             = 1 computes  +C*GRAD(D)
             = 2 adds +D to the sources
             = 3 +DIV(D) from interface data
             = 4 +C*GRAD(D) from interface data
             = 5 +C for list of scalar indices
        c = array of source variables (1d float array of size npt)
        d = I/P real array (NPT) : array of source variables (1d float array of size npt)
        d0, d1 = first and last boundary values of d (float)
        '''
        i0p = i0 + 1
        i1p = i1 + 1
        dth = 0.5 * dt
        dtq = 0.25 * dt

        # [+DIV(D)] is computed conservatively and added to SOURCE
        if mode == 0:
            s.scrh[i0] = dt * s.ah[i0] * d0
            s.scrh[i1p] = dt * s.ah[i1p] * d1
            for i in range(i1, i0, -1):
                s.scrh[i] = dth * s.ah[i] * (d[i] + d[i-1])
                s.source[i] = s.source[i] + c[i] * (s.scrh[i+1] - s.scrh[i])
            s.source[i0] = s.source[i0] + c[i0] * (s.scrh[i0p] - s.scrh[i0])

        # [+C*grad(D)] is computed efficiently and added to s.source
        elif mode == 1:
            s.scrh[i0] = dth * d0
            s.scrh[i1p] = dth * d1
            for i in range(i1, i0, -1):
                s.scrh[i] = dtq * (d[i] + d[i-1])
                s.diff[i] = s.scrh[i+1] - s.scrh[i]
                s.source[i] = s.source[i] + c[i] * (s.ah[i+1] + s.ah[i]) * s.diff[i]
            s.source[i0] = s.source[i0] + c[i0] * (s.ah[i0p] + s.ah[i0]) * (s.scrh[i0p] - s.scrh[i0])

        # [+D] is added to s.source in an explicit formulation  +++++
        elif mode == 2:
            for i in range(i0, i1p):
                s.source[i] = s.source[i] + dt * s.lo[i] * d[i]

        # [+div(D)] is computed conservatively from interface data
        elif mode == 3:
            s.scrh[i1p] = dt * s.ah[i1p] * d1
            s.scrh[i0] = dt * s.ah[i0] * d0
            for i in range(i1, i0, -1):
                s.scrh[i] = dt * s.ah[i] * d[i]
                s.source[i] = s.source[i] + s.scrh[i+1] - s.scrh[i]
            s.source[i0] = s.source[i0] + s.scrh[i0p] - s.scrh[i0]

        # [+C*grad(D)] is computed using interface data
        elif mode == 4:
            s.scrh[i0] = dth * d0
            s.scrh[i1p] = dth * d1
            for i in range(i1, i0, -1):
                s.scrh[i] = dth * d[i]
                s.diff[i] = s.scrh[i+1] - s.scrh[i]
                s.source[i] = s.source[i] + c[i] * (s.ah[i+1] + s.ah[i]) * s.diff[i]
            s.source[i0] = s.source[i0] + c[i0] * (s.ah[i0p] + s.ah[i0]) * (s.scrh[i0p] - s.scrh[i0])

        # [+C] for s.source terms only at a list of indices
        elif mode == 5:
            for ii in range(0, s.nind):
                i = s.index(ii)
                s.source[i] = s.source[i] + s.scalars(ii)

    def cnvfct(s, rhoo, i0, i1, srho0, vrho0, srho1, vrho1, pbc):
        ''' This function solves advective continuity equations of the form: d(RHO)/dt = -V*grad(RHO) + SOURCES in the users's choice of cartesian, cylindrical or spherical coordinates. A facility is included to allow definition of other coordinates. The grid can be Eulerian, sliding rezone, or Lagrangian, and can be arbitrarily spaced. The algorithm is a low phase-error FCT algorithm, vectorized and optimized for a combination of speed and flexibility.

        INPUT:
        rhoo = I/P real array: grid point densities at start of step (1d float array)
        i0, i1 = first and last grid points of integration (both inclusive) (int)
        srho0 = boundary guard cell factor at cell (i0-1) (1d float array)
        vrho0 = boundary value added to guard cell (i0-1) (1d float array)
        srho1 = boundary guard cell factor at cell (i1+1) (1d float array)
        vrho1 = boundary value added to guard cell (i1+1) (1d float array)
        pbc = uses periodic boundaries if True (bool)

        OUTPUT:
        rhon = grid point densities at end of step (1d float array)
        '''
        i0p = i0 + 1
        i1p = i1 + 1

        # calculate convective and diffusive fluxes
        if pbc:
            rho0m = rhoo[i1]
            rho1p = rhoo[i0]
        else:
            rho0m = srho0 * rhoo[i0] + vrho0
            rho1p = srho1 * rhoo[i1] + vrho1

        s.diff[i0] = s.nulh[i0] * (rhoo[i0] - rho0m)
        s.flxh[i0] = s.vdtodr[i0] * (rhoo[i0] - rho0m)

        for i in range(i0p, i1p):
            s.diff[i] = (rhoo[i] - rhoo[i-1])
            s.flxh[i] = s.vdtodr[i] * s.diff[i]
            s.diff[i] = s.nulh[i] * s.diff[i]
        s.diff[i1p] = s.nulh[i1p] * (rho1p - rhoo[i1])
        s.flxh[i1p] = s.vdtodr[i1p] * (rho1p - rhoo[i1])

        # calculate lorhot, the transported mass elements, and lnrhot, the transported and diffused mass elements:
        for i in range(i0, i1p):
            s.lorhot[i] = s.ln[i] * (rhoo[i] - 0.5 * (s.flxh[i+1] + s.flxh[i])) + s.source[i]
            s.lnrhot[i] = s.lorhot[i] + s.diff[i+1] - s.diff[i]
            s.rhot[i] = s.lorhot[i] * s.rlo[i]
            s.rhotd[i] = s.lnrhot[i] * s.rln[i]

        # evaluate boundary conditions for (rhot, rhotd)
        if pbc:
            rhot0m = s.rhot[i1]
            rhot1p = s.rhot[i0]
            rhotd0m = s.rhotd[i1]
            rhotd1p = s.rhotd[i0]
        else:
            rhot0m = srho0 * s.rhot[i0] + vrho0
            rhot1p = srho1 * s.rhot[i1] + vrho1
            rhotd0m = srho0 * s.rhotd[i0] + vrho0
            rhotd1p = srho1 * s.rhotd[i1] + vrho1

        # calculate the transported antidiffusive fluxes and transported and diffused density differences
        s.flxh[i0] = s.mulh[i0] * (s.rhot[i0] - rhot0m)
        s.diff[i0] = s.rhotd[i0] - rhotd0m
        s.fabs[i0] = np.abs(s.flxh[i0])
        s.fsgn[i0] = np.sign(s.diff[i0]) * np.abs(s.diff1)

        for i in range(i0p, i1p):
            s.flxh[i] = s.mulh[i] * (s.rhot[i] - s.rhot[i-1])
            s.diff[i] = s.rhotd[i] - s.rhotd[i-1]

        s.flxh[i1p] = s.mulh[i1p] * (rhot1p - s.rhot[i1])
        s.diff[i1p] = rhotd1p - s.rhotd[i1]

        # calculate the magnitude & sign of the antidiffusive flux followed by the flux-limiting changes on the right and left
        for i in range(i0, i1p):
            s.fabs[i+1] = np.abs(s.flxh[i+1])
            s.fsgn[i+1] = np.sign(s.diff[i+1]) * np.abs(s.diff1)
            s.term[i+1] = s.fsgn[i+1] * s.ln[i] * s.diff[i]
            s.terp[i] = s.fsgn[i] * s.ln[i] * s.diff[i+1]

        if pbc:
            s.terp[i1p] = s.terp[i0]
            s.term[i0] = s.term[i1p]
        else:
            s.terp[i1p] = s.bignum
            s.term[i0] = s.bignum

        # correct the transported fluxes completely and then calculate the new Flux-Corrected Transport densities:
        rhon = np.array(rhoo)
        s.flxh[i0] = s.fsgn[i0] * max(0.0, min(s.term[i0], s.fabs[i0], s.terp[i0]))
        for i in range(i0, i1p):
            s.flxh[i+1] = s.fsgn[i+1] * max(0.0, min(s.term[i+1], s.fabs[i+1], s.terp[i+1]))
            rhon[i] = s.rln[i] * (s.lnrhot[i] + (s.flxh[i] - s.flxh[i+1]))
            s.source[i] = 0.0

        return rhon

    def conserve(s, rho, i0, i1):
        ''' Computes the ostensibly conserved sum. Beware your boundary conditions and note that only one continuity equation is summed for each call to this function.

        INPUT:
        rho = cell values for physical variable rho (1d float array of size npt)
        i0, i1 = first and last cells to be integrated (both inclusive) (int)
        
        OUTPUT:
        csum = value of the conservative sum of rho (float)
        '''
        csum = 0.0
        for i in range(i0, i1+1):
            csum = csum + s.ln[i] * rho[i]
        return csum

    def copygrid(s, mode, i0, i1):
        ''' Makes a complete copy of the grid variables defined by the most recent call to makegrid() from cell i0 to i1, including the boundary values at interface i1p when the argument mode=0. When mode=1, these grid variables are reset from OLD geometry variables. This function is used where the same grid is needed repeatedly after some of the values have been over-written, for example, by a grid which moves between the halfstep and the whole step.

        INPUT:
        i0, i1 = first and last cell indices (both inclusive) (int)
        mode = decides which way to copy (int)
             = 0, grid variables copied from FCT to OLD
             = 1, grid variables copied from OLD to FCT
        '''
        if mode == 0:
            for i in range(i0, i1+1):
                s.lop[i] = s.lo[i]
                s.lnp[i] = s.ln[i]
                s.rlnp[i] = s.rln[i]
            for i in range(i0, i1+2):
                s.ahp[i] = s.ah[i]
                s.lhp[i] = s.lh[i]
                s.rlhp[i] = s.rlh[i]
                s.rohp[i] = s.roh[i]
                s.rnhp[i] = s.rnh[i]
                s.adugthp[i] = s.adugth[i]
        elif mode == 1:
            for i in range(i0, i1+1):
                s.lo[i] = s.lop[i]
                s.ln[i] = s.lnp[i]
                s.rln[i] = s.rlnp[i]
            for i in range(i0, i1+2):
                s.ah[i] = s.ahp[i]
                s.lh[i] = s.lhp[i]
                s.rlh[i] = s.rlhp[i]
                s.roh[i] = s.rohp[i]
                s.rnh[i] = s.rnhp[i]
                s.adugth[i] = s.adugthp[i]
        else:
            print('COPYGRID error!!  mode =', mode)
            sys.exit()

    def new_grid(s, radhn, i0, i1p, alpha):
        ''' Initializes geometry variables and coefficients when the most recent call to makegrid() used the same set of values radho and the new interface locations radhn are different. new_grid() is computationally more efficient than the complete grid procedure in makegrid() because several formulas do not need to be recomputed. The grid should generally be defined for the entire number of grid interfaces from 0 to i1p. However, subsets of the entire grid may be reinitialized with care.

        INPUT:
        radhn = new cell interface positions (1d float array of size i1p)
        i0, i1p = first and last interface indices (both inclusive) (int)
        alpha = (0, 1, 2, 3) for different geometries, same as in makegrid() (int)
        '''
        i0p = i0 + 1
        i1 = i1p - 1

        # store the old and new grid interface locations from input and then update the new and average interface and grid coefficients:
        s.rnh[i0:i1p+1] = s.radhn[i0:i1p+1]

        # cartesian coordinates
        if alpha == 0:
            s.ah[i1p] = 1.0
            for i in range(i0, i1p):
                s.ln[i] = s.rnh[i+1] - s.rnh[i]
        # cylindrical coordinates (radial)
        elif alpha == 1:
            s.diff[i0] = s.rnh[i0] * s.rnh[i0]
            s.ah[i1p] = np.pi * (s.roh[i1p] + s.rnh[i1p])
            for i in range(i0, i1p):
                s.ah[i] = np.pi * (s.roh[i] + s.rnh[i])
                s.diff[i+1] = s.rnh[i+1] * s.rnh[i+1]
                s.ln[i] = np.pi * (s.diff[i+1] - s.diff[i])
        # spherical coordinates (radial):
        elif alpha == 2:
            s.diff[i0] = s.rnh[i0]**3
            s.scrh[i1p] = (s.roh[i1p] + s.rnh[i1p]) * s.roh[i1p]
            s.ah[i1p] = s.ftpi * (s.scrh[i1p] + s.rnh[i1p] * s.rnh[i1p])
            for i in range(i0, i1p):
                s.diff[i+1] = s.rnh[i+1]**3
                s.scrh[i] = (s.roh[i] + s.rnh[i]) * s.roh[i]
                s.ah[i] = s.ftpi * (s.scrh[i] + s.rnh[i] * s.rnh[i])
                s.ln[i] = s.ftpi * (s.diff[i+1] - s.diff[i])
        # user supplied (define below)
        elif alpha == 3:
            pass

        # additional system-independent geometric variables
        for i in range(i0, i1p):
            s.rln[i] = 1.0 / s.ln[i]
        s.lh[i0] = s.ln[i0]
        s.rlh[i0] = s.rln[i0]
        for i in range(i0p, i1p):
            s.lh[i] = 0.5 * (s.ln[i] + s.ln[i-1])
            s.rlh[i] = 0.5 * (s.rln[i] + s.rln[i-1])
        s.lh[i1p] = s.ln[i1]
        s.rlh[i1p] = s.rln[i1]
        for i in range(i0, i1p+1):
            s.adugth[i] = s.ah[i] * (s.rnh[i] - s.roh[i])

    def residiff(s, diffa):
        ''' Allows the user to provide some residual numerical diffusion by making the anti-diffusion coefficient smaller.

            INPUT:
            diffa = Replacement residual diffusion coefficient
        '''
        s.diff1 = diffa

    def set_grid(s, radr, i0, i1):
        ''' Includes the radial factor in the cell volume for polar coordinates. It must be preceded by a call to make_grid() with alpha=0 to establish the angular dependence of the cell volumes and areas, and a call to copy_grid() to save this angular dependence. The angular coordinate is measured in radians (0 to 2*pi) in cylindrical coordinates and cos(theta) (-1 to +1) in spherical coordinates. set_grid() is called inside the loop over radius in a multi-dimensional model to append the appropriate radial factors when integrating in the angular direction.

        INPUT:
        radr = radius of cell center (float)
        i0, i1 = first and last cell indices (both inclusive) (int)
        '''
        i0p = i0 + 1
        i1p = i1 + 1

        # multiply each volume element by the local radius
        for i in range(i0, i1p):
            s.ln[i] = s.lnp[i] * radr
            s.lo[i] = s.lop[i] * radr

        # additional system independent geometric variables
        for i in range(i0, i1p):
            s.rln[i] = 1.0 / s.ln[i]
        s.lh[i0] = s.ln[i0]
        s.rlh[i0] = s.rln[i0]
        for i in range(i0p, i1p):
            s.lh[i] = 0.5 * (s.ln[i] + s.ln[i-1])
            s.rlh[i] = 0.5 * (s.rln[i] + s.rln[i-1])
        s.lh[i1p] = s.ln[i1]
        s.rlh[i1p] = s.rln[i1]

    def zerodiff(s, ind):
        ''' Sets the FCT diffusion and anti-diffusion parameters to zero at the specified cell interface to inhibit unwanted diffusion across the interface. This routine is used for inflow and outflow boundary conditions. If argument ind is positive, the coefficients at that particular interface are reset. If ind is negative, the list of nind indices in index are used to reset that many interface coefficients.

            INPUT:
            ind = index of interface to be reset (int)
        '''
        if ind > -1:
            s.nulh[ind] = 0.0
            s.mulh[ind] = 0.0
        else:
            if s.nind < 0 or s.nind > s.nindmax or ind == -1:
                print('ZERODIFF Error!! IND, NIND =', ind, ',', s.nind)
                sys.exit()
            for ii in range(0, s.nind):
                i = s.index[ii]
                s.nulh[i] = 0.0
                s.mulh[i] = 0.0

    def zeroflux(s, ind):
        ''' Sets all velocity dependent FCT parameters to zero at the specified cell interfaces to transport fluxes AND diffusion of material across the interface. This routine is needed in solid wall boundary conditions. If ind is positive, the coefficients at that particular interface are reset. If ind is negative, the list of nind indices in index are used to reset that many interface coeffs.

            INPUT:
            ind = index of interface to be reset (int)
        '''
        if ind > -1:
            s.hadudth[ind] = 0.0
            s.nulh[ind] = 0.0
            s.mulh[ind] = 0.0
        else:
            if s.nind < 0 or s.nind > s.nindmax or ind == -1:
                print('ZERODIFF Error!! IND, NIND =', ind, ',', s.nind)
                sys.exit()
            for ii in range(0, s.nind):
                i = s.index[ii]
                s.hadudth[i] = 0.0
                s.nulh[i] = 0.0
                s.mulh[i] = 0.0

    def set_index(s, nind, index, scalars):
        ''' Sets internal parameters nind, index and scalars; usable only if using mode 5 in sources() or, ind < 0 in zerodiff() or zeroflux()

            INPUT:
            nind = number of entries in index and scalars (int)
            index = indices at which operations in sources(), zerodiff() or zeroflux() are needed (1d int array of size nind)
            scalars = values of sources to be changed at index in sources() (1d float array of size nind)
        '''
        s.nind = nind
        s.index = np.array(index)
        s.scalars = np.array(scalars)

