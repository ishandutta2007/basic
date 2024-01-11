! Last updated: 31-Jul-2016
! Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
! Source: https://github.com/udy11, https://gitlab.com/udy11
! Subroutine (64-bit) to solve two coupled ordinary differential
! equations with boundary values type-4 using Shooting Method
! via Bisection method and Runge Kutta 4 (RK4) method

! This program solves for two coupled ODEs:
!   y'(1)=f(x,y(1),y(2))(1)
!   y'(2)=f(x,y(1),y(2))(2)
!   y(2)=y21 at x=x1 and y(2)=y22 at x=x2

! ALL YOU NEED TO DO:
! Call subroutine shooting4_64() with:
!   fx = external subroutine that describes ODE (as described below INPUT FUNCTION)
!   nt = number of steps between x1 and x2 for RK4 test runs (excluding x1, including x2)
!   nf = number of steps between x1 and x2 for RK4 final run (excluding x1, including x2)
!   x1, x2 = initial and final values of x
!   y21, y22 = boundary values of y(2), i.e., y(2) at x1 and x2
!   y1g1, y1g2 = guess values for y(1) at x1 (Bisection method will try to find y(1) at x1 between these two guesses)
!   er = tolerance below which Bisection method accepts the root, i.e., when |g(c)|<er, c is accepted as root of g(x)
!   ofln = output file name

! OUTPUT:
! Output is in the text file, whose name is given by ofln
! First column represents x, followed by y(1) and y(2)

! A 2nd order ODE can be broken into two coupled ODEs, as exemplified below:
! y''-y'+y=x*x, can be broken as y'(1)=y(2); y'(2)=y(2)-y(1)+x*x

    implicit real*8(A-H,O-Z)
    character*150 ofln
    external fx

! INPUTS
    nt=2000                     ! number of steps for test RK4s
    nf=10000                    ! number of steps for final RK4
    x1=0.d0; x2=1.d0            ! boundary values of x
    y21=1.7635d0; y22=2.1256d0  ! values for y(2) at x1 and y(1) at x2
    y1g1=-1.d0; y1g2=3.d0       ! guess values for y(1) at x1
    er=1.d-8                    ! tolerance for Bisection method
    
    ofln="sh4.out.txt"          ! output file name

    call shooting4_64(fx,nt,nf,x1,x2,y21,y22,y1g1,y1g2,er,ofln)

    end

! INPUT FUNCTION
! Simply define functions f(1) and f(2)
! for coupled ODEs: y'(1)=f(x,y(1),y(2))(1) and y'(2)=f(x,y(1),y(2))(2)
! Example:
! Suppose you want to solve: y'(1)=y(2); y'(2)=-100*y(1)
! Then define f(1)=y(2) and f(2)=-100.0d0*y(1)
! This means these functions are simply the RHS in those...
! ... coupled ODEs, when arranged properly.
    subroutine fx(f,x,y)
    implicit real*8(A-H,O-Z)
    dimension f(2),y(2)
    f(1)=y(2)
    f(2)=y(2)-y(1)+x*x
    endsubroutine

! Shooting Method BVP-4 (64-bit)
    subroutine shooting4_64(fx,nt,nf,x1,x2,y21,y22,y1g1,y1g2,er,ofln)
    implicit real*8(A-H,O-Z)
    character*150 ofln
    external fx
    ht=(x2-x1)/nt
    call bsctn4_64(fx,nt,ht,y21,y22,y1g1,y1g2,er,y11,istt)
    if(istt<0) then
        write(6,*) "ERROR: Bisection method could not find y(1) at x1 between given guess values."
        stop
    endif
    hf=(x2-x1)/nf
    call rk44shooting_64(fx,hf,nf,x1,y11,y21,ofln)
    write(6,*) "Output written in file: ",trim(ofln)
    endsubroutine

! Bisection Method (64-bit) to be used by Shooting Method BVP-4
    subroutine bsctn4_64(fx,nt,ht,y21,y22,a0,b0,er,c,istt)
    implicit real*8(A-H,O-Z)
    logical ifa,ifb
    external fx
    fa=rk44bisection4_64(fx,ht,nt,x0,a0,y21)-y22
    fb=rk44bisection4_64(fx,ht,nt,x0,b0,y21)-y22
!    if(fa*fb>0.d0) write(6,*) "WARNING: Bisection Method may fail, consider choosing different guess values."
    if(abs(fa)<er) then
        c=a0
        istt=2
        return
    endif
    if(abs(fb)<er) then
        c=b0
        istt=3
        return
    endif
    eps=2.d0*epsilon(1.d0)
    a=a0; b=b0; ifa=.false.; ifb=.false.
    c=0.5d0*(a+b)
    if(abs(c-1.d0)<eps) then
        c0=2.d0
    else
        c0=1.d0
    endif
    do
        fc=rk44bisection4_64(fx,ht,nt,x0,c,y21)-y22
        if(abs(fc)<er) then
            istt=1
            exit
        else if(c0==0.d0 .and. c==0.d0) then
            istt=-1
            exit
        else if(c0/=0.d0 .and. abs(1.d0-c/c0)<eps) then
            istt=-1
            exit
        else
            if(ifa) then
                fa=rk44bisection4_64(fx,ht,nt,x0,a,y21)-y22
            else if(ifb) then
                fb=rk44bisection4_64(fx,ht,nt,x0,b,y21)-y22
            endif
            if(fa*fc<0) then
                b=c
                ifa=.false.
                ifb=.true.
            else if(fb*fc<0) then
                a=c
                ifa=.true.
                ifb=.false.
            else if(abs(fa)<abs(fb)) then
                b=c
                ifa=.false.
                ifb=.true.
            else
                a=c
                ifa=.true.
                ifb=.false.
            endif
        endif
        c0=c
        c=0.5d0*(a+b)
    enddo
    endsubroutine

! Runge Kutta 4 Method (64-bit) to be used by Bisection Method (SM BVP-4)
    real*8 function rk44bisection4_64(fx,h,ns,x0,y1,y2)
    implicit real*8(A-H,O-Z)
    dimension f(2),y(2)
    real*8 k1(2),k2(2),k3(2),k4(2)
    external fx
    x=x0
    y(1)=y1
    y(2)=y2
    do i=1,ns
        call fx(f,x,y)
        k1=h*f
        xh=x+0.5d0*h
        call fx(f,xh,y+0.5d0*k1)
        k2=h*f
        call fx(f,xh,y+0.5d0*k2)
        k3=h*f
        call fx(f,x+h,y+k3)
        k4=h*f
        x=x0+i*h
        y=y+(k1+2.0d0*(k2+k3)+k4)*0.166666666666666667d0
    enddo
    rk44bisection4_64=y(2)
    endfunction

! Runge Kutta 4 Method (64-bit) to be used by Shooting Method
    subroutine rk44shooting_64(fx,h,ns,x0,y1,y2,ofln)
    implicit real*8(A-H,O-Z)
    character*150,intent(in) :: ofln
    dimension f(2),y(2)
    real*8 k1(2),k2(2),k3(2),k4(2)
    external fx
    open(479,file=ofln)
    write(479,*) x0,y1,y2       ! Initial values written to output file
    x=x0
    y(1)=y1
    y(2)=y2
    do i=1,ns
        call fx(f,x,y)
        k1=h*f
        xh=x+0.5d0*h
        call fx(f,xh,y+0.5d0*k1)
        k2=h*f
        call fx(f,xh,y+0.5d0*k2)
        k3=h*f
         call fx(f,x+h,y+k3)
        k4=h*f
        x=x0+i*h
        y=y+(k1+2.0d0*(k2+k3)+k4)*0.166666666666666667d0
        write(479,*) x,y
    enddo
    close(479)
    endsubroutine
