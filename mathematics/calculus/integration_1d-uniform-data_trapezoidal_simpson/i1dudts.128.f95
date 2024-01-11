! Last updated: 07-Sep-2013
! Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
! Source: https://github.com/udy11, https://gitlab.com/udy11
! Subroutines (128-bit) to integrate a one-dimensional uniformly
! spaced data using Trapezoidal Rule and Simpson's 1/3rd Rule

! ALL YOU NEED TO DO:
! Call the required subroutine with:
!   INPUT:
!     a and b as range of integration
!     f as array of numbers to be integrated
!     n as the length of array f
!   OUTPUT:
!     sm as integrated value

! NOTE:
! It is assumed that for n-length array f, f(1) corresponds
!   to a and f(n) corresponds to b
! Note that integration(f,(a,b))=-integration(f,(b,a))
!   so specify the range a,b accordingly
! For Simpson's 1/3rd Rule, n should be odd

    implicit real*16(A-H,O-Z)
    dimension f(1001)

    n=11
    a=0.q0; b=2.q0
    do i=1,n
        f(i)=i-1
    enddo

    call intd_trpzdl_128(a,b,f,n,s1)
    write(6,*) s1
    call intd_smpsn_128(a,b,f,n,s2)
    write(6,*) s2
    end

! Trapezoidal Rule Subroutine (128-bit)
! for 1D uniform data
    subroutine intd_trpzdl_128(a,b,f,n,sm)
    implicit real*16(A-H,O-Z)
    dimension f(n)  
    h=(b-a)/(n-1)
    sm=h*0.5q0*(f(1)+f(n))
    do i=2,n-1
        sm=sm+h*f(i)
    end do
    end

! Simpson's 1/3rd Rule Subroutine (128-bit)
! for 1D uniform data
    subroutine intd_smpsn_128(a,b,f,n,sm)
    implicit real*16(A-H,O-Z)
    dimension f(n)
    if(and(n,1)==0) then
        write(6,*) "ERROR: n should be odd..."
        return
    endif
    h=(b-a)/(n-1)
    smi=h*(f(1)+f(n))
    smo=0.q0
    do i=2,n-1,2
        smo=smo+h*f(i)
    end do
    sme=0.q0
    do i=3,n-1,2
        sme=sme+h*f(i)
    end do
    sm=(smi+4.q0*smo+2.q0*sme)*0.3333333333333333333333333333333333333q0
    end
