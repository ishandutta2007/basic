# Last updated: 04-Jun-2016
# Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
# Source: https://github.com/udy11, https://gitlab.com/udy11
# Function to find roots of a one dimensional
# function by recursively using Bisection Method

# ALL YOU NEED TO DO:
# Call function bsctns() with:
#   f = function whose root is to be found (must return num)
#   a,b = range in which root is to be found (inclusive)
#   er = tolerance in f() below which root will be accepted,
#        i.e., when |f(c)|<er, c is accepted as root
#   nk = in how many equal intervals to divide (a, b) into,
#        recursive root finding is attempted in each of
#        these intervals
#   nd = simply put, keep this low like 1, 2, 3 or 4. this int
#        decides how closely to single-out a root once it is found.
#        a larger int will better single-out the root but will
#        require several function calls too, so better keep it low
# Define f(x), external function whose roots are to be found
# Function bsctns() outputs list of roots

# ALGORITHM:
# (a, b) is divided into nk equal intervals then bisection
# method is applied in all these intervals (say one of them is
# (p, q)). if a root r is found in (p, q), then new roots are recursively
# attempted to find between (p, r-dr1) and (r+dr2, q) where
# dr1 and dr2 are approximately calculated such that all x
# in (r-dr1, r+dr2) have |f(x)| < er. how better dr1 and dr2 are
# depends on how large nd is, but a large nd will also require
# many function calls (which might be costly) so better keep nd low.

# SUGGESTIONS:
# Obviously this method is not guaranteed to find all roots of the
# function, so it is suggested that:
# 1. If possible check the plot of f(x) and identify all intervals
#    where roots might exist, it will be best if f(x) has opposite
#    signs on the ends of these intervals
# 2. If satisfactory roots are not found, first try increasing
#    er (compromise with accuracy); next try to increase nk (compromise
#    with efficiency); lastly, changing nd should not have much effect
#    but try to vary it in 1-5 (large nd is compromise with efficiency,
#    low nd is compromise with accuracy)

# NOTE:
# If f(x) does not cross the x-axis but only touches it,
#   like f(x)=x*x at x=0, then that root will most probably not be found
# Below method does not check for opposite signs to continue operating
#   as conventional bisection method does, which makes it likely to find
#   a root if it exists, even if signs at boundaries are not opposite
# Method is optimized for minimum calls to f(x)
# Roots will not be sorted

import math

def bsctns(f, a, b, er, nk, nd):
    ''' (function, float, float, float, int, int) -> list of float

        Function to find roots of f(x) by recursively using Bisection Method
    '''
    def bsctn(a, b):
        fa = f(a)
        fb = f(b)
        if abs(fa) < er:
            return (2, a)
        if abs(fb) < er:
            return (3, b)
        ifa = False
        ifb = False
        c = 0.5 * (a + b)
        if abs(c - 1.0) < eps:
            c0 = 2.0
        else:
            c0 = 1.0
        while True:
            fc = f(c)
            if abs(fc) < er:
                return (1, c)
            elif c0 == 0.0 and c == 0.0:
                return (-1, c)
            elif c0 != 0.0 and abs(1 - c / c0) < eps:
                return (-1, c)
            else:
                if ifa:
                    fa = f(a)
                elif ifb:
                    fb = f(b)
                if fa * fc < 0.0:
                    b = c
                    ifa = False
                    ifb = True
                elif fb * fc < 0.0:
                    a = c
                    ifa = True
                    ifb = False
                elif abs(fa) < abs(fb):
                    b = c
                    ifa = False
                    ifb = True
                else:
                    a = c
                    ifa = True
                    ifb = False
            c0 = c
            c = 0.5 * (a + b)
    def fbdr(b):
        e2 = max(abs(b) * eps, fmn)
        while abs(f(b - e2)) < er:
            e2 *= 2
        e1 = e2 * 0.5
        i = 0
        while i < nd and abs(1 - e2 / e1) > eps:
            e3 = 0.5 * (e1 + e2)
            if abs(f(b - e3)) < er:
                e1 = e3
            else:
                e2 = e3
            i += 1
        return e2
    def fadr(a):
        e2 = max(abs(a) * eps, fmn)
        while abs(f(a + e2)) < er:
            e2 *= 2
        e1 = e2 * 0.5
        i = 0
        while i < nd and abs(1 - e2 / e1) > eps:
            e3 = 0.5 * (e1 + e2)
            if abs(f(a + e3)) < er:
                e1 = e3
            else:
                e2 = e3
            i += 1
        return e2
    def rrtf(a, b):
        nonlocal rts
        r = bsctn(a, b)
        if r[0] == 1:
            rts.append(r[1])
            dr = fbdr(r[1])
            rrtf(a, r[1] - dr)
            dr = fadr(r[1])
            rrtf(r[1] + dr, b)
        elif r[0] == 2:
            rts.append(r[1])
            dr = fadr(r[1])
            rrtf(r[1] + dr, b)
        elif r[0] == 3:
            rts.append(r[1])
            dr = fbdr(r[1])
            rrtf(a, r[1] - dr)
    eps = 4.4408920985006262e-16
    fmn = 2.225073858507201383e-308
    rts = []
    dab = (b - a) / nk
    for k in range(nk):
        a1 = a + k * dab
        if a1 in rts:
            adr = fadr(a1)
        else:
            adr = 0
        rrtf(a1 + adr, a + (k + 1) * dab)
    return rts

def g(x):
    ''' (float) -> float
        Input Function g(x), whose roots are to be found
    '''
    return 0.999999999 + math.sin(x)

p = -20
q = 20
er = 1.0e-14
nk = 10
nd = 3
r = bsctns(g, p, q, er, nk, nd)
print(r)
