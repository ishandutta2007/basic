! Last updated: 11-May-2013
! Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
! Source: https://github.com/udy11, https://gitlab.com/udy11
! Functions (64-bit) to calculate Factorial, Permutation,
! Combination and Multinomial Coefficient

! All functions are independent of each other
! They all assume correct input is given
! If incorrect input is given, unexpected results may come
! All input must be in integer*8 (except size of array in mcf)

    implicit integer*8(I-N)
    integer*8 na(3),fct,prm,cmb,mcf
    
    n1=20; n2=10; n3=7; n4=4
    na(1)=n2; na(2)=n3; na(3)=n4
    write(6,*) 'Factorial(20):',fct(n1)
    write(6,*) 'Permutation(10,7):',prm(n2,n3)
    write(6,*) 'Combination(10,7):',cmb(n2,n3)
    write(6,*) 'Multinomial Coefficient(10,7,4):',mcf(na,size(na))
    end

! Factorial (64-bit)
! Maximum input n = 20
! Factorial defined as:
!   F(n) = 1*2*3* ... *n (for n>0)
!   F(0) = 1
    integer*8 function fct(n)
    integer*8 n,i
    if(n<2) then
        fct=1
    else
        fct=2
        do i=3,n
            fct=fct*i
        enddo
    endif
    endfunction

! Permutation (64-bit)
! Permutation defined as:
! P(n,r) = n!/(n-r)!
    integer*8 function prm(n,r)
    integer*8 n,i,r
    if(r==0) then
        prm=1
    else
        prm=n
        do i=n-r+1,n-1
            prm=prm*i
        end do
    endif
    endfunction

! Combination (64-bit)
! Combination defined as:
! C(n,r) = n!/((n-r)! * r!)
    integer*8 function cmb(n,r)
    integer*8 n,i,r,r1
    if(r>n-r) then
        r1=n-r
    else
        r1=r
    end if
    cmb=1
    do i=1,r1
        cmb=cmb*(n-i+1)/i
    end do
    endfunction

! Multinomial Coefficient (64-bit)
! Multinomial Coefficient defines as:
! MC(n1, n2, n3...) = (n1 + n2 + n3 + ...)! / ( n1! n2! n3! ...)
    integer*8 function mcf(nn,nl)
    integer*8 nn(nl),n(nl),ns
    n=nn
    ns=n(1)
    nm=maxval(n)
    if(n(1)==nm) n(1)=1
    do i=2,nl
        ns=ns+n(i)
        if(n(i)==nm) n(i)=1
    enddo
    mcf=ns
    do i=nm+1,ns-1
        mcf=mcf*i
    enddo
    do j=1,nl
        if(n(j)>1) then
            mcf=mcf/n(j)
            do i=2,n(j)-1
                mcf=mcf/i
            enddo
        endif
    enddo
    endfunction
