# Last updated: 15-Sept-2014
# Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
# Source: https://github.com/udy11, https://gitlab.com/udy11
# Function to sort one-dimensional list using Quicksort

# ALL YOU NEED TO DO:
# Call function quicksort_asc (for ascending) or
#   quicksort_dsc (for descending) with:
#   a = list to be sorted (will be overwritten)

# a can have any type of elements as long as they can be
#   compared with logical operators < and >

# Before using this code, know that Python has inbuilt sorting
#   command and they must be much better

# Time Complexity  ~ O(n.log(n))
# Space Complexity ~ O(n)
# In-Place

def quicksort_asc(a):
    ''' (list) -> none

        Function to sort a one-dimensional list
        in ascending order using Quicksort

        a = list of comparable elements (will be overwritten)
    '''
    def pivot(n1, n2):
        im = n1 + (n2-n1) // 2
        if a[n1] > a[im]:
            if a[n1] > a[n2]:
                if a[im] > a[n2]:
                    return im
                else:
                    return n2
            else:
                return n1
        else:
            if a[im] > a[n2]:
                if a[n1] > a[n2]:
                    return n1
                else:
                    return n2
            else:
                return im
    def fitr(n1, n2, n):
        for i in range(n1, n):
            yield i
        for i in range(n+1, n2+1):
            yield i
    def ritr(n1, n2, n):
        for i in range(n2, n, -1):
            yield i
        for i in range(n-1, n1-1, -1):
            yield i
    def exchng(i1, i2):
        t = a[i1]
        a[i1] = a[i2]
        a[i2] = t
    def qs(n1, n2):
        dn = n2 - n1
        if dn < 1:
            return
        elif dn == 1:
            if a[n1] > a[n2]:
                exchng(n1, n2)
            return
        elif dn == 2:
            nm = n1 + 1
            if a[n1] > a[n2]:
                exchng(n1, n2)
                if a[n1] > a[nm]:
                    exchng(n1, nm)
                elif a[nm] > a[n2]:
                    exchng(n2, nm)
            elif a[n1] > a[nm]:
                exchng(n1, nm)
            elif a[nm] > a[n2]:
                exchng(nm, n2)
            return
        pv = pivot(n1, n2)
        j2 = ritr(n1, n2, pv)
        i2 = n2 + 1
        for i1 in fitr(n1, n2, pv):
            if i1 >= i2:
                if pv < i1:
                    exchng(i1-1, pv)
                    qs(n1, i1-2)
                    qs(i1, n2)
                else:
                    exchng(i1, pv)
                    qs(n1, i1-1)
                    qs(i1+1, n2)
                break
            ch = False
            if a[i1] > a[pv]:
                i2 = next(j2)
                while True:
                    if i1 >= i2:
                        if pv < i1:
                            exchng(i1-1, pv)
                            qs(n1, i1-2)
                            qs(i1, n2)
                        else:
                            exchng(i1, pv)
                            qs(n1, i1-1)
                            qs(i1+1, n2)
                        ch = True
                        break
                    if a[i2] <= a[pv]:
                        exchng(i2, i1)
                        break
                    if i2 <= n1:
                        break
                    i2 = next(j2)
            if ch:
                break
        else:
            exchng(n2, pv)
            qs(n1, n2-1)
    n = len(a)
    qs(0, n-1)
    return

def quicksort_dsc(a):
    ''' (list) -> none

        Function to sort a one-dimensional list
        in descending order using Quicksort

        a = list of comparable elements (will be overwritten)
    '''
    def pivot(n1, n2):
        im = n1 + (n2-n1) // 2
        if a[n1] > a[im]:
            if a[n1] > a[n2]:
                if a[im] > a[n2]:
                    return im
                else:
                    return n2
            else:
                return n1
        else:
            if a[im] > a[n2]:
                if a[n1] > a[n2]:
                    return n1
                else:
                    return n2
            else:
                return im
    def fitr(n1, n2, n):
        for i in range(n1, n):
            yield i
        for i in range(n+1, n2+1):
            yield i
    def ritr(n1, n2, n):
        for i in range(n2, n, -1):
            yield i
        for i in range(n-1, n1-1, -1):
            yield i
    def exchng(i1, i2):
        t = a[i1]
        a[i1] = a[i2]
        a[i2] = t
    def qs(n1, n2):
        dn = n2 - n1
        if dn < 1:
            return
        elif dn == 1:
            if a[n1] < a[n2]:
                exchng(n1, n2)
            return
        elif dn == 2:
            nm = n1 + 1
            if a[n1] < a[n2]:
                exchng(n1, n2)
                if a[n1] < a[nm]:
                    exchng(n1, nm)
                elif a[nm] < a[n2]:
                    exchng(n2, nm)
            elif a[n1] < a[nm]:
                exchng(n1, nm)
            elif a[nm] < a[n2]:
                exchng(nm, n2)
            return
        pv = pivot(n1, n2)
        j2 = ritr(n1, n2, pv)
        i2 = n2 + 1
        for i1 in fitr(n1, n2, pv):
            if i1 >= i2:
                if pv < i1:
                    exchng(i1-1, pv)
                    qs(n1, i1-2)
                    qs(i1, n2)
                else:
                    exchng(i1, pv)
                    qs(n1, i1-1)
                    qs(i1+1, n2)
                break
            ch = False
            if a[i1] < a[pv]:
                i2 = next(j2)
                while True:
                    if i1 >= i2:
                        if pv < i1:
                            exchng(i1-1, pv)
                            qs(n1, i1-2)
                            qs(i1, n2)
                        else:
                            exchng(i1, pv)
                            qs(n1, i1-1)
                            qs(i1+1, n2)
                        ch = True
                        break
                    if a[i2] >= a[pv]:
                        exchng(i2, i1)
                        break
                    if i2 <= n1:
                        break
                    i2 = next(j2)
            if ch:
                break
        else:
            exchng(n2, pv)
            qs(n1, n2-1)
    n = len(a)
    qs(0, n-1)
    return

if __name__ == "__main__":
    a = [7, 5, 4, 2, 12, 9, 8, 3, 10, 1, 11, 6, 0]
    quicksort_asc(a)
    print(a)
