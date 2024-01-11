/*
Last updated: 19-Nov-2014
Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
Source: https://github.com/udy11, https://gitlab.com/udy11
Template program (64-bit) to calculate inverse Fast Fourier Transform
of n-dimensional complex array to real array using FFTW libraries

This template program is for quick reference to calculate FFTs
For more efficient usage, it is recommended to refer the FFTW documentation
at http://www.fftw.org/doc/index.html

ALL YOU NEED TO DO:
Copy the code in main() to wherever you wish to use
Define rank of array as m and its dimensions in array n[m]
  input array double[n0*n1*...*n(m-1)], output array fftw_complex[n0*n1*...*(1+n(m-1)/2)]
Your input should be defined under "Define input here"
Use output under "Use output here"
If input and output arrays are not required anymore, deallocate them as
  mentioned under "If not required, deallocate input and output arrays"
Compile your program with g++ and proper path to FFTW library, for example in Ubuntu:
    g++ tcndfftufftwl.c2r.64.cpp -L/usr/local/bin -lfftw3
  If you instead wish to compile using gcc:
    gcc tcndfftufftwl.c2r.64.cpp -L/usr/local/bin -lfftw3 -lstdc++ -lm

NOTE:
c2r is an inverse transform; for forward transform, use r2c
In case of c2r, input is fftw_complex array of size n0*n1*...*(1+n(m-1)/2) and
  output is double array of size n0*n1*...*n(m-1)
Do not forget to include fftw3.h header file in your code as well
Input and Output arrays can be same, in which case the input array
  will be overwritten with output array
FFTW computes unnormalized FFTs
Arrays are stored as one-dimensional arrays in row-major format and 
  (i0,i1,...,i(m-1)) element of input can be accessed via:
      i(m-1) + (1+n(m-1)/2) * { i(m-2) + n(m-2) * { ... + i0 * n1 } } element
  (i0,i1,...,i(m-1)) element of output can be accessed via:
      i(m-1) + n(m-1) * { i(m-2) + n(m-2) * { ... + i0 * n1 } } element
  For 4D:
    Input:  i[3]+(1+n[3]/2)*(i[2]+n[2]*(i[1]+n[1]*i[0]))
    Output: i[3]+n[3]*(i[2]+n[2]*(i[1]+n[1]*i[0]))
  For 5D:
    Input:  i[4]+(1+n[4]/2)*(i[3]+n[3]*(i[2]+n[2]*(i[1]+n[1]*i[0])))
    Output: i[4]+n[4]*(i[3]+n[3]*(i[2]+n[2]*(i[1]+n[1]*i[0])))
  For 6D:
    Input:  i[5]+(1+n[5]/2)*(i[4]+n[4]*(i[3]+n[3]*(i[2]+n[2]*(i[1]+n[1]*i[0]))))
    Output: i[5]+n[5]*(i[4]+n[4]*(i[3]+n[3]*(i[2]+n[2]*(i[1]+n[1]*i[0]))))
Storing only 1+n(m-1)/2 entries in last dimension of input is done because (n(m-1)-1)th entry
  is complex conjugate of 1st (not 0th, as per c++ convention), (n(m-1)-2)th is complex
  conjugate of 2nd and so on..
Default c2r transform for nd changes the input array
*/

#include <iostream>
#include <fftw3.h>

using namespace std;

int main()
{
    cout.precision(15);

    int m = 4;
    int n[4] = {3, 5, 7, 5};
    fftw_complex *innc2r;
    double *outnc2r;
    int np = n[0]; for(int i=1;i<m;i++) np *= n[i];
    innc2r = (fftw_complex*) fftw_malloc(sizeof(fftw_complex) * np * (1+n[m-1]/2) / n[m-1]);
    outnc2r = (double*) fftw_malloc(sizeof(double) * np);
    fftw_plan pnc2r;
    pnc2r = fftw_plan_dft_c2r(m, n, innc2r, outnc2r, FFTW_ESTIMATE);

// Define input here
    int i[m];
    for(i[0]=0;i[0]<n[0];i[0]++) {
        for(i[1]=0;i[1]<n[1];i[1]++) {
            for(i[2]=0;i[2]<n[2];i[2]++) {
                for(i[3]=0;i[3]<(1+n[3]/2);i[3]++) {
                    innc2r[i[3]+(1+n[3]/2)*(i[2]+n[2]*(i[1]+n[1]*i[0]))][0]=i[0]*i[1]*i[2]*i[3]*1.0;
                    innc2r[i[3]+(1+n[3]/2)*(i[2]+n[2]*(i[1]+n[1]*i[0]))][1]=i[0]*i[1]*i[2]*i[3]*0.5;
                }
            }
        }
    }

    fftw_execute(pnc2r);
    fftw_destroy_plan(pnc2r);
    
// Use output here
    for(i[0]=0;i[0]<n[0];i[0]++) {
        for(i[1]=0;i[1]<n[1];i[1]++) {
            for(i[2]=0;i[2]<n[2];i[2]++) {
                for(i[3]=0;i[3]<n[3];i[3]++) {
                    cout<<outnc2r[i[3]+n[3]*(i[2]+n[2]*(i[1]+n[1]*i[0]))]<<endl;
                }
            }
        }
    }
    
// If not required, deallocate input and output arrays
    fftw_free(innc2r); fftw_free(outnc2r);

    return 0;
}

