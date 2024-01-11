! Last updated: 28-Feb-2012
! Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
! Source: https://github.com/udy11, https://gitlab.com/udy11
! Subroutine (8-byte) to calculate electric field of a point charge

! All variables in SI Units
! (x,y,z) = co-ordinates where electric field is to be calculated
! (rx,ry,rz) = co-ordinates where point-charge is placed
! q = value of charge
! k = relative permittivity of the medium (eps=k*eps_0)
! (ex,ey,ez) = electric field vector components

	real*8 x,y,z,k,q,rx,ry,rz,ex,ey,ez
	k=1.0d0; q=1.602176565d-19
	x=-1.0d0; y=0.0d0; z=0.0d0
	rx=0.0d0; ry=0.0d0; rz=0.0d0
	call elcf_pts(x,y,z,k,q,rx,ry,rz,ex,ey,ez)
	write(*,*) ex,ey,ez
	end

! Subroutine (8-byte) to calculate electric field of a point charge
	subroutine elcf_pts(x,y,z,k,q,rx,ry,rz,ex,ey,ez)
	real*8,intent(in) :: x,y,z,k,q,rx,ry,rz
	real*8,intent(out) :: ex,ey,ez
	real*8 eps,fc,pi,rr,xx,yy,zz
	eps=8.85418781762038985d-12
	pi=3.14159265358979324d0
	xx=x-rx; yy=y-ry; zz=z-rz
	rr=xx*xx+yy*yy+zz*zz
	fc=q/(4.0d0*pi*k*eps*rr*sqrt(rr))
	ex=fc*xx; ey=fc*yy; ez=fc*zz
	end subroutine