! Last updated: 04-Jun-2016
! Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
! Source: https://github.com/udy11, https://gitlab.com/udy11
! Subroutine (128-bit) to find a root of a one
! dimensional function using Bisection Method

! ALL YOU NEED TO DO:
! Call subroutine bsctn_128() with:
!   f(x) = external function whose root is to be found
!   a0,b0 = range in which root is to be found (inclusive)
!   er = tolerance below which root will be accepted,
!        i.e., when |f(c)|<er, c is accepted as root
!   c = output, which will contain the root
!   istt = status code of subroutine's execution (see below for details)

! STATUS CODE:
! istt=1, success: root found between a and b
! istt=2, success: root found at a
! istt=3, success: root found at b
! istt=-1, error: root could not be found between a and b

! NOTE:
! Don't forget to define your function as external
! If f(x) does not cross the x-axis but only touches it,
!   like f(x)=x*x at x=0, then that root will most probably not be found
! Below method does not check for opposite signs to continue operating
!   as conventional bisection method does, but it is then likely to find
!   a root if it exists, even if signs at boundaries are same
! Subroutine is optimized for minimum calls to f(x)

    implicit real*16(A-H,O-Z)
    external g
    a0=-2.q0; b0=20.q0
    er=5.q-34

    call bsctn_128(g,a0,b0,er,c,istt)

    if(istt==1) then
        write(6,*) 'Root found at',c
    else if(istt==2) then
        write(6,*) 'Root found at a,',c
    else if(istt==3) then
        write(6,*) 'Root found at b,',c
    else if(istt==-1) then
        write(6,*) 'Root could not be found in given range.'
    endif
    end

! Function whose root is to be found
    real*16 function g(x)
    implicit real*16(A-H,O-Z)
    g=x*x-1.q0
    endfunction

! Subroutine (128-bit) to find a root of f(x) using Bisection Method
    subroutine bsctn_128(f,a0,b0,er,c,istt)
    implicit real*16(A-H,O-Z)
    logical ifa,ifb
    external f
    fa=f(a0)
    fb=f(b0)
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
    eps=2.q0*epsilon(1.q0)
    a=a0; b=b0; ifa=.false.; ifb=.false.
    c=0.5q0*(a+b)
    if(abs(c-1.q0)<eps) then
        c0=2.q0
    else
        c0=1.q0
    endif
    do
        fc=f(c)
        if(abs(fc)<er) then
            istt=1
            exit
        else if(c0==0.q0 .and. c==0.q0) then
            istt=-1
            exit
        else if(c0/=0.q0 .and. abs(1.q0-c/c0)<eps) then
            istt=-1
            exit
        else
            if(ifa) then
                fa=f(a)
            else if(ifb) then
                fb=f(b)
            endif
            if(fa*fc<0.q0) then
                b=c
                ifa=.false.
                ifb=.true.
            else if(fb*fc<0.q0) then
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
        c=0.5q0*(a+b)
    enddo
    endsubroutine
