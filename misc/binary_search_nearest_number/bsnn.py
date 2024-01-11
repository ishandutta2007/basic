# Last updated: 04-Jan-2024
# Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
# Source: https://github.com/udy11, https://gitlab.com/udy11
# Function to binary search nearest number in a sorted array

# ALL YOU NEED TO DO:
# Call function binarySearchNN(a, x) with:
#   a = numerical array in which nearest number to be searched
#   x = number whose nearest index to be searched

# OUTPUT:
# Output of the functions is the index of number to be searched

# NOTE:
# If x is at the center of two indices, output will be the left index

def binarySearchNN(a, x):
    ''' (array, num) -> int
        Binary Search Nearest Number in a sorted Array of real numbers
    '''
    na = len(a)
    if na < 2:
        return 0
    i0 = 0
    i1 = na - 1
    asc = -1 + 2 * (a[1] > a[0])    # 1 if ascending, -1 if descending
    while i1 - i0 > 1:
        im = (i0 + i1) // 2
        dx = asc * (x - a[im])
        if dx > 0:
            i0 = im
        elif dx < 0:
            i1 = im
        else:
            return im
    if asc * (a[i0] + a[i1] - 2*x) >= 0:
        return i0
    else:
        return i1

if __name__ == '__main__':
    a = [i*i for i in  range(1, 6)]
    xx = (6.3, 6.5, 6.6, -1, 48, 1, 9, 25)
    for _ in range(2):
        print('Array:', a)
        for x in xx:
            print(f'Index nearest to {x} is', binarySearchNN(a, x))
        print()
        a.reverse()
