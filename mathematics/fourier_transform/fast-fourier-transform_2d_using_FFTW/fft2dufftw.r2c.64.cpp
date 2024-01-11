/*
Last updated: 19-Nov-2014
Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
Source: https://github.com/udy11, https://gitlab.com/udy11
Template program (64-bit) to calculate Fast Fourier Transform
of two-dimensional real array using FFTW libraries

This template program is for quick reference to calculate FFTs
For more efficient usage, it is recommended to refer the FFTW documentation
at http://www.fftw.org/doc/index.html

ALL YOU NEED TO DO:
Copy the code in main() to wherever you wish to use
Define values of n0 and n1 as lengths of array, where
  input array double[n0*n1], output array fftw_complex[n0*(1+n1/2)]
Your input should be defined under "Define input here"
Use output under "Use output here"
If input and output arrays are not required anymore, deallocate them as
  mentioned under "If not required, deallocate input and output arrays"
Compile your program with g++ and proper path to FFTW library, for example in Ubuntu:
    g++ tc2dfftufftwl.r2c.64.cpp -L/usr/local/bin -lfftw3
  If you instead wish to compile using gcc:
    gcc tc2dfftufftwl.r2c.64.cpp -L/usr/local/bin -lfftw3 -lstdc++ -lm

NOTE:
r2c is a forward transform; for inverse transform, use c2r
In case of r2c, the input is double array of size n0*n1 and output is
  fftw_complex array of size n0*(1+n1/2)
Do not forget to include fftw3.h header file in your code as well
Input and Output arrays can be same, in which case the input array
  will be overwritten with output array; but the input array should be
  of sufficient size, i.e. n0*2*(1+n1/2)
FFTW computes unnormalized FFTs
Arrays are stored as one-dimensional arrays in row-major format and 
  (i0,i1) element of input can be accessed via (i0*n1+i1) element
  (i0,i1) element of output can be accessed via (i0*(1+n1/2)+i1) element
Storing only 1+n1/2 columns of output is done because (n1-1)th column is complex
  conjugate of 1st (not 0th, as per c++ convention), (n1-2)th is complex
  conjugate of 2nd and so on..
*/

#include <iostream>
#include <fftw3.h>

using namespace std;

int main()
{
    cout.precision(15);

    int n0 = 5;
    int n1 = 4;
    double *in2r2c;
    fftw_complex *out2r2c;
    in2r2c = (double*) fftw_malloc(sizeof(double) * n0 * n1);
    out2r2c = (fftw_complex*) fftw_malloc(sizeof(fftw_complex) * n0 * (1+n1/2));
    fftw_plan p2r2c;
    p2r2c = fftw_plan_dft_r2c_2d(n0, n1, in2r2c, out2r2c, FFTW_ESTIMATE);

// Define input here
    for(int i0=0;i0<n0;i0++) {
        for(int i1=0;i1<n1;i1++) {
            in2r2c[i0*n1+i1]=i0*i1*1.0;
        }
    }

    fftw_execute(p2r2c);
    fftw_destroy_plan(p2r2c);
    
// Use output here
    for(int i0=0;i0<n0;i0++) {
        for(int i1=0;i1<(1+n1/2);i1++) {
            cout<<out2r2c[i0*(1+n1/2)+i1][0]<<"  "<<out2r2c[i0*(1+n1/2)+i1][1]<<endl;
        }
    }
    
// If not required, deallocate input and output arrays
    fftw_free(in2r2c); fftw_free(out2r2c);

    return 0;
}

