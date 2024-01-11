# Last updated: 15-Aug-2013
# Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
# Source: https://github.com/udy11, https://gitlab.com/udy11
# Function to get permutations of objects

# Method self-discovered, so there may be better ones

# ALL YOU NEED TO DO:
# Call prmsl() function with a and r
#   where a is list/tuple/array
#   and r is what permutations are required

# Method is to use successive calls of same function
# to populate the list with permutations

# Output is sorted according to indices of a
# Same elements in a are treated as distinct

def prmsl(a, r):
    ''' (list/tuple, int) -> list of list
        Returns r permutations of list/tuple a

        >>> a = [1, 2, 3]; r = 2
        >>> prmsl(a, r)
        [[1, 2], [1, 3], [2, 1], [2, 3], [3, 1], [3, 2]]
    '''
    if r == 1:
        return [[i] for i in a]
    n = len(a)
    if r < 1 or r > n:
        return []
    pt = []
    pts = []
    ss = set([i for i in range(n)])
    sr = set()
    m = 0
    def prms():
        nonlocal pt, pts, ss, sr, m
        if m == 0:
            for k in ss:
                pt = [a[k]]
                m = 1
                sr = set([k])
                prms()
        elif m == r-1:
            for k in ss - sr:
                pts.append(pt + [a[k]])
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
    return pts

a = (1, 2, 3, 4, 5)
print(prmsl(a, 3))
