! Last updated: 15-Aug-2013
! Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
! Source: https://github.com/udy11, https://gitlab.com/udy11
! Functions to calculate Greatest Common Divisor
! (GCD) or Highest Common Factor (HCF) using
! Euclidean's Algorithm

! ALL YOU NEED TO DO:
! Call appropriate ngcd_() function with
!   integers (in any order)

! Integers passed to functions don't
!   change after calculation

    integer ngcd_32
    integer*8 ngcd_64
    integer*16 ngcd_128

    m=98; n=77
    write(6,*) ngcd_32(m,n)
    end

! Greatest Common Divisor (GCD) Function (32-bit)
    integer function ngcd_32(m, n)
    ngcd_32=m; n1=n
    do while(n1/=0)
        k=n1
        n1=mod(ngcd_32,k)
        ngcd_32=k
    enddo
    endfunction

! Greatest Common Divisor (GCD) Function (64-bit)
    integer*8 function ngcd_64(m, n)
    implicit integer*8(I-N)
    ngcd_64=m; n1=n
    do while(n1/=0)
        k=n1
        n1=mod(ngcd_64,k)
        ngcd_64=k
    enddo
    endfunction

! Greatest Common Divisor (GCD) Function (128-bit)
    integer*16 function ngcd_128(m, n)
    implicit integer*16(I-N)
    ngcd_128=m; n1=n
    do while(n1/=0)
        k=n1
        n1=mod(ngcd_128,k)
        ngcd_128=k
    enddo
    endfunction
