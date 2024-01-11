! Last updated: 19-Aug-2014
! Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
! Source: https://github.com/udy11, https://gitlab.com/udy11
! Subroutine (64-bit) to solve Knapsack 0-1 Problem
! using Dynamic Programming

! Knapsack 0-1 Problem is:
! Given m items with values nv(1:m) and weights nw(1:m)
!   which items to choose so that the total value is maximized
!   and the total weight is <= [given] knapsack capacity, nwm
! i.e. maximize sum[tt(i)*nv(i)] for sum[tt(i)*nw(i)]<=nwm
!   where tt(i) is 0 or 1, and i runs on items

! ALL YOU NEED TO DO:
! Call subroutine knapsack_01_dp_int64(m,nv,nw,nwm,tt) with:
!   m = number of items
!   nv = values of items
!   nw = weights of items
!   nwm = maximum capacity of the knapsack
!   tt = output boolean array, whose i^th entry tells
!        whether i^th item should be in knapsack or not

! NOTE:
! The algorithm gives "one" solution, there may actually be many
! Output array tt must be defined as a logical array

    implicit integer*8(I-N)

    logical tt
    dimension nv(10),nw(10),tt(10)

    m=10
    nv=(/ 92,57,49,68,60,43,67,84,87,72 /)
    nw=(/ 23,31,29,44,53,38,63,85,89,82 /)
    nwm=165

    call knapsack_01_dp_int64(m,nv,nw,nwm,tt)
    write(6,*) tt
    end

! Subroutine (64-bit) to solve Knapsack 0-1 Problem
! using Dynamic Programming
    subroutine knapsack_01_dp_int64(m,nv,nw,nwm,tt)
    implicit integer*8(I-N)
    logical tt
    dimension nv(m),nw(m),tt(m),kv(m,0:nwm)
    kv(:,0)=0
    do j=1,nw(1)-1
        kv(1,j)=0
    enddo
    do j=nw(1),nwm
        kv(1,j)=nv(1)
    enddo
    do i=2,m
        do j=1,nw(i)-1
            kv(i,j)=kv(i-1,j)
        enddo
        do j=nw(i),nwm
            kv(i,j)=max(kv(i-1,j),kv(i-1,j-nw(i))+nv(i))
        enddo
    enddo
    j=nwm
    i=m
    tt=.false.
    do while(i>1)
        if(kv(i,j)/=kv(i-1,j)) then
            tt(i)=.true.
            j=j-nw(i)
        endif
        i=i-1
    enddo
    if(kv(1,j)/=0) tt(1)=.true.
    endsubroutine
