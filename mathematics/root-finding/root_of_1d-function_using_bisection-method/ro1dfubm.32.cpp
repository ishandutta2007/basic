/*
Last updated: 04-Jun-2016
Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
Source: https://github.com/udy11, https://gitlab.com/udy11
Function (32-bit) to find a root of a one
dimensional function using Bisection Method

ALL YOU NEED TO DO:
Call function bsctn_32() with:
  f = float function whose root is to be found
  a,b = range in which root is to be found (inclusive)
  er = tolerance below which root will be accepted,
       i.e., when |f(c)|<er, c is accepted as root
  istt = status code of function's execution (see below for details)
Define f(x), external function whose root is to be found
Function bsctn_32() outputs the root

STATUS CODE:
istt=1, success: root found between a and b
istt=2, success: root found at a
istt=3, success: root found at b
istt=-1, error: root could not be found between a and b

NOTE:
If f(x) does not cross the x-axis but only touches it,
  like f(x)=x*x at x=0, then that root will most probably not be found
Below method does not check for opposite signs to continue operating
  as conventional bisection method does, but it is then likely to find
  a root if it exists, even if signs at boundaries are same
Method is optimized for minimum calls to f(x)
*/

#include <iostream>
#include <limits>
#include <cmath>

// Input Function g(x), whose root is to be found
float g(float x)
{
    return x * x - 1.0;
}

// Function (32-bit) to find a root of f(x) using Bisection Method
float bsctn_32(float (*f)(float), float a, float b, float er, int& istt)
{
    float fa = (*f)(a);
    float fb = (*f)(b);
    if (std::fabs(fa) < er) {
        istt = 2;
        return a;
    }
    if (std::fabs(fb) < er) {
        istt = 3;
        return b;
    }
    float eps = 2.0 * std::numeric_limits<float>::epsilon();
    bool ifa = false;
    bool ifb = false;
    float c = 0.5 * (a + b);
    float fc, c0;
    if (std::fabs(c - 1.0) < eps) c0 = 2.0;
    else c0 = 1.0;
    while (true) {
        fc = (*f)(c);
        if (std::fabs(fc) < er) {
            istt = 1;
            break;
        }
        else if (c0 == 0.0 && c == 0.0) {
            istt = -1;
            break;
        }
        else if (c0 == 0.0 && std::fabs(1.0 - c / c0) < eps) {
            istt = -1;
            break;
        }
        else {
            if (ifa) fa = (*f)(a);
            else if (ifb) fb = (*f)(b);
            if (fa * fc < 0.0) {
                b = c;
                ifa = false;
                ifb = true;
            }
            else if (fb * fc < 0.0) {
                a = c;
                ifa = true;
                ifb = false;
            }
            else if (std::fabs(fa) < std::fabs(fb)) {
                b = c;
                ifa = false;
                ifb = true;
            }
            else {
                a = c;
                ifa = true;
                ifb = false;
            }
        }
        c0 = c;
        c = 0.5 * (a + b);
    }
    return c;
}

int main()
{
    float a, b, er, c;
    int istt;
    a = -2.0; b = 20.0;
    er = 3.e-7;

    c = bsctn_32(g, a, b, er, istt);

    std::cout.precision(7);
    if (istt == 1) std::cout << "Root found at " << c << std::endl;
    else if (istt == 2) std::cout << "Root found at a, " << c << std::endl;
    else if (istt == 3) std::cout << "Root found at b, " << c << std::endl;
    else if (istt == -1) std::cout << "Root could not be found in given range." <<std::endl;

    return 0;
}
