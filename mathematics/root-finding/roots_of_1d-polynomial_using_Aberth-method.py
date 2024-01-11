# Last updated: 08-Mar-2015
# Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
# Source: https://github.com/udy11, https://gitlab.com/udy11
# Function to find roots of one-dimensional polynomial
# using Aberth Method

# ALL YOU NEED TO DO:
# Call function polyroot_aberth(a, NITMX), where:
#   a = list/tuple of complex coefficients of polynomial whose
#       roots are to be found such that polynomial is
#       p(x) = a[0] + a[1]*x + ... + a[n]*x**n
#   NITMX (optional) = maximum number of Aberth iterations to make
#                      in case default stop criteria is not satisfied,
#                      by default it is set to 1000
# Function returns list of roots

# ALGORITHM:
# Aberth Method with some modifications as suggested in:
# "Dario Andrea Bini, Numerical Algorithms 13 (1996) 179-200"
# Quadratic, Cubic and Quartic polynomials are handled conventionally

# NOTE:
# You can make your own initial guesses other than default ones
#   by changing "x = init(n, a)" line in the function
# Polynomial coefficients can be zero
# Do not forget to import cmath library

import cmath

def polyroot_aberth(aa, NITMX = 1000):
    ''' (array [, int]) -> list

        To find roots of a 1D polynomial using Aberth Method '''
    def acrc(a):
        ''' To adjust the polynomial coefficients '''
        m = len(a)
        if m < 1:
            return ([], 0)
        i1 = 0
        if a[0] == 0:
            while i1 < m and a[i1] == 0:
                i1 += 1
        if i1 == m:
            return ([], 0)
        i2 = m
        if a[m-1] == 0:
            while i2 > -1 and a[i2-1] == 0:
                i2 -= 1
        return (list(a[i1:i2]), i1)
    def exctpoly(n, a):
        ''' To exactly solve equations upto Quartic '''
        if n < 1:
            return []
        elif n == 1:
            return [-a[0] / a[1]]
        elif n == 2:
            a1 = a[1] * 0.5
            ds = cmath.sqrt(a1 * a1 - a[2] * a[0])
            return [(-a1 + ds) / a[2], (-a1 - ds) / a[2]]
        elif n == 3:
            a13 = a[1] * a[3]
            a22 = a[2] * a[2]
            d0 = a22 - 3 * a13
            d1 = (2 * a22 - 9 * a13) * a[2] + 27 * a[3] * a[3] * a[0]
            if d0 == 0 and d1 == 0:
                tt = -0.3333333333333333 * a[2] / a[3]
                return [tt, tt, tt]
            cd = cmath.sqrt(d1 * d1 - 4 * d0 * d0 * d0)
            if abs(d1 + cd) > abs(d1 - cd):
                cc = ((d1 + cd) * 0.5) ** 0.3333333333333333
            else:
                cc = ((d1 - cd) * 0.5) ** 0.3333333333333333
            u1 = (-0.5+0.8660254037844386j) * cc
            u2 = (-0.5-0.8660254037844386j) * cc
            tt = -0.3333333333333333 / a[3]
            return [tt * (a[2] + cc + d0 / cc), tt * (a[2] + u1 + d0 / u1), tt * (a[2] + u2 + d0 / u2)]
        else:
            a33 = a[3] * a[3]
            a24 = a[2] * a[4]
            a44 = a[4] * a[4]
            p = (a24 - 0.375 * a33) / a44
            q = ((0.125 * a33 - 0.5 * a24) * a[3] + a44 * a[1]) / (a[4] * a44)
            d0 = a[2] * a[2] - 3 * (a[1] * a[3] - 4 * a[0] * a[4])
            d1 = (a[2] * a[2] - 4.5 * (a[3] * a[1] + 8 * a[0] * a[4])) * a[2] + 13.5 * (a[1] * a[1] * a[4] + a[0] * a33)
            if d1 == 0 and d0 == 0:
                if p == 0:
                    b34 = -0.25 * a[3] / a[4]
                    return [b34, b34, b34, b34]
                else:
                    ss = 0.28867513459481288 * cmath.sqrt(-2 * p)
            else:
                qds = cmath.sqrt(d1 * d1 - d0 * d0 * d0)
                if abs(d1 + qds) > abs(d1 - qds):
                    qq = (d1 + qds) ** 0.3333333333333333
                else:
                    qq = (d1 - qds) ** 0.3333333333333333
                ss = 0.28867513459481288 * cmath.sqrt(-2 * p + (qq + d0 / qq) / a[4])
                q1 = qq * (-0.5 + 0.86602540378443865j)
                s1 = 0.28867513459481288 * cmath.sqrt(-2 * p + (q1 + d0 / q1) / a[4])
                if abs(s1) > abs(ss):
                    ss = s1
                q1 = qq * (-0.5 - 0.86602540378443865j)
                s1 = 0.28867513459481288 * cmath.sqrt(-2 * p + (q1 + d0 / q1) / a[4])
                if abs(s1) > abs(ss):
                    ss = s1
            qs = 0.25 * q / ss
            b34 = -0.25 * a[3] / a[4]
            sp = -ss * ss - 0.5 * p
            return [b34 - ss - cmath.sqrt(sp + qs), b34 - ss + cmath.sqrt(sp + qs), b34 + ss - cmath.sqrt(sp - qs), b34 + ss + cmath.sqrt(sp - qs)]
    def pol(n, a, x):
        ''' Ruffini-Horner Rule '''
        p = a[n]
        for i in range(n-1, -1, -1):
            p = p * x + a[i]
        return p
    def st(n, a, x):
        ''' A function needed for stop conditions '''
        ac = []
        for i in range(n+1):
            ac.append(abs(a[i]) * (4 * i + 1))
        return pol(n, ac, x)
    def init(n, a):
        ''' To get initial guess for roots '''
        for i in range(n+1):
            if a[i] == 0:
                a[i] = 2 ** (-53)
        u = [0 for i in range(n+1)]
        tm = abs(a[1] / a[0])
        for i in range(2, n+1):
            tt = abs(a[i] / a[0])
            if tt > tm:
                tm = tt
        u[0] = 1 / (1 + tm)
        for k in range(1, n+1):
            u[k] = abs(a[0] / a[k]) ** (1 / k)
            for i in range(1, k):
                tt = abs(a[i] / a[k]) ** (1 / (k - i))
                if tt > u[k]:
                    u[k] = tt
        v = [0 for i in range(n+1)]
        for k in range(n):
            v[k] = abs(a[k] / a[k+1])
            for i in range(k+2, n+1):
                tt = abs(a[i] / a[k]) ** (1 / (k - i))
                if tt < v[k]:
                    v[k] = tt
        tm = abs(a[0] / a[n])
        for i in range(1, n):
            tt = abs(a[i] / a[n])
            if tt > tm:
                tm = tt
        v[n] = 1 + tm

        k = []
        for i in range(n+1):
            if u[i] <= v[i]:
                k.append(i)
        q = len(k)

        x0 = []
        for i in range(1, q):
            for j in range(1, 1 + k[i] - k[i-1]):
                x0.append(u[k[i]] * cmath.exp((j / (k[i] - k[i-1]) + i / n + 0.1) * cmath.pi * 2j))
        return x0
    def abiter(n, a, x, NITMX):
        ''' Aberth Iterations '''
        mu = 2 ** (-53)
        ar = list(a)
        ar.reverse()
        ap = []
        arp = []
        for i in range(1, n+1):
            ap.append(a[i] * i)
            arp.append(ar[i] * i)
        k = 0
        cc = [True for i in range(n)]
        while True in cc or k < NITMX:
            for i in range(n):
                if cc[i]:
                    if abs(x[i]) > 1:
                        gm = 1 / x[i]
                        pp = gm * (n - gm * pol(n-1, arp, gm) / pol(n, ar, gm))
                    else:
                        pp = pol(n-1, ap, x[i]) / pol(n, a, x[i])
                    sx = 0
                    for j in range(i):
                        sx += 1 / (x[i] - x[j])
                    for j in range(i+1, n):
                        sx += 1 / (x[i] - x[j])
                    x[i] -= 1 / (pp -  sx)
                    if abs(pol(n, a, x[i])) <= mu * st(n, a, abs(x[i])):
                        cc[i] = False
                k += 1
        return x
    (a, i1) = acrc(aa)
    n = len(a) - 1
    if n < 5:
        x = exctpoly(n, a)
    else:
        x = init(n, list(a))
        x = abiter(n, a, x, NITMX)
    return x + [0 for i in range(i1)]

a = (0, 0, 1, -1, 0, 0, 0, 1, 0, 0, 0)
print(polyroot_aberth(a))
