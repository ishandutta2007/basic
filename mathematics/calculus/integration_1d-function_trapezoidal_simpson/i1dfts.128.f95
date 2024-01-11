! Last updated: 07-Oct-2015
! Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
! Source: https://github.com/udy11, https://gitlab.com/udy11
! Subroutines (128-bit) to integrate one-dimensional function
! using Trapezoidal and Simpson's 1/3rd Rules

! ALL YOU NEED TO DO:
! Call required subroutine with parameters
!   INPUT:
!   f = external function whose integration is to be calculated
!   a, b = range in which to integrate
!   n = number of sample points to take for integration (including end-points)
!   OUTPUT:
!   s = output of integration

! NOTE:
! Choosing a large n will cause truncation error to reduce
!   but will increase roundoff error, so choose as per needs
! In case your function has some parameters, you can specify them in function
!   itself or in common block; for latter, common block definition is needed
!   in both main program and function f but not in integration subroutines,
!   however, note that order of parameters must be same in both common blocks
! Note that integration(f(x),(a,b))=-integration(f(x),(b,a))
!   so specify the range a,b accordingly
! Don't forget to specify function f as external
! In case of Simpson's 1/3rd rule, number of points n should be odd (or
!   equivalently, number of intervals should be even); however, if n is
!   given even, the program uses n-1 points (maintaining the range a to b)

! Below is example of integration(d/(1+x*x),(x,0,1)), with d=4

    implicit real*16(A-H,O-Z)
    external fx
    common d

    a=0.0q0; b=1.0q0; n=129999
    d=4.0q0

    call int_trpzdl_128(fx,a,b,n,sm)
    write(6,*) sm
    call int_smpsn_128(fx,a,b,n,sm)
    write(6,*) sm
    end

! INPUT FUNCTION
    real*16 function fx(x)
    implicit real*16(A-H,O-Z)
    common d
    fx=d/(1.q0+x*x)
    end function

! Trapezoidal Rule Subroutine (128-bit)
! Truncation Error = -(b-a)(h^2)f''(z)/12, a<z<b
    subroutine int_trpzdl_128(f,a,b,n,s)
    implicit real*16(A-H,O-Z)
    external f
    h=(b-a)/(n-1)
    s=h*0.5q0*(f(a)+f(b))
    do i=1,n-2
        s=s+h*f(a+i*h)
    end do
    end

! Simpson's 1/3rd Rule Subroutine (128-bit)
! Truncation Error = -(b-a)(h^4)f''''(z)/180, a<z<b
    subroutine int_smpsn_128(f,a,b,n,s)
    implicit real*16(A-H,O-Z)
    external f
    if(and(n,1)==0) then
        m=n-1
    else
        m=n
    endif
    h=(b-a)/(m-1)
    s=h*(f(a)+f(b)+4.0q0*f(b-h))*0.33333333333333333333333333333333333333q0
    do i=1,m/2-1
        s=s+h*(4.0q0*f(a+(2*i-1)*h)+2.0q0*f(a+2*i*h))* &
            0.33333333333333333333333333333333333333q0
    end do
    end
