! Last updated: 08-Oct-2015
! Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
! Source: https://github.com/udy11, https://gitlab.com/udy11
! Subroutines (32-bit) to calculate single derivative of a
! one-dimensional uniformly spaced data using 5-Point Formula

! ALL YOU NEED TO DO:
! Call subroutine der1_32() with:
!   INPUT:
!     n as the length of array f (and df)
!     h as the spacing in abscissa
!     f as array whose derivative needs to be calculated
!   OUTPUT:
!     df as array containing single derivative of f

! NOTE:
! According to 5-Point Formula, the size of output array df
!   should be 4 less than the size of f becasue to get the
!   derivative at any point it needs 2 points before and after it,
!   however, one expects that df should be of same size
!   and so, interpolation is used on initial and last points
!   to get derivatives on them, however, this will make
!   derivatives at initail and last points to be less accurate

! Given below is example of exp(x) in 0 to 1
! Only first 10 values are printed on screen

    dimension f(1000),df(1000)

    n=100
    do i=1,n
        f(i)=exp((i-1)*1.0/(n-1))
    enddo

    call der1_32(n,1.0/(n-1),f,df)

    do i=1,min(n,10)
        write(6,*) (i-1)*1.0/(n-1),f(i),df(i)
    enddo

    end

! Subroutine (32-bit) to calculate single derivative of
! one-dimensional uniformly spaced data using
! the 5-point formula
! Time Complexity ~ O(n)
! Space Complexity ~ O(n)
! Truncation Error: h**4*f'''''(z)/30, x-2h<z<x+2h
    subroutine der1_32(n,h,f,df)
    dimension f(n),df(n)
    if(h==0.0) then
        write(6,*) 'ERROR: Derivative step size cannot be zero...'
        return
    else if(h<0.0) then
        h=-h
    endif
    if(n>3) then
        h12=1.0/(12.0*h)
        a1=4.0*f(1)-6.0*f(2)+4.0*f(3)-f(4)
        a2=10.0*f(1)-20.0*f(2)+15.0*f(3)-4.0*f(4)
        b1=4.0*f(n)-6.0*f(n-1)+4.0*f(n-2)-f(n-3)
        b2=10.0*f(n)-20.0*f(n-1)+15.0*f(n-2)-4.0*f(n-3)
        df(1)=(a2-8.0*a1+8.0*f(2)-f(3))*h12
        df(n)=(f(n-2)-8.0*f(n-1)+8.0*b1-b2)*h12
        df(2)=(a1-8.0*f(1)+8.0*f(3)-f(4))*h12
        df(n-1)=(f(n-3)-8.0*f(n-2)+8.0*f(n)-b1)*h12
        do i=3,n-2
            df(i)=(f(i-2)-8.0*f(i-1)+8.0*f(i+1)-f(i+2))*h12
        enddo
    else if(n==3) then
        df(1)=-0.5*(3.0*f(1)-4.0*f(2)+f(3))/h
        df(2)=(f(3)-f(1))*0.5/h
        df(3)=0.5*(f(1)-4.0*f(2)+3.0*f(3))/h
    else if(n==2) then
        df(1)=(f(2)-f(1))/h
        df(2)=df(1)
    else
        df=0.0
    endif
    endsubroutine
