! Last updated: 11-May-2013
! Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
! Source: https://github.com/udy11, https://gitlab.com/udy11
! Functions (32-bit) to calculate Factorial, Permutation,
! Combination and Multinomial Coefficient

! All functions are independent of each other
! They all assume correct input is given
! If incorrect input is given, unexpected results may come

    integer na(3),fct,prm,cmb,mcf
    
    n1=12; n2=5; n3=2; n4=4
    na(1)=n2; na(2)=n3; na(3)=n4
    write(6,*) 'Factorial(12):',fct(n1)
    write(6,*) 'Permutation(5,2):',prm(n2,n3)
    write(6,*) 'Combination(5,2):',cmb(n2,n3)
    write(6,*) 'Multinomial Coefficient(5,2,4):',mcf(na,size(na))
    end

! Factorial (32-bit)
! Maximum input n = 12
! Factorial defined as:
!   F(n) = 1*2*3* ... *n (for n>0)
!   F(0) = 1
    integer function fct(n)
    if(n<2) then
        fct=1
    else
        fct=2
        do i=3,n
            fct=fct*i
        enddo
    endif
    endfunction

! Permutation (32-bit)
! Permutation defined as:
! P(n,r) = n!/(n-r)!
    integer function prm(n,r)
    integer r
    if(r==0) then
        prm=1
    else
        prm=n
        do i=n-r+1,n-1
            prm=prm*i
        end do
    endif
    endfunction

! Combination (32-bit)
! Combination defined as:
! C(n,r) = n!/((n-r)! * r!)
    integer function cmb(n,r)
    integer r,r1
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

! Multinomial Coefficient (32-bit)
! Multinomial Coefficient defines as:
! MC(n1, n2, n3...) = (n1 + n2 + n3 + ...)! / ( n1! n2! n3! ...)
    integer function mcf(nn,nl)
    integer nn(nl),n(nl)
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
