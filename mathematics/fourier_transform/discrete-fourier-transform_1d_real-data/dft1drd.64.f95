! Last updated: 25-Jun-2013
! Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
! Source: https://github.com/udy11, https://gitlab.com/udy11
! Subroutine (64-bit) to calculate one-dimensional
! discrete fourier transform of uniformly spaced real data

! Number of operations ~ O(N^2), N is the number of data points

! The definition used is:
! F(w) = Sum[f(t)*exp(-iota*2*pi*w*t/N),t]
! This definition is also used by
! Pythons's numpy library and R's standard function fft
! No normalization is applied in this program, note that
! Mathematica's Fourier command normalizes by sqrt(N)

! ALL YOU NEED TO DO:
! The inputs in the subroutine are:
!   ifl = Input Filename
!   nh  = number of header lines in ifl to skip reading
!   tc  = column of time values
!   dc  = column of actual data (to be fourier transformed)
!   ofl = Output Filename
! If you want something other than absolute sqaure (power)
!   of dft, make appropriate changes at write statement
!   in the subroutine, see instructions there

! WHAT YOU NEED TO MAKE SURE:
! The input file ifl ends with data to be analyzed though...
!   it may begin with some header lines supposed to be skipped
! Number of data points is less than 100001, else you need...
!   to increase that number in the subroutine
! Column number of time values or data is within 21
!   else you need to increase that also in subroutine

! OUTPUT:
! The first column in output file ofl contains frequency
! The second column consists of unnormalized discrete fourier transform
!   by default, it is absolute square of dft
! Negative frequencies are omitted in output since
!   dft of real data must be symmetric about 0

	character*150 ifl,ofl
	ifl="time_series_01.txt"
    ofl="dft_ts01.txt"
	call dft_1d_64(ifl,0,1,2,ofl)
    end

! Subroutine (64-bit) to calculate one-dimensional
! discrete fourier transform of uniformly spaced real data
    subroutine dft_1d_64(ifl,nh,tc,dc,ofl)
    implicit real*8(A-H,O-Z)
    complex*16 ft
    character*150 ifl,ofl
    integer tc,dc
    dimension xr(100000,20),ft(100000)

    open(873,file=ifl)
    pi=3.1415926535897932d0
    n=max(tc,dc)

! To skip nh number of header lines
    do ih=1,nh
		read(873,*)
    enddo
    i=0
	do
    	i=i+1
    	read(873,fmt=*,end=947) (xr(i,j),j=1,n)
    enddo
947	close(873)
	i=i-1

! To sinusoidally suppress initial and final nc points
	nc=-1
	do k=0,nc
		xr(k+1,dc)=xr(k+1,dc)*sin(k*pi*0.5d0/nc)
        xr(i-k,dc)=xr(i-k,dc)*sin(k*pi*0.5d0/nc)
    enddo

	ff=2.d0*pi/abs(xr(i,tc)-xr(1,tc))
    ft=(0.d0,0.d0)
    open(396,file=ofl)
    do j=0,(i-1)/2
    	do k=0,i-1
            ft(j+1)=ft(j+1)+xr(k+1,dc)*exp((0.d0,-2.d0)*pi*j*k/i)
        enddo
! for absolute square:  abs(ft(j+1))**2    (default)
! for absolute:         abs(ft(j+1))
! for real part:        real(ft(j+1))
! for complex:          ft(j+1)
        write(396,*) ff*j,abs(ft(j+1))**2
    enddo
	close(396)
    endsubroutine
