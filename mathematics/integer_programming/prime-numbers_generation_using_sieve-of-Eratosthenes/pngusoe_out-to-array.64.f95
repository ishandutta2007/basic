! Last updated 13-Apr-2015
! Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
! Source: https://github.com/udy11, https://gitlab.com/udy11
! Subroutine (64-bit) to generate prime numbers upto
! n using the sieve of Eratosthenes

! ALL YOU NEED TO DO:
! Call subroutine primes_soe_64(n,np,m), where:
!   n = (input) number upto which primes are needed (inclusive)
!   np = (output) array containing primes
!   m = (output) number of primes generated

    implicit integer*8(I-N)
    dimension np(2000)
    n=289
    call primes_soe_64(n,np,m)
    do i=1,m
        write(6,*) np(i)
    enddo
    end

! Subroutine (64-bit) to generate
! Prime Numbers using the sieve of Eratosthenes
    subroutine primes_soe_64(n,np,m)
    implicit integer*8(I-N)
    logical ip((n-1)/2)
    dimension np(1+(n-1)/2)
    if(n<2) then
        m=0
        return
    endif
    ip=.true.
    n2=(n-1)/2
    k=3
    nsq=int(sqrt(n*1.d0)+0.5d0,8)
    do while(k<=nsq)
        do i=k*k/2,n2,k
            ip(i)=.false.
        enddo
        do while(k<=nsq)
            k=k+2
            if(ip(k/2)) then
                exit
            endif
        enddo
    enddo
    m=1
    np(1)=int(2,8)
    do i=1,n2
        if(ip(i)) then
            m=m+1
            np(m)=2*i+1
        endif
    enddo
    endsubroutine
