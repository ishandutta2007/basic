/*
Last updated: 24-Nov-2014
Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
Source: https://github.com/udy11, https://gitlab.com/udy11
Template program (64-bit) to calculate Discrete Cosine and
Sine Transform of n-dimensional real array using FFTW libraries

This template program is for quick reference to calculate FFTs
For more efficient usage, it is recommended to refer the FFTW documentation
at http://www.fftw.org/doc/index.html

ALL YOU NEED TO DO:
Copy the code in main() to wherever you wish to use
Define rank of array as m and its dimensions in array n[m]
Define Transform types along each dimension (in kind[m] array) in plan as:
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
    g++ tcdcastufftwl.nd.64.cpp -L/usr/local/bin -lfftw3
  If you instead wish to compile using gcc:
    gcc tcdcastufftwl.nd.64.cpp -L/usr/local/bin -lfftw3 -lstdc++ -lm

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
  i0,i1,i2,...i_(m-1) element can be accessed via
  i(m-1) + n(m-1) * { i(m-2) + n(m-2) * { ... + i0 * n1 } } element
  For 4D: i[3]+n[3]*(i[2]+n[2]*(i[1]+n[1]*i[0]))
  For 5D: i[4]+n[4]*(i[3]+n[3]*(i[2]+n[2]*(i[1]+n[1]*i[0])))
  For 6D: i[5]+n[5]*(i[4]+n[4]*(i[3]+n[3]*(i[2]+n[2]*(i[1]+n[1]*i[0]))))
*/

#include <iostream>
#include <fftw3.h>

using namespace std;

int main()
{
    cout.precision(15);

    int m = 4;
    int n[4] = {3, 5, 7, 5};
    fftw_r2r_kind kind[4] = {FFTW_REDFT10, FFTW_REDFT10, FFTW_REDFT10, FFTW_REDFT10};
    double *inncs, *outncs;
    int np = n[0]; for(int i=1;i<m;i++) np *= n[i];
    inncs = (double*) fftw_malloc(sizeof(double) * np);
    outncs = (double*) fftw_malloc(sizeof(double) * np);
    fftw_plan pncs;
    pncs = fftw_plan_r2r(m, n, inncs, outncs, kind, FFTW_ESTIMATE);

// Define input here
    int i[m];
    for(i[0]=0;i[0]<n[0];i[0]++) {
        for(i[1]=0;i[1]<n[1];i[1]++) {
            for(i[2]=0;i[2]<n[2];i[2]++) {
                for(i[3]=0;i[3]<n[3];i[3]++) {
                    inncs[i[3]+n[3]*(i[2]+n[2]*(i[1]+n[1]*i[0]))]=i[0]*i[1]*i[2]*i[3]*1.0;
                }
            }
        }
    }

    fftw_execute(pncs);
    fftw_destroy_plan(pncs);
    
// Use output here
    for(i[0]=0;i[0]<n[0];i[0]++) {
        for(i[1]=0;i[1]<n[1];i[1]++) {
            for(i[2]=0;i[2]<n[2];i[2]++) {
                for(i[3]=0;i[3]<n[3];i[3]++) {
                    cout<<outncs[i[3]+n[3]*(i[2]+n[2]*(i[1]+n[1]*i[0]))]<<endl;
                }
            }
        }
    }
    
// If not required, deallocate input and output arrays
    fftw_free(inncs); fftw_free(outncs);

    return 0;
}

