/*
Last updated: 19-Nov-2014
Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
Source: https://github.com/udy11, https://gitlab.com/udy11
Template program (64-bit) to calculate Fast Fourier Transform
of two-dimensional complex array using FFTW libraries

This template program is for quick reference to calculate FFTs
For more efficient usage, it is recommended to refer the FFTW documentation
at http://www.fftw.org/doc/index.html

ALL YOU NEED TO DO:
Copy the code in main() to wherever you wish to use
Define values of n0 and n1 as lengths of array
Your input should be defined under "Define input here"
Use output under "Use output here"
If input and output arrays are not required anymore, deallocate them as
  mentioned under "If not required, deallocate input and output arrays"
Compile your program with g++ and proper path to FFTW library, for example in Ubuntu:
    g++ tc2dfftufftwl.c2c.64.cpp -L/usr/local/bin -lfftw3
  If you instead wish to compile using gcc:
    gcc tc2dfftufftwl.c2c.64.cpp -L/usr/local/bin -lfftw3 -lstdc++ -lm

NOTE:
TO calculate inverse fourier transform, change FFTW_FORWARD to FFTW_BACKWARD
Do not forget to include fftw3.h header file in your code as well
Input and Output arrays can be same, in which case the input array
  will be overwritten with output array
FFTW computes unnormalized FFTs
Arrays are stored as one-dimensional arrays in row-major format and 
  (i0,i1) element can be accessed via (i0*n1+i1) element
*/

#include <iostream>
#include <fftw3.h>

using namespace std;

int main()
{
    cout.precision(15);

    int n0 = 5;
    int n1 = 7;
    fftw_complex *in2c2c, *out2c2c;
    in2c2c = (fftw_complex*) fftw_malloc(sizeof(fftw_complex) * n0 * n1);
    out2c2c = (fftw_complex*) fftw_malloc(sizeof(fftw_complex) * n0 * n1);
    fftw_plan p2c2c;
    p2c2c = fftw_plan_dft_2d(n0, n1, in2c2c, out2c2c, FFTW_FORWARD, FFTW_ESTIMATE);

// Define input here
    for(int i0=0;i0<n0;i0++) {
        for(int i1=0;i1<n1;i1++) {
            in2c2c[i0*n1+i1][0]=i0*i1*1.0; in2c2c[i0*n1+i1][1]=i0*i1*0.5;
        }
    }

    fftw_execute(p2c2c);
    fftw_destroy_plan(p2c2c);
    
// Use output here
    for(int i0=0;i0<n0;i0++) {
        for(int i1=0;i1<n1;i1++) {
            cout<<out2c2c[i0*n1+i1][0]<<"  "<<out2c2c[i0*n1+i1][1]<<endl;
        }
    }
    
// If not required, deallocate input and output arrays
    fftw_free(in2c2c); fftw_free(out2c2c);

    return 0;
}

