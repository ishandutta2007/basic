# Last updated: 08-May-2013
# Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
# Source: https://github.com/udy11, https://gitlab.com/udy11
# Function to get all permutations of a list (maximum 20)

# Permutations of list objects (max 20)
# Technique is to appropriately swap entries in input array
# Method self-discovered (hence many improvements will follow soon)

# In case some input are same, they will still be treated as distinct
# and their repeatation will be reflected in the output

# ALL YOU NEED TO DO:
# Call function perms_file with:
#   ofln, output file name
#   a as list of objects to be permuted

# The output is not sorted
# Program will become terribly slow for list size more than 9

def swaps(a, ac):
    ''' (list, list) -> list
        Performs swap of list a based on list ac.
        The nth entry of ac decides where to swap
        the nth entry of list a. '''
    b = list(a)
    j = 0
    for i in ac:
        if i:
            t = b[j]
            b[j] = b[j + i]
            b[j + i] = t
        j += 1
    return b

def fctrl(n):
    ''' (int) -> int
        Function to calculate Factorial.
        Assumes non-negative input. '''
    if n<2:
        return 1
    fc = 2
    for i in range(3,n+1):
        fc *= i
    return fc

def perms_file(ofln, aa):
    ''' (str, list) -> int
        Writes all permutations of objects in the list aa
        in file specified by ofln.
        Function returns the total number of permutations,
        i.e. factorial of len(aa).
        Repeated entries in list aa are treated as distinct.'''
    n = len(aa) - 1
    a = [i for i in range(n+1)]
    nf = [1]
    for i in range(2, n + 1):
        nf = [fctrl(i)] + nf
    an = list(a)
    ac = [0 for j in range(n)]
    n1f = nf[0] * (n+1)
    ofl = open(ofln, 'w')
    for i in aa:
        ofl.write(str(i) + ' ')
    ofl.write('\n')
    for m in range(1, n1f):
        for j in range(n):
            mq = m // nf[j]
            ac[j] = mq
            m -= mq * nf[j]
        an = swaps(aa, ac)
        for i in an:
            ofl.write(str(i) + ' ')
        ofl.write('\n')
    ofl.close()
    return n1f

ofln = 'permutations.txt'
a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
perms_file(ofln, a)
