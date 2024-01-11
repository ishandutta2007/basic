! Last updated: 13-Sept-2014
! Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
! Source: https://github.com/udy11, https://gitlab.com/udy11
! Subroutine (128-bit) to sort list of integers using Merge Sort

! ALL YOU NEED TO DO:
! Call subroutine merge_sort_asc_intg128 (for ascending) or
!   merge_sort_dsc_intg128 (for descending) with:
!   n  = number of elements in array na to be sorted
!   na = array to be sorted (will be overwritten)

! Time Complexity  = O(n.log(n))
! Space Complexity = O(n)
! Not In-Place

    implicit integer*16(I-N)
    dimension na(101)

    n=13
    do i=1,n
        na(i)=int(10000*rand())-4000
    enddo

    call merge_sort_asc_intg128(n,na(1:n))
    write(6,*) na(1:n)

    end

! Subroutine (128-bit) to sort list of integers
! in ascending order using Merge Sort
    subroutine merge_sort_asc_intg128(n,na)
    implicit integer*16(I-N)
    logical sw
    dimension na(n),nb(n)
    if(n<2) return
    j=1
    nb(n)=na(n)
    do while(j<n)
        if(na(j)>na(j+1)) then
            nb(j)=na(j+1)
            nb(j+1)=na(j)
        else
            nb(j)=na(j)
            nb(j+1)=na(j+1)
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
                    nb(i1:n)=na(i1:n)
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
                    if(na(i1)<na(i2)) then
                        nb(j)=na(i1)
                        i1=i1+1
                    else
                        nb(j)=na(i2)
                        i2=i2+1
                    endif
                    j=j+1
                    if(i1>i10) then
                        nb(j:j0)=na(i2:j0)
                        exit
                    endif
                    if(i2>j0) then
                        nb(j:j0)=na(i1:i10)
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
                    na(i1:n)=nb(i1:n)
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
                    if(nb(i1)<nb(i2)) then
                        na(j)=nb(i1)
                        i1=i1+1
                    else
                        na(j)=nb(i2)
                        i2=i2+1
                    endif
                    j=j+1
                    if(i1>i10) then
                        na(j:j0)=nb(i2:j0)
                        exit
                    endif
                    if(i2>j0) then
                        na(j:j0)=nb(i1:i10)
                        exit
                    endif
                enddo
                i1=j0+1
            enddo
            sw=.true.
            m=2*m
        endif
    enddo
    if(.not. sw) na(1:n)=nb(1:n)
    endsubroutine

! Subroutine (128-bit) to sort list of integers
! in descending order using Merge Sort
    subroutine merge_sort_dsc_intg128(n,na)
    implicit integer*16(I-N)
    logical sw
    dimension na(n),nb(n)
    if(n<2) return
    j=1
    nb(n)=na(n)
    do while(j<n)
        if(na(j)<na(j+1)) then
            nb(j)=na(j+1)
            nb(j+1)=na(j)
        else
            nb(j)=na(j)
            nb(j+1)=na(j+1)
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
                    nb(i1:n)=na(i1:n)
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
                    if(na(i1)>na(i2)) then
                        nb(j)=na(i1)
                        i1=i1+1
                    else
                        nb(j)=na(i2)
                        i2=i2+1
                    endif
                    j=j+1
                    if(i1>i10) then
                        nb(j:j0)=na(i2:j0)
                        exit
                    endif
                    if(i2>j0) then
                        nb(j:j0)=na(i1:i10)
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
                    na(i1:n)=nb(i1:n)
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
                    if(nb(i1)>nb(i2)) then
                        na(j)=nb(i1)
                        i1=i1+1
                    else
                        na(j)=nb(i2)
                        i2=i2+1
                    endif
                    j=j+1
                    if(i1>i10) then
                        na(j:j0)=nb(i2:j0)
                        exit
                    endif
                    if(i2>j0) then
                        na(j:j0)=nb(i1:i10)
                        exit
                    endif
                enddo
                i1=j0+1
            enddo
            sw=.true.
            m=2*m
        endif
    enddo
    if(.not. sw) na(1:n)=nb(1:n)
    endsubroutine
