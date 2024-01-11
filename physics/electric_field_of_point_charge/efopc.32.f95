! Last updated: 28-Feb-2012
! Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
! Source: https://github.com/udy11, https://gitlab.com/udy11
! Subroutine (4-byte) to calculate electric field of a point charge

! All variables in SI Units
! (x,y,z) = co-ordinates where electric field is to be calculated
! (rx,ry,rz) = co-ordinates where point-charge is placed
! q = value of charge
! k = relative permittivity of the medium (eps=k*eps_0)
! (ex,ey,ez) = electric field vector components

	real x,y,z,k,q,rx,ry,rz,ex,ey,ez
	k=1.0; q=1.602176565e-19
	x=1.0; y=0.0; z=0.0
	rx=0.0; ry=0.0; rz=0.0
	call elcf_pts(x,y,z,k,q,rx,ry,rz,ex,ey,ez)
	write(*,*) ex,ey,ez
	end

! Subroutine (4-byte) to calculate electric field of a point charge
	subroutine elcf_pts(x,y,z,k,q,rx,ry,rz,ex,ey,ez)
	real,intent(in) :: x,y,z,k,q,rx,ry,rz
	real,intent(out) :: ex,ey,ez
	eps=8.8541878e-12
	pi=3.14159265
	xx=x-rx; yy=y-ry; zz=z-rz
	rr=xx*xx+yy*yy+zz*zz
	fc=q/(4.0*pi*k*eps*rr*sqrt(rr))
	ex=fc*xx; ey=fc*yy; ez=fc*zz
	end subroutine