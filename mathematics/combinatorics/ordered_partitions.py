# Last updated: 2020-Sep-12
# Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
# Source: https://github.com/udy11, https://gitlab.com/udy11
# Function to find all ordered partitions of an array

# ALL YOU NEED TO DO:
# Call function orderedpartitions() with any array-type object
# like list, tuple, str, etc.

def orderedpartitions(a):
    ''' (array) -> list(list(array))
        Finds all ordered partitions of a given array
        Array can be any object that has elements like list, tuple, str, etc
        Output is unsorted

        Examples:
        >>> a = 'abcd'
        [['abc', 'd'], ['abcd'], ['ab', 'c', 'd'], ['a', 'bcd'], ['a', 'b', 'cd'], ['a', 'b', 'c', 'd'], ['ab', 'cd'], ['a', 'bc', 'd']]
        >>> a = (6,7,8)
        [[(6,), (7, 8)], [(6,), (7,), (8,)], [(6, 7), (8,)], [(6, 7, 8)]]
    '''
    n = len(a)
    p = {1 : [(1,)]}
    for k in range(2, n+1):
        p[k] = [(k,)]
        for m in range(1, k):
            for p0 in p[m]:
                for p1 in p[k-m]:
                    p[k].append(p0 + p1)
        p[k] = list(set(p[k]))
    pa = []
    for q in p[n]:
        s = []
        i = 0
        for j in q:
            s.append(a[i:i+j])
            i += j
        pa.append(s)
    return pa

if __name__ == '__main__':
    a = 'abcde'
    for b in orderedpartitions(a):
        print(b)
