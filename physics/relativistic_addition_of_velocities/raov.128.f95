! Last updated: 02-Feb-2014
! Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
! Source: https://github.com/udy11, https://gitlab.com/udy11
! Subroutines (128-bit) to relativistically add velocities
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

	implicit real*16(A-H,O-Z)
	dimension u2(2),v2(2),w2(2)
    dimension u3(3),v3(3),w3(3)

!    c=2.99792458q8 ! m/s

    u1=1.q8
    v1=-1.5q8

    u2= (/ 1.q8, 1.q8 /)
    v2= (/ 1.q8, -1.q8 /)

    u3= (/ 1.q8, 2.q7, 5.q7 /)
    v3= (/ -1.q8, 2.q7, -5.q7 /)

    call addvelrel_1d_128(u1,v1,w1)
    write(6,*) w1
    call addvelrel_2d_128(u2,v2,w2)
    write(6,*) w2
    call addvelrel_3d_128(u3,v3,w3)
    write(6,*) w3

    end

! Subroutine (128-bit) to relativistically add
! velocities in one dimension
    subroutine addvelrel_1d_128(u,v,w)
    implicit real*16(A-H,O-Z)
    rc2=1.11265005605361843217408996484800999q-17
    w=(u+v)/(1.q0+u*v*rc2)
    endsubroutine

! Subroutine (128-bit) to relativistically add
! velocities in two dimensions
    subroutine addvelrel_2d_128(u,v,w)
    implicit real*16(A-H,O-Z)
    dimension u(2),v(2),w(2)
    rc2=1.11265005605361843217408996484800999q-17
    uvc2=(u(1)*v(1)+u(2)*v(2))*rc2
    gmv=1.q0/sqrt(1.q0-(v(1)*v(1)+v(2)*v(2))*rc2)
    w=((1.q0+uvc2/(1.q0+gmv))*v+u/gmv)/(1.q0+uvc2)
    endsubroutine

! Subroutine (128-bit) to relativistically add
! velocities in three dimensions
    subroutine addvelrel_3d_128(u,v,w)
    implicit real*16(A-H,O-Z)
    dimension u(3),v(3),w(3)
    rc2=1.11265005605361843217408996484800999q-17
    uvc2=(u(1)*v(1)+u(2)*v(2)+u(3)*v(3))*rc2
    gmv=1.q0/sqrt(1.q0-(v(1)*v(1)+v(2)*v(2)+v(3)*v(3))*rc2)
    w=((1.q0+uvc2/(1.q0+gmv))*v+u/gmv)/(1.q0+uvc2)
    endsubroutine
