! Last updated: 23-Sep-2013
! Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
! Source: https://github.com/udy11, https://gitlab.com/udy11
! Subroutine (128-bit) to integrate one-dimensional
! non-uniformly spaced data using Trapezoidal Rule

! ALL YOU NEED TO DO:
! Call subroutine intnud_trpzdl_128(x,f,n,sm) with x as array of abscissae
!   and f as array of data to be integrated

    implicit real*16(A-H,O-Z)
    dimension f(100),x(100)

    n=11
    a=0.q0; b=10.q0
    do i=1,n
        x(i)=i-1
        f(i)=i-1
    enddo

    call intnud_trpzdl_128(x,f,n,sm)
    write(6,*) sm
    end

! Trapezoidal Rule Subroutine (128-bit)
! for 1D non-uniform data with abscissae
! and data entered as separate arrays
    subroutine intnud_trpzdl_128(x,f,n,sm)
    implicit real*16(A-H,O-Z)
    dimension x(n),f(n) 
    sm=0.0
    do i=1,n-1
        sm=sm+(x(i+1)-x(i))*(f(i+1)+f(i))
    end do
    sm=sm*0.5q0
    end
