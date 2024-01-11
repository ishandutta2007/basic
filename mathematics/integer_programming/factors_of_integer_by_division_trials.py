# Last updated: 01-Apr-2015
# Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
# Source: https://github.com/udy11, https://gitlab.com/udy11
# Function to get all factors of a positive
# integer using Trial Division method

# ALL YOU NEED TO DO:
# Call the function fctrs_tdm(n) with
# positive integer n, whose factors
# are to be calculated

# NOTE:
# Do not forget to import math library
# Output list is ascendingly sorted and
#   also contains 1 and n
# This is one of the slowest known method, so use
#   another method if you want to get factors of
#   large integers

import math

def fctrs_tdm(n):
    ''' (int) -> list

        Function to get all factors of n using Trial Division method
        Resulting list is ascendingly sorted and also contains 1 and n
    '''
    if n < 1:
        return []
    ch = n == (n >> 1) << 1
    c2 = 1
    while ch:
        c2 += 1
        n = n >> 1
        ch = n == (n >> 1) << 1
    fc = [1, n]
    for i in range(2, 1 + math.ceil(math.sqrt(n))):
        if n % i == 0:
            fc.append(i)
            fc.append(n // i)
    if fc[-1] * fc[-1] == n:
        fc.pop()
    fc2 = list(fc)
    for i in range(1, c2):
        fc2 += [2 ** i * f for f in fc]
    fc2.sort()
    return fc2

for j in range(77, 98):
    print(j, fctrs_tdm(j))
