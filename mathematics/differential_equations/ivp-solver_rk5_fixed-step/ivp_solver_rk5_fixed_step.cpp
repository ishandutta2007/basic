/*
Last updated: 04-Aug-2016
Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
Source: https://github.com/udy11, https://gitlab.com/udy11
Function to solve coupled ordinary differential equations with
initial values (coupled-ODEs-IVP) using Butcher's Runge Kutta 5 method

The program solves coupled ODEs y'[i]=f(x,y[j])[i]; {i,j: 0-->n-1}

ALL YOU NEED TO DO:
Call function brk5() with:
  fx = external function that defines ODEs (see below INPUT FUNCTION)
  n = number of unknowns y[i]
  h = step size in which x increases per iteration
  ns = number of iterations
  x0 = initial value of x, from which iteration begins
  y0 = initial value(s) of y at x0
  ofln = output file name

OUTPUT:
Output is in the text file, whose name is given by ofln
First column represents x, followed by the y vector

EXAMPLE:
Example ODE is:
  y'''-6y''+11y'-6y=x^2-1, y(0)=-0.5, y'(0)=-1, y''(0)=0.5
broken into three coupled ODEs as:
  y0'=y1, y1'=y2, y2'=6*y2-11*y1+6*y0+x^2-1,
  y0(0)=-0.5, y1(0)=-1, y2(0)=0.5
Its exact solution (for y(x) or y0(x)) is:
  y(x)=(-67+189*exp(x)-297*exp(2*x)+121*exp(3*x)-66*x-18*x^2)/108

NOTE:
This implementation of Butcher's Runge-Kutta 5 uses
  constant step size, predefined by user
If you want to run RK5 from x0 to x1, then h or ns can be calculated as:
  h = (x1 - x0) / ns
  ns = (x1 - x0) / h
A higher order ODE can be broken into coupled ODEs, e.g.,
  y''+100*y=0, can be broken as y0'=y1; y1'=-100*y0
Program uses a template class for real numbers that allows it to work
  for either float, double or long double. However, make sure that
  all real input numbers are of same class and if any other real variable
  is decalred in the input function or brk5(), it is declared as an object
  of template class flt
Compilation requires -std=c++11 or -std=gnu++11 flag to be used,
  however, if this flag is unavailable, you can manually set
  output precision in ofl.precision() line in brk5() and ignore 
  <limits> library
*/

#include <iostream>
#include <fstream>
#include <limits>

/*
INPUT FUNCTION
Simply define functions f[0], f[1], ..., f[n-1]
for coupled ODEs: y'[i] = f(x, y[j])[i]
Example:
Suppose you want to solve: y'[0] = y[1]; y'[1] = -100 * y[0]
Then define f[0] = y[1] and f[1] = -100.0 * y[0]
This means f are simply the RHS in the coupled ODEs when arranged properly.
*/
template <class flt>
int gx(flt f[], flt x, flt y[], int n)
{
    f[0] = y[1];
    f[1] = y[2];
    f[2] = 6.0 * y[2] - 11.0 * y[1] + 6.0 * y[0] + x * x - 1.0;
    return 0;
}

// Butcher's RK5 Function
template <class flt>
int brk5(int (*fx)(flt[], flt, flt[], int), int n, flt h, int ns, flt x0, flt y0[],char ofln[])
{
    flt k1[n], k2[n], k3[n], k4[n], k5[n], k6[n], f[n], ta[n], y[n];
    flt x;
    flt obs = 1.0 / 7.0;
    flt obn = 1.0 / 9.0;
    int i;
    std::ofstream ofl;
    ofl.open(ofln);
    ofl.precision(std::numeric_limits<decltype(h)>::digits10);
    x = x0;
    ofl << x << ' ';
    for (i = 0; i < n; i++) {
        y[i] = y0[i];
        ofl << y[i] << ' ';
    }
    ofl << '\n';
    for (int j = 1; j <= ns; j++) {
        (*fx)(f, x, y, n);
        for (i = 0; i < n; i++) {
            k1[i] = h * f[i];
        }
        for (i = 0; i < n; i++) {
            ta[i] = y[i] + 0.25 * k1[i];
        }
        (*fx)(f, x + 0.25 * h, ta, n);
        for (i = 0; i < n; i++) {
            k2[i] = h * f[i];
        }
        for (i = 0; i < n; i++) {
            ta[i] = y[i] + 0.125 * (k1[i] + k2[i]);
        }
        (*fx)(f, x + 0.25 * h, ta, n);
        for (i = 0; i < n; i++) {
            k3[i] = h * f[i];
        }
        for (i = 0; i < n; i++) {
            ta[i] = y[i] - 0.5 * k2[i] + k3[i];
        }
        (*fx)(f, x + 0.5 * h, ta, n);
        for (i = 0; i < n; i++) {
            k4[i] = h * f[i];
        }
        for (i = 0; i < n; i++) {
            ta[i] = y[i] + 0.1875 * k1[i] + 0.5625 * k4[i];
        }
        (*fx)(f, x + 0.75 * h, ta, n);
        for (i = 0; i < n; i++) {
            k5[i] = h * f[i];
        }
        for (i = 0; i < n; i++) {
            ta[i] = y[i] + (-3.0 * k1[i] + 2.0 * k2[i] + 12.0 * k3[i] - 12.0 * k4[i] + 8.0 * k5[i]) * obs;
        }
        (*fx)(f, x + h, ta, n);
        for (i = 0; i < n; i++) {
            k6[i] = h * f[i];
        }
        x = x0 + j * h;
        ofl << x << ' ';
        for (i = 0; i < n; i++) {
            y[i] = y[i] + (0.7 * k1[i] + 3.2 * k3[i] + 1.2 * k4[i] + 3.2 * k5[i] +0.7 * k6[i]) * obn;
            ofl << y[i] << ' ';
        }
        ofl << '\n';
    }
    ofl.close();
    std::cout << "output written to file: " << ofln << std::endl;
    return 0;
}

int main()
{
    double x0, h;

    // INPUT:
    h = 0.0001;                         // step size in which iteration proceeds
    int ns = 6000;                      // number of steps
    x0 = 0.0;                           // initial value from which iteration begins
    double y0[] = {-0.5, -1.0, 0.5};    // initial values for unknowns
    char ofln[] = "brk5_tst.cpp.txt";   // output file name (overwrites if already exists)

    int n = sizeof(y0) / sizeof(y0[0]);
    brk5(gx, n, h, ns, x0, y0, ofln);
    return 0;
}
