! Last updated: 18-Feb-2015
! Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
! Source: https://github.com/udy11, https://gitlab.com/udy11
! Subroutine (32-bit) to find a root of a one
! dimensional function using False Position Method

! ALL YOU NEED TO DO:
! Call subroutine falspos_32() with:
!   a0,b0 = range in which root is to be found (inclusive)
!   er = tolerance below which root will be accepted,
!        i.e., when |f(c)|<er, c is accepted as root
!   c = output, which will contain the root
!   istt = status code of subroutine's execution (see below for details)
!   f(x) = external 1D function whose root is to be found

! STATUS CODE:
! istt=1, success: root found between a and b
! istt=2, success: root found at a
! istt=3, success: root found at b
! istt=-1, error: root could not be found between a and b

! NOTE:
! Don't forget to define f as external
! If f(x) does not cross the x-axis but only touches it,
!   like f(x)=x*x at x=0, then that root will most probably not be found
! Below method does not check for opposite signs to continue operating
!   as conventional false position method does, but it is then likely to
!   find a root if it exists, even if signs at boundaries are not opposite
! Subroutine is optimized for minimum calls to f(x)

    external f
    a0=-15.0; b0=4.0
    er=4.e-7

    call falspos_32(a0,b0,er,c,istt,f)

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
    real function f(x)
    f=x*x-1.0
    endfunction

! Subroutine (32-bit) to find a root of f(x) using False Position Method
    subroutine falspos_32(a0,b0,er,c,istt,f)
    logical ifa
    external f
    fa=f(a0)
    if(abs(fa)<er) then
        c=a0
        istt=2
        return
    endif
    fb=f(b0)
    if(abs(fb)<er) then
        c=b0
        istt=3
        return
    endif
    a=a0; b=b0
    if(fb==fa) then
        c=0.5*(a+b)
    else
        c=(a*fb-b*fa)/(fb-fa)
    endif
    if(c==0.0) then
        c0=1.0
    else
        c0=0.0
    endif
    do
        fc=f(c)
        if(abs(fc)<er) then
            istt=1
            exit
        else if(c==c0) then
            istt=-1
            exit
        else
            if(fa*fc<0.0) then
                b=c
                ifa=.false.
            else
                a=c
                ifa=.true.
            endif
            if(ifa) then
                fa=f(a)
            else
                fb=f(b)
            endif
        endif
        c0=c
        if(fb==fa) then
            c=0.5*(a+b)
        else
            c=(a*fb-b*fa)/(fb-fa)
        endif
    enddo
    endsubroutine
