# Last updated: 15-Aug-2013
# Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
# Source: https://github.com/udy11, https://gitlab.com/udy11
# Function to calculate Greatest Common Divisor
# (GCD) or Highest Common Factor (HCF) using
# Euclidean's Algorithm

# ALL YOU NEED TO DO:
# Call gcd() function with integers (in any order)

def gcd(a, b):
    ''' (int, int) -> int
        Computes GCD or HCF using Euclidean Algorithm
    '''
    while b != 0:
        c = b
        b = a % c
        a = c
    return a
