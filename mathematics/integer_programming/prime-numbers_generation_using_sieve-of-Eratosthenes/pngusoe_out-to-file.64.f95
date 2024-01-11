! Last updated 13-Apr-2015
! Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
! Source: https://github.com/udy11, https://gitlab.com/udy11
! Subroutine (64-bit) to generate prime numbers upto
! n using the sieve of Eratosthenes

! ALL YOU NEED TO DO:
! Call subroutine primes_soe_fyl_64(n,ofln), where:
!   n = (input) number upto which primes are needed (inclusive)
!   ofln = (input) file name that will contain the primes (will be overwritten)

    implicit integer*8(I-N)
    character*150 ofln
    n=289
    ofln="prms.txt"
    call primes_soe_fyl_64(n,ofln)
    end

! Subroutine (64-bit) to generate
! Prime Numbers using the sieve of Eratosthenes
    subroutine primes_soe_fyl_64(n,ofln)
    implicit integer*8(I-N)
    logical ip((n-1)/2)
    character*150 ofln
    open(143,file=ofln)
    if(n<2) then
        write(143,*)
        close(143)
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
    write(143,*) int(2,8)
    do i=1,n2
        if(ip(i)) then
            write(143,*) i*2+1
        endif
    enddo
    endsubroutine
