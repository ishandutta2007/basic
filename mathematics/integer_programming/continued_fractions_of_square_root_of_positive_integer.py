# Last updated: 12-Aug-2013
# Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
# Source: https://github.com/udy11, https://gitlab.com/udy11
# Function to calculate continued fraction of square root of a positive integer

# ALL YOU NEED TO DO:
# To calculate continued fractions of sqrt(n), call cfsq(n)
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
    if is_sqrn(r):
        return((round(math.sqrt(r)),[]))
    ss = math.sqrt(r)
    n = int(ss)
    m1 = 1
    p1 = n
    m = p1
    p = r - m * m
    c1 = []
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
    return (int(math.sqrt(r)), c1)
