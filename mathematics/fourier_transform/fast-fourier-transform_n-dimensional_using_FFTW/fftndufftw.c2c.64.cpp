/*
Last updated: 19-Nov-2014
Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
Source: https://github.com/udy11, https://gitlab.com/udy11
Template program (64-bit) to calculate Fast Fourier Transform
of n-dimensional complex array using FFTW libraries

This template program is for quick reference to calculate FFTs
For more efficient usage, it is recommended to refer the FFTW documentation
at http://www.fftw.org/doc/index.html

ALL YOU NEED TO DO:
Copy the code in main() to wherever you wish to use
Define rank of array as m and its dimensions in array n[m]
Your input should be defined under "Define input here"
Use output under "Use output here"
If input and output arrays are not required anymore, deallocate them as
  mentioned under "If not required, deallocate input and output arrays"
Compile your program with g++ and proper path to FFTW library, for example in Ubuntu:
    g++ tcndfftufftwl.c2c.64.cpp -L/usr/local/bin -lfftw3
  If you instead wish to compile using gcc:
    gcc tcndfftufftwl.c2c.64.cpp -L/usr/local/bin -lfftw3 -lstdc++ -lm

NOTE:
TO calculate inverse fourier transform, change FFTW_FORWARD to FFTW_BACKWARD
Do not forget to include fftw3.h header file in your code as well
Input and Output arrays can be same, in which case the input array
  will be overwritten with output array
FFTW computes unnormalized FFTs
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
    fftw_complex *innc2c, *outnc2c;
    int np = n[0]; for(int i=1;i<m;i++) np *= n[i];
    innc2c = (fftw_complex*) fftw_malloc(sizeof(fftw_complex) * np);
    outnc2c = (fftw_complex*) fftw_malloc(sizeof(fftw_complex) * np);
    fftw_plan pnc2c;
    pnc2c = fftw_plan_dft(m, n, innc2c, outnc2c, FFTW_FORWARD, FFTW_ESTIMATE);

// Define input here
    int i[m];
    for(i[0]=0;i[0]<n[0];i[0]++) {
        for(i[1]=0;i[1]<n[1];i[1]++) {
            for(i[2]=0;i[2]<n[2];i[2]++) {
                for(i[3]=0;i[3]<n[3];i[3]++) {
                    innc2c[i[3]+n[3]*(i[2]+n[2]*(i[1]+n[1]*i[0]))][0]=i[0]*i[1]*i[2]*i[3]*1.0;
                    innc2c[i[3]+n[3]*(i[2]+n[2]*(i[1]+n[1]*i[0]))][1]=i[0]*i[1]*i[2]*i[3]*0.5;
                }
            }
        }
    }

    fftw_execute(pnc2c);
    fftw_destroy_plan(pnc2c);
    
// Use output here
    for(i[0]=0;i[0]<n[0];i[0]++) {
        for(i[1]=0;i[1]<n[1];i[1]++) {
            for(i[2]=0;i[2]<n[2];i[2]++) {
                for(i[3]=0;i[3]<n[3];i[3]++) {
                    cout<<outnc2c[i[3]+n[3]*(i[2]+n[2]*(i[1]+n[1]*i[0]))][0]<<"  "<<outnc2c[i[3]+n[3]*(i[2]+n[2]*(i[1]+n[1]*i[0]))][1]<<endl;
                }
            }
        }
    }
    
// If not required, deallocate input and output arrays
    fftw_free(innc2c); fftw_free(outnc2c);

    return 0;
}

