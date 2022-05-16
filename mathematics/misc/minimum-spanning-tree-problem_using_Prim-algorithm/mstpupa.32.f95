! Last updated: 06-May-2014
! Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
! Source: https://github.com/udy11, https://gitlab.com/udy11
! Subroutine (32-bit) to solve minimum spanning tree problem
! using Prim's Algorithm

! Input of graph is via Adjacency Matrix with zero
!   weight corresponding to disconnected vertices

! ALL YOU NEED TO DO:
! Call the subroutine prim_real32(n,a,b) for real weights
!   or prim_intg32(n,a,b) for integer weights, where
!   n = number of vertices (always 32-bit integer)
!   a = input weighted di-graph
!   b = output tree

! NOTE:
! This program reads a sample file 'mstpupa.in.txt', however,
!    the subroutines are independent of that
! The weights must be positive
! If digraph is symmetric, it will not be directional; however, one
!   expects output tree also to be symmetric, which will not happen
!   with this subroutine; you can handle this problem manually

    integer a(100,100),b(100,100)

    n=7
    open(67,file='mstpupa.in.txt')
    do i=1,n
        read(67,*) (a(i,j),j=1,n)
    enddo

    call prim_intg32(n,a(1:n,1:n),b(1:n,1:n))

    do i=1,n
        write(6,*) b(i,1:n)
    enddo

    end

! Subroutine (32-bit) to solve minimum spanning tree problem
! using Prim's Algorithm with real weights
    subroutine prim_real32(n,a,b)
    real a(n,n),b(n,n)
    logical vt(n),vg(n)
    b=0
    vt=.false.
    vg=.true.
    vg(1)=.false.
    vt(1)=.true.
    k=1
    imin=0
    jmin=0
    do while(k<n)
        wmin=3.4028235e+38
        do i=1,n
            if(vt(i)) then
                do j=1,n
                    if(vg(j) .and. a(i,j)<wmin .and. a(i,j)>0) then
                        wmin=a(i,j)
                        imin=i
                        jmin=j
                    endif
                enddo
            endif
        enddo
        vt(jmin)=.true.
        vg(jmin)=.false.
        b(imin,jmin)=a(imin,jmin)
        k=k+1
    enddo
    endsubroutine

! Subroutine (32-bit) to solve minimum spanning tree problem
! using Prim's Algorithm with integer weights
    subroutine prim_intg32(n,a,b)
    integer a(n,n),b(n,n)
    logical vt(n),vg(n)
    b=0
    vt=.false.
    vg=.true.
    vg(1)=.false.
    vt(1)=.true.
    k=1
    imin=0
    jmin=0
    do while(k<n)
        minw=2147483647
        do i=1,n
            if(vt(i)) then
                do j=1,n
                    if(vg(j) .and. a(i,j)<minw .and. a(i,j)>0) then
                        minw=a(i,j)
                        imin=i
                        jmin=j
                    endif
                enddo
            endif
        enddo
        vt(jmin)=.true.
        vg(jmin)=.false.
        b(imin,jmin)=a(imin,jmin)
        k=k+1
    enddo
    endsubroutine
