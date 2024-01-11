# Last updated: 11-May-2013
# Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
# Source: https://github.com/udy11, https://gitlab.com/udy11
# Functions to calculate Factorial, Permutation,
# Combination and Multinomial Coefficient

# All functions are independent of each other
# They all assume correct input is given
# If incorrect input is given, unexpected results may come

def fct(n):
    ''' (int) -> int
        To calculate factorial defined as:
        F(n) = 1*2*3* ... *n (for n>0)
        F(0) = 1
    '''
    if(n < 2):
        return 1
    f = n
    for i in range(2, n):
        f *= i
    return f

def prm(n, r):
    ''' (int, int) -> int
        To calculate permutation defined as:
        P(n,r) = n!/(n-r)!
    '''
    if(r == 0):
        return 1
    p = n
    for i in range(n - r + 1, n):
        p *= i
    return p

def cmb(n, r):
    ''' (int, int) -> int
        To calculate combination defined as:
        C(n,r) = n!/((n-r)! * r!)
    '''
    if(r > n - r):
        r = n - r
    c = 1
    for i in range(r):
        c = c * (n - i) // (i + 1)
    return c

def mcf(nn):
    ''' (list or tuple of int) -> int
        To calculate Multinomial Coefficient defined as:
        MC(n1, n2, n3...) = (n1 + n2 + n3 + ...)! / ( n1! n2! n3! ...)
    '''
    n = list(nn)
    nl = len(n)
    ns = n[0]
    for i in range(1, nl):
        ns += n[i]
    nm = max(n)
    n.remove(nm)
    mc = ns
    for i in range(nm + 1, ns):
        mc *= i
    for j in n:
        if(j > 1):
            mc //= j
            for i in range(2, j):
                mc //= i
    return mc

print('Factorial(35):',fct(35))
print('Permutation(36, 29):',prm(36, 29))
print('Combination(36, 29):',cmb(36, 29))
print('Multinomial Coefficient(12, 31, 26):',mcf((12, 31, 26)))
