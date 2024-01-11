/*
Last updated: 04-Jun-2016
Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
Source: https://github.com/udy11, https://gitlab.com/udy11
Function (64-bit) to find roots of a one dimensional
function by recursively using Bisection Method

ALL YOU NEED TO DO:
Call function bsctns_64() with:
  f = double function whose root is to be found
  a,b = range in which root is to be found (inclusive)
  er = tolerance in f() below which root will be accepted,
       i.e., when |f(c)|<er, c is accepted as root
  nk = in how many equal intervals to divide (a, b) into,
       recursive root finding is attempted in each of
       these intervals
  nd = simply put, keep this low like 1, 2, 3 or 4. this int
       decides how closely to single-out a root once it is found.
       a larger int will better single-out the root but will
       require several function calls too, so better keep it low
  rts = double array which will contain the found roots, its size
        should be sufficient to keep all the roots found
  nr = number of roots found by bsctns_64()
Define f(x), external double function whose roots are to be found

ALGORITHM:
(a, b) is divided into nk equal intervals then bisection
method is applied in all these intervals (say one of them is
(p, q)). if a root r is found in (p, q), then new roots are recursively
attempted to find between (p, r-dr1) and (r+dr2, q) where
dr1 and dr2 are approximately calculated such that all x
in (r-dr1, r+dr2) have |f(x)| < er. how better dr1 and dr2 are
depends on how large nd is, but a large nd will also require
many function calls (which might be costly) so better keep nd low.

SUGGESTIONS:
Obviously this method is not guaranteed to find all roots of the
function, so it is suggested that:
1. If possible check the plot of f(x) and identify all intervals
   where roots might exist, it will be best if f(x) has opposite
   signs on the ends of these intervals
2. If satisfactory roots are not found, first try increasing
   er (compromise with accuracy); next try to increase nk (compromise
   with efficiency); lastly, changing nd should not have much effect
   but try to vary it in 1-5 (large nd is compromise with efficiency,
   low nd is compromise with accuracy)

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
double g(double x)
{
    return 0.999999 + sin(x);
}

double bsctn_64(double (*f)(double), double a, double b, double &er, double &eps, int &istt)
{
    double fa = (*f)(a);
    double fb = (*f)(b);
    if (std::fabs(fa) < er) {
        istt = 2;
        return a;
    }
    if (std::fabs(fb) < er) {
        istt = 3;
        return b;
    }
    bool ifa = false;
    bool ifb = false;
    double c = 0.5 * (a + b);
    double fc, c0;
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
        else if (c0 != 0.0 && std::fabs(1.0 - c / c0) < eps) {
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

double fbdr(double (*f)(double), double b, double &er, int &nd, double &eps, double &fmn)
{
    double e2 = std::max(std::fabs(b) * eps, fmn);
    while (std::fabs((*f)(b - e2)) < er) e2 *= 2.0;
    double e1 = e2 * 0.5;
    int i = 0;
    double e3;
    while (i < nd && std::fabs(1.0 - e2 / e1) > eps) {
        e3 = 0.5 * (e1 + e2);
        if (std::fabs((*f)(b - e3)) < er) e1 = e3;
        else e2 = e3;
        i++;
    }
    return e2;
}

double fadr(double (*f)(double), double a, double &er, int &nd, double &eps, double &fmn)
{
    double e2 = std::max(std::fabs(a) * eps, fmn);
    while (std::fabs((*f)(a + e2)) < er) e2 *= 2.0;
    double e1 = e2 * 0.5;
    int i = 0;
    double e3;
    while (i < nd && std::fabs(1.0 - e2 / e1) > eps) {
        e3 = 0.5 * (e1 + e2);
        if (std::fabs((*f)(a + e3)) < er) e1 = e3;
        else e2 = e3;
        i++;
    }
    return e2;
}

int rrtf(double (*f)(double), double a, double b, double &er, int &nd, double &eps, double &fmn, double *rts, int &nr)
{
    int ist;
    double dr;
    double r = bsctn_64((*f), a, b, er, eps, ist);
    if (ist == 1) {
        rts[nr] = r;
        nr++;
        dr = fbdr((*f), r, er, nd, eps, fmn);
        rrtf((*f), a, r - dr, er, nd, eps, fmn, rts, nr);
        dr = fadr((*f), r, er, nd, eps, fmn);
        rrtf((*f), r + dr, b, er, nd, eps, fmn, rts, nr);
    }
    else if (ist == 2) {
        rts[nr] = r;
        nr++;
        dr = fadr((*f), r, er, nd, eps, fmn);
        rrtf((*f), r + dr, b, er, nd, eps, fmn, rts, nr);
    }
    else if (ist == 3) {
        rts[nr] = r;
        nr++;
        dr = fbdr((*f), r, er, nd, eps, fmn);
        rrtf((*f), a, r - dr, er, nd, eps, fmn, rts, nr);
    }
    return 0;
}

// Function (64-bit) to find roots of f(x) by recursively using Bisection Method
int bsctns_64(double (*f)(double), double a, double b, double er, int nk, int nd, double *rts, int &nr)
{
    double dab = (b - a) / nk;
    double a1, adr;
    bool ch;
    double eps = 2.0 * std::numeric_limits<double>::epsilon();
    double fmn = std::numeric_limits<double>::min();
    nr = 0;
    for (int k = 0; k < nk; k++) {
        a1 = a + k * dab;
        ch = true;
        for (int j = 0; j < nr; j++) {
            if (rts[j] == a1) {
                adr = fadr((*f), a1, er, nd, eps, fmn);
                ch = false;
                break;
            }
        }
        if (ch) adr = 0.0;
        rrtf((*f), a1 + adr, a + (k + 1) * dab, er, nd, eps, fmn, rts, nr);
    }
    return 0;
}

int main()
{
    double a, b, er;
    double * r = new double[100];
    int nk, nd, nr;
    a = -20.0; b = 20.0;
    er = 1.e-14;
    nk = 10; nd = 3;

    bsctns_64((*g), a, b, er, nk, nd, r, nr);

    std::cout.precision(15);
    for (int i = 0; i < nr; i++) {
        std::cout << r[i] << '\n';
    }

    delete[] r;
    return 0;
}
