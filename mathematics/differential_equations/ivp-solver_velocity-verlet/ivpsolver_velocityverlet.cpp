/*
Last updated: 30-Aug-2016
Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
Source: https://github.com/udy11, https://gitlab.com/udy11
Function to solve 2nd order ordinary differential
equation with initial values using Velocity Verlet algorithm

This program solves for the following second order ODE:
  y'' = f(y)
i.e., f() depends only on y and NOT on x or y'

ALL YOU NEED TO DO:
Call function velverlet() with:
  fx = external function that defines ODEs (see below INPUT FUNCTION)
  h = step size in which x increases per iteration
  ns = number of iterations
  x0 = initial value of x, from which iteration begins
  y0 = value of y at x0
  yp0 = value of y' at x0
  ofln = output file name

OUTPUT:
Output is in the text file, whose name is given by ofln
The three columns represent x, y and y' respectively

EXAMPLE:
Example ODE is:
  y''+100*y=0, y(0)=0.0, y'(0)=10
Its exact solution is:
  y(x)=sin(10*x)

NOTE:
If you want to run from x0 to x1, then h or ns can be calculated as:
  h = (x1 - x0) / ns
  ns = (x1 - x0) / h
Error ~ h^2
Program uses a template class for real numbers that allows it to work
  for either float, double or long double. However, make sure that
  all real input numbers are of same class and if any other real variable
  is decalred in the input function or velverlet(), it is declared as
  an object of template class flt
Compilation requires -std=c++11 or -std=gnu++11 flag to be used,
  however, if this flag is unavailable, you can manually set
  output precision in ofl.precision() line in velverlet() and ignore 
  <limits> library
*/

#include <iostream>
#include <fstream>
#include <limits>

// INPUT FUNCTION
// Simply define it as the RHS of the 2nd order ODE y'' = f(y)
template <class flt>
flt gx(flt y)
{
    return -100.0 * y;
}

// Velocity Verlet algorithm function
template <class flt>
int velverlet(flt (*fx)(flt), flt h, int ns, flt x0, flt y0, flt yp0, char ofln[])
{
    int i;
    flt y, yp, hh, b;
    hh = h * 0.5;
    y = y0;
    yp = yp0;
    std::ofstream ofl;
    ofl.open(ofln);
    ofl.precision(std::numeric_limits<decltype(h)>::digits10);
    ofl << x0 << ' ' << y0 << ' ' << yp0 << '\n';
    for (int j = 1; j <= ns; j++) {
        b = yp + (*fx)(y) * hh;
        y += b * h;
        yp = b + (*fx)(y) * hh;
        ofl << x0 + j * h << ' ' << y << ' ' << yp << '\n';
    }
    ofl.close();
    std::cout << "output written to file: " << ofln << std::endl;
    return 0;
}

int main()
{
    int ns;
    double x0, h, y0, yp0;

    // INPUT:
    h = 1.e-3;                               // step size in which iteration proceeds
    ns = 1000;                               // number of steps
    x0 = 0.0;                                // initial value from which iteration begins
    y0 = 0.0;                                // initial value of y
    yp0 = 10.0;                              // initial value of y'
    char ofln[] = "velverlet_tst.cpp.txt";   // output file name (overwrites if already exists)

    velverlet(gx, h, ns, x0, y0, yp0, ofln);
    return 0;
}
