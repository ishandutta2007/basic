# Last updated: 17-Aug-2019
# Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
# Source: https://github.com/udy11, https://gitlab.com/udy11
# Function to get all factors of a positive
# integer by finding prime factors

# ALL YOU NEED TO DO:
# Before calling the main function fctrs_fpf(), generate
#   a list of primes prms containing primes more than sqrt
#   of number whose prime factors you want to compute
#   Use the provided function prm_ert_upto_n_lst() for this
#   This step needs to be done only once
# Then simply call pdvsrs() function with the number whose
#   prime factors are required

# NOTE:
# Do not forget to import math library
# Output list is ascendingly sorted and
#   also contains 1 and n
# It is safe to generate up to sqrt(n) but usually less
#   will also work. If it gives error that "index out of range" for
#   prms, that means you need to generate more prime numbers.
#   Sometimes prime numbers even up to sqrt(n) will also
#   not work, in which case make sure to generate one extra
#   prime number higher than sqrt(n) (this problem should mathematically
#   not be there, but exists due to floating number limitations)
# It uses recursion to generate n-tuples of prime factors to find all
#   factors, during which it uses "nonlocal" command that might not work
#   in Python 2, though an alternative of nonlocal should fix this

import math

def prm_ert_upto_n_lst(n):
    ''' (int) -> list of int
        Function to generate list of prime numbers
        using Sieves of Eratosthenes
        n = upto which primes are needed (inclusive)
    '''
    np = [2 for i in range(n)]
    ip = [True for i in range(n)]
    ip[0] = False
    ip[1] = True
    for i in range(3, n, 2):
        ip[i] = False
    k = 3
    nsq = math.sqrt(n)
    while k < nsq:
        for j in range(k*k - 1, n, k):
            ip[j] = False
        while k < nsq:
            k += 2
            if ip[k - 1]:
                break
    m = 1
    np[0] = 2
    for i in range(2, n, 2):
        if ip[i]:
            np[m] = i + 1
            m += 1
    return np[:m]

def prdc(aa):
    ''' Returns Product of all elements in input array aa '''
    p = 1
    for a in aa:
        p *= a
    return p

def fctrs_fpf(n0):
    ''' (int) -> tuple
        To get all factors of a positive integer

        It needs prms list containing list of primes at least
        up to sqrt(n) and sometimes one more than that,
        use prm_ert_upto_n_lst() for that before calling this function

        >>> fctrs_fpf(36)
        [1, 2, 3, 4, 6, 9, 12, 18, 36]
    '''
    def ntps():
        nonlocal m, ct, nt
        if m == 0:
            for k in range(ne[0]):
                ct = [es[0][k]]
                m = 1
                ntps()
        elif m == r-1:
            for k in range(ne[r-1]):
                nt.append(prdc(ct + [es[r-1][k]]))
        else:
            for k in range(ne[m]):
                ct.append(es[m][k])
                m += 1
                ntps()
                ct = ct[:-1]
                m -= 1
    nprms = len(prms)
    k = 0
    pdvs = []
    n = n0
    while k < nprms and prms[k] <= n:
        if n % prms[k] == 0:
            n = n // prms[k]
            pc = 1
            while n % prms[k] == 0:
                n = n // prms[k]
                pc += 1
            pdvs.append((prms[k], pc))
        k += 1
    if n > 1:
        pdvs.append((n, 1))
    r = len(pdvs)
    if r == 1:
        return [pdvs[0][0] ** i for i in range(pdvs[0][1] + 1)]
    elif r == 0:
        return [1]
    es = [[p[0] ** i for i in range(p[1] + 1)] for p in pdvs]
    ne = [len(e) for e in es]
    ct = []
    nt = []
    m = 0
    ntps()
    return sorted(nt)

prms = prm_ert_upto_n_lst(11)
print(fctrs_fpf(16*27*49*11))
