# Last updated: 13-Sept-2014
# Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
# Source: https://github.com/udy11, https://gitlab.com/udy11
# Function to sort one-dimensional list using Merge Sort

# ALL YOU NEED TO DO:
# Call function merge_sort_asc (for ascending) or
#   merge_sort_dsc (for descending) with:
#   a = list to be sorted (will be overwritten)

# a can have any type of elements as long as they can be
#   compared with logical operators < and >

# Before using this code, know that Python has inbuilt sorting
#   command and they must be much better

# Time Complexity  = O(n.log(n))
# Space Complexity = O(n)
# Not In-Place

def merge_sort_asc(a):
    ''' (list) -> none

        Function to sort a one-dimensional list
        in ascending order using Merge Sort.

        a = list of comparable elements (will be overwritten)
    '''
    n = len(a)
    if n < 2:
        return
    b = list(a)
    j = 0
    while j < n - 1:
        if a[j] > a[j+1]:
            b[j] = a[j+1]
            b[j+1] = a[j]
        else:
            b[j] = a[j]
            b[j+1] = a[j+1]
        j += 2
    sw = False
    m = 2
    while m < n:
        if sw:
            i1 = 0
            while i1 < n:
                i2 = i1 + m
                if i2 >= n:
                    b[i1:n] = a[i1:n]
                    break
                if i2 + m > n:
                    j0 = n
                else:
                    j0 = i1 + 2 * m
                j = i1
                i10 = i1 + m
                while j < j0:
                    if a[i1] < a[i2]:
                        b[j] = a[i1]
                        i1 += 1
                    else:
                        b[j] = a[i2]
                        i2 += 1
                    j += 1
                    if i1 >= i10:
                        b[j:j0] = a[i2:j0]
                        break
                    if i2 >= j0:
                        b[j:j0] = a[i1:i10]
                        break
                i1 = j0
            sw = False
            m *= 2
        else:
            i1 = 0
            while i1 < n:
                i2 = i1 + m
                if i2 >= n:
                    a[i1:n] = b[i1:n]
                    break
                if i2 + m > n:
                    j0 = n
                else:
                    j0 = i1 + 2 * m
                j = i1
                i10 = i1 + m
                while j < j0:
                    if b[i1] < b[i2]:
                        a[j] = b[i1]
                        i1 += 1
                    else:
                        a[j] = b[i2]
                        i2 += 1
                    j += 1
                    if i1 >= i10:
                        a[j:j0] = b[i2:j0]
                        break
                    if i2 >= j0:
                        a[j:j0] = b[i1:i10]
                        break
                i1 = j0
            sw = True
            m *= 2
    if not sw:
        a = list(b)
    return

def merge_sort_dsc(a):
    ''' (list) -> none

        Function to sort a one-dimensional list
        in descending order using Merge Sort.

        a = list of comparable elements (will be overwritten)
    '''
    n = len(a)
    if n < 2:
        return
    b = list(a)
    j = 0
    while j < n - 1:
        if a[j] < a[j+1]:
            b[j] = a[j+1]
            b[j+1] = a[j]
        else:
            b[j] = a[j]
            b[j+1] = a[j+1]
        j += 2
    sw = False
    m = 2
    while m < n:
        if sw:
            i1 = 0
            while i1 < n:
                i2 = i1 + m
                if i2 >= n:
                    b[i1:n] = a[i1:n]
                    break
                if i2 + m > n:
                    j0 = n
                else:
                    j0 = i1 + 2 * m
                j = i1
                i10 = i1 + m
                while j < j0:
                    if a[i1] > a[i2]:
                        b[j] = a[i1]
                        i1 += 1
                    else:
                        b[j] = a[i2]
                        i2 += 1
                    j += 1
                    if i1 >= i10:
                        b[j:j0] = a[i2:j0]
                        break
                    if i2 >= j0:
                        b[j:j0] = a[i1:i10]
                        break
                i1 = j0
            sw = False
            m *= 2
        else:
            i1 = 0
            while i1 < n:
                i2 = i1 + m
                if i2 >= n:
                    a[i1:n] = b[i1:n]
                    break
                if i2 + m > n:
                    j0 = n
                else:
                    j0 = i1 + 2 * m
                j = i1
                i10 = i1 + m
                while j < j0:
                    if b[i1] > b[i2]:
                        a[j] = b[i1]
                        i1 += 1
                    else:
                        a[j] = b[i2]
                        i2 += 1
                    j += 1
                    if i1 >= i10:
                        a[j:j0] = b[i2:j0]
                        break
                    if i2 >= j0:
                        a[j:j0] = b[i1:i10]
                        break
                i1 = j0
            sw = True
            m *= 2
    if not sw:
        a = list(b)
    return

if __name__ == "__main__":
    a = [5, 9, 4, 8, 7, 0, 1, 6, 3, 2]
    merge_sort_asc(a)
    print(a)
