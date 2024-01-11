# Last updated: 24-may-2013
# Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
# Source: https://github.com/udy11, https://gitlab.com/udy11
# Functions to list Prime Numbers
# using divisibility checking method

import math
def prm_upto_n(n):
    ''' (int) -> list
        Returns the list of prime numbers upto n (inclusive)
    '''
    np = [2, 3]
    k = 2
    for i in range(5, n + 1, 2):
        c = True
        j = 0
        while np[j] <= math.sqrt(i * 1.0):
            if i % np[j] == 0:
                c = False
                break
            j += 1
        if c:
            k += 1
            np.append(i)
    print('Listed', k, 'primes')
    return np

def prm_n(n):
    ''' (int) -> list
        Returns the list of n prime numbers
    '''
    np = [0 for i in range(n)]
    np[0] = 2
    np[1] = 3
    k = 1
    i = 5
    while(k < n - 1):
        c = True
        j = 0
        while np[j] <= math.sqrt(i * 1.0):
            if i % np[j] == 0:
                c = False
                break
            j += 1
        if c:
            k += 1
            np[k] = i
        i += 2
    print('Listed primes upto', np[-1])
    return np

print(prm_upto_n(31))
print(prm_n(31))
