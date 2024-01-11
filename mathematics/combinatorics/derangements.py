# Last updated: 30-Sep-2020
# Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
# Source: https://github.com/udy11, https://gitlab.com/udy11
# Functions to calculate derangements and partial derangements

# Also known as subfactorial, Recontres number and de Montmort number
# Sequence for derangements is OEIS A000166
# Sequence for partial derangements is OEIS A098825

import math
import scipy.special

def derangement(n):
    ''' (int) -> int
        Finds derangements of n objects
        Reference: https://mathworld.wolfram.com/Subfactorial.html
    '''
    if n == 0:
        return 1
    elif n < 19:
        return round(math.factorial(n) / math.e)
    else:
        d0 = round(math.factorial(18) / math.e)
        for k in range(19, n+1):
            d1 = k * d0 + (-1)**k
            d0 = d1
        return d1

def derangement_partial(n, k):
    ''' (int, int) -> int
        Finds partial derangements, number of derangements of n objects
        in which exactly k objects are in place
        Reference: https://mathworld.wolfram.com/PartialDerangement.html
    '''
    if n < k or k == n - 1:
        return 0
    elif n == k:
        return 1
    else:
        return scipy.special.comb(n, k, exact = True) * derangement(n - k)

for n in range(9):
    for k in range(n, -1, -1):
        print(derangement_partial(n, k), end = ' ')
    print()
