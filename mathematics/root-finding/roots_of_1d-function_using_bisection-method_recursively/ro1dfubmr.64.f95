! Last updated: 05-Jun-2016
! Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
! Source: https://github.com/udy11, https://gitlab.com/udy11
! Subroutine (64-bit) to find roots of a one dimensional
! function by recursively using Bisection Method

! ALL YOU NEED TO DO:
! Call subroutine bsctns_64() with:
!   f(x) = external function whose root is to be found
!   a0,b0 = range in which root is to be found (inclusive)
!   er = tolerance below which root will be accepted,
!        i.e., when |f(c)|<er, c is accepted as root
!   nk = in how many equal intervals to divide (a, b) into,
!        recursive root finding is attempted in each of
!        these intervals
!   nd = simply put, keep this low like 1, 2, 3 or 4. this int
!        decides how closely to single-out a root once it is found.
!        a larger int will better single-out the root but will
!        require several function calls too, so better keep it low
!   rts = array which will contain the found roots, its size
!         should be sufficient to keep all the roots found
!   nr = number of roots found by bsctns_64()
!   c = output, which will contain the root
!   istt = status code of subroutine's execution (see below for details)

! ALGORITHM:
! (a, b) is divided into nk equal intervals then bisection
! method is applied in all these intervals (say one of them is
! (p, q)). if a root r is found in (p, q), then new roots are recursively
! attempted to find between (p, r-dr1) and (r+dr2, q) where
! dr1 and dr2 are approximately calculated such that all x
! in (r-dr1, r+dr2) have |f(x)| < er. how better dr1 and dr2 are
! depends on how large nd is, but a large nd will also require
! many function calls (which might be costly) so better keep nd low.

! SUGGESTIONS:
! Obviously this method is not guaranteed to find all roots of the
! function, so it is suggested that:
! 1. If possible check the plot of f(x) and identify all intervals
!    where roots might exist, it will be best if f(x) has opposite
!    signs on the ends of these intervals
! 2. If satisfactory roots are not found, first try increasing
!    er (compromise with accuracy); next try to increase nk (compromise
!    with efficiency); lastly, changing nd should not have much effect
!    but try to vary it in 1-5 (large nd is compromise with efficiency,
!    low nd is compromise with accuracy)

! NOTE:
! If f(x) does not cross the x-axis but only touches it,
!   like f(x)=x*x at x=0, then that root will most probably not be found
! Below method does not check for opposite signs to continue operating
!   as conventional bisection method does, but it is then likely to find
!   a root if it exists, even if signs at boundaries are same
! Method is optimized for minimum calls to f(x)
! Roots will not be sorted

    implicit real*8(A-H,O-Z)
    dimension rt(100)
    external g
    a0=-20.d0; b0=20.d0
    er=1.d-14
    nk=10; nd=3

    call bsctns_64(g,a0,b0,er,nk,nd,rt,nr)

    do i=1,nr
        write(6,*) rt(i)
    enddo

    end

! Function whose root is to be found
    real*8 function g(x)
    implicit real*8(A-H,O-Z)
    g=0.999999d0+sin(x)
    endfunction

    subroutine bsctn_64(f,a0,b0,er,eps,c,istt)
    implicit real*8(A-H,O-Z)
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
    a=a0; b=b0; ifa=.false.; ifb=.false.
    c=0.5d0*(a+b)
    if(abs(c-1.d0)<eps) then
        c0=2.d0
    else
        c0=1.d0
    endif
    do
        fc=f(c)
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
                fa=f(a)
            else if(ifb) then
                fb=f(b)
            endif
            if(fa*fc<0.d0) then
                b=c
                ifa=.false.
                ifb=.true.
            else if(fb*fc<0.d0) then
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

    real*8 function fbdr(f,b,er,nd,eps,fmn)
    implicit real*8(A-H,O-Z)
    external f
    e2=max(abs(b)*eps,fmn)
    do while(abs(f(b-e2))<er)
        e2=e2*2.d0
    enddo
    e1=e2*0.5d0
    i=1
    do while(i<=nd .and. abs(1.d0-e2/e1)>eps)
        e3=0.5d0*(e1+e2)
        if(abs(f(b-e3))<er) then
            e1=e3
        else
            e2=e3
        endif
        i=i+1
    enddo
    fbdr=e2
    endfunction

    real*8 function fadr(f,a,er,nd,eps,fmn)
    implicit real*8(A-H,O-Z)
    external f
    e2=max(abs(a)*eps,fmn)
    do while(abs(f(a+e2))<er)
        e2=e2*2.d0
    enddo
    e1=e2*0.5d0
    i=1
    do while(i<=nd .and. abs(1.d0-e2/e1)>eps)
        e3=0.5d0*(e1+e2)
        if(abs(f(a+e3))<er) then
            e1=e3
        else
            e2=e3
        endif
        i=i+1
    enddo
    fbdr=e2
    endfunction

    recursive subroutine rrtf(f,a,b,er,nd,eps,fmn,rts,nr)
    implicit real*8(A-H,O-Z)
    dimension rts(*)
    external f
    call bsctn_64(f,a,b,er,eps,r,ist)
    if(ist==1) then
        rts(nr)=r
        nr=nr+1
        dr=fbdr(f,r,er,nd,eps,fmn)
        call rrtf(f,a,r-dr,er,nd,eps,fmn,rts,nr)
        dr=fadr(f,r,er,nd,eps,fmn)
        call rrtf(f,r+dr,b,er,nd,eps,fmn,rts,nr)
    else if(ist==2) then
        rts(nr)=r
        nr=nr+1
        dr=fadr(f,r,er,nd,eps,fmn)
        call rrtf(f,r+dr,b,er,nd,eps,fmn,rts,nr)
    else if(ist==3) then
        rts(nr)=r
        nr=nr+1
        dr=fbdr(f,r,er,nd,eps,fmn)
        call rrtf(f,a,r-dr,er,nd,eps,fmn,rts,nr)
    endif
    endsubroutine

! Subroutine (64-bit) to find roots of f(x) by recursively using Bisection Method
    subroutine bsctns_64(f,a,b,er,nk,nd,rts,nr)
    implicit real*8(A-H,O-Z)
    logical ch
    dimension rts(*)
    external f
    eps=2.d0*epsilon(1.d0)
    fmn=tiny(1.d0)
    dab=(b-a)/nk
    nr=1
    do k=1,nk
        a1=a+(k-1)*dab
        ch=.true.
        do j=1,nr
            if(rts(j)==a1) then
                adr=fadr(f,a1,er,nd,eps,fmn)
                ch=.false.
                exit
            endif
        enddo
        if(ch) adr=0.d0
        call rrtf(f,a1+adr,a+k*dab,er,nd,eps,fmn,rts,nr)
    enddo
    nr=nr-1
    endsubroutine
