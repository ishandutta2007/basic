! Last updated: 13-Sept-2014
! Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
! Source: https://github.com/udy11, https://gitlab.com/udy11
! Subroutine (128-bit) to sort list of real numbers using Merge Sort

! ALL YOU NEED TO DO:
! Call subroutine merge_sort_asc_real128 (for ascending) or
!   merge_sort_dsc_real128 (for descending) with:
!   n = number of elements in array a to be sorted
!   a = array to be sorted (will be overwritten)

! Time Complexity  = O(n.log(n))
! Space Complexity = O(n)
! Not In-Place

    implicit real*16(A-H,O-Z)
    dimension a(101)

    n=11
    do i=1,n
        a(i)=rand()
    enddo

    call merge_sort_asc_real128(n,a(1:n))
    write(6,*) a(1:n)

    end

! Subroutine (128-bit) to sort list of real numbers
! in ascending order using Merge Sort
    subroutine merge_sort_asc_real128(n,a)
    implicit real*16(A-H,O-Z)
    logical sw
    dimension a(n),b(n)
    if(n<2) return
    j=1
    b(n)=a(n)
    do while(j<n)
        if(a(j)>a(j+1)) then
            b(j)=a(j+1)
            b(j+1)=a(j)
        else
            b(j)=a(j)
            b(j+1)=a(j+1)
        endif
        j=j+2
    enddo
    sw=.false.
    m=2
    do while(m<=n)
        if(sw) then
            i1=1
            do while(i1<=n)
                i2=i1+m
                if(i2>n) then
                    b(i1:n)=a(i1:n)
                    exit
                endif
                if(i2+m-1>n) then
                    j0=n
                else
                    j0=i1+2*m-1
                endif
                j=i1
                i10=i1+m-1
                do while(j<=j0)
                    if(a(i1)<a(i2)) then
                        b(j)=a(i1)
                        i1=i1+1
                    else
                        b(j)=a(i2)
                        i2=i2+1
                    endif
                    j=j+1
                    if(i1>i10) then
                        b(j:j0)=a(i2:j0)
                        exit
                    endif
                    if(i2>j0) then
                        b(j:j0)=a(i1:i10)
                        exit
                    endif
                enddo
                i1=j0+1
            enddo
            sw=.false.
            m=2*m
        else
            i1=1
            do while(i1<=n)
                i2=i1+m
                if(i2>n) then
                    a(i1:n)=b(i1:n)
                    exit
                endif
                if(i2+m-1>n) then
                    j0=n
                else
                    j0=i1+2*m-1
                endif
                j=i1
                i10=i1+m-1
                do while(j<=j0)
                    if(b(i1)<b(i2)) then
                        a(j)=b(i1)
                        i1=i1+1
                    else
                        a(j)=b(i2)
                        i2=i2+1
                    endif
                    j=j+1
                    if(i1>i10) then
                        a(j:j0)=b(i2:j0)
                        exit
                    endif
                    if(i2>j0) then
                        a(j:j0)=b(i1:i10)
                        exit
                    endif
                enddo
                i1=j0+1
            enddo
            sw=.true.
            m=2*m
        endif
    enddo
    if(.not. sw) a(1:n)=b(1:n)
    endsubroutine

! Subroutine (128-bit) to sort list of real numbers
! in descending order using Merge Sort
    subroutine merge_sort_dsc_real128(n,a)
    implicit real*16(A-H,O-Z)
    logical sw
    dimension a(n),b(n)
    if(n<2) return
    j=1
    b(n)=a(n)
    do while(j<n)
        if(a(j)<a(j+1)) then
            b(j)=a(j+1)
            b(j+1)=a(j)
        else
            b(j)=a(j)
            b(j+1)=a(j+1)
        endif
        j=j+2
    enddo
    sw=.false.
    m=2
    do while(m<=n)
        if(sw) then
            i1=1
            do while(i1<=n)
                i2=i1+m
                if(i2>n) then
                    b(i1:n)=a(i1:n)
                    exit
                endif
                if(i2+m-1>n) then
                    j0=n
                else
                    j0=i1+2*m-1
                endif
                j=i1
                i10=i1+m-1
                do while(j<=j0)
                    if(a(i1)>a(i2)) then
                        b(j)=a(i1)
                        i1=i1+1
                    else
                        b(j)=a(i2)
                        i2=i2+1
                    endif
                    j=j+1
                    if(i1>i10) then
                        b(j:j0)=a(i2:j0)
                        exit
                    endif
                    if(i2>j0) then
                        b(j:j0)=a(i1:i10)
                        exit
                    endif
                enddo
                i1=j0+1
            enddo
            sw=.false.
            m=2*m
        else
            i1=1
            do while(i1<=n)
                i2=i1+m
                if(i2>n) then
                    a(i1:n)=b(i1:n)
                    exit
                endif
                if(i2+m-1>n) then
                    j0=n
                else
                    j0=i1+2*m-1
                endif
                j=i1
                i10=i1+m-1
                do while(j<=j0)
                    if(b(i1)>b(i2)) then
                        a(j)=b(i1)
                        i1=i1+1
                    else
                        a(j)=b(i2)
                        i2=i2+1
                    endif
                    j=j+1
                    if(i1>i10) then
                        a(j:j0)=b(i2:j0)
                        exit
                    endif
                    if(i2>j0) then
                        a(j:j0)=b(i1:i10)
                        exit
                    endif
                enddo
                i1=j0+1
            enddo
            sw=.true.
            m=2*m
        endif
    enddo
    if(.not. sw) a(1:n)=b(1:n)
    endsubroutine
