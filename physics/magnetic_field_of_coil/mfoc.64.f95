! Last Updated: 07-Dec-2015
! Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
! Source: https://github.com/udy11, https://gitlab.com/udy11
! Subrotuine (64-bit) to compute magnetic field due to
! current carrying coil at any point in space
! Uses Complete Elliptic Integrals subroutine

! ALL YOU NEED TO DO:
! Call coil_bxyz_64() with:
!   INPUT:
!     uu = permeability constant of the medium
!     cr = coil radius
!     ci = coil current (sign sensitive)
!     ax(3) = direction in which coil axis is pointing (can be unnormalized)
!     xc(3) = co-ordinates of the center of coil
!     xr(3) = co-ordinates at which magnetic field is to be calculated
!   OUTPUT:
!     bm(3) = cartesian components of magnetic field

! NOTE:
! All numbers and calculations in SI Units
! Please read the attached pdf file for the expression of magnetic field
! ax, xc, xr and bm have 3 elements each representing x, y and z
!   components respectively
! If elliptic integral shows any error, try increasing the 4th parameter
!   in elpt12_64() in coil_bxyz_64() subroutine
! Magnetic field blows up at the coil's position, make sure xr is not
!   very near the coil

    implicit real*8(A-H,O-Z)
    dimension ax(3),xc(3),xr(3),bm(3)

    uu=3.14159265358979324d0*4.d-7
    ci=1.d0
    cr=0.8d0
    xc=(/0.d0,0.d0,0.d0/)
    ax=(/0.d0,0.d0,1.d0/)

    xr=(/0.d0,1.d0,1.d0/)
    call coil_bxyz_64(uu,cr,ci,ax,xc,xr,bm)
    write(6,*) bm

! To write magnetic field in a file, first 3 columns as position
! and last 3 columns as magnetic field components
!!     open(718,file='tcmfdtac.out.txt')
!!     do i=1,51
!!       xr(1)=-1.d0+(i-1)*0.04d0
!!       do j=1,51
!!         xr(2)=-1.d0+(j-1)*0.04d0
!!         do k=1,51
!!           xr(3)=-1.d0+(k-1)*0.04d0
!!           call coil_bxyz_64(uu,cr,ci,ax,xc,xr,bm)
!!           write(718,*) xr,bm
!!         enddo
!!       enddo
!!     enddo
!!     close(718)

    end

! Magnetic Field at (xr(1),xr(2),xr(3)) due to a coil centered
! at (xc(1),xc(2),xc(3)) and axis pointing at (ax(1),ax(2),ax(3))
! Look at the attached pdf file for exact setup
    subroutine coil_bxyz_64(uu,cr,ci,ax,xc,xr,bm)
    implicit real*8(A-H,O-Z)
    dimension ax(3),xc(3),xr(3),bm(3),x1(3),x2(3),rt(3,3)
    ax12=ax(1)*ax(1)+ax(2)*ax(2)
    ax123s=sqrt(ax12+ax(3)*ax(3))
    cth=ax(3)/ax123s
    sth=sqrt(ax12)/ax123s
    ph=atan2(ax(2),ax(1))
    cph=cos(ph)
    sph=sin(ph)
    x1=xr+xc
    x1cs=x1(1)*cph+x1(2)*sph
    x2(1)=x1cs*cth-x1(3)*sth
    x2(2)=-x1(1)*sph+x1(2)*cph
    x2(3)=x1cs*sth+x1(3)*cth
    x2r=sqrt(x2(1)*x2(1)+x2(2)*x2(2))
    if(x2r<2.22044604925032d-16) then
        tv1=uu*ci*cr*cr*0.5d0*(1.d0/sqrt(cr*cr+x2(3)*x2(3)))**3
        bm(1)=tv1*cph*sth
        bm(2)=tv1*sth*sph
        bm(3)=tv1*cth
    else
        x2t=atan2(x2(2),x2(1))
        ck2=4.d0*cr*x2r/((x2r+cr)*(x2r+cr)+x2(3)*x2(3))
        ck=sqrt(ck2)
        call elpt12_64(ck,ek,ee,5.6d-17)
        tv1=uu*ci*ck*0.07957747154594766788d0/x2r/sqrt(cr*x2r)
        tv2=0.5d0*ee/(1.d0-ck2)
        tv3=tv1*(tv2*(2.d0-ck2)-ek)*x2(3)
        bm(1)=tv3*cos(x2t)
        bm(2)=tv3*sin(x2t)
        bm(3)=tv1*(tv2*(ck2*(x2r+cr)-2.d0*x2r)+ek*x2r)
        rt(1,1)=cth*cph
        rt(1,2)=-sph
        rt(1,3)=sth*cph
        rt(2,1)=cth*sph
        rt(2,2)=cph
        rt(2,3)=sth*sph
        rt(3,1)=-sth
        rt(3,2)=0.d0
        rt(3,3)=cth
        bm=matmul(rt,bm)
    endif
    endsubroutine

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
