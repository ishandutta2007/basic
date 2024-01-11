# Last updated: 23-Sep-2013
# Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
# Source: https://github.com/udy11, https://gitlab.com/udy11
# Function to integrate one-dimensional non-uniformly 
# spaced data using Trapezoidal Rule

# ALL YOU NEED TO DO:
# Call function intnud_trpzdl_1(x, f) with x as array of abscissae
#   and f as array of data to be integrated
# Call function intd_nu_trpzdl_2(d) with d as array of abscissae
#   and data where d is in the form [[x0, f0], [x1, f1], ...]

# Array can be list, tuple or numpy.array

def intnud_trpzdl_1(x, f):
    ''' (array, array) -> float
    Returns Integration of array f with abscissae x'''
    sm = 0
    for i in range(len(x) - 1):
        sm += (x[i+1] - x[i]) * (f[i+1] + f[i])
    return 0.5 * sm

def intnud_trpzdl_2(d):
    ''' (array, array) -> float
    Returns Integration of array d
    where d = [[x0, f0], [x1, f1], ...]
    and x are abscissae and f are data to be integrated'''
    sm = 0
    for i in range(len(d) - 1):
        sm += (d[i+1][0] - d[i][0]) * (d[i+1][1] + d[i][1])
    return 0.5 * sm

x = [0, 1, 3, 4, 5, 8, 9, 10]
f = [0, 1, 3, 4, 5, 8, 9, 10]
print(intnud_trpzdl_1(x, f))

d = [[0, 0], [1, 1], [3, 3], [4, 4], [5, 5], [8, 8], [9, 9], [10, 10]]
print(intnud_trpzdl_2(d))
