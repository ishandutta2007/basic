! Last updated: 25-Sep-2013
! Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
! Source: https://github.com/udy11, https://gitlab.com/udy11
! Subroutine (64-bit) to interpolate one-dimensional data
! using Newton Divided Difference formula

! ALL YOU NEED TO DO:
! Call subroutine nddif_64() with:
!   INPUT:
!     n is the number of data to be interpolated
!     x is the array of abscissas on which data is given
!     y is the array of data to be interpolated
!     n1 is the number of points on which to interpolate
!     x1 is the array of abscissas on which interpolation is required
!   OUTPUT:
!     y1 is the array of interpolated values

! NOTE:
! The subroutine works on non-uniform data and thus requires array
!   x to be specified; however if your abscissas are uniform such that
!   spacing dx and starting value x0 are known, then you can generate
!   required input array x using
!    do i=1,n
!        x(i)=x0+(i-1)*dx
!    enddo
! Abscissas x can be input as an unsorted array, the
!   interpolation is unaffected by it
! It is assumed that input abscissas x are all different
! The provided example interpolates 10 points and gives
!   interpolated values at 4 points

    implicit real*8(A-H,O-Z)
	dimension x(100),y(100),x1(100),y1(100)
    n=10
    open(1,file='i1ddunddf.in.txt')
    do i=1,n
        read(1,*) x(i),y(i)
    enddo
    n1=4
    x1(1:n1)=(/ 0.15d0,0.35d0,0.55d0,0.75d0 /)
    call nddif_64(n,x,y,n1,x1,y1)
    do j=1,n1
        write(6,*) x1(j),y1(j)
    enddo
    end

! Subroutine (64-bit) to interpolate data points y(x)
! Gives interpolated values y1 at points x1
    subroutine nddif_64(n,x,y,n1,x1,y1)
    implicit real*8(A-H,O-Z)
    dimension x(n),y(n),x1(n1),y1(n1),f(n,n)
    do i=1,n
        f(i,1)=y(i)
    enddo
    do j=2,n
        do i=j,n
            f(i,j)=(f(i,j-1)-f(i-1,j-1))/(x(i)-x(i-j+1))
        enddo
    enddo
    y1=f(1,1)
    do j=1,n1
        p=1.d0
        do i=1,n-1
            p=p*(x1(j)-x(i))
            y1(j)=y1(j)+p*f(i+1,i+1)
        enddo
    enddo
    endsubroutine
