# Last updated: 15-Aug-2013
# Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
# Source: https://github.com/udy11, https://gitlab.com/udy11
# Function to get combinations of objects

# Method self-discovered, so there may be better ones

# ALL YOU NEED TO DO:
# Call cmbsl() function with a and r
#   where a is list/tuple/array
#   and r is what combinations are required

# Method is to use successive calls of same function
# to populate the list with combinations

# Output is sorted according to indices of a
# Same elements of a are treated as distinct

def cmbsl(a, r):
    ''' (list/tuple, int) -> list of list
        Returns r combinations of list/tuple a

        >>> a = [1, 2, 3, 4]; r = 3
        >>> cmbsl(a, r)
        [[1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4]]
    '''
    if r == 1:
        return [[i] for i in a]
    n = len(a)
    if r < 1 or r > n:
        return []
    ct = []
    cm = []
    m = 0
    i = 0
    def cmbs():
        nonlocal m, ct, cm, i
        if m == 0:
            for k in range(n-r+2):
                i = k
                ct = [a[k]]
                m = 1
                cmbs()
        elif m == r-1:
            for k in range(i+1, n):
                cm.append(ct + [a[k]])
        else:
            for k in range(i+1, n):
                i = k
                ct.append(a[k])
                m += 1
                cmbs()
                ct = ct[:-1]
                m -= 1
    cmbs()
    return cm

if __name__ == '__main__':
    a = (1, 2, 3, 4, 5, 6)
    print(cmbsl(a, 3))
