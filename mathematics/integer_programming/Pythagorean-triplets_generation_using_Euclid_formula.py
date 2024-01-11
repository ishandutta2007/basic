# Last updated: 21-Oct-2015
# Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
# Source: https://github.com/udy11, https://gitlab.com/udy11
# Functions to generate Pythagorean Triplets
# using Euclid's Formula

# Euclid's Formula is that for any positive integers m and n (m>n):
# the triplet (m**2 - n**2, 2*m*n, m**2 + n**2) is a
# Pythagorean Triplet. However, this formula does not produce
# all triplets for all values of m and n.
# To get all "primitive" triplets, we need that
# m>n, gcd(m,n)=1, m-n is odd
# and from these primitive triplets, one can get
# rest of the triplets by multiplying a factor k

# ALL YOU NEED TO DO:
# Call one of the pgts functions with required inputs:
#   Call pgts_1(m1, n1, k1) where m1, n1 and k1
#     are limits of m, n and k as described above,
#     these limits are not inclusive (as python's convention);
#     and so to get primitive triplets only, pass k1 = 2
#   Call pgts_h(hmx, ip) where hmx is limit on hypotenuse,
#     this limit is not inclusive (as python's convention),
#     and ip is (optional) logical variable, set it True if you
#     only want primitive triplets
#   Call pgts_p(pmx, ip) where pmx is limit on perimeter,
#     this limit is not inclusive (as python's convention),
#     and ip is (optional) logical variable, set it True if you
#     only want primitive triplets
#   Call pgts_a(amx, ip) where amx is limit on area,
#     this limit is not inclusive (as python's convention),
#     and ip is (optional) logical variable, set it True if you
#     only want primitive triplets

# NOTE:
# The output is not sorted
# int() is used on floats to determine some limits within
#   function, so it is possible limits to be incorrectly
#   calculated due to roundoff error; such an error occurs
#   in pgts_a() for amx = 31; if required, one can get rid
#   of such errors by checking difference between the
#   calculated float and its rounded integer, if difference
#   is very low (< 1.e-13 or so), then one can take rounded
#   number as limit instead of its int() value

import math

def gcd(a, b):
    ''' (int, int) -> int
        Computes GCD or HCF using Euclidean Algorithm
    '''
    while b != 0:
        c = b
        b = a % c
        a = c
    return a

def pgts_1(m1, n1, k1):
    ''' (int, int, int) -> list of tuples
        Generates all Pythagorean Triplets using
        Euclid's Formula upto some limit
    '''
    ptl = []
    for n in range(1, n1):
        for m in range(n+1, m1, 2):
            if gcd(n, m) == 1:
                k = 1
                for k in range(1, k1):
                    m2 = m * m
                    n2 = n * n
                    ptl.append((k * (m2 - n2), 2 * k * m * n, k * (m2 + n2)))
    return ptl

def pgts_h(hmx, ip = False):
    ''' (int) -> list of tuples
        Generates all Pythagorean Triplets using
        Euclid's Formula upto given limit of hypotenuse
    '''
    ptp = []
    mmx = int(math.sqrt(hmx - 2)) + 1
    for m in range(1, mmx, 2):
        for n in range(2, min(m, 1 + int(math.sqrt(hmx - 1 - m * m))), 2):
            if gcd(n, m) == 1:
                m2 = m * m
                n2 = n * n
                ptp.append((m2 - n2, 2 * m * n, m2 + n2))
    for m in range(2, mmx, 2):
        for n in range(1, min(m, 1 + int(math.sqrt(hmx - 1 - m * m))), 2):
            if gcd(n, m) == 1:
                m2 = m * m
                n2 = n * n
                ptp.append((m2 - n2, 2 * m * n, m2 + n2))
    if ip:
        return ptp
    ptl = []
    for pt in ptp:
        k = 2
        p2 = k * pt[2]
        while p2 < hmx:
            ptl.append((k * pt[0], k * pt[1], p2))
            k += 1
            p2 = k * pt[2]
    return ptp + ptl

def pgts_p(pmx, ip = False):
    ''' (int) -> list of tuples
        Generates all Pythagorean Triplets using
        Euclid's Formula upto given limit of perimeter
    '''
    ptp = []
    mmx = int(0.5 * (math.sqrt(2 * pmx - 1) - 1)) + 1
    for m in range(1, mmx, 2):
        for n in range(2, min(m, 1 + int(0.5 * (pmx - 1) / m - m)), 2):
            if gcd(n, m) == 1:
                m2 = m * m
                n2 = n * n
                ptp.append((m2 - n2, 2 * m * n, m2 + n2))
    for m in range(2, mmx, 2):
        for n in range(1, min(m, 1 + int(0.5 * (pmx - 1) / m - m)), 2):
            if gcd(n, m) == 1:
                m2 = m * m
                n2 = n * n
                ptp.append((m2 - n2, 2 * m * n, m2 + n2))
    if ip:
        return ptp
    ptl = []
    for pt in ptp:
        k = 2
        pp = k * sum(pt)
        while pp < pmx:
            ptl.append((k * pt[0], k * pt[1], k * pt[2]))
            k += 1
            pp = k * sum(pt)
    return ptp + ptl

def pgts_a(amx, ip = False):
    ''' (int) -> list of tuples
        Generates all Pythagorean Triplets using
        Euclid's Formula upto given limit of area
    '''
    ptp = []
    a = amx - 1
    nmx = int((-1+(18*a+math.sqrt(-3+324*a**2))**(1/3)/3**(2/3)+(54*a+3*math.sqrt(-3+324*a**2))**(-1/3))*0.5)
    for n in range(1, 1 + nmx):
        mmx = int((24**(1/3)*n**4+2**(1/3)*(n**2*(9*a+math.sqrt(81*a**2-12*n**8)))**(2/3))/(6**(2/3)*n**(5/3)*(9*a+math.sqrt(81*a**2-12*n**8))**(1/3)))
        for m in range(n + 1, 1 + mmx, 2):
            if gcd(n, m) == 1:
                m2 = m * m
                n2 = n * n
                ptp.append((m2 - n2, 2 * m * n, m2 + n2))
    if ip:
        return ptp
    ptl = []
    for pt in ptp:
        k = 2
        pa = 0.5 * pt[0] * pt[1] * k * k
        while pa < amx:
            ptl.append((k * pt[0], k * pt[1], k * pt[2]))
            k += 1
            pa = 0.5 * pt[0] * pt[1] * k * k
    return ptp + ptl

# Pythagorean Triplets with limits in m, n and k
pgs = pgts_1(5, 5, 3)
print(pgs)

# Pythagorean Triplets with limit in hypotenuse
pgs = pgts_h(30)
print(pgs)

# Pythagorean Triplets with limit in perimeter
pgs = pgts_p(60)
print(pgs)

# Pythagorean Triplets with limit in area
pgs = pgts_a(100)
print(pgs)
