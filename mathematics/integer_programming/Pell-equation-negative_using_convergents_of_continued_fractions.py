# Last updated: 29-Mar-2015
# Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
# Source: https://github.com/udy11, https://gitlab.com/udy11
# Function to solve Negative Pell's Equation using
# Convergents of Continued Fractions

# Negative Pell's Equation is defined as:
# x**2 - D * y**2 = -1
# whose integer solutions in x and y are seeked for valid positive
# integer D (such D are given by OEIS A031396)

# Method is to calculate continued fraction of sqrt(D)
# Then calculate its convergents and seek fundamental
# solution using them, then construct more solutions out of
# the fundamental solution

# ALL YOU NEED TO DO:
# Call npelleq(D, j) with posiitve non-square integer D
#   and positive integer j for first j solutions

# NOTE
# Don't forget to import math

import math

def is_sqrn(n):
    ''' (int) -> logical
        To check if a non-negative integer n is a square number
        Sq(n) = n * n
    '''
    if n % 4 == 0 or n % 8 == 1:
        r = round(math.sqrt(n))
        if r * r == n:
            return True
    return False

def cfsq(r):
    ''' (int) -> tuple
    Returns Continued Fractions of sqrt(r)
    Assumes input to be positive integer
    '''
    ss = math.sqrt(r)
    n = int(ss)
    m1 = 1
    p1 = n
    m = p1
    p = r - m * m
    c1 = [n]
    w = []
    while True:
        if [m1, p1] in w:
            break
        else:
            w.append([m1, p1])
        s = (ss + m) / p
        n = int(s)
        m1 = p
        p1 = (p * n - m)
        m = p1
        p = (r - m * m) // m1
        c1.append(n)
    return (c1[0], c1[1:])

def npf(x, y, D):
    ''' (int, int, int) -> logical
        Returns true if parameters satisfy Negative Pell's Equation
    '''
    return D * y * y - x * x == 1

def npelleq(m, j):
    ''' (int, int) -> list of tuple
        Solves Negative Pell's Equation using
        Convergents of Continued Fractions
        Returns list of tuple of first j solutions of the equation
    '''
    if is_sqrn(m):
        return
    b = cfsq(m)
    n = len(b[1])
    if n % 2 == 0:
        return
    x = [b[0], 0, 0]
    y = [1, 0, 0]
    if npf(x[0], y[0], m):
        xf = x[0]
        yf = y[0]
    elif n > 0:
        x[1] = b[0] * b[1][0] + 1
        y[1] = b[1][0]
        if npf(x[1], y[1], m):
            xf = x[1]
            yf = y[1]
        elif n > 1:
            k = 1
            while True:
                kk = k % n
                x[2] = b[1][kk] * x[1] + x[0]
                y[2] = b[1][kk] * y[1] + y[0]
                if npf(x[2], y[2], m):
                    xf = x[2]
                    yf = y[2]
                    break
                else:
                    x[0] = x[1]; x[1] = x[2]
                    y[0] = y[1]; y[1] = y[2]
                    k += 1
    sol = []
    for i in range(1, 2*j+1, 2):
        t1 = xf ** i
        xa = t1
        ya = 0
        k = 0
        while k < i + 1:
            t1 = t1 * (i - k) * yf // (k + 1) // xf
            ya += t1
            k += 1
            if k > i:
                break
            t1 = t1 * (i - k) * yf * m // (k + 1) // xf
            xa += t1
            k += 1
        sol.append((xa, ya))
    return sol

print(npelleq(2, 10))
