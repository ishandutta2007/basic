! Last updated: 12-Apr-2013
! Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
! Source: https://github.com/udy11, https://gitlab.com/udy11
! Function (64-bit) to generate random numbers
! of a specified distribution using
! Acceptance-Rejection Method (or Rejection Sampling)

! The rn_pd() function generates a random number which
! obeys distribution specified by the function f(x)

! ALL YOU NEED TO DO:
! Specify distribution function f(x) (may be unnormalized)
!   (will be effctive only between 0 and 1)
! Specify parameter in rn_pd() as the maximum of your f(x)

! The given example of f(x) is a highly peaked Lorentzian
! function with maximum of 100 at 0.5, thus random numbers
! generated have high probability of lying near 0.5

    implicit real*8(A-H,O-Z)
    do k=1,100
      write(*,*) rn_pd(100.0d0)
    enddo
    end

! Distribution Function
    real*8 function f(x)
    implicit real*8(A-H,O-Z)
    f=1.0d0/(0.01d0 + ((x-0.5d0)/0.1d0)**2)
    endfunction

! Function to generate a random number
! of distribution specified by f(x),
! using Acceptance-Rejection Method
    real*8 function rn_pd(xm)
    implicit real*8(A-H,O-Z)
    call random_number(u)
    u=xm*u
    call random_number(rn_pd)
    do
      if(f(rn_pd) >= u) exit
      call random_number(u)
      u=xm*u
      call random_number(rn_pd)
    enddo
    endfunction
