! Last updated: 07-Jun-2013
! Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
! Source: https://github.com/udy11, https://gitlab.com/udy11
! Function (128-bit) to binary search a number in a sorted array

! ALL YOU NEED TO DO:
! Call function bsa_128(a, n1, n2, b) with:
!   a = numerical array in which a number to be searched
!   n1 = first index from which to begin search (inclusive)
!   n2 = last index upto which search is to be made (inclusive)
!   b = number to be searched
! Make sure variable types are consistent in both function and main program
!   you can quickly change variable types of aa, ad and b by changing
!   real*8 declaration everywhere below to any numerical type you want
!   but then make sure that their declaration is also consistent

! OUTPUT:
! Output of the functions is the index of number to be searched
! If the number does not exist in the array, -1 is returned

    implicit integer*16(I-N)
    real*8 aa,ad,b
    dimension aa(1000),ad(1000)

    b=101.7d0
    do i=1,1000
        aa(i)=11.d0 + 0.1d0*i
        ad(1001-i)=aa(i)
    enddo

    n1=1
    n2=size(aa)
    nba=nbsa_asc_128(aa,n1,n2,b)
    write(6,*) nba,aa(nba)
    nbd=nbsa_dec_128(ad,n1,n2,b)
    write(6,*) nbd,ad(nbd)
    end

! For ascendingly sorted array
    integer*16 function nbsa_asc_128(a,nn1,nn2,b)
    implicit integer*16(I-N)
    real*8 a,b
    dimension a(nn2)
    if(b>a(nn2)) then
        nbsa_asc_128=-1  ! Not Found
        return
    endif
    if(b<a(nn1)) then
        nbsa_asc_128=-1  ! Not Found
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
    if(a(n1)==b) then
        nbsa_asc_128=n1
    else if(a(n2)==b) then
        nbsa_asc_128=n2
    else
        nbsa_asc_128=-1  ! Not Found
    endif
    endfunction

! For descendingly sorted array
    integer*16 function nbsa_dec_128(a,nn1,nn2,b)
    implicit integer*16(I-N)
    real*8 a,b
    dimension a(nn2)
    if(b<a(nn2)) then
        nbsa_dec_128=-1  ! Not Found
        return
    endif
    if(b>a(nn1)) then
        nbsa_dec_128=-1  ! Not Found
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
    if(a(n1)==b) then
        nbsa_dec_128=n1
    else if(a(n2)==b) then
        nbsa_dec_128=n2
    else
        nbsa_dec_128=-1  ! Not Found
    endif
    endfunction
