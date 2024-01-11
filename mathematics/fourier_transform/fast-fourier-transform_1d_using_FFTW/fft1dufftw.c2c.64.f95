! Last updated: 28-Nov-2014
! Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
! Source: https://github.com/udy11, https://gitlab.com/udy11
! Template program (64-bit) to calculate Fast Fourier Transform
! of one-dimensional complex array using FFTW libraries

! This template program is for quick reference to calculate FFTs
! For more efficient usage, it is recommended to refer the FFTW documentation
! at http:!www.fftw.org/doc/index.html

! ALL YOU NEED TO DO:
! Copy the code to your code at proper places
! Define value of n0 as length of array
! Your input should be defined under "Define input here"
! Use output under "Use output here"
! Compile your program with gfortran and proper path to FFTW library, for example in Ubuntu:
!     gfortran tc1dfftufftwl.c2c.64.f95 -L/usr/local/bin -lfftw3

! NOTE:
! TO calculate inverse fourier transform, change FFTW_FORWARD to FFTW_BACKWARD
! Input and Output arrays can be same, in which case the input array
!   will be overwritten with output array
! FFTW computes unnormalized FFTs
! Don't forget to give sufficient dimensions in declaration of input and output arrays
! Output array is in standard form, i.e. first entry for 0 frequency
!   followed by positive frequencies and then negative frequencies

    include 'fftw3.f'
    complex*16 in1c2c,out1c2c
    dimension in1c2c(100),out1c2c(100)
    integer*8 p1c2c

    n0=19
    call dfftw_plan_dft_1d(p1c2c,n0,in1c2c,out1c2c,FFTW_FORWARD,FFTW_ESTIMATE)

! Define input here
    do i=1,n0
        in1c2c(i)=i+0.5d0*i*(0.d0,1.d0)
    enddo

    call dfftw_execute_dft(p1c2c,in1c2c,out1c2c)
    call dfftw_destroy_plan(p1c2c)
    
! Use output here
    do i=1,n0
        write(6,*) out1c2c(i)
    enddo

    end

