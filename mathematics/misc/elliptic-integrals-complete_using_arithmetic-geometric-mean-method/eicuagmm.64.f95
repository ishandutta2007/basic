! Last updated: 29-Sep-2015
! Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
! Source: https://github.com/udy11, https://gitlab.com/udy11
! Subroutine (64-bit) to calculate Complete Elliptic Integrals
! of first and second kind using Arithmetic-Geometric Mean Method

! Complete Elliptic Integrals:
! First Kind: ek(x)=Integration[1/sqrt(1-x*x*sin(t)*sin(t)),{t,0,pi/2}]
! Second Kind: ee(x)=Integration[sqrt(1-x*x*sin(t)*sin(t)),{t,0,pi/2}]

! ALL YOU NEED TO DO:
! Call subroutine elpt12_64(x,ek,ee,er), where
!   INPUT:
!   x = point in [0,1] on which you want to calculate these functions
!   er = some accuracy related parameter, just keep it low
!   OUTPUT:
!   ek = complete elliptic integral of first kind at x
!   ek = complete elliptic integral of second kind at x

! NOTE:
! The values will not match with inbuilt functions of Mathematica and Matlab
!   because their definitions are different
! Reference for algorithm: Computation of Special Functions, Zhang-Jin, 18.3.2

    implicit real*8(A-H,O-Z)
    x=0.999d0; er=5.6d-17
    call elpt12_64(x,ek,ee,er)
    write(6,*) ek,ee
    end

! Subroutine (64-bit) to calculate Complete Elliptic Integrals
! of First and Second Kind using Arithmetic Geometric Mean Method
    subroutine elpt12_64(x,ek,ee,er)
    implicit real*8(A-H,O-Z)
    if(x==1.d0) then
        ee=1.0d0
        ek=1.797693134862315d308
    else
        pib2=1.57079632679489662d0
        a0=1.0d0; b0=sqrt(1.0d0-x*x); c1=x; d0=pib2
        i=1; ee=2.0d0-c1*c1
        do while(abs(c1)>er)
            a1=(a0+b0)*0.5d0
            b1=sqrt(a0*b0)
            c1=(a0-b0)*0.5d0
            d1=d0+atan(b0*tan(d0)/a0)
            a0=a1; b0=b1; d0=d1
            ee=ee-(2.0d0**i)*c1*c1
            i=i+1
        enddo
        ek=pib2/a0
        ee=ee*pib2*0.5d0/a0
    endif
    endsubroutine
