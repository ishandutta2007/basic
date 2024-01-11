/*
Last updated: 19-Nov-2014
Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
Source: https://github.com/udy11, https://gitlab.com/udy11
Template program (64-bit) to calculate Fast Fourier Transform
of one-dimensional real array using FFTW libraries

This template program is for quick reference to calculate FFTs
For more efficient usage, it is recommended to refer the FFTW documentation
at http://www.fftw.org/doc/index.html

ALL YOU NEED TO DO:
Copy the code in main() to wherever you wish to use
Define value of n0 as length of array, where
  input array double[n0], output array fftw_complex[1+n0/2]
Your input should be defined under "Define input here"
Use output under "Use output here"
If input and output arrays are not required anymore, deallocate them as
  mentioned under "If not required, deallocate input and output arrays"
Compile your program with g++ and proper path to FFTW library, for example in Ubuntu:
    g++ tc1dfftufftwl.r2c.64.cpp -L/usr/local/bin -lfftw3
  If you instead wish to compile using gcc:
    gcc tc1dfftufftwl.r2c.64.cpp -L/usr/local/bin -lfftw3 -lstdc++ -lm

NOTE:
r2c is a forward transform; for inverse transform, use c2r
In case of r2c, the input is double array of size n0 and output is
  fftw_complex array of size (1+n0/2)
Do not forget to include fftw3.h header file in your code as well
Input and Output arrays can be same, in which case the input array
  will be overwritten with output array; but the input array should be
  of sufficient size, i.e. 2*(1+n0/2)
FFTW computes unnormalized FFTs
Output array is in standard form, i.e. first entry for 0 frequency
  followed by positive frequencies; in case of r2c the fourier transform
  for negative frequencies will be complex conjugate of those of positive
  frequencies and thus need not be stored explicitly
*/

#include <iostream>
#include <fftw3.h>

using namespace std;

int main()
{
    cout.precision(15);

    int n0 = 19;
    double *in1r2c;
    fftw_complex *out1r2c;
    in1r2c = (double*) fftw_malloc(sizeof(double) * n0);
    out1r2c = (fftw_complex*) fftw_malloc(sizeof(fftw_complex) * (1+n0/2));
    fftw_plan p1r2c;
    p1r2c = fftw_plan_dft_r2c_1d(n0, in1r2c, out1r2c, FFTW_ESTIMATE);

// Define input here
    for(int i=0;i<n0;i++) {
        in1r2c[i]=i*1.0;
    }

    fftw_execute(p1r2c);
    fftw_destroy_plan(p1r2c);
    
// Use output here
    for(int i=0;i<(1+n0/2);i++) {
        cout<<out1r2c[i][0]<<"  "<<out1r2c[i][1]<<endl;
    }
    
// If not required, deallocate input and output arrays
    fftw_free(in1r2c); fftw_free(out1r2c);

    return 0;
}

