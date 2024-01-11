! Last updated: 28-Nov-2014
! Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
! Source: https://github.com/udy11, https://gitlab.com/udy11
! Template program (64-bit) to calculate inverse Fast Fourier Transform
! of one-dimensional complex array to real array using FFTW libraries

! This template program is for quick reference to calculate FFTs
! For more efficient usage, it is recommended to refer the FFTW documentation
! at http:!www.fftw.org/doc/index.html

! ALL YOU NEED TO DO:
! Copy the code to your code at proper places
! Define value of n0 as length of array, where
!   input array complex*16(1+n0/2), output array real*8(n0)
! Your input should be defined under "Define input here"
! Use output under "Use output here"
! Compile your program with gfortran and proper path to FFTW library, for example in Ubuntu:
!     gfortran tc1dfftufftwl.c2r.64.f95 -L/usr/local/bin -lfftw3

! NOTE:
! c2r is an inverse transform; for forward transform, use r2c
! In case of c2r, the input is complex*16 array of size (1+n0/2) and output is
!   real*8 array of size n0
! FFTW computes unnormalized FFTs
! Don't forget to give sufficient dimensions in declaration of input and output arrays
! Output array is in standard form, i.e. first entry for 0 frequency
!   followed by positive frequencies; in case of r2c the fourier transform
!   for negative frequencies will be complex conjugate of those of positive
!   frequencies and thus need not be stored explicitly
! In case of c2r the input's negative frequencies will be complex conjugate
!   of those of positive frequencies and thus need not be stored explicitly

    include 'fftw3.f'
    complex*16 in1c2r
    real*8 out1c2r
    dimension in1c2r(100),out1c2r(100)
    integer*8 p1c2r

    n0=19
    call dfftw_plan_dft_c2r_1d(p1c2r,n0,in1c2r,out1c2r,FFTW_ESTIMATE)

! Define input here
    do i=1,1+n0/2
        in1c2r(i)=i+0.5d0*i*(0.d0,1.d0)
    enddo

    call dfftw_execute_dft_c2r(p1c2r,in1c2r,out1c2r)
    call dfftw_destroy_plan(p1c2r)

! Use output here
    do i=1,n0
        write(6,*) out1c2r(i)
    enddo

    end

