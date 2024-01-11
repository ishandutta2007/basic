# Last updated: 13-Feb-2014
# Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
# Source: https://github.com/udy11, https://gitlab.com/udy11
# Function to calculate Integer Partition

# Integer Partition is defined as number of ways an integer n > 0:
# can be written as sums of positive integers.
# (For 0, it is defined to be 1)

# Algorithm uses recurrence relation from
# Euler's Pentagonal Number Theorem:
# p(n) = Sum[ (-1)**j (p(n- j(3j-1)/2) + p(n- j(3j+1)/2)) ]
# until p(0) or p(n-1) are hit in summation
# where p(n) is integer partition

# Sequence A000041 on OEIS

# ALL YOU NEED TO DO:
# Call function intpart(m) with non-negative integer m.

# NOTE:
# Function may not calculate for high input (e.g. above
# 1986 on my machine) due to recursion depth restrictions
# in python. To change the limit use the command
#   sys.setrecursionlimit(limit)
# Use it at your own risk

def intpart(m):
    ''' (int) -> int
        Function to calculate Integer Partitions
        using recurrence relation
        from Euler's Pentagonal Number Theorem:
        p(n) = Sum[ (-1)**j (p(n- j(3j-1)/2) + p(n- j(3j+1)/2)) ]
        until p(0) or p(n-1) are hit in summation
        where p(n) is integer partition

        Generates OEIS A000041
    '''
    if m == 0:
        return 1
    elif m < 4:
        return m
    t = [0 for i in range(m+1)]
    t[0] = 1
    for i in range(1, 4):
        t[i] = i
    def p(n):
        nonlocal t
        if t[n] != 0:
            return t[n]
        else:
            ps = 0
            j = 1
            jp = 2
            while jp <= n:
                ps += (-1)**(j+1) * p(n - jp)
                j += 1
                jp = j * (3*j+1) // 2
            j = 1
            jn = 1
            while jn <= n:
                ps += (-1)**(j+1) * p(n - jn)
                j += 1
                jn = j * (3*j-1) // 2
            t[n] = ps
            return ps
    return p(m)

## import sys
## sys.setrecursionlimit(2000)

for i in range(41):
    print(i, intpart(i))
