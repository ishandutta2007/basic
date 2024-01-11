/*
Last updated: 16-Apr-2013
Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
Source: https://github.com/udy11, https://gitlab.com/udy11
Function (32-bit) to find a root of a one
dimensional function using Secant Method

ALL YOU NEED TO DO:
Specify two initial guesses x0 and x1,
  they must be near the desired root
Specify the function y(x), whose root is needed
Specify positive small er; when |y(x2)|<er, further
  computation stops and x2 is returned as root
*/

#include<iostream>
#include<math.h>

using namespace std;

// Input Function y(x), whose root is to be found
float y(float x)
{
    return sin(x);
}

// Function (32-bit) to find root of y(x)=0
// using Secant Method
// x0, x1 are initial guesses
// er is a small positive number such that when
// |y(x2)|<er, further calculation is stopped
// and x2 is returned as root
float scnt_32(float x0,float x1,float er)
{
    float x2;
    while (1) {
        x2=x1-y(x1)*(x1-x0)/(y(x1)-y(x0));
        if(fabs(y(x2))<er) break;
        x0=x1;
        x1=x2;
    };
    return x2;
}

int main()
{
    float x0,x1,er,x2;
    x0=2.1;
    x1=4.8;
    er=9.e-8;
    x2=scnt_32(x0,x1,er);
    cout.precision(7);
    cout<<x2<<"  "<<y(x2);
    return 0;
}
