! Last updated: 12-Feb-2013
! Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
! Source: https://github.com/udy11, https://gitlab.com/udy11
! Subroutine and Function (64-bit) to calculate
! Associated Legendre Polynomial of First Kind
! (only for x between -1 and 1)

! Reference: Computation of Special Functions, S. Zhang, J. Jin
!            Section 4.4

! Both subroutine and function are independent of each other,
! use whichever is convenient

! Associated Legendre Polynomial of First Kind Definition:
! For non-negative m (< l+1):
! P^m_l(x) = (-1)^m * (1-x^2)^(m/2) * d^m/dx^m(P_l(x))
! where P_l(x) is Legendre Polynomial.
! And for negative m (> -l-1):
! P^(-m)_l(x) = (-1)^m * (l-m)!/(l+m)! * P^m_l(x)
! If |m|>l, P^m_l = 0

! The following properties were used to calculate the polynomial:
! P^l_l(x) = -(2*l-1) * sqrt(1-x^2) * P^(l-1)_(l-1)(x)
! P^l_(l+1) = (2*l+1) * x * P^l_l(x)
! P^m_l(x) = ( (2*l-1)*x*P^m_(l-1)(x) - (l+m-1)*P^m_(l-2)(x) ) / (l-m)

! What are l and m:
! Usually, m is written in superscript
! and l in subscript. However, if both are written
! in subscript, the first one should be l
! Also, l is free to have any non-negative integer value,
! but will decide the upper and lower limit on m

! Input Precondition:
! l is NOT a negative integer
! m is any integer
! -1.0 <= x <= 1.0

	real*8 x,plmfkf64,pp
    x=0.5d0
    do l=0,3
        do m=-l,l
            call plmfks64(l,m,x,pp)
            write(*,*) l,m,pp,plmfkf64(l,m,x)
        enddo
    enddo
    end

! Function to calculate Associated Legendre
! Polynomial of First Kind (64-bit)
    real*8 function plmfkf64(l,m1,x)
	real*8 x,p(abs(m1):l)
    ifng=0
    if(m1<0) then
        ifng=1
        m=-m1
    else
        m=m1
    endif
    if(m>l) then
        plmfkf64=0.0d0
        return
    endif
    p(m)=1.0d0
    do i=1,m
        p(m)=p(m)*dsqrt(1-x*x)*(1-2*i)
    enddo
    plmfkf64=p(m)
    if(l/=m) then
        p(m+1)=p(m)*x*(2*m+1)
        plmfkf64=p(m+1)
    endif
    if(l>m+1) then
        do i=m+2,l
            p(i)=((2*i-1)*x*p(i-1)-(i+m-1)*p(i-2))/(i-m)
        enddo
        plmfkf64=p(l)
    endif
    if(ifng==1) then
        dn=1.0d0*(-1)**m
        do k=(l-m+1),(l+m)
            dn=dn/k
        enddo
        plmfkf64=dn*plmfkf64
    endif
    endfunction

! Subroutine to calculate Associated Legendre
! Polynomial of First Kind (64-bit)
    subroutine plmfks64(l,m1,x,plm)
    integer,intent(in) :: l,m1
	real*8,intent(in) :: x
    real*8,intent(out) :: plm
    real*8 p(abs(m1):l),dn
    ifng=0
    if(m1<0) then
        ifng=1
        m=-m1
    else
        m=m1
    endif
    if(m>l) then
        plm=0.0d0
        return
    endif
    p(m)=1.0d0
    do i=1,m
        p(m)=p(m)*dsqrt(1-x*x)*(1-2*i)
    enddo
    plm=p(m)
    if(l/=m) then
        p(m+1)=p(m)*x*(2*m+1)
        plm=p(m+1)
    endif
    if(l>m+1) then
        do i=m+2,l
            p(i)=((2*i-1)*x*p(i-1)-(i+m-1)*p(i-2))/(i-m)
        enddo
        plm=p(l)
    endif
    if(ifng==1) then
        dn=1.0d0*(-1)**m
        do k=(l-m+1),(l+m)
            dn=dn/k
        enddo
        plm=dn*plm
    endif
    endsubroutine
    