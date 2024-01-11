# Last updated: 07-Jun-2013
# Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
# Source: https://github.com/udy11, https://gitlab.com/udy11
# Function to binary search a number in a sorted array

# ALL YOU NEED TO DO:
# Call function bsa(a, n1, n2, b) with:
#   a = numerical array in which a number to be searched
#   n1 = first index from which to begin search (inclusive)
#   n2 = last index upto which search is to be made (not inclusive)
#   b = number to be searched
# NOTE that index n2 is not included in the search

# OUTPUT:
# Output of the functions is the index of number to be searched
# If the number does not exist in the array, None is returned

# For ascendingly sorted array
def bsa_asc(a, n1, n2, b):
    if b > a[n2 - 1]:
        return  # Not Found
    if b < a[n1]:
        return  # Not Found
    nd = n2 - n1
    nm = n1 + nd // 2
    while nd > 1:
        if a[nm] > b:
            n2 = nm
        else:
            n1 = nm
        nd = n2 - n1
        nm = n1 + nd // 2
    if a[n1] == b:
        return n1
    elif a[n2] == b:
        return n2
    else:
        return  # Not Found

# For descendingly sorted array
def bsa_dec(a, n1, n2, b):
    if b < a[n2 - 1]:
        return  # Not Found
    if b > a[n1]:
        return  # Not Found
    nd = n2 - n1
    nm = n1 + nd // 2
    while nd > 1:
        if a[nm] < b:
            n2 = nm
        else:
            n1 = nm
        nd = n2 - n1
        nm = n1 + nd // 2
    if a[n1] == b:
        return n1
    elif a[n2] == b:
        return n2
    else:
        return  # Not Found

a = [11 + i * 0.1 for i in  range(1000)]
b = 101.7

print(bsa_asc(a, 0, 1000, b))
a.reverse()
print(bsa_dec(a, 0, 1000, b))
