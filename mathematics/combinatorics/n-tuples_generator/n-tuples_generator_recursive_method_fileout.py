# Last updated: 15-Aug-2013
# Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
# Source: https://github.com/udy11, https://gitlab.com/udy11
# Function to get n-tuples of objects

# Method self-discovered, so there may be better ones

# ALL YOU NEED TO DO:
# Call ntpsf() function with a, r and ofln
#   where a is list/tuple/array
#   and r is what r-tuples are required
#   ofln is output file name (will be overwritten)

# Method is to use successive calls of same function
# to populate the list with n-tuples

# Output is sorted according to indices of a
# Same elements of a are treated as distinct

def ntpsf(a, r, ofln):
    ''' (list/tuple, int, str) -> list of list
        Writes r-tuples of list/tuple a to file ofln
    '''
    n = len(a)
    if r < 1 or r > n:
        return 0
    ofl = open(ofln, 'w')
    if r == 1:
        for i in a:
            ofl.write(str([i]) + '\n')
        ofl.close()
        return n
    ct = []
    m = 0
    def ntps():
        nonlocal m, ct
        if m == 0:
            for k in range(n):
                ct = [a[k]]
                m = 1
                ntps()
        elif m == r-1:
            for k in range(n):
                ofl.write(str(ct + [a[k]]) + '\n')
        else:
            for k in range(n):
                ct.append(a[k])
                m += 1
                ntps()
                ct = ct[:-1]
                m -= 1
    ntps()
    ofl.close()
    return n ** r

ofln = 'ntpls.txt'
a = (1, 2, 3, 4, 5)
ntpsf(a, 3, ofln)
