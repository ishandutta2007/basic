! Last updated: 17-Dec-2014
! Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
! Source: https://github.com/udy11, https://gitlab.com/udy11
! Subroutine (64-bit) to solve Poisson's Equation in Two Dimensional Uniform
! Grid with Dirichlet Boundary Conditions using Finite Difference Method
! (Five-Point Stencil and Fourier Transform)
! (uses FFTW Libraries, http://www.fftw.org/)

! ALL YOU NEED TO DO:
! Define Boundary Conditions in subroutine bcs() as per its description below
! Define the known function f(x,y) in subroutine fxy() as per its description below
! Call the poisson solver subroutine poisson_solver_fft_2d_64(nx,x0,x1,ny,y0,y1,u), where
!   u is unknown in Poisson's Equation (read its description below)
!   nx and ny are number of points in x and y axes (includes boundaries), ny is number of rows
!   x0, x1, y0 and y1 are values at boundaries
! Include provided fftw3.f file with your program too
! Compile with gfortran and proper path to FFTW library, for example in Ubuntu:
!     gfortran tspei2dugwdbcufdm(5psaft).64.f95 -L/usr/local/bin -lfftw3
! Please follow General Example given below for practical usage

! POISSON'S EQUATION:
! The Poisson's Equation: u_xx + u_yy = f(x,y)
! where u_xx is double derivative of unknown u with respect to x,
! similarly for u_yy; and f(x,y) is a known function

! UNKNOWN QUANTITY u in LHS of POISSON'S EQUATION:
! It is of size ny * nx
! It includes values at boundaries
! Arrangement is such that for nx=5 and ny=4, the indices look like:
!   41 42 43 44 45
!   31 32 33 34 35
!   21 22 23 24 25
!   11 12 13 14 15
! where y on vertical increases from down to up and x on horizontal
! increases from left to right
! its boundaries are defined by boundary conditions subroutine bcs(), the boundaries
! in above configuration are:
!   up:    41 42 43 44 45
!   down:  11 12 13 14 15
!   left:  21 31
!   right: 25 35

! INPUT FUNCTION f in RHS of POISSON'S EQUATION:
! It is of size ny * nx
! It includes values at boundaries (however boundary values of f are actually not used)
! Arrangement is such that for nx=5 and ny=4, the indices look same as u:
!   41 42 43 44 45
!   31 32 33 34 35
!   21 22 23 24 25
!   11 12 13 14 15
! where y on vertical increases from down to up and x on horizontal
! increases from left to right
! Function f must be specified in the subroutine fxy()

! DIRICHLET BOUNDARY CONDITIONS:
! Define boundary conditions in subroutine bcs(). Whatever you do in the
! subroutine, it should give u with required boundary values.
! Up and down boundaries have length nx, whereas left and right have
! length ny-2. The arrangement for nx=5,ny=4 looks like:
!   41 42 43 44 45
!   31          35
!   21          25
!   11 12 13 14 15
! where y on vertical increases from down to up and x on horizontal
! increases from left to right
!   up:    41 42 43 44 45
!   down:  11 12 13 14 15
!   left:  21 31
!   right: 25 35
! Note that you are free to change any value of u in bcs() subroutine, but
! boundaries should be properly defined as required.

! 5-POINT STENCIL:
! It refers to the approximation of double derivatives:
! u_xx(i,j) = (u(i-1,j) - 2u(i,j) + u(i+1,j)) / hx^2
! u_yy(i,j) = (u(i,j-1) - 2u(i,j) + u(i,j+1)) / hy^2

! ALGORITHM:
! Refer to: http://www.cs.berkeley.edu/~demmel/cs267/lecture24/lecture24.html

! COMPLEXITY:
! Time Complexity = O(nx*ny*log(nx*ny))
! Space Complexity = O(nx*ny)

! QUICK TESTING:
! A quick test to verify the program's working is to calculate
! u_xx + u_yy at every point from output and match against f,
! where u_xx and u_yy should be calculated using 5-point stencil

! GENERAL EXAMPLE:
! Suppose you want to solve u_xx+u_yy=f(y,x)
! in the rectangular grid [x0,x1] x [y0,y1] with boundary conditions
! u(y,x0)=left(y,x0); u(y,x1)=right(y,x1); u(y0,x)=down(y0,x); u(y1,x)=up(y1,x)
! Choose some values of nx and ny
! Define boundaries in bcs() as:
!   u(j,1)=left(y,x0)
!   u(j,nx)=right(y,x1)
!   u(1,i)=down(y0,x)
!   u(ny,i)=up(y1,x)
!   where x -> x0+hx*(i-1) and y -> y0+hy*(j-1)
!   and hx, hy are grid spacings defined below in the example as
!   hx=(x1-x0)/(nx-1); hy=(y1-y0)/(ny-1)
!   and loops go as i: 1 -> nx and j: 1 -> ny
! Define function in fxy() as:
!   f(j,i)=f(y,x)
!   where x -> x0+hx*(i-1) and y -> y0+hy*(j-1)
!   and loops go as i: 1 -> nx and j: 1 -> ny
! Now return to your main program
! Say values of nx, x0, x1, ny, y0, y1 are:
!   nx=1500; x0=0; x1=1; ny=2000; y0=0; y1=1
! and calculate the solution of Poisson's Equation:
!   call poisson_solver_fft_2d_64(nx,x0,x1,ny,y0,y1,(1:ny,1:nx))
! Write the values of u, see commented lines in main program for different ways

! GIVEN EXAMPLE:
! The example given below has f(y,x)=2*exp(x+y)
! in the square grid [0,1]x[0,1] with boundary conditions:
! u(0,y)=exp(y); u(1,y)=exp(1+y); u(x,0)=exp(x); u(x,1)=exp(1+x);
! Its exact solution is u=exp(x+y)

    implicit real*8(A-H,O-Z)
    include 'fftw3.f'

    dimension u(5000,5000)

    nx=5; ny=9
    x0=0.d0; x1=1.d0; y0=0.d0; y1=1.d0

    call poisson_solver_fft_2d_64(nx,x0,x1,ny,y0,y1,u(1:ny,1:nx))

! To directly print on screen:
    do j=1,ny
        write(6,*) (u(j,i),i=1,nx)
    enddo

! To write to a file:
!    open(7,file="poisson64_u.txt")
!    do j=1,ny
!        write(7,*) (u(j,i),i=1,nx)
!    enddo
!    close(7)

    end

! Right Hand Side Function in Poisson's Equation
! Includes values at boundaries
    subroutine fxy(nx,x0,x1,ny,y0,y1,f)
    implicit real*8(A-H,O-Z)
    dimension f(ny,nx)
    hx=(x1-x0)/(nx-1); hy=(y1-y0)/(ny-1)

    do j=1,ny
        y=y0+(j-1)*hy
        do i=1,nx
            x=x0+(i-1)*hx
            f(j,i)=2*exp(x+y)
        enddo
    enddo

    endsubroutine

! Dirichlet Boudary Conditions
    subroutine bcs(nx,x0,x1,ny,y0,y1,u)
    implicit real*8(A-H,O-Z)
    dimension u(ny,nx)
    hx=(x1-x0)/(nx-1); hy=(y1-y0)/(ny-1)

    do j=2,ny-1
        y=y0+(j-1)*hy
        u(j,1)=exp(y)       ! Left Boundary
        u(j,nx)=exp(1+y)    ! Right Boundary
    enddo
    do i=1,nx
        x=x0+(i-1)*hx
        u(1,i)=exp(x)       ! Down Boundary
        u(ny,i)=exp(1+x)    ! Up Boundary
    enddo

    endsubroutine

! Subroutine to solve Poisson's Equation in 2D using FFT Method
    subroutine poisson_solver_fft_2d_64(nx,x0,x1,ny,y0,y1,u)
    implicit real*8(A-H,O-Z)
    complex*16 cx,cy
    integer*8 px,py
    dimension u(ny,nx),f(ny,nx),bx(2*nx-2),by(2*ny-2),cx(2*nx-2),cy(2*ny-2)

    pi=3.14159265358979324d0
    hx=(x1-x0)/(nx-1); hy=(y1-y0)/(ny-1)
    rhx2=1.d0/hx/hx; rhy2=1.d0/hy/hy
    nx2=2*nx-2; ny2=2*ny-2

! Obtaining Boudaries and Function values
    call bcs(nx,x0,x1,ny,y0,y1,u)
    call fxy(nx,x0,x1,ny,y0,y1,f)

! Redefining Function values to include effects of boundaries
    do j=2,ny-1
        f(j,2)=f(j,2)-u(j,1)*rhx2
        f(j,nx-1)=f(j,nx-1)-u(j,nx)*rhx2
    enddo
    do i=2,nx-1
        f(2,i)=f(2,i)-u(1,i)*rhy2
        f(ny-1,i)=f(ny-1,i)-u(ny,i)*rhy2
    enddo

! Defining plans for FFTs
    call dfftw_plan_dft_r2c_1d(px,nx2,bx,cx,FFTW_ESTIMATE)
    call dfftw_plan_dft_r2c_1d(py,ny2,by,cy,FFTW_ESTIMATE)

! Matrix Multiplications using FFT
    do j=2,ny-1
        bx(1)=0.d0
        bx(2:nx-1)=f(j,2:nx-1)
        bx(nx:nx2)=0.d0
        call dfftw_execute_dft_r2c(px,bx,cx)
        u(j,2:nx-1)=aimag(cx(2:nx-1))
    enddo
    do i=2,nx-1
        by(1)=0.d0
        by(2:ny-1)=u(2:ny-1,i)
        by(ny:ny2)=0.d0
        call dfftw_execute_dft_r2c(py,by,cy)
        u(2:ny-1,i)=aimag(cy(2:ny-1))
    enddo
    do j=2,ny-1
        do i=2,nx-1
            u(j,i)=u(j,i)*0.5d0/((1.d0-cos((i-1)*pi/(nx-1)))*rhx2+(1.d0-cos((j-1)*pi/(ny-1)))*rhy2)
        enddo
    enddo
    do j=2,ny-1
        bx(1)=0.d0
        bx(2:nx-1)=u(j,2:nx-1)
        bx(nx:nx2)=0.d0
        call dfftw_execute_dft_r2c(px,bx,cx)
        u(j,2:nx-1)=aimag(cx(2:nx-1))
    enddo
    tt=-4.d0/((nx-1)*(ny-1))
    do i=2,nx-1
        by(1)=0.d0
        by(2:ny-1)=u(2:ny-1,i)
        by(ny:ny2)=0.d0
        call dfftw_execute_dft_r2c(py,by,cy)
        u(2:ny-1,i)=tt*aimag(cy(2:ny-1))
    enddo

    call dfftw_destroy_plan(px)
    call dfftw_destroy_plan(py)
    endsubroutine

