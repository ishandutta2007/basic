# Last updated: 15-Aug-2013
# Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
# Source: https://github.com/udy11, https://gitlab.com/udy11
# Function to get combinations of objects

# Method self-discovered, so there may be better ones

# ALL YOU NEED TO DO:
# Call cmbsf() function with a, r and ofln
#   where a is list/tuple/array
#   r is what combinations are required
#   ofln is output file name (will be overwritten)

# Method is to use successive calls of same function
# to populate the list with combinations

# Output is sorted according to indices of a
# Same elements of a are treated as distinct

def cmbsf(a, r, ofln):
    ''' (list/tuple, int, str) -> list of list
        Writes r combinations of list/tuple a to file ofln
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
    ct = []
    m = 0
    i = 0
    def cmbs():
        nonlocal m, ct, i
        if m == 0:
            for k in range(n-r+2):
                i = k
                ct = [a[k]]
                m = 1
                cmbs()
        elif m == r-1:
            for k in range(i+1, n):
                ofl.write(str(ct + [a[k]]) + '\n')
        else:
            for k in range(i+1, n):
                i = k
                ct.append(a[k])
                m += 1
                cmbs()
                ct = ct[:-1]
                m -= 1
    cmbs()
    ofl.close()

if __name__ == '__main__':
    ofln = 'combs.txt'
    a = (1, 2, 3, 4, 5, 6)
    cmbsf(a, 3, ofln)
