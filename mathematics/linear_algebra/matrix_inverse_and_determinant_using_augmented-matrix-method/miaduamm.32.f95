! Last updated: 11-Mar-2014
! Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
! Source: https://github.com/udy11, https://gitlab.com/udy11
! Subroutine (32-bit) to calculate the inverse and
! determinant of a matrix using Augmented Matrix Method

! The arguments of function invmat_32() are:
!   n = number of rows/columns of the square matrix a
!   a = the square matrix, whose inverse and determinant to calculate
!   ai = the inverse of input matrix a
!   det = the determinant of the input matrix a

! ALL YOU NEED TO DO:
! Call subroutine invmat_32(n,a,ai,det)

! NOTE:
! If the matrix is not invertible, ai will contain wrong values
!   and det will be 0; however, an error will be printed on screen
! Row exchanges are performed if diagonal entry becomes 0
!   during operations. Instead, if you want it to be < eps (some
!   small number like 1.e-10, then change four conditions marked by
!   "zero-checking" and "non-zero-checking" in the function,
!   change it to check for appropriate relation
! Example given is from a sample file "miaduamm.in.txt"; main program
!   reads this file. Read instructions in that file on how to input data.
!   But the subroutine is independent of this file reading

    dimension a(100,100),ai(100,100)
    open(148,file="miaduamm.in.txt")
    read(148,*) n
    do i=1,n
        read(148,*) (a(i,j),j=1,n)
    enddo
    close(148)

    call invmat_32(n,a(1:n,1:n),ai(1:n,1:n),det)

    write(6,*) "Determinant:"
    write(6,*) det
    write(6,*)
    write(6,*) "Inverse:"
    do i=1,n
        write(6,*) (ai(i,j),j=1,n)
    enddo
    end

! Subroutine (32-bit) to calculate the inverse and determinant
! of a square matrix using Augmented Matrix Method
    subroutine invmat_32(n,aa,ai,det)
    logical exc
    dimension aa(n,n),ai(n,n),a(n,n),t1(n)
    det=1.0
    exc=.true.

! Copying aa to a and initializing ai to identity matrix
    ai=0.0;
    do i=1,n
        do j=1,n
            a(i,j)=aa(i,j)
        enddo
        ai(i,i)=1.0
    enddo

! Exchanging first row with anouther such that a[0]!=0
    if(a(1,1)==0.0) then               ! zero-checking; abs(a(1,1))<eps
        do i=2,n
            if(a(i,1)/=0.0) then       ! non-zero-checking; abs(a(i,1))>eps
                exc=.false.
                det=-1.0*det
                do k=1,n
                    t1(k)=a(i,k)
                    a(i,k)=a(1,k)
                    a(1,k)=t1(k)
                    t1(k)=ai(i,k)
                    ai(i,k)=ai(1,k)
                    ai(1,k)=t1(k)
                enddo
                exit
            endif
        enddo
        if(exc) then
            write(6,*) 'ERROR: Input matrix is not invertible!'
            det=0.0
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
                    det=-1.0*det
                    do j=1,n
                        t1(j)=a(i,j)
                        a(i,j)=a(k,j)
                        a(k,j)=t1(j)
                        t1(j)=ai(i,j)
                        ai(i,j)=ai(k,j)
                        ai(k,j)=t1(j)
                    enddo
                    exit
                endif
            enddo
            if(exc) then
                write(6,*) 'ERROR: Input matrix is not invertible!'
                det=0.0
                return
            endif
        endif
        do j=k+1,n
            af=-a(j,k)/a(k,k)
            do i=k+1,n
                a(j,i)=a(j,i)+a(k,i)*af
            enddo
            do i=1,j
                ai(j,i)=ai(j,i)+ai(k,i)*af
            enddo
        enddo
    enddo

! Exiting if last element is 0
    if(a(n,n)==0.0) then
        write(6,*) 'ERROR: Input matrix is not invertible!'
        det=0.0
        return
    endif

! Calculating the determinant
    do i=1,n
        det=det*a(i,i)
    enddo

! Applying operations that convert a to diagonal matrix
    do k=n,1,-1
        do j=k-1,1,-1
            af=-a(j,k)/a(k,k)
            a(j,k)=0.0
            do i=1,n
                ai(j,i)=ai(j,i)+ai(k,i)*af
            enddo
        enddo
    enddo

! Applying operations that normalize diagonals of a
    do j=1,n
        do i=1,n
            ai(j,i)=ai(j,i)/a(j,j)
        enddo
    enddo

    endsubroutine
