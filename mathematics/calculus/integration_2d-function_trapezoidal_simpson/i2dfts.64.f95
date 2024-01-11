! Last updated: 08-Oct-2015
! Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
! Source: https://github.com/udy11, https://gitlab.com/udy11
! Subroutines (64-bit) to integrate a two-dimensional function
! using Trapezoidal Rule and Simpson's 1/3rd Rule

! ALL YOU NEED TO DO:
! Call required subroutine with parameters
!   INPUT:
!     f(x,y) = external 2D function whose integration is to be calculated
!     ax, bx = range of x in which to integrate
!     ay, by = range of y in which to integrate
!     nx, ny = number of sample points to take for integration in x and
!              y respectively (including end-points)
!   OUTPUT:
!     sm = output of integration

! NOTE:
! Choosing a large n will cause truncation error to reduce
!   but will increase roundoff error, so choose as per needs
! In case your function has some parameters, you can specify them in function
!   itself or in common block; for latter, common block definition is needed
!   in both main program and function f but not in integration subroutines,
!   however, note that order of parameters must be same in both common blocks
! Note that integration(f(x,y),(ax,bx))=-integration(f(x,y),(bx,ax))
!   so specify the range ax,bx accordingly (similarly for y)
! Don't forget to specify function f as external
! In case of Simpson's 1/3rd rule, number of points nx and ny should be odd (or
!   equivalently, number of intervals should be even); however, if they are
!   given even, the program uses one less point (maintaining the given range)

! Below is example of integration(sin(d*x*y),(x,0,1),(y,0,2)), with d=3

    implicit real*8(A-H,O-Z)
    external fxy
    common d

    ax=0.0d0; bx=1.0d0; nx=1999
    ay=0.0d0; by=2.0d0; ny=3999
    d=3.0d0

    call int_trpzdl_2d_64(fxy,ax,bx,nx,ay,by,ny,sm)
    write(6,*) sm
    call int_smpsn_2d_64(fxy,ax,bx,nx,ay,by,ny,sm)
    write(6,*) sm
    end

! INPUT FUNCTION
    real*8 function fxy(x,y)
    implicit real*8(A-H,O-Z)
    common d
    fxy=sin(d*x*y)
    endfunction

! 2D Trapezoidal Rule Subroutine (64-bit)
! Truncation Error ~ O(hx**2) + O(hy**2)
    subroutine int_trpzdl_2d_64(f,ax,bx,nx,ay,by,ny,sm)
    implicit real*8(A-H,O-Z)
    external f
    hx=(bx-ax)/(nx-1)
    hy=(by-ay)/(ny-1)
    h=hx*hy
    sm=h*0.25d0*(f(ax,ay)+f(bx,ay)+f(ax,by)+f(bx,by))
    s1=0.0d0
    do j=2,ny-1
        s1=s1+h*(f(ax,ay+j*hy)+f(bx,ay+j*hy))
    enddo
    s2=0.0d0
    do i=2,nx-1
        s2=s2+h*(f(ax+i*hx,ay)+f(ax+i*hx,by))
        do j=2,ny-1
            sm=sm+h*f(ax+i*hx,ay+j*hy)
        enddo
    enddo
    sm=sm+0.5d0*(s1+s2)
    endsubroutine

! 2D Simpson's 1/3rd Rule Subroutine (64-bit)
! Truncation Error ~ O(hx**4) + O(hy**4)
    subroutine int_smpsn_2d_64(f,ax,bx,mx,ay,by,my,sm)
    implicit real*8(A-H,O-Z)
    external f
    if(and(mx,1)==0) then
        nx=mx-1
    else
        nx=mx
    endif
    if(and(my,1)==0) then
        ny=my-1
    else
        ny=my
    endif
    hx=(bx-ax)/(nx-1)
    hy=(by-ay)/(ny-1)
    h=hx*hy
    sm=h*0.5d0*(f(ax,ay)+f(bx,ay)+f(ax,by)+f(bx,by))
    s1=0.0d0
    do j=1,ny-2,2
        s1=s1+h*(f(ax,ay+j*hy)+f(bx,ay+j*hy))
    enddo
    s1=s1*2.0d0
    do j=2,ny-2,2
        s1=s1+h*(f(ax,ay+j*hy)+f(bx,ay+j*hy))
    enddo
    s2=0.0d0
    s3=0.0d0
    do i=1,nx-2,2
        s2=s2+h*(f(ax+i*hx,ay)+f(ax+i*hx,by))
        do j=1,ny-2,2
            s3=s3+h*f(ax+i*hx,ay+j*hy)
        enddo
    enddo
    s3=2.0d0*s3
    do i=1,nx-2,2
        do j=2,ny-2,2
            s3=s3+h*f(ax+i*hx,ay+j*hy)
        enddo
    enddo
    s2=s2*2.0d0
    s3=s3*2.0d0
    s4=0.0d0
    do i=2,nx-2,2
        s2=s2+h*(f(ax+i*hx,ay)+f(ax+i*hx,by))
        do j=1,ny-2,2
            s4=s4+h*f(ax+i*hx,ay+j*hy)
        enddo
    enddo
    s4=s4*2.0d0
    do i=2,nx-2,2
        do j=2,ny-2,2
            s4=s4+h*f(ax+i*hx,ay+j*hy)
        enddo
    enddo
    sm=0.222222222222222222d0*(sm+s1+s2+2.0d0*(s3+s4))
    endsubroutine
