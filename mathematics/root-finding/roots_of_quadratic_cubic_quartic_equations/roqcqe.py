# Last updated: 08-Mar-2015
# Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
# Source: https://github.com/udy11, https://gitlab.com/udy11
# Functions to solve quadratic, cubic and quartic
# equations with complex coefficients

# ALL YOU NEED TO DO:
# Call qdreqn(a) to solve quadratic equation
#   a[0] + a[1] * x + a[2] * x**2 == 0
#   or cbceqn(a) to solve cubic equation
#   a[0] + a[1] * x + a[2] * x**2 + a[3] * x**3 == 0
#   or qrteqn(a) to solve quartic equation
#   a[0] + a[1] * x + a[2] * x**2 + a[3] * x**3 + a[4] * x**4 == 0
#   where a[i] and x are complex numbers
# Functions return roots as a tuple of complex numbers

# NOTE:
# Do not forget to import cmath library

import cmath

def qdreqn(a):
    ''' (array) -> tuple

    Returns the roots of the quadratic equation
    a[0] + a[1] * x + a[2] * x**2 == 0
    a[i] and x are complex numbers '''
    if len(a) != 3:
        return tuple([])
    if a[2] == 0:
        if a[1] == 0:
            return tuple([])
        else:
            return (-a[0] / a[1], )
    else:
        a1 = a[1] * 0.5
        ds = cmath.sqrt(a1 * a1 - a[2] * a[0])
        return ((-a1 + ds) / a[2], (-a1 - ds) / a[2])

def cbceqn(a):
    ''' (array) -> tuple

    Returns the roots of the cubic equation
    a[0] + a[1] * x + a[2] * x**2 + a[3] * x**3 == 0
    a[i] and x are complex numbers '''
    if len(a) != 4:
        return tuple([])
    if a[3] == 0:
        if a[2] == 0:
            if a[1] == 0:
                return tuple([])
            else:
                return (-a[0] / a[1], )
        else:
            a1 = a[1] * 0.5
            ds = cmath.sqrt(a1 * a1 - a[2] * a[0])
            return ((-a1 + ds) / a[2], (-a1 - ds) / a[2])
    else:
        a13 = a[1] * a[3]
        a22 = a[2] * a[2]
        d0 = a22 - 3 * a13
        d1 = (2 * a22 - 9 * a13) * a[2] + 27 * a[3] * a[3] * a[0]
        if d0 == 0 and d1 == 0:
            tt = -0.3333333333333333 * a[2] / a[3]
            return (tt, tt, tt)
        cd = cmath.sqrt(d1 * d1 - 4 * d0 * d0 * d0)
        if abs(d1 + cd) > abs(d1 - cd):
            cc = ((d1 + cd) * 0.5) ** 0.3333333333333333
        else:
            cc = ((d1 - cd) * 0.5) ** 0.3333333333333333
        u1 = (-0.5+0.8660254037844386j) * cc
        u2 = (-0.5-0.8660254037844386j) * cc
        tt = -0.3333333333333333 / a[3]
        return (tt * (a[2] + cc + d0 / cc), tt * (a[2] + u1 + d0 / u1), tt * (a[2] + u2 + d0 / u2))

def qrteqn(a):
    ''' (array) -> tuple

    Returns the roots of the quartic equation
    a[0] + a[1] * x + a[2] * x**2 + a[3] * x**3 + a[4] ** x**4 == 0
    a[i] and x are complex numbers '''
    if len(a) != 5:
        return tuple([])
    if a[4] == 0:
        if a[3] == 0:
            if a[2] == 0:
                if a[1] == 0:
                    return tuple([])
                else:
                    return (-a[0] / a[1], )
            else:
                a1 = a[1] * 0.5
                ds = cmath.sqrt(a1 * a1 - a[2] * a[0])
                return ((-a1 + ds) / a[2], (-a1 - ds) / a[2])
        else:
            a13 = a[1] * a[3]
            a22 = a[2] * a[2]
            d0 = a22 - 3 * a13
            d1 = (2 * a22 - 9 * a13) * a[2] + 27 * a[3] * a[3] * a[0]
            if d0 == 0 and d1 == 0:
                tt = -0.3333333333333333 * a[2] / a[3]
                return (tt, tt, tt)
            cd = cmath.sqrt(d1 * d1 - 4 * d0 * d0 * d0)
            if abs(d1 + cd) > abs(d1 - cd):
                cc = ((d1 + cd) * 0.5) ** 0.3333333333333333
            else:
                cc = ((d1 - cd) * 0.5) ** 0.3333333333333333
            u1 = (-0.5+0.8660254037844386j) * cc
            u2 = (-0.5-0.8660254037844386j) * cc
            tt = -0.3333333333333333 / a[3]
            return (tt * (a[2] + cc + d0 / cc), tt * (a[2] + u1 + d0 / u1), tt * (a[2] + u2 + d0 / u2))
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
                return (b34, b34, b34, b34)
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
        return (b34 - ss - cmath.sqrt(sp + qs), b34 - ss + cmath.sqrt(sp + qs), b34 + ss - cmath.sqrt(sp - qs), b34 + ss + cmath.sqrt(sp - qs))

print(qdreqn((2, 3-7j, 5j)))
print(cbceqn((9, 0, 3+7j, 2j)))
print(qrteqn((9, 0, 3+7j, 2j, -5-2j)))
