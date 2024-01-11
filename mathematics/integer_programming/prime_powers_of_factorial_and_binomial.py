# Last updated: 2020-Oct-15
# Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
# Source: https://github.com/udy11, https://gitlab.com/udy11
# Functions to get power of a prime number in factorial and binomial coefficient

# ALL YOU NEED TO DO:
# Call required function with valid inputs

import math

def prime_power_factorial(n, p):
    ''' (int, int) -> int
        Returns power of prime p in n! (factorial of n)
        Input p should be a prime number, otherwise
        incorrect result will be produced
    '''
    if p < 2:
        print('Prime', p, 'should be > 1')
        return False
    elif p > n:
        return 0
    elif p == n:
        return 1
    else:
        k = 0
        s = 0
        while True:
            k += 1
            d = math.floor(n / p ** k)
            if d == 0:
                break
            s += d
        return s

def prime_power_binomial(n, k, p):
    ''' (int, int, int) -> int
        Returns power of prime p in C(n,k)
        Input p should be a prime number, otherwise
        incorrect result will be produced
        Refernce:
        [1] http://www.numbertheory.org/php/binomial.html
        [2] P. Goetgheluck, Computing Binomial Coefficients, American Math. Monthly 94 (1987) 360-365
    '''
    if k > n // 2:
        k = n - k
    if p > n - k:
        return 1
    if p > n // 2:
        return 0
    if p * p > n:
        if n % p < k % p:
            return 1
        else:
            return 0
    e = 0
    r = 0
    while n > 0:
        a = n % p
        n = n / p
        b = k % p + r
        k = k // p
        if a < b:
            e += 1
            r = 1
        else:
            r = 0
    return e

if __name__ == '__main__':
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    print('Prime factorization of 100!')
    for p in primes:
        print((p, prime_power_factorial(100, p)), end = ', ')
    print('\n')
    print('Prime factorization of C(100, 25)')
    for p in primes:
        print((p, prime_power_binomial(100, 51, p)), end = ', ')
    print()
