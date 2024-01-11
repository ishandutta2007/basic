! Last updated: 14-Aug-2013
! Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
! Source: https://github.com/udy11, https://gitlab.com/udy
! Power Method Subroutine (128-bit) to calculate greatest
! Eigenvalue of a Real Matrix and corresponding Eigenvector

! ALL YOU NEED TO DO:
! Call pwr_ev_128() with n, a, eg, ev and ef
!   a is the matrix whose eigens to calculate
!   n is the size of ev (or nxn is size of a)
!   eg will contain the greatest eigenvalue
!   ef is precision parameter for eigenvalue
!     such that when difference in successive calculations
!     of eigenvalues is < ef, the iteration stops
!   ev is the initial guess for eigenvector
!     and will later contain (normalized) eigenvector
! If iteration never stops, you can limit the while
!   loop where it is indicated in the function

    implicit real*16(A-H,O-Z)
    dimension a(10,10),ev(10)
    n=3

! Precision parameter for eigenvalue
    ef=1.q-33

! Matrix A whose eigens to be calculated
    a(1,1)=1.q0; a(1,2)=0.q0; a(1,3)=0.q0
    a(2,1)=0.q0; a(2,2)=1.q0; a(2,3)=2.q0
    a(3,1)=0.q0; a(3,2)=1.q0; a(3,3)=0.q0

! Initial guess for eigenvector
    ev(1)=1.q0; ev(2)=1.q0; ev(3)=1.q0

! Calling Power Method
    call pwr_ev_128(n,a(1:n,1:n),eg,ev(1:n),ef)

! Printing Output
    write(6,*) "Greatest Eigenvalue: ",eg
    write(6,*) "Eigenvector (normalized): "
    write(6,*) ev(1:n)
    end

! Power Method Function (128-bit)
    subroutine pwr_ev_128(n,a,eg,ev,ef)
    implicit real*16(A-H,O-Z)
    dimension a(n,n),ev(n),v(n)
    df=1.q+30
! If iteration does not stop, limit this
!   while loop to some finite iterations
    do while(df>ef)
        v=ev/vm(ev,n)
        ev=matmul(a,v)
        eg=dot(v,ev,n)
        v=ev-eg*v
        df=abs(eg-eg1)
        eg1=eg
    enddo
    ev=ev/vm(ev,n)
    endsubroutine

! To calculate magnitude of vector v (128-bit)
    real*16 function vm(v,n)
    implicit real*16(A-H,O-Z)
    dimension v(n)
    vm=v(1)*v(1)
    do i=2,n
        vm=vm+v(i)*v(i)
    enddo
    vm=sqrt(vm)
    endfunction

! To calculate dot product of vectors v and w (128-bit)
    real*16 function dot(v,w,n)
    implicit real*16(A-H,O-Z)
    dimension v(n),w(n)
    dot=v(1)*w(1)
    do i=2,n
        dot=dot+v(i)*w(i)
    enddo
    endfunction
