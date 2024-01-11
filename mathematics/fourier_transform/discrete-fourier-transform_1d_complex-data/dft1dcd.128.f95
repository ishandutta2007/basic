! Last updated: 25-Jun-2013
! Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
! Source: https://github.com/udy11, https://gitlab.com/udy11
! Subroutine (128-bit) to calculate one-dimensional
! discrete fourier transform of uniformly spaced complex data

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
!   ofl = Output Filename
! First column of input file should be time values
! Second column of input file should be actual data (to be fourier transformed)
!   and it should be in standard Fortran complex form, e.g.
!   1+2i should be written as (1,2) in the input file
! Default output is complex form of dft; for something else,
!   make appropriate changes at write statements in the
!   subroutine, see instructions there

! WHAT YOU NEED TO MAKE SURE:
! The input file ifl ends with data to be analyzed though...
!   it may begin with some header lines supposed to be skipped
! Number of data points is less than 100001, else you need...
!   to increase that number in the subroutine

! OUTPUT:
! The first column in output file ofl contains frequency
! The second column consists of unnormalized discrete fourier transform;
!   by default, it is complex form of dft
! Subroutine automatically shifts the frequency domain
!   similar to numpy.fft.fftshift in Python

	character*150 ifl,ofl
	ifl="time_series_02.txt"
    ofl="dftc_ts02.txt"
	call dftc_1d_128(ifl,0,ofl)
    end

! Subroutine (128-bit) to calculate one-dimensional
! discrete fourier transform of uniformly spaced complex data
    subroutine dftc_1d_128(ifl,nh,ofl)
    implicit real*16(A-H,O-Z)
    complex*32 ft,xc
    character*150 ifl,ofl
    dimension t(100000),xc(100000),ft(100000)

    open(873,file=ifl)
    pi=3.141592653589793238462643383279502884q0

! To skip nh number of header lines
    do ih=1,nh
		read(873,*)
    enddo
    i=0
	do
    	i=i+1
    	read(873,fmt=*,end=947) t(i),xc(i)
    enddo
947	close(873)
	i=i-1

! To sinusoidally suppress initial and final nc points
	nc=-1
	do k=0,nc
		xc(k+1)=xc(k+1)*sin(k*pi*0.5q0/nc)
        xc(i-k)=xc(i-k)*sin(k*pi*0.5q0/nc)
    enddo

	ff=2.q0*pi/abs(t(i)-t(1))
    ft=(0.q0,0.q0)
    open(396,file=ofl)
    do j=(i-1)/2+1,i-1
    	do k=0,i-1
        	ft(j+1)=ft(j+1)+xc(k+1)*exp((0.q0,-2.q0)*pi*j*k/i)
        enddo
! for absolute square:  abs(ft(j+1))**2
! for absolute:         abs(ft(j+1))
! for real part:        real(ft(j+1))
! for complex:          ft(j+1)          (default)
        write(396,*) ff*(j-i),ft(j+1)
    enddo
    do j=0,(i-1)/2
    	do k=0,i-1
            ft(j+1)=ft(j+1)+xc(k+1)*exp((0.q0,-2.q0)*pi*j*k/i)
        enddo
! for absolute square:  abs(ft(j+1))**2
! for absolute:         abs(ft(j+1))
! for real part:        real(ft(j+1))
! for complex:          ft(j+1)          (default)
        write(396,*) ff*j,ft(j+1)
    enddo
	close(396)
    endsubroutine
