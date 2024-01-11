! compile with lcpfct.f from https://www.nrl.navy.mil/lcp/LCPFCT

    implicit real(A-H,O-Z)
    real xint(6), vint(6), rho(5), c(5), d(5)
    nx = 5
    dt = 0.1
    do i = 1, nx+1
        xint(i) = sin((i-1) * 1.0 / nx)
        vint(i) = cos((i-1) * 3.1415926536 / nx)
    enddo
    rho(1:nx) = (/0.1, 0.3, 0.5, 0.4, 0.2/)
    d(1:nx) = (/0.3, 0.1, -0.1, 0.1, 0.3/)
    c = cos(d)
    write(6,*) rho(1:nx)
    call residiff(0.9)
    call makegrid(xint, xint, 1, nx+1, 3)
    call velocity(vint, 1, nx+1, dt)
    call sources(1, nx, dt, 2, c, d, 0.4, 0.4)
    call sources(1, nx, dt, 4, c, d, 0.4, 0.4)

    do it = 1, 5
        tym = it * dt
        call lcpfct(rho, rho, 1, nx, 0.1, 0.05, 0.2, -0.03, .false.)
        write(6,*) rho(1:nx)
    enddo

    end

