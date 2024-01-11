/*
Last updated: 26-Apr-2013
Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
Source: https://github.com/udy11, https://gitlab.com/udy11
Function (64-bit) to find a root of a one
dimensional function using Newton-Raphson Method

ALL YOU NEED TO DO:
Specify an initial guess x0,
  it must be near the desired root
Specify the function y(x), whose root is needed
Specify the derivative of y(x) as yp(x)
Specify positive small er; when |y(x1)|<er, further
  computation stops and x1 is returned as root
*/

#include<iostream>
#include<math.h>

using namespace std;

// Input Function y(x), whose root is to be found
double y(double x)
{
    return sin(x);
}

// Derivative of y(x), i.e. dy(x)/dx
double yp(double x)
{
    return cos(x);
}

// Function (64-bit) to find root of y(x)=0
// using Newton-Raphson Method
// x0 is initial guess
// er is a small positive number such that when
// |y(x1)|<er, further calculation is stopped
// and x1 is returned as root
double nwtn_rphsn_64(double x0, double er)
{
    double x1;
    while (1) {
        x1=x0-y(x0)/yp(x0);
        if(fabs(y(x1))<er) break;
        x0=x1;
    };
    return x1;
}

int main()
{
    double x0,er,x1;
    x0=9.7;
    er=4.e-16;
    x1=nwtn_rphsn_64(x0,er);
    cout.precision(15);
    cout<<x1<<"  "<<y(x1);
    return 0;
}
