! Last updated: 11-Mar-2014
! Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
! Source: https://github.com/udy11, https://gitlab.com/udy
! Subroutine (32-bit) to calculate the determinant
! of a matrix using Lower Decomposition Method

! The arguments of function detmat_32() are:
!   n = number of rows/columns of the square matrix a
!   a = the square matrix, whose inverse and determinant to calculate
!   det = the determinant of the input matrix a

! ALL YOU NEED TO DO:
! Call subroutine detmat_32(n,a,det)

! NOTE:
! If the matrix is not invertible, det will be 0
! Row exchanges are performed if diagonal entry becomes 0
!   during operations. Instead, if you want it to be < eps (some
!   small number like 1.e-10, then change four conditions marked by
!   "zero-checking" and "non-zero-checking" in the function,
!   change it to check for appropriate relation
! Example given is from a sample file "mduldm.in.txt"; main program
!   reads this file. Read instructions in that file on how to input data.
!   But the subroutine is independent of this file reading

    dimension a(100,100)
    open(148,file="mduldm.in.txt")
    read(148,*) n
    do i=1,n
        read(148,*) (a(i,j),j=1,n)
    enddo
    close(148)

    call detmat_32(n,a(1:n,1:n),det)

    write(6,*) "Determinant: ",det
    end

! Subroutine (32-bit) to calculate the determinant
! of a square matrix using Lower Decomposition Method
    subroutine detmat_32(n,aa,det)
    logical exc
    dimension aa(n,n),a(n,n),t1(n)
    det=1.0
    exc=.true.

! Copying aa to a
    do i=1,n
        do j=1,n
            a(i,j)=aa(i,j)
        enddo
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
                enddo
                exit
            endif
        enddo
        if(exc) then
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
                    enddo
                    exit
                endif
            enddo
            if(exc) then
                det=0.0
                return
            endif
        endif
        do j=k+1,n
            af=-a(j,k)/a(k,k)
            do i=k+1,n
                a(j,i)=a(j,i)+a(k,i)*af
            enddo
        enddo
    enddo

! Calculating the determinant
    do i=1,n
        det=det*a(i,i)
    enddo

    endsubroutine
