! Last updated: 26-Apr-2013
! Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
! Source: https://github.com/udy11, https://gitlab.com/udy11
! Subroutine (64-bit) to find a root of a one
! dimensional function using Newton-Raphson Method

! ALL YOU NEED TO DO:
! Specify an initial guess x0,
!   it must be near the desired root
! Specify the function y(x), whose root is needed
! Specify the derivative of y(x) as yp(x)
! Specify positive small er; when |y(x1)|<er, further
!   computation stops and x1 is returned as root

    implicit real*8(A-H,O-Z)
    x0=9.7d0
    er=4.0d-16

    call nwtn_rphsn_64(x0,er,x1)

    write(6,*) x1,y(x1)
    end

! Input Function y(x), whose root is to be found
    real*8 function y(x)
    implicit real*8(A-H,O-Z)
    y=sin(x)
    endfunction

! Derivative of y(x), i.e. dy(x)/dx
    real*8 function yp(x)
    implicit real*8(A-H,O-Z)
    yp=cos(x)
    endfunction

! Subroutine (64-bit) to find root of y(x)=0
! using Newton-Raphson Method
! x0 is initial guess
! er is a small positive number such that when
! |y(x1)|<er, further calculation is stopped
    subroutine nwtn_rphsn_64(x0,er,x1)
    implicit real*8(A-H,O-Z)
    do
      x1=x0-y(x0)/yp(x0)
      if(abs(y(x1))<er) exit
      x0=x1
    enddo
    endsubroutine
