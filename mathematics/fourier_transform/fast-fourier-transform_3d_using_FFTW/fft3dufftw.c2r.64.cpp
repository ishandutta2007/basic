/*
Last updated: 19-Nov-2014
Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
Source: https://github.com/udy11, https://gitlab.com/udy11
Template program (64-bit) to calculate inverse Fast Fourier Transform
of three-dimensional complex array to real array using FFTW libraries

This template program is for quick reference to calculate FFTs
For more efficient usage, it is recommended to refer the FFTW documentation
at http://www.fftw.org/doc/index.html

ALL YOU NEED TO DO:
Copy the code in main() to wherever you wish to use
Define values of n0 and n1 as lengths of array, where
  input array fftw_complex[n0*n1*(1+n2/2)], output array double[n0*n1*n2]
Your input should be defined under "Define input here"
Use output under "Use output here"
If input and output arrays are not required anymore, deallocate them as
  mentioned under "If not required, deallocate input and output arrays"
Compile your program with g++ and proper path to FFTW library, for example in Ubuntu:
    g++ tc3dfftufftwl.c2r.64.cpp -L/usr/local/bin -lfftw3
  If you instead wish to compile using gcc:
    gcc tc3dfftufftwl.c2r.64.cpp -L/usr/local/bin -lfftw3 -lstdc++ -lm

NOTE:
c2r is an inverse transform; for forward transform, use r2c
In case of c2r, input is fftw_complex array of size n0*n1*(1+n2/2) and
  output is double array of size n0*n1*n2
Do not forget to include fftw3.h header file in your code as well
Input and Output arrays can be same, in which case the input array
  will be overwritten with output array
FFTW computes unnormalized FFTs
Arrays are stored as one-dimensional arrays in row-major format and 
  (i0,i1,i2) element of input can be accessed via ((i0*n1+i1)*(1+n2/2)+i2) element
  (i0,i1,i2) element of output can be accessed via ((i0*n1+i1)*n2+i2) element
Storing only 1+n2/2 entries of last dimension of input is done because (n1-1)th 
  entry is complex conjugate of 1st (not 0th, as per c++ convention), (n1-2)th is
  complex conjugate of 2nd and so on..
Default c2r transform for 3d changes the input array
*/

#include <iostream>
#include <fftw3.h>

using namespace std;

int main()
{
    cout.precision(15);

    int n0 = 3;
    int n1 = 4;
    int n2 = 5;
    fftw_complex *in3c2r;
    double *out3c2r;
    in3c2r = (fftw_complex*) fftw_malloc(sizeof(fftw_complex) * n0 * n1 * (1+n2/2));
    out3c2r = (double*) fftw_malloc(sizeof(double) * n0 * n1 * n2);
    fftw_plan p3c2r;
    p3c2r = fftw_plan_dft_c2r_3d(n0, n1, n2, in3c2r, out3c2r, FFTW_ESTIMATE);

// Define input here
    for(int i0=0;i0<n0;i0++) {
        for(int i1=0;i1<n1;i1++) {
            for(int i2=0;i2<(1+n2/2);i2++) {
                in3c2r[(i0*n1+i1)*(1+n2/2)+i2][0]=i0*i1*i2*1.0; in3c2r[(i0*n1+i1)*(1+n2/2)+i2][1]=i0*i1*i2*0.5;
            }
        }
    }
    
    fftw_execute(p3c2r);
    fftw_destroy_plan(p3c2r);
    
// Use output here
    for(int i0=0;i0<n0;i0++) {
        for(int i1=0;i1<n1;i1++) {
            for(int i2=0;i2<n2;i2++) {
                cout<<out3c2r[(i0*n1+i1)*n2+i2]<<endl;
            }
        }
    }
    
// If not required, deallocate input and output arrays
    fftw_free(in3c2r); fftw_free(out3c2r);

    return 0;
}

