! Last updated: 28-Nov-2014
! Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
! Source: https://github.com/udy11, https://gitlab.com/udy11
! Template program (64-bit) to calculate Fast Fourier Transform
! of one-dimensional real array using FFTW libraries

! This template program is for quick reference to calculate FFTs
! For more efficient usage, it is recommended to refer the FFTW documentation
! at http:!www.fftw.org/doc/index.html

! ALL YOU NEED TO DO:
! Copy the code to your code at proper places
! Define value of n0 as length of array, where
!   input array real*8(n0), output array complex*16(1+n0/2)
! Your input should be defined under "Define input here"
! Use output under "Use output here"
! Compile your program with gfortran and proper path to FFTW library, for example in Ubuntu:
!     gfortran tc1dfftufftwl.r2c.64.f95 -L/usr/local/bin -lfftw3

! NOTE:
! r2c is a forward transform; for inverse transform, use c2r
! In case of r2c, the input is real*8 array of size n0 and output is
!   complex*16 array of size (1+n0/2)
! FFTW computes unnormalized FFTs
! Don't forget to give sufficient dimensions in declaration of input and output arrays
! Output array is in standard form, i.e. first entry for 0 frequency
!   followed by positive frequencies; in case of r2c the fourier transform
!   for negative frequencies will be complex conjugate of those of positive
!   frequencies and thus need not be stored explicitly

    include 'fftw3.f'
    real*8 in1r2c
    complex*16 out1r2c
    dimension in1r2c(100),out1r2c(100)
    integer*8 p1r2c

    n0=20
    call dfftw_plan_dft_r2c_1d(p1r2c,n0,in1r2c,out1r2c,FFTW_ESTIMATE)

! Define input here
    do i=1,n0
        in1r2c(i)=i*1.d0
    enddo

    call dfftw_execute_dft_r2c(p1r2c,in1r2c,out1r2c)
    call dfftw_destroy_plan(p1r2c)

! Use output here
    do i=1,1+n0/2
        write(6,*) out1r2c(i)
    enddo

    end

