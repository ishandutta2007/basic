! Last updated: 07-Jun-2013
! Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
! Source: https://github.com/udy11, https://gitlab.com/udy11
! Function (64-bit) to binary search nearest number in a sorted array

! ALL YOU NEED TO DO:
! Call function nbsan_64(a, n1, n2, b) with:
!   a = numerical array in which nearest number to be searched
!   n1 = first index from which to begin search (inclusive)
!   n2 = last index upto which search is to be made (inclusive)
!   b = number whose nearest to be searched
! Make sure variable types are consistent in both function and main program
!   you can quickly change variable types of aa, ad and b by changing
!   real*8 declaration everywhere below to any numerical type you want
!   but then make sure that their declaration is also consistent

! OUTPUT:
! Output of the functions is the index of number to be searched

    implicit integer*8(I-N)
    real*8 aa,ad,b
    dimension aa(1000),ad(1000)

    b=101.78d0
    do i=1,1000
        aa(i)=11.d0 + 0.1d0*i
        ad(1001-i)=aa(i)
    enddo

    n1=1
    n2=size(aa)
    nba=nbsan_asc_64(aa,n1,n2,b)
    write(6,*) nba,aa(nba)
    nbd=nbsan_dec_64(ad,n1,n2,b)
    write(6,*) nbd,ad(nbd)
    end

! For ascendingly sorted array
    integer*8 function nbsan_asc_64(a,nn1,nn2,b)
    implicit integer*8(I-N)
    real*8 a,b,d1,d2
    dimension a(nn2)
    if(b>a(nn2)) then
        nbsan_asc_64=nn2
        return
    endif
    if(b<a(nn1)) then
        nbsan_asc_64=nn1
        return
    endif
    n1=nn1; n2=nn2
    nd=n2-n1
    nm=n1+nd/2
    do while(nd>1)
        if(a(nm)>b) then
            n2=nm
        else
            n1=nm
        endif
        nd=n2-n1
        nm=n1+nd/2
    enddo
    d1=b-a(n1)
    d2=a(n2)-b
    if(d1<d2) then
        nbsan_asc_64=n1
    else
        nbsan_asc_64=n2
    endif
    endfunction

! For descendingly sorted array
    integer*8 function nbsan_dec_64(a,nn1,nn2,b)
    implicit integer*8(I-N)
    real*8 a,b,d1,d2
    dimension a(nn2)
    if(b<a(nn2)) then
        nbsan_dec_64=nn2
        return
    endif
    if(b>a(nn1)) then
        nbsan_dec_64=nn1
        return
    endif
    n1=nn1; n2=nn2
    nd=n2-n1
    nm=n1+nd/2
    do while(nd>1)
        if(a(nm)<b) then
            n2=nm
        else
            n1=nm
        endif
        nd=n2-n1
        nm=n1+nd/2
    enddo
    d1=a(n1)-b
    d2=b-a(n2)
    if(d1<d2) then
        nbsan_dec_64=n1
    else
        nbsan_dec_64=n2
    endif
    endfunction
