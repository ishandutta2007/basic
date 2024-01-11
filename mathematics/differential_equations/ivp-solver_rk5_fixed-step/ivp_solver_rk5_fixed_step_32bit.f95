! Last updated: 13-Jul-2015
! Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
! Source: https://github.com/udy11, https://gitlab.com/udy11
! Subroutine (32-bit) to solve coupled ordinary differential equations with
! initial values (coupled-ODEs-IVP) using Butcher's Runge Kutta 5 method

! The program solves coupled ODEs y'(i)=f(x,y(j))(i); {i,j: 1-->n}

! ALL YOU NEED TO DO:
! Call subroutine brk5_32() with:
!   fx = external function that defines ODEs (see below INPUT FUNCTION)
!   n = number of unknowns y(i)
!   h = step size in which x increases per iteration
!   ns = number of iterations
!   x0 = initial value of x, from which iteration begins
!   y0 = initial value(s) of y at x0
!   ofln = output file name

! OUTPUT:
! Output is in the text file, whose name is given by ofln
! First column represents x, followed by the y vector

! NOTE:
! This implementation of Butcher's Runge-Kutta 5 uses
!   constant step size, predefined by user
! If you want to run RK5 from x0 to x1, then h or ns can be calculated as:
!   h=(x1-x0)/ns
!   ns=(x1-x0)/h
! A higher order ODE can be broken into coupled ODEs, e.g.,
!   y''+100*y=0, can be broken as y1'=y2; y2'=-100*y1

    dimension y0(2)
    character*150 ofln
    external gx

! INPUTS
    n=2                         ! number of unknowns y(i) or number of equations
    h=1.e-4                     ! step size in which iteration proceeds
    ns=10**4                    ! number of steps
    x0=0.0                      ! initial value from which iteration begins
    y0(1)=0.0; y0(2)=10.0       ! initial values for unknowns
    ofln="brk5_32_tst.f95.txt"  ! output file name (overwrites if already exists)

    call brk5_32(gx,n,h,ns,x0,y0,ofln)

    end

! INPUT FUNCTION
! Simply define functions f(1),f(2),...,f(n)
! for coupled ODEs: y'(i)=f(x,y(j))(i)
! Example:
! Suppose you want to solve: y'(1)=y(2); y'(2)=-100*y(1)
! Then define f(1)=y(2) and f(2)=-100.0*y(1)
! This means f are simply the RHS in the coupled ODEs when arranged properly.
    subroutine gx(f,x,y,n)
    dimension f(n),y(n)
    f(1)=y(2)
    f(2)=-100.0*y(1)
    endsubroutine

! Butcher's RK5 subroutine (32-bit)
    subroutine brk5_32(fx,n,h,ns,x0,y0,ofln)
    character*150,intent(in) :: ofln
    dimension y0(n),f(n),y(n)
    real k1(n),k2(n),k3(n),k4(n),k5(n),k6(n)
    external fx
    x=x0
    y=y0
    open(489,file=ofln)
    write(489,*) x,y       ! Initial values written to output file
    do i=1,ns
        call fx(f,x,y,n)
        k1=h*f
        call fx(f,x+0.25*h,y+0.25*k1,n)
        k2=h*f
        call fx(f,x+0.25*h,y+0.125*(k1+k2),n)
        k3=h*f
         call fx(f,x+0.5*h,y-0.5*k2+k3,n)
        k4=h*f
         call fx(f,x+0.75*h,y+0.1875*k1+0.5625*k4,n)
        k5=h*f
         call fx(f,x+h,y+(-3.0*k1+2.0*k2+12.0*k3-12.0*k4+8.0*k5)*0.142857143,n)
        k6=h*f
        x=x0+i*h
        y=y+(0.7*k1+3.2*k3+1.2*k4+3.2*k5+0.7*k6)*0.111111111
        write(489,*) x,y
    enddo
    close(489)
    endsubroutine
