/*
Last updated: 24-Nov-2014
Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
Source: https://github.com/udy11, https://gitlab.com/udy11
Template program (64-bit) to calculate Discrete Hartley Transform
of one-dimensional real array using FFTW libraries

This template program is for quick reference to calculate FFTs
For more efficient usage, it is recommended to refer the FFTW documentation
at http://www.fftw.org/doc/index.html

ALL YOU NEED TO DO:
Copy the code in main() to wherever you wish to use
Define value of n0 as length of array
Your input should be defined under "Define input here"
Use output under "Use output here"
If input and output arrays are not required anymore, deallocate them as
  mentioned under "If not required, deallocate input and output arrays"
Compile your program with g++ and proper path to FFTW library, for example in Ubuntu:
    g++ tcdhtufftwl.1d.64.cpp -L/usr/local/bin -lfftw3
  If you instead wish to compile using gcc:
    gcc tcdhtufftwl.1d.64.cpp -L/usr/local/bin -lfftw3 -lstdc++ -lm

DEFINITION:
For input data X_0, X_1, ... , X_(n-1), the transform H_k
  (for k=0,n-1) is defined as:
  H_k = sum_(j=0)^(n-1) [X_j * (cos(2*pi*j*k/n) + sin(2*pi*j*k/n)) ]

NOTE:
DHT is inverse of itself
Do not forget to include fftw3.h header file in your code as well
Input and Output arrays can be same, in which case the input array
  will be overwritten with output array
FFTW computes unnormalized transforms
*/

#include <iostream>
#include <fftw3.h>

using namespace std;

int main()
{
    cout.precision(15);

    int n0 = 15;
    double *in1ht, *out1ht;
    in1ht = (double*) fftw_malloc(sizeof(double) * n0);
    out1ht = (double*) fftw_malloc(sizeof(double) * n0);
    fftw_plan p1ht;
    p1ht = fftw_plan_r2r_1d(n0, in1ht, out1ht, FFTW_DHT, FFTW_ESTIMATE);

// Define input here
    for(int i=0;i<n0;i++) {
        in1ht[i]=i*1.0;
    }

    fftw_execute(p1ht);
    fftw_destroy_plan(p1ht);
    
// Use output here
    for(int i=0;i<n0;i++) {
        cout<<out1ht[i]<<endl;
    }
    
// If not required, deallocate input and output arrays
    fftw_free(in1ht); fftw_free(out1ht);

    return 0;
}

