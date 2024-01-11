# Last updated: 17-Aug-2019
# Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
# Source: https://github.com/udy11, https://gitlab.com/udy11
# Function to calculate Greatest Common Divisor
# (GCD) or Highest Common Factor (HCF) using
# Binary GCD Algorithm or Stein's Algorithm

# ALL YOU NEED TO DO:
# Call bgcd() function with two non-negative integers (in any order)

def bgcd(a, b):
    ''' (int, int) -> int
        Computes GCD or HCF using Binary GCD/Stein's Algorithm
    '''
    if a == 0:
        return b
    if b == 0:
        return a
    k = 0
    while (a | b) & 1 == 0:
        a >>= 1
        b >>= 1
        k += 1
    while a & 1 == 0:
        a >>= 1
    while b != 0:
        while b & 1 == 0:
            b >>= 1
        if a > b:
            t = b
            b = a
            a = t
        b -= a
    return a << k
