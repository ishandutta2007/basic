# Last Updated: 2019-Jul-10
# Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
# Source: https://github.com/udy11, https://gitlab.com/udy11

# Tested with Python 3.6.4, Numpy 1.13.3

# NOTE:
# Indices k0 and k1 passed to gasdyn() are both inclusive, unlike usual python conventions
# Modes bc0 and bc1 are one less than what they are in original code. So if you are using BCN=2 in original LCPFCT's GASDYN(), use bc1=1 in this gasdyn()
# Use setvars() to declare the required variables. You may only declare the ones that will be applicable to you, but all the required variables should be declared together

import numpy as np

class gasdyn:
    def __init__(s, nxp):
        nx = nxp - 1
        s.vint = np.empty(nxp)
        s.mpint = np.empty(nxp)
        s.mpvint = np.empty(nxp)
        s.unit = np.ones(nxp)
        s.vel = np.empty(nx)
        s.pre = np.empty(nx)
        s.rhoo = np.empty(nx)
        s.rvro = np.empty(nx)
        s.rvto = np.empty(nx)
        s.ergo = np.empty(nx)

        s.gammam = 1.0
        s.relax = 0.0
        s.pre_in = 0.0
        s.vel_in = 0.0
        s.preamb = 0.0
        s.velamb = 0.0
        s.rho_in = 0.0
        s.rhoamb = 0.0

    def setvars(s, gammam = 1.0, relax = 0.0, pre_in = 0.0, vel_in = 0.0, rho_in = 0.0, preamb = 0.0, velamb = 0.0, rhoamb = 0.0):
        '''
            Set all the required variables at once
        '''
        s.gammam = gammam
        s.relax = relax
        s.pre_in = pre_in
        s.vel_in = vel_in
        s.rho_in = rho_in
        s.preamb = preamb
        s.velamb = velamb
        s.rhoamb = rhoamb

    def gasdyn(s, k0, k1, bc0, bc1, dt, rhon, rvrn, rvtn, ergn, lh):
        '''
        This function integrates the gasdynamic equations using the momentum component rvrn as the direction of integration and the momentum rvtn as the transverse direction. In 2D models the two directions of integration are chosen by exchanging rvrn and rvtn

        INPUT:
        k0, k1 = first and last grid points of integration (both inclusive) (int)
        bc0, bc1 = modes for boundary conditions, see below for details (int)
        dt = timestep for the integration of this step (float)
        rhon = density of gas (1d float array)
        rvrn = speed of gas (1d float array)
        rvtn = temperature of gas (1d float array)
        ergn = energy of gas (1d float array)
        lh = (lcpfct class object)

        BOUNDARY CONDITIONS:
        bc0, bc1 = 0  => ideal solid wall or axis boundary condition 
        bc0, bc1 = 1  => an extrapolative outflow boundary condition 
        bc0, bc1 = 2  => periodic boundary conditions
        bc0, bc1 = 3  => specified boundary values (e.g., shock tube problem)

        '''
        # Prepare for the time integration. Index k is either i or j depending on the definitions of rvrn and rvtn. Copies of the physical variable are needed to recover values for the whole step integration...
        k1p = k1 + 1
        k0p = k0 + 1
        pbc = bc0 == 2 or bc1 == 2
        for k in range(k0, k1p):
            s.rhoo[k] = rhon[k]
            s.rvro[k] = rvrn[k]
            s.rvto[k] = rvtn[k]
            s.ergo[k] = ergn[k]

        # Integrate first the half step then the whole step...
        for it in (1, 2):
            dtsub = 0.5 * dt * it
            for k in range(k0, k1p):
                s.vel[k] = rvrn[k] / rhon[k]
                s.pre[k] = s.gammam * (ergn[k] - 0.5 * (rvrn[k]**2 + rvtn[k]**2) / rhon[k])

            # Calculate the interface velocities and pressures as weighted values of the cell-centered values computed just above...
            for k in range(k0p, k1p):
                s.vint[k] = 0.5 * (s.vel[k] + s.vel[k-1])
                s.mpint[k] = -0.5 * (s.pre[k] + s.pre[k-1])
                s.mpvint[k] = -0.5 * (s.pre[k] * s.vel[k] + s.pre[k-1] * s.vel[k-1])

            # Call the FCT utility routines and set the boundary conditions. Other boundary conditions could be added for inflow, outflow, etc...
            if bc0 == 0:
                s.vint[k0] = 0.0
                s.mpint[k0] = -s.pre[k0]
                s.mpvint[k0] = 0.0
            elif bc0 == 1:
                s.vint[k0] = s.vel[k0] * (1.0 - s.relax)
                s.mpint[k0] = -s.pre[k0] * (1.0 - s.relax) - s.relax * s.pre_in
                s.mpvint[k0] = s.mpint[k0] * s.vint[k0]
            elif bc0 == 2:
                s.mpvint[k0] = 1.0 / (rhon[k0] + rhon[k1])
                s.vint[k0] = (s.vel[k0] * rhon[k1] + s.vel[k1] * rhon[k0]) * s.mpvint[k0]
                s.mpint[k0] = -(s.pre[k0] * rhon[k1] + s.pre[k1] * rhon[k0]) * s.mpvint[k0]
                s.mpvint[k0] = -(s.vel[k0] * s.pre[k0] * rhon[k1] + s.vel[k1] * s.pre[k1] * rhon[k0]) * s.mpvint[k0]
            elif bc0 == 3:
                s.vint[k0] = s.vel_in
                s.mpint[k0] = -s.pre_in
                s.mpvint[k0] = s.vint[k0] * s.mpint[k0]

            if bc1 == 0:
                s.vint[k1p] = 0.0
                s.mpint[k1p] = -s.pre[k1]
                s.mpvint[k1p] = 0.0
            elif bc1 == 1:
                s.vint[k1p] = s.vel[k1] * (1.0 - s.relax)
                s.mpint[k1p] = -s.pre[k1] * (1.0 - s.relax) - s.relax * s.preamb
                s.mpvint[k1p] = s.mpint[k1p] * s.vint[k1p]
            elif bc1 == 2:
                s.vint[k1p] = s.vint[k0]
                s.mpint[k1p] = s.mpint[k0]
                s.mpvint[k1p] = s.mpvint[k0]
            elif bc1 == 3:
                s.vint[k1p] = s.velamb
                s.mpint[k1p] = -s.preamb
                s.mpvint[k1p] = s.vint[k1p] * s.mpint[k1p]

            lh.velocity(s.vint, k0, k1p, dtsub)

            # The velocity dependent FCT coefficients are set and the boundary condition calculations are completed. In case of periodic boundary conditions (S)lope and (V)alue boundary value specifiers are ignored in lcpfct
            if bc0 == 0:
                lh.zeroflux(k0)
                sbc0 = 1.0
                srv0 = -1.0
                vrho0 = 0.0
                vrvr0 = 0.0
                vrvt0 = 0.0
                verg0 = 0.0
            elif bc0 == 1:
                lh.zerodiff(k0)
                sbc0 = 1.0 - s.relax
                srv0 = 1.0 - s.relax
                vrho0 = s.relax * s.rho_in
                vrvr0 = 0.0
                vrvt0 = 0.0
                verg0 = s.relax * s.pre_in / s.gammam
            elif bc0 == 2:
                sbc0 = 0.0
                srv0 = 0.0
                vrho0 = 0.0
                vrvr0 = 0.0
                vrvt0 = 0.0
                verg0 = 0.0
            elif bc0 == 3:
                sbc0 = 0.0
                srv0 = 0.0
                vrho0 = s.rho_in
                vrvr0 = s.rho_in * s.vel_in
                vrvt0 = 0.0
                verg0 = s.pre_in / s.gammam + 0.5 * s.rho_in * s.vel_in**2

            if bc1 == 0:
                lh.zeroflux(k1p)
                sbc1 = 1.0
                srv1 = -1.0
                vrho1 = 0.0
                vrvr1 = 0.0
                vrvt1 = 0.0
                verg1 = 0.0
            elif bc1 == 1:
                lh.zerodiff(k1p)
                sbc1 = 1.0 - s.relax
                srv1 = 1.0 - s.relax
                vrho1 = s.relax * s.rhoamb
                vrvr1 = 0.0
                vrvt1 = 0.0
                verg1 = s.relax * s.preamb / s.gammam
            elif bc1 == 2:
                sbc1 = 0.0
                srv1 = 0.0
                vrho1 = 0.0
                vrvr1 = 0.0
                vrvt1 = 0.0
                verg1 = 0.0
            elif bc1 == 3:
                sbc1 = 0.0
                srv1 = 0.0
                vrho1 = s.rhoamb
                vrvr1 = s.rhoamb * s.velamb
                vrvt1 = 0.0
                verg1 = s.preamb / s.gammam + 0.5 * s.rhoamb * s.velamb**2

            # Integrate the continuity equations using LCPFCT...
            rhon = lh.lcpfct(s.rhoo, k0, k1, sbc0, vrho0, sbc1, vrho1, pbc)
            lh.sources(k0, k1, dtsub, 4, s.unit, s.mpint, s.mpint[k0], s.mpint[k1p])
            rvrn = lh.lcpfct(s.rvro, k0, k1, srv0, vrvr0, srv1, vrvr1, pbc)
            rvtn = lh.lcpfct(s.rvto, k0, k1, sbc0, vrvt0, sbc1, vrvt1, pbc)
            lh.sources(k0, k1, dtsub, 3, s.unit, s.mpvint, s.mpvint[k0], s.mpvint[k1p])
            ergn = lh.lcpfct(s.ergo, k0, k1, sbc0, verg0, sbc1, verg1, pbc)

        return rhon, rvrn, rvtn, ergn
