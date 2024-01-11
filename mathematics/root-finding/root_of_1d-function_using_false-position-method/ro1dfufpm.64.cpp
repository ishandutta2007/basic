/*
Last updated: 18-Feb-2015
Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
Source: https://github.com/udy11, https://gitlab.com/udy11
Function (64-bit) to find a root of a one
dimensional function using False Position Method

ALL YOU NEED TO DO:
Call function falspos_64() with:
  a,b = range in which root is to be found (inclusive)
  er = tolerance below which root will be accepted,
       i.e., when |f(c)|<er, c is accepted as root
  istt = status code of function's execution (see below for details)
Define f(x), external function whose root is to be found
Function falspos_64() outputs the root

STATUS CODE:
istt=1, success: root found between a and b
istt=2, success: root found at a
istt=3, success: root found at b
istt=-1, error: root could not be found between a and b

NOTE:
If f(x) does not cross the x-axis but only touches it,
  like f(x)=x*x at x=0, then that root will most probably not be found
Below method does not check for opposite signs to continue operating
  as conventional false position method does, but it is then likely to
  find a root if it exists, even if signs at boundaries are not opposite
Method is optimized for minimum calls to f(x)
*/

#include <iostream>
#include <cmath>

using namespace std;

double f(double x);
double falspos_64(double a, double b, double er, int& istt);

int main()
{
    double a, b, er, c;
    int istt;
    a = -15.0; b = 4.0;
    er = 5.e-15;

    c = falspos_64(a, b, er, istt);

    cout.precision(15);
    if (istt == 1) cout<<"Root found at "<<c<<endl;
    else if (istt == 2) cout<<"Root found at a,"<<c<<endl;
    else if (istt == 3) cout<<"Root found at b,"<<c<<endl;
    else if (istt == -1) cout<<"Root could not be found in given range."<<endl;

    return 0;
}

// Input Function f(x), whose root is to be found
double f(double x)
{
    return x * x - 1.0;
}

// Function (64-bit) to find a root of f(x) using False Position Method
double falspos_64(double a, double b, double er, int& istt)
{
    double fa = f(a);
    if (fabs(fa)<er) {
        istt = 2;
        return a;
    }
    double fb = f(b);
    if (fabs(f(b))<er) {
        istt = 3;
        return b;
    }
    bool ifa;
    double c, c0, fc;
    if (fb == fa) c = 0.5 * (a + b);
    else c = (a * fb - b * fa) / (fb - fa);
    if (c == 0.0) c0 = 1.0;
    else c0 = 0.0;
    while (true) {
        fc = f(c);
        if (fabs(fc) < er) {
            istt = 1;
            break;
        }
        else if (c == c0) {
            istt = -1;
            break;
        }
        else {
            if (fa * fc < 0.0) {
                b = c;
                ifa = false;
            }
            else {
                a = c;
                ifa = true;
            }
            if (ifa) fa = f(a);
            else fb = f(b);
        }
        c0 = c;
        if (fb == fa) c = 0.5 * (a + b);
        else c = (a * fb - b * fa) / (fb - fa);
    }
    return c;
}
