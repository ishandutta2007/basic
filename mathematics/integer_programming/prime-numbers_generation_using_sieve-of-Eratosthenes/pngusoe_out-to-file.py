# Last updated: 13-Apr-2015
# Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
# Source: https://github.com/udy11, https://gitlab.com/udy11
# Function to generate prime numbers upto
# n using the sieve of Eratosthenes

# ALL YOU NEED TO DO:
# Call the function primes_soe_fyl(n, ofln)
# where n is the limit up to
# which primes are needed (inclusive)
# and ofln is the output file name
# The function returns the number of primes
# generated

import math
def primes_soe_fyl(n, ofln):
    ''' (int, str) -> int
        Function to generate list of prime numbers
        using the sieve of Eratosthenes
        Function returns number of primes generated
        n = upto which primes are needed (inclusive)
        ofln = output file name
    '''
    ofl = open(ofln, 'w')
    if n < 2:
        ofl.close()
        return 0
    n2 = (n - 1) // 2
    prms = [2] * (n2 + 1)
    ip = [True for i in range(n2)]
    k = 3
    nsq = round(math.sqrt(n))
    while k <= nsq:
        for i in range(k * k // 2 - 1, n2, k):
            ip[i] = False
        while k <= nsq:
            k += 2
            if ip[k // 2 - 1]:
                break
    m = 1
    ofl.write(str(2) + '\n')
    for i in range(n2):
        if ip[i]:
            ofl.write(str(2 * i + 3) + '\n')
            m += 1
    ofl.close()
    return m

n = 289
ofln = "prms.txt"
print(primes_soe_fyl(n, ofln))
