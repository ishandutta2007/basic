/*
Last updated: 19-Nov-2014
Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
Source: https://github.com/udy11, https://gitlab.com/udy11
Template program (64-bit) to calculate inverse Fast Fourier Transform
of one-dimensional complex array to real array using FFTW libraries

This template program is for quick reference to calculate FFTs
For more efficient usage, it is recommended to refer the FFTW documentation
at http://www.fftw.org/doc/index.html

ALL YOU NEED TO DO:
Copy the code in main() to wherever you wish to use
Define value of n0 as length of array, where
  input array fftw_complex[1+n0/2], output array double[n0]
Your input should be defined under "Define input here"
Use output under "Use output here"
If input and output arrays are not required anymore, deallocate them as
  mentioned under "If not required, deallocate input and output arrays"
Compile your program with g++ and proper path to FFTW library, for example in Ubuntu:
    g++ tc1dfftufftwl.c2r.64.cpp -L/usr/local/bin -lfftw3
  If you instead wish to compile using gcc:
    gcc tc1dfftufftwl.c2r.64.cpp -L/usr/local/bin -lfftw3 -lstdc++ -lm

NOTE:
c2r is an inverse transform; for forward transform, use r2c
In case of c2r, the input is fftw_complex array of size (1+n0/2) and
  output is double array of size n0
Do not forget to include fftw3.h header file in your code as well
Input and Output arrays can be same, in which case the input array
  will be overwritten with output array
FFTW computes unnormalized FFTs
In case of c2r the input's negative frequencies will be complex conjugate
  of those of positive frequencies and thus need not be stored explicitly
Default c2r transform changes the input array, but can be avoided using
  FFTW_PRESERVE_INPUT flag (with some sacrifice in performance);
  for example: FFTW_ESTIMATE | FFTW_PRESERVE_INPUT
*/

#include <iostream>
#include <fftw3.h>

using namespace std;

int main()
{
    cout.precision(15);

    int n0 = 19;
    fftw_complex *in1c2r;
    double *out1c2r;
    in1c2r = (fftw_complex*) fftw_malloc(sizeof(fftw_complex) * (1+n0/2));
    out1c2r = (double*) fftw_malloc(sizeof(double) * n0);
    fftw_plan p1c2r;
    p1c2r = fftw_plan_dft_c2r_1d(n0, in1c2r, out1c2r, FFTW_ESTIMATE);

// Define input here
    for(int i=0;i<(1+n0/2);i++) {
        in1c2r[i][0]=i*1.0; in1c2r[i][1]=i*0.5;
    }

    fftw_execute(p1c2r);
    fftw_destroy_plan(p1c2r);
    
// Use output here
    for(int i=0;i<n0;i++) {
        cout<<out1c2r[i]<<endl;
    }
    
// If not required, deallocate input and output arrays
    fftw_free(in1c2r); fftw_free(out1c2r);

    return 0;
}

