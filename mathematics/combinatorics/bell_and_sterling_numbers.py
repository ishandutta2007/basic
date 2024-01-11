# Last updated: 04-Feb-2014
# Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
# Source: https://github.com/udy11, https://gitlab.com/udy11
# Functions to compute Bell Number and (unsigned) Stirling
# Number of First and Second kind

# Bell Number B(n) is defined by:
#   B(0) = 0
#   B(n+1) = sum(C(n, k)*B(k), k=0:n)
#     where C(n,k) is n-choose-k or binomial symbol
# Also defined as sum over Stirling Number of Second Kind:
#   B(n) = sum(s2(n, k), k=0:n)

# Stirling Number of First Kind (unsigned) s1(n, k) defined by:
#   s1(0, 0) = 1
#   s1(n, 0) = s1(0, n) = 0  for n>0
#   s1(n+1, k) = n * s1(n, k) + s1(n, k-1)

# Stirling Number of Second Kind s2(n, k) defined by:
#   s2(0, 0) = 1
#   s2(n, 0) = s1(0, n) = 0  for n>0
#   s2(n+1, k) = k * s2(n, k) + s2(n, k-1)

# ALL YOU NEED TO DO:
# Call function with non-negative n and k

# All functions are coded independent of each other

def belln(n):
    ''' (int) -> int
        Computes Bell Number by computing Bell Triangle

        Pre-condition: n should be non-negative
    '''
    if n == 0:
        return 1
    br1 = [0 for i in range(n)]
    br2 = [0 for i in range(n)]
    br1[0] = 1
    for i in range(n-1):
        br2[0] = br1[i]
        for j in range(1, i+2):
            br2[j] = br2[j-1] + br1[j-1]
        br1 = br2[:]
    return br1[n-1]

def stirl_s1(n, k):
    ''' (int, int) -> int
        Computes unsigned Stirling Number of First Kind
        using recursive relation:
        s(n+1, k) = n * s(n, k) + s(n, k-1)

        Pre-condition: n and k should be non-negative
    '''
    if n == k:
        return 1
    elif n == k+1:
        return k * (k + 1) // 2
    elif n == k+2:
        k2 = k * k
        k3 = k * k2
        k4 = k2 * k2
        return (10 * k + 21 * k2 + 14 * k3 + 3 * k4) // 24
    elif n == k+3:
        t1 = (k + 3) * (k + 2)
        return t1 * t1 * (k+1) * k // 48
    elif k == 0 or k > n:
        return 0
    elif k == 1:
        p = n - 1
        for i in range(2, n-1):
            p = p * i
        return p
    else:
        return (n-1) * stirl_s1(n-1, k) + stirl_s1(n-1, k-1)

def stirl_s2(n, k):
    ''' (int, int) -> int
        Computes Stirling Number of Second Kind
        using recursive relation:
        s(n+1, k) = k * s(n, k) + s(n, k-1)

        Pre-condition: n and k should be non-negative
    '''
    if n == k:
        return 1
    elif n == k+1:
        return k * (k + 1) // 2
    elif k == 0 or k > n:
        return 0
    elif k == 1:
        return 1
    elif k == 2:
        return -1 + 2 ** (n-1)
    elif k == 3:
        return (3 ** (n-1) + 1) // 2 - 2 ** (n-1)
    else:
        return k * stirl_s2(n-1, k) + stirl_s2(n-1, k-1)
