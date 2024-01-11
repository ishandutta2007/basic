# Last updates: 25-Jul-2018
# Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
# Source: https://github.com/udy11, https://gitlab.com/udy11
# Function to get list of prime factors of a positive integer

# ALL YOU NEED TO DO:
# Before calling the main function pdvsrs(), generate
#   a list of primes prms containing primes more than sqrt
#   of number whose prime factors you want to compute
#   Use the provided function prm_ert_upto_n_lst() for this
#   This step needs to be done only once
# Then simply call pdvsrs() function with the number whose
#   prime factors are required

# It is safe to generate up to sqrt(n) but usually less
# will also work. If it gives error that "index out of range" for
# prms, that means you need to generate more prime numbers.
# Sometimes prime numbers even up to sqrt(n) will also
# not work, in which case make sure to generate one extra
# prime number higher than sqrt(n) (this problem should mathematically
# not be there, but exists due to floating number limitations)

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

def pdvsrs(n):
    ''' (int) -> list of tuple
        To get all prime factors of a positive integer
        The list contains tuples of prime factors and their multiplicities

        It needs prms list containing list of primes at least
        up to sqrt(n) and sometimes one more than that,
        use prm_ert_upto_n_lst() for that before calling this function

        >>> pdvsrs(360)
        [(2, 3), (3, 2), (5, 1)]
    '''
    k = 0
    pdvs = []
    m = n
    while prms[k] <= m:
        if prms[k] > math.ceil(math.sqrt(m)):
            pdvs.append((m, 1))
            return pdvs
        if m % prms[k] == 0:
            m = m // prms[k]
            pc = 1
            while m % prms[k] == 0:
                m = m // prms[k]
                pc += 1
            pdvs.append((prms[k], pc))
        k += 1
    return pdvs

prms = prm_ert_upto_n_lst(10000)
print(pdvsrs(44123*8*121*31))
