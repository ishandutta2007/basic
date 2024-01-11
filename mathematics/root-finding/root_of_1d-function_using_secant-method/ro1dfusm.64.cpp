/*
Last updated: 16-Apr-2013
Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
Source: https://github.com/udy11, https://gitlab.com/udy11
Function (64-bit) to find a root of a one
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
double y(double x)
{
    return sin(x);
}

// Function (32-bit) to find root of y(x)=0
// using Secant Method
// x0, x1 are initial guesses
// er is a small positive number such that when
// |y(x2)|<er, further calculation is stopped
// and x2 is returned as root
double scnt_64(double x0,double x1,double er)
{
    double x2;
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
    double x0,x1,er,x2;
    x0=2.1;
    x1=4.8;
    er=2.e-16;
    x2=scnt_64(x0,x1,er);
    cout.precision(15);
    cout<<x2<<"  "<<y(x2);
    return 0;
}
