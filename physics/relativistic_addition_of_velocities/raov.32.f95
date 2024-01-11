! Last updated: 02-Feb-2014
! Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
! Source: https://github.com/udy11, https://gitlab.com/udy11
! Subroutines (32-bit) to relativistically add velocities
! in one dimension, two dimensions and three dimensions

! ALL YOU NEED TO DO:
! Call any subroutine with:
!   u and v as velocities to add
!   w as output velocity

! NOTE:
! u and v should be in SI units
! Speed of light, c is 299792458 m/s (exact)
!   and NOT 3x10^8 m/s
! Input u and v with proper signs in cartesian coordinates,
!   they will add to (u+v) in classical mechanics

	dimension u2(2),v2(2),w2(2)
    dimension u3(3),v3(3),w3(3)

!    c=2.99792458e8 ! m/s

    u1=1.e8
    v1=-1.5e8

    u2= (/ 1.e8, 1.e8 /)
    v2= (/ 1.e8, -1.e8 /)

    u3= (/ 1.e8, 2.e7, 5.e7 /)
    v3= (/ -1.e8, 2.e7, -5.e7 /)

    call addvelrel_1d_32(u1,v1,w1)
    write(6,*) w1
    call addvelrel_2d_32(u2,v2,w2)
    write(6,*) w2
    call addvelrel_3d_32(u3,v3,w3)
    write(6,*) w3

    end

! Subroutine (32-bit) to relativistically add
! velocities in one dimension
    subroutine addvelrel_1d_32(u,v,w)
    rc2=1.11265006e-17
    w=(u+v)/(1.0+u*v*rc2)
    endsubroutine

! Subroutine (32-bit) to relativistically add
! velocities in two dimensions
    subroutine addvelrel_2d_32(u,v,w)
    dimension u(2),v(2),w(2)
    rc2=1.11265006e-17
    uvc2=(u(1)*v(1)+u(2)*v(2))*rc2
    gmv=1.0/sqrt(1.0-(v(1)*v(1)+v(2)*v(2))*rc2)
    w=((1.0+uvc2/(1.0+gmv))*v+u/gmv)/(1.0+uvc2)
    endsubroutine

! Subroutine (32-bit) to relativistically add
! velocities in three dimensions
    subroutine addvelrel_3d_32(u,v,w)
    dimension u(3),v(3),w(3)
    rc2=1.11265006e-17
    uvc2=(u(1)*v(1)+u(2)*v(2)+u(3)*v(3))*rc2
    gmv=1.0/sqrt(1.0-(v(1)*v(1)+v(2)*v(2)+v(3)*v(3))*rc2)
    w=((1.0+uvc2/(1.0+gmv))*v+u/gmv)/(1.0+uvc2)
    endsubroutine
