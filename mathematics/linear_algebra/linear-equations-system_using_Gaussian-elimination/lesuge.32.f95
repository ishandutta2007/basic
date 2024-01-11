! Last updated: 05-May-2014
! Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
! Source: https://github.com/udy11, https://gitlab.com/udy11
! Subroutine (32-bit) to solve a system of linear
! equations using Gaussian Elimination

! The arguments of function gs_elm_32() [to solve Ax=b] are:
!   n = number of unknown x
!   a = the square matrix A
!   b = the right hand side of the equation
!   x = the solution for unknown x

! ALL YOU NEED TO DO:
! Call subroutine gs_elm_32(n,a,b,x)

! NOTE:
! If system is not solvable, x will contain wrong values
! Row exchanges are performed if diagonal entry becomes 0
!   during operations. Instead, if you want it to be < eps (some
!   small number like 1.e-10, then change four conditions marked by
!   "zero-checking" and "non-zero-checking" in the function,
!   change it to check for appropriate relation
! Example given is from a sample file "lesuge.in.txt"; main program
!   reads this file. Read instructions in that file on how to input data.
!   But the subroutine is independent of this file reading

    dimension a(100,100),b(100),x(100)
    open(158,file="lesuge.in.txt")
    read(158,*) n
    do i=1,n
        read(158,*) (a(i,j),j=1,n)
    enddo
    read(158,*) (b(j),j=1,n)
    close(158)

    call gs_elm_32(n,a(1:n,1:n),b(1:n),x(1:n))

    write(6,*) "Solution:"
    do i=1,n
        write(6,*) x(i)
    enddo
    end

! Subroutine (32-bit) to solve a system of linear
! equations using Gaussian Elimination
    subroutine gs_elm_32(n,aa,bb,x)
    logical exc
    dimension aa(n,n),a(n,n),bb(n),b(n),t1(n),x(n)
    exc=.true.

! Copying aa to a and bb to b
    do i=1,n
        do j=1,n
            a(i,j)=aa(i,j)
        enddo
        b(i)=bb(i)
    enddo

! Exchanging first row with anouther such that a[0]!=0
    if(a(1,1)==0.0) then               ! zero-checking; abs(a(1,1))<eps
        do i=2,n
            if(a(i,1)/=0.0) then       ! non-zero-checking; abs(a(i,1))>eps
                exc=.false.
                do k=1,n
                    t1(k)=a(i,k)
                    a(i,k)=a(1,k)
                    a(1,k)=t1(k)
                enddo
                t1(1)=b(i)
                b(i)=b(1)
                b(1)=t1(1)
                exit
            endif
        enddo
        if(exc) then
            write(6,*) 'ERROR: Given system not solvable!'
            x=0.0
            return
        endif
    endif

! Applying operations that convert a to upper-triangular
!   and applying row exchanges as necessary
    do k=1,n-1
        if(a(k,k)==0.0) then           ! zero-checking; abs(a(k,k))<eps
            exc=.true.
            do i=k+1,n
                if(a(i,k)/=0.0) then   ! non-zero-checking; abs(a(i,k))>eps
                    exc=.false.
                    do j=1,n
                        t1(j)=a(i,j)
                        a(i,j)=a(k,j)
                        a(k,j)=t1(j)
                    enddo
                    t1(1)=b(i)
                    b(i)=b(1)
                    b(1)=t1(1)
                    exit
                endif
            enddo
            if(exc) then
                write(6,*) 'ERROR: Given system not solvable!'
                x=0.0
                return
            endif
        endif
        do j=k+1,n
            af=-a(j,k)/a(k,k)
            do i=k+1,n
                a(j,i)=a(j,i)+a(k,i)*af
            enddo
            b(j)=b(j)+b(k)*af
        enddo
    enddo

! Exiting if last element is 0
    if(a(n,n)==0.0) then
        write(6,*) 'ERROR: Given system not solvable!'
        x=0.0
        return
    endif

! Calculating unknown x
    do i=n,1,-1
        x(i)=b(i)
        do j=i+1,n
            x(i)=x(i)-x(j)*a(i,j)
        enddo
        x(i)=x(i)/a(i,i)
    enddo

    endsubroutine
