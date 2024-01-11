! Last updated: 08-Oct-2015
! Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
! Source: https://github.com/udy11, https://gitlab.com/udy11
! Subroutines (64-bit) to integrate two-dimensional uniformly
! spaced data using Trapezoidal Rule and Simpson's 1/3rd Rule

! ALL YOU NEED TO DO:
! Call the required subroutine with:
!   INPUT:
!     ax and bx as range of integration along x
!     ay and by as range of integration along y
!     f as 1D array to be integrated (see below for details)
!     nx and ny as the number of rows and columns of f
!   OUTPUT:
!     sm as integrated value

! INPUT ARRAY:
! Input 2D array f (which is to be integrated) is input as a 1D
! array where (i,j) 2D index will correspond to (i-1)*ny+j 1D index

! It is assumed that f(1) corresponds to value at (ax,ay) point and
!   f(nx*ny) corresponds to value at (bx,by) point
! Note that integration(f,(ax,bx))=-integration(f,(bx,ax))
!   and similarly for ay,by
!   so specify the range (ax,bx) and (ay,by) accordingly
! For Simpson's 1/3rd Rule, nx and ny should be odd

! Example given below is Integration(Sin(x)+Sin(2y),(x,0,1),(y,0,2))

    implicit real*8(A-H,O-Z)
    dimension f(1001*2001)

    ax=0.0d0; bx=1.0d0; nx=401
    ay=0.0d0; by=2.0d0; ny=801

    do i=1,nx
        do j=1,ny
            f((i-1)*ny+j)=sin((bx-ax)*(i-1)/(nx-1)) &
                          +sin(2.d0*(by-ay)*(j-1)/(ny-1))
        enddo
    enddo

    call intd_trpzdl_2d_64(ax,bx,nx,ay,by,ny,f,sm)
    write(6,*) sm
    call intd_smpsn_2d_64(ax,bx,nx,ay,by,ny,f,sm)
    write(6,*) sm
    end

! Trapezoidal Rule Subroutine (64-bit)
! for 2D uniform data
    subroutine intd_trpzdl_2d_64(ax,bx,nx,ay,by,ny,f,sm)
    implicit real*8(A-H,O-Z)
    dimension f(nx*ny)
    h=((bx-ax)/(nx-1))*((by-ay)/(ny-1))
    sm=h*0.25d0*(f(1)+f((nx-1)*ny+1)+f(ny)+f(nx*ny))
    s1=0.0d0
    do j=2,ny-1
        s1=s1+h*(f(j)+f((nx-1)*ny+j))
    enddo
    s2=0.0d0
    do i=2,nx-1
        s2=s2+h*(f((i-1)*ny+1)+f(i*ny))
        do j=2,ny-1
            sm=sm+h*f((i-1)*ny+j)
        enddo
    enddo
    sm=sm+0.5d0*(s1+s2)
    end

! Simpson's 1/3rd Rule Subroutine (64-bit)
! for 2D uniform data
    subroutine intd_smpsn_2d_64(ax,bx,nx,ay,by,ny,f,sm)
    implicit real*8(A-H,O-Z)
    dimension f(nx*ny)
    if(and(nx,1)==0) then
        write(6,*) "ERROR: Number of rows of f, nx should be odd..."
        return
    endif
    if(and(ny,1)==0) then
        write(6,*) "ERROR: Number of columns of f, ny should be odd..."
        return
    endif
    h=((bx-ax)/(nx-1))*((by-ay)/(ny-1))
    sm=h*0.5d0*(f(1)+f((nx-1)*ny+1)+f(ny)+f(nx*ny))
    s1=0.0d0
    do j=2,ny-1,2
        s1=s1+h*(f(j)+f((nx-1)*ny+j))
    enddo
    s1=s1*2.0d0
    do j=3,ny-1,2
        s1=s1+h*(f(j)+f((nx-1)*ny+j))
    enddo
    s2=0.0d0
    s3=0.0d0
    do i=2,nx-1,2
        s2=s2+h*(f((i-1)*ny+1)+f(i*ny))
        do j=2,ny-1,2
            s3=s3+h*f((i-1)*ny+j)
        enddo
    enddo
    s3=2.0d0*s3
    do i=2,nx-1,2
        do j=3,ny-1,2
            s3=s3+h*f((i-1)*ny+j)
        enddo
    enddo
    s2=s2*2.0d0
    s3=s3*2.0d0
    s4=0.0d0
    do i=3,nx-1,2
        s2=s2+h*(f((i-1)*ny+1)+f(i*ny))
        do j=2,ny-1,2
            s4=s4+h*f((i-1)*ny+j)
        enddo
    enddo
    s4=s4*2.0d0
    do i=3,nx-1,2
        do j=3,ny-1,2
            s4=s4+h*f((i-1)*ny+j)
        enddo
    enddo
    sm=0.222222222222222222d0*(sm+s1+s2+2.0d0*(s3+s4))
    end
