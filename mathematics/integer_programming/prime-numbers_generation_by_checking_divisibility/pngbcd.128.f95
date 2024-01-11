! Last updated: 24-May-2013
! Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
! Source: https://github.com/udy11, https://gitlab.com/udy11
! Subroutines (128-bit) to list prime numbers
! using divisibility checking method

! The subroutine prm_upto_n_128 computes all prime numbers upto n (inclusive)
!   k stores the number of primes upto that
! The subroutine prm_n_128 computes n prime numbers

! Output of each subroutine is stored in arrays passed from main program

! The idea to check for prime-ness is to check divisibility upto sqrt of that number
! 128-bit should ideally list well over 10^16 number of primes, but will take a lot of time
! Defining large arrays may cause slow compilations

    implicit integer*16(I-N)
    dimension np1(1000),np2(1000)
    n=31
    call prm_upto_n_128(np1,n,k)
    call prm_n_128(np2,n)
    write(6,*) k,'Prime Numbers upto ',n,':'
    do i=1,k
        write(6,*) np1(i)
    enddo
    write(6,*)
    write(6,*) n,'Prime Numbers:'
    do i=1,n
        write(6,*) np2(i)
    enddo
    end

! Subroutine (128-bit) to list all prime numbers upto n (inclusive)
    subroutine prm_upto_n_128(np,n,k)
    implicit integer*16(I-N)
    logical c
    dimension np(n)
    np(1)=2; np(2)=3; k=2
    do i=5,n,2
        c=.true.; j=1
        do while(np(j)<=sqrt(i*1.0q0))
            if(mod(i,np(j))==0) then
                c=.false.
                exit
            endif
            j=j+1
        enddo
        if(c) then
            k=k+1
            np(k)=i
        endif
    enddo
    endsubroutine

! Subroutine (128-bit) to list n prime numbers
    subroutine prm_n_128(np,n)
    implicit integer*16(I-N)
    logical c
    dimension np(n)
    np(1)=2; np(2)=3; k=2; i=5
    do while(k<n)
        c=.true.; j=1
        do while(np(j)<=sqrt(i*1.0q0))
            if(mod(i,np(j))==0) then
                c=.false.
                exit
            endif
            j=j+1
        enddo
        if(c) then
            k=k+1
            np(k)=i
        endif
        i=i+2
    enddo
    endsubroutine
