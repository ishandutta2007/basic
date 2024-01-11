! Last updated: 30-Aug-2016
! Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
! Source: https://github.com/udy11, https://gitlab.com/udy11
! Subroutine (128-bit) to solve 2nd order ordinary differential
! equation with initial values using Velocity Verlet algorithm

! This program solves for the following second order ODE:
!   y'' = f(y)
! i.e., f() depends only on y and NOT on x or y'

! ALL YOU NEED TO DO:
! Call subroutine velverlet_128() with:
!   fx = external function that defines ODE (see below INPUT FUNCTION)
!   h = step size in which x increases per iteration
!   ns = number of iterations
!   x0 = initial value of x, from which iteration begins
!   y0 = value of y at x0
!   yp0 = value of y' at x0
!   ofln = output file name

! OUTPUT:
! Output is in the text file, whose name is given by ofln
! The three columns represent x, y and y' respectively

! NOTE:
! If you want to run from x0 to x1, then h or ns can be calculated as:
!   h=(x1-x0)/ns
!   ns=(x1-x0)/h
! Error ~ h**2

    implicit real*16(A-H,O-Z)
    character*150 ofln
    external gx

! INPUTS
    h=1.q-3                           ! step size in which iteration proceeds
    ns=10**3                          ! number of steps
    x0=0.0q0                          ! initial value from which iteration begins
    y0=0.q0                           ! initial value of y
    yp0=10.q0                         ! initial value of y'
    ofln="velverlet_128_tst.f95.txt"  ! output file name (overwrites if already exists)

    call velverlet_128(gx,h,ns,x0,y0,yp0,ofln)

    end

! INPUT FUNCTION
! Simply define f as the RHS of the 2nd order ODE y'' = f(y)
    subroutine gx(f,y)
    implicit real*16(A-H,O-Z)
    f=-100.q0*y
    endsubroutine

! Velocity Verlet algorithm subroutine (128-bit)
    subroutine velverlet_128(fx,h,ns,x0,y0,yp0,ofln)
    implicit real*16(A-H,O-Z)
    character*150,intent(in) :: ofln
    external fx
    hh=0.5q0*h
    y=y0
    yp=yp0
    open(494,file=ofln)
    write(494,*) x0,y,yp       ! Initial values written to output file
    do i=1,ns
        call fx(a,y)
        b=yp+a*hh
        y=y+b*h
        call fx(a,y)
        yp=b+a*hh
        write(494,*) x0+i*h,y,yp
    enddo
    close(494)
    endsubroutine
