! Last updated: 03-Jul-2013
! Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
! Source: https://github.com/udy11, https://gitlab.com/udy11
! Subroutines (32-bit) to sort real numbers using Bubble Sort

! Performance ~ O(n^2)

! There are 4 subroutines in this file:
! bblsrt_real_lst_asc_32: To sort real numbers in a list in Ascendance
! bblsrt_real_lst_dsc_32: To sort real numbers in a list in Descendance
! bblsrt_real_tbl_asc_32: To sort real numbers in a table in Ascendance
! bblsrt_real_tbl_dsc_32: To sort real numbers in a table in Descendance

! WARNING: ALL SUBROUTINES MODIFY INPUT ARRAY

! list is a one-dimensional array
! table is a multi-dimensional array
!   rest of the table is also sorted accordng to selected column (ns)

! ra = real array supposed to be sorted
! nr = number of rows in list or table
! nc = number of columns in table
! ns = column number, according to which table will be sorted

! This file only contains subroutines and no main program
! To use them, either copy subroutines from here or use include
!   command in Fortran to include these subroutines in your program

! Subroutine (32-bit) to sort real number list in Ascendance using Bubble Sort
    subroutine bblsrt_real_lst_asc_32(ra,nr)
    dimension ra(nr)
    k=nr-1
    do while(k>-1)
        do i=1,k
            if(ra(i)>ra(i+1)) then
                t=ra(i)
                ra(i)=ra(i+1)
                ra(i+1)=t
            endif
        enddo
        k=k-1
    enddo
    endsubroutine

! Subroutine (32-bit) to sort real number list in Descendance using Bubble Sort
    subroutine bblsrt_real_lst_dsc_32(ra,nr)
    dimension ra(nr)
    k=nr-1
    do while(k>-1)
        do i=1,k
            if(ra(i)<ra(i+1)) then
                t=ra(i)
                ra(i)=ra(i+1)
                ra(i+1)=t
            endif
        enddo
        k=k-1
    enddo
    endsubroutine

! Subroutine (32-bit) to sort real number table in Ascendance using Bubble Sort
    subroutine bblsrt_real_tbl_asc_32(ra,nr,nc,ns)
    dimension ra(nr,nc),t(nc)
    k=nr-1
    do while(k>-1)
        do i=1,k
            if(ra(i,ns)>ra(i+1,ns)) then
                t=ra(i,:)
                ra(i,:)=ra(i+1,:)
                ra(i+1,:)=t
            endif
        enddo
        k=k-1
    enddo
    end subroutine

! Subroutine (32-bit) to sort real number table in Descendance using Bubble Sort
    subroutine bblsrt_real_tbl_dsc_32(ra,nr,nc,ns)
    dimension ra(nr,nc),t(nc)
    k=nr-1
    do while(k>-1)
        do i=1,k
            if(ra(i,ns)<ra(i+1,ns)) then
                t=ra(i,:)
                ra(i,:)=ra(i+1,:)
                ra(i+1,:)=t
            endif
        enddo
        k=k-1
    enddo
    end subroutine
