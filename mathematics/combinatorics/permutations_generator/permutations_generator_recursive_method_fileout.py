# Last updated: 15-Aug-2013
# Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
# Source: https://github.com/udy11, https://gitlab.com/udy11
# Function to get permutations of objects

# Method self-discovered, so there may be better ones

# ALL YOU NEED TO DO:
# Call prmsf() function with a and r
#   where a is list/tuple/array
#   and r is what permutations are required
#   ofln is output file name (will be overwritten)

# Method is to use successive calls of same function
# to populate the list with permutations

# Output is sorted according to indices of a
# Same elements in a are treated as distinct

def prmsf(a, r, ofln):
    ''' (list/tuple, int, str) -> list of list
        Writes r permutations of list/tuple a to file ofln
    '''
    n = len(a)
    if r < 1 or r > n:
        return
    ofl = open(ofln, 'w')
    if r == 1:
        for i in a:
            ofl.write(str([i]) + '\n')
        ofl.close()
        return
    pt = []
    ss = set([i for i in range(n)])
    sr = set()
    m = 0
    def prms():
        nonlocal pt, ss, sr, m
        if m == 0:
            for k in ss:
                pt = [a[k]]
                m = 1
                sr = set([k])
                prms()
        elif m == r-1:
            for k in ss - sr:
                ofl.write(str(pt + [a[k]]) + '\n')
        else:
            for k in ss - sr:
                pt.append(a[k])
                m += 1
                sr = sr.union(set([k]))
                prms()
                sr = sr - set([k])
                m -= 1
                pt = pt[:-1]
    prms()
    ofl.close()

ofln = 'perms.txt'
a = (1, 2, 3, 4, 5)
prmsf(a, 4, ofln)
