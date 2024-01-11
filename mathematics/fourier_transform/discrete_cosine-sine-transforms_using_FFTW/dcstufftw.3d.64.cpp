/*
Last updated: 24-Nov-2014
Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
Source: https://github.com/udy11, https://gitlab.com/udy11
Template program (64-bit) to calculate Discrete Cosine and
Sine Transform of three-dimensional real array using FFTW libraries

This template program is for quick reference to calculate FFTs
For more efficient usage, it is recommended to refer the FFTW documentation
at http://www.fftw.org/doc/index.html

ALL YOU NEED TO DO:
Copy the code in main() to wherever you wish to use
Define values of n0, n1 and n2 as lengths of array
Define Transform types along each dimension in plan as:
  FFTW_REDFT00 for DCT-I
  FFTW_REDFT10 for DCT-II (commonly used)
  FFTW_REDFT01 for DCT-III
  FFTW_REDFT11 for DCT-IV
  FFTW_RODFT00 for DST-I
  FFTW_RODFT10 for DST-II (commonly used)
  FFTW_RODFT01 for DST-III
  FFTW_RODFT11 for DST-IV
Your input should be defined under "Define input here"
Use output under "Use output here"
If input and output arrays are not required anymore, deallocate them as
  mentioned under "If not required, deallocate input and output arrays"
Compile your program with g++ and proper path to FFTW library, for example in Ubuntu:
    g++ tcdcastufftwl.3d.64.cpp -L/usr/local/bin -lfftw3
  If you instead wish to compile using gcc:
    gcc tcdcastufftwl.3d.64.cpp -L/usr/local/bin -lfftw3 -lstdc++ -lm

DEFINITIONS:
Also check official documentation for definitions:
  http://www.fftw.org/doc/1d-Real_002deven-DFTs-_0028DCTs_0029.html
  http://www.fftw.org/doc/1d-Real_002dodd-DFTs-_0028DSTs_0029.html
Multidimensional DCT and DST are simply separate products along each dimension
For 1D input data X_0, X_1, ... , X_(n-1), the transform Y_k (for k=0,n-1)
DCT-I   defined as: X_0 + (-1)^k * X_(n-1) + 2 * sum_(j=1)^(n-2) [X_j * cos(pi*j*k/(n-1))]
DCT-II  defined as: 2 * sum_(j=0)^(n-1) [X_j * cos(pi*(j+1/2)*k/n)]
DCT-III defined as: X_0 + 2 * sum_(j=1)^(n-1) [X_j * cos(pi*j*(k+1/2)/n)]
DCT-IV  defined as: 2 * sum_(j=0)^(n-1) [X_j * cos(pi*(j+1/2)*(k+1/2)/n)]
DST-I   defined as: 2 * sum_(j=0)^(n-1) [X_j * sin(pi*(j+1)*(k+1)/(n+1))]
DST-II  defined as: 2 * sum_(j=0)^(n-1) [X_j * sin(pi*(j+1/2)*(k+1)/n)]
DST-III defined as: (-1)^k * X_(n-1) + 2 * sum_(j=0)^(n-2) [X_j * sin(pi*(j+1)*(k+1/2)/n)]
DST-IV  defined as: 2 * sum_(j=0)^(n-1) [X_j * sin(pi*(j+1/2)*(k+1/2)/n)]

NOTE:
To calculate (unnormalized) inverse transforms:
  DCT-I is inverse of itself
  DCT-II is inverse of DCT-III and vice-versa
  DCT-IV is inverse of itself
  DST-I is inverse of itself
  DST-II is inverse of DST-III and vice-versa
  DST-IV is inverse of itself
Do not forget to include fftw3.h header file in your code as well
Input and Output arrays can be same, in which case the input array
  will be overwritten with output array
FFTW computes unnormalized transforms
DCT-I or REDFT00 is not defined for length 1
Speed-wise: R*DFT10, R*DFT01 > R*DFT11 > R*DFT00
Arrays are stored as one-dimensional arrays in row-major format and 
  (i0,i1,i2) element can be accessed via ((i0*n1+i1)*n2+i2) element
*/

#include <iostream>
#include <fftw3.h>

using namespace std;

int main()
{
    cout.precision(15);

    int n0 = 5;
    int n1 = 7;
    int n2 = 3;
    double *in3cs, *out3cs;
    in3cs = (double*) fftw_malloc(sizeof(double) * n0 * n1 * n2);
    out3cs = (double*) fftw_malloc(sizeof(double) * n0 * n1 * n2);
    fftw_plan p3cs;
    p3cs = fftw_plan_r2r_3d(n0, n1, n2, in3cs, out3cs, FFTW_REDFT10, FFTW_REDFT10, FFTW_REDFT10, FFTW_ESTIMATE);

// Define input here
    for(int i0=0;i0<n0;i0++) {
        for(int i1=0;i1<n1;i1++) {
            for(int i2=0;i2<n2;i2++) {
                in3cs[(i0*n1+i1)*n2+i2]=i0*i1*i2*1.0;
            }
        }
    }

    fftw_execute(p3cs);
    fftw_destroy_plan(p3cs);
    
// Use output here
    for(int i0=0;i0<n0;i0++) {
        for(int i1=0;i1<n1;i1++) {
            for(int i2=0;i2<n2;i2++) {
                cout<<out3cs[(i0*n1+i1)*n2+i2]<<endl;
            }
        }
    }
    
// If not required, deallocate input and output arrays
    fftw_free(in3cs); fftw_free(out3cs);

    return 0;
}

