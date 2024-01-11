! compile with lcpfct.f and gasdyn.f from https://www.nrl.navy.mil/lcp/LCPFCT

    real xint(6), vint(6), rhon(202), rvxn(202), rvtn(202), ergn(202)
    integer bc1, bcn
    common / ARRAYS / rhon,rvxn,rvtn,ergn,relax,rho_in,pre_in,vel_in,gamma0,rhoamb,preamb,velamb,gammam
    
    gammam = 1.0
    relax = 0.1
    pre_in = 0.1
    vel_in = 0.2
    preamb = 1.0
    velamb = 0.5
    rho_in = 0.4
    rhoamb = 0.6
    
    nx = 5
    do i = 1, nx+1
        xint(i) = sin((i-1) * 1.0 / nx)
        vint(i) = cos((i-1) * 3.1415926536 / nx)
    enddo
    dt = 0.01
    
    rhon(1:nx) = (/0.4, 0.2, 0.1, 0.3, 0.6/)
    rvxn(1:nx) = (/0.08, 0.1, 0.17, 0.26, 0.3/)
    rvtn(1:nx) = (/0.1, 0.2, 0.5, 0.6, 0.8/)
    ergn(1:nx) = (/0.4, 0.3, 0.2, 0.4, 0.6/)

    write(6,*) rhon(1:nx)
    write(6,*) rvxn(1:nx)
    write(6,*) rvtn(1:nx)
    write(6,*) ergn(1:nx)
    write(6,*)
    
    gamma0 = gammam + 1.0
    bc1 = 2
    bcn = 2
    call residiff(0.9)
    call makegrid(xint, xint, 1, nx+1, 1)
    do i=1,5
        call gasdyn(1, nx, bc1, bcn, dt)
        write(6,*) rhon(1:nx)
        write(6,*) rvxn(1:nx)
        write(6,*) rvtn(1:nx)
        write(6,*) ergn(1:nx)
        write(6,*)
    enddo

    end

