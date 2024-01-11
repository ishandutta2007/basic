/*
Last updated: 18-Nov-2014
Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
Source: https://github.com/udy11, https://gitlab.com/udy11
Template program (64-bit) to calculate Fast Fourier Transform
of one-dimensional complex array using FFTW libraries

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
    g++ tc1dfftufftwl.c2c.64.cpp -L/usr/local/bin -lfftw3
  If you instead wish to compile using gcc:
    gcc tc1dfftufftwl.c2c.64.cpp -L/usr/local/bin -lfftw3 -lstdc++ -lm

NOTE:
TO calculate inverse fourier transform, change FFTW_FORWARD to FFTW_BACKWARD
Do not forget to include fftw3.h header file in your code as well
Input and Output arrays can be same, in which case the input array
  will be overwritten with output array
FFTW computes unnormalized FFTs
Output array is in standard form, i.e. first entry for 0 frequency
  followed by positive frequencies and then negative frequencies
*/

#include <iostream>
#include <fftw3.h>

using namespace std;

int main()
{
    cout.precision(15);

    int n0 = 19;
    fftw_complex *in1c2c, *out1c2c;
    in1c2c = (fftw_complex*) fftw_malloc(sizeof(fftw_complex) * n0);
    out1c2c = (fftw_complex*) fftw_malloc(sizeof(fftw_complex) * n0);
    fftw_plan p1c2c;
    p1c2c = fftw_plan_dft_1d(n0, in1c2c, out1c2c, FFTW_FORWARD, FFTW_ESTIMATE);

// Define input here
    for(int i=0;i<n0;i++) {
        in1c2c[i][0]=i*1.0; in1c2c[i][1]=i*0.5;
    }

    fftw_execute(p1c2c);
    fftw_destroy_plan(p1c2c);
    
// Use output here
    for(int i=0;i<n0;i++) {
        cout<<out1c2c[i][0]<<"  "<<out1c2c[i][1]<<endl;
    }
    
// If not required, deallocate input and output arrays
    fftw_free(in1c2c); fftw_free(out1c2c);

    return 0;
}

