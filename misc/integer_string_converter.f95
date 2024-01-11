! Last updated: 11-Mar-2014
! Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
! Source: https://github.com/udy11, https://gitlab.com/udy11
! Subroutines to convert integer to string and vice versa

! ALL YOU NEED TO DO:
! Call subroutine with parameters:
!   k = length of the character ch, must be sufficiently large
!   ii = integer form of ch
!   ch = character form of ii

! Use subroutine in2st_w0() if you want output string with leading zeros
!   for example '003008' or '-03008'
! Use subroutine in2st_ws() if you want output string with leading spaces
!   for example '  3008' or ' -3008'

! Use subroutine st2in_w0() if input string has integer with leading zeros
!   for example '003008' or '-03008'
! Use subroutine st2in_ws() if input string has integer with leading spaces
!   for example '  3008' or ' -3008'

! If subroutines are called with insufficient string lengths,
!   undesired results will come

    character*6 ch0,chs
    
    ii=-490
    k=6
    call in2st_w0(k,ii,ch0)
    write(6,*) ch0
    call in2st_ws(k,ii,chs)
    write(6,*) chs
    
    ch0='-03058'
    chs=' -3058'
    call st2in_w0(len(ch0),ch0,ii0)
    write(6,*) ii0
    call st2in_ws(len(chs),chs,iis)
    write(6,*) iis
    
    end    

! Integer to String converter (with leading zeros)
!  1201 --> '001201'
! -1201 --> '-01201'
    subroutine in2st_w0(k,ii,ch0)
    character(len=k) ch0
    if(ii<0) then
        m=-1*ii
        ch0(1:1)='-'
        do i=2,k
            ki=k-i
            ch0(i:i)=char(48+m/10**ki)
            m=m-(m/10**ki)*10**ki
        enddo
    else
        m=ii
        do i=1,k
            ki=k-i
            ch0(i:i)=char(48+m/10**ki)
            m=m-(m/10**ki)*10**ki
        enddo
    endif
    endsubroutine

! Integer to String converter (with leading zeros)
!  1201 --> '  1201'
! -1201 --> ' -1201'
    subroutine in2st_ws(k,ii,chs)
    character(len=k) chs
    if(ii<0) then
        m=-1*ii
        n=int(log(m*1.d0)/log(1.d1))+1
        kn=k-n
        do i=1,kn-1
            chs(i:i)=' '
        enddo
        chs(kn:kn)='-'
        do i=kn+1,k
            ki=k-i
            chs(i:i)=char(48+m/10**ki)
            m=m-(m/10**ki)*10**ki
        enddo
    else
        m=ii
        n=int(log(m*1.d0)/log(1.d1))+1
        do i=1,k-n
            chs(i:i)=' '
        enddo
        do i=k-n+1,k
            ki=k-i
            chs(i:i)=char(48+m/10**ki)
            m=m-(m/10**ki)*10**ki
        enddo
    endif
    endsubroutine

! String to Integer converter (with leading zeros)
! '001201' --> 1201
! '-01201' --> -1201
    subroutine st2in_w0(k,ch,ii)
    character(len=k) ch
    ii=ichar(ch(k:k))-48
    i=k-1
    do while(ch(i:i)/='-' .and. i>0)
        ii=ii+(ichar(ch(i:i))-48)*10**(k-i)
        i=i-1
    end do
    if(ch(1:1)=='-') ii=-1*ii
    endsubroutine

! String to Integer converter (with leading spaces)
! It will convert a string '  1201' to integer 1201
! '  1201' --> 1201
! ' -1201' --> -1201
    subroutine st2in_ws(k,ch,ii)
    character(len=k) ch
    ii=ichar(ch(k:k))-48
    i=k-1
    do while(ch(i:i)/=' ' .and. ch(i:i)/='-')
        ii=ii+(ichar(ch(i:i))-48)*10**(k-i)
        i=i-1
    enddo
    if(ch(i:i)=='-') ii=-1*ii
    endsubroutine
