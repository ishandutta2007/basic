# Last updated: 2020-Oct-29
# Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
# Source: https://github.com/udy11, https://gitlab.com/udy11
# Functions to find Modular Inverse

# Prefer inbuilt function pow()

# Reference:
# https://www.geeksforgeeks.org/multiplicative-inverse-under-modulo-m/

def modinverse_eea(a, b):
    ''' (int, int) -> int
        Finds Modular Inverse a**-1 (mod b) using Extended
        Euclidean Algorithm. Assumes a and b to be co-prime
    '''
    g = a
    b0 = b
    qq = []
    while b0 != 0:
        t = b0
        b0 = g // t
        qq.append(b0)
        b0 = g - b0 * t
        g = t
    s0 = 1; s1 = 0
    t0 = 0; t1 = 1
    for q in qq:
        t = s1
        s1 = s0 - q * t
        s0 = t
        t = t1
        t1 = t0 - q * t
        t0 = t
    return s0 % b

def modinverse_flt(a, b):
    ''' (int, int) -> int
        Finds Modular Inverse a**-1 (mod b) using inbuilt
        function pow() and Fermat's Little Theorem
    '''
    return pow(a, b-2, mod = b)

def modinverse_pow(a, b):
    ''' (int, int) -> int
        Finds Modular Inverse a**-1 (mod b) using inbuilt
        function pow()
    '''
    return pow(a, -1, mod = b)

if __name__ == '__main__':
    import time
    m = 10**9 + 7
    n = 2 * 10**5

    tym0 = time.time()
    for i in range(1, n):
        modinverse_eea(i, m)
    print('Time taken by modinverse_eea():', time.time() - tym0, 's')

    tym0 = time.time()
    for i in range(1, n):
        modinverse_flt(i, m)
    print('Time taken by modinverse_flt():', time.time() - tym0, 's')

    tym0 = time.time()
    for i in range(1, n):
        modinverse_pow(i, m)
    print('Time taken by modinverse_pow():', time.time() - tym0, 's')
