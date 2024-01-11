# Last updated: 06-Sep-2013
# Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
# Source: https://github.com/udy11, https://gitlab.com/udy11
# Functions to integrate a one-dimensional uniformly
# spaced data using Trapezoidal Rule and Simpson's 1/3rd Rule

# ALL YOU NEED TO DO:
# Call function with 1D array of data (f) to be integrated and
#   with limits in which to integrate (a, b)
# Function returns the integrated value

# It is assumed that for array f, f[0] corresponds to a
#   and f[-1] corresponds to b
# Note that integration(f,(a,b))=-integration(f,(b,a))
#   so specify the range a,b accordingly
# For Simpson's 1/3rd Rule, number of points in f should be odd
# Array can be list, tuple or numpy.array

def intd_trpzdl(a, b, f):
    ''' (num, num, array) -> float
    Returns Integration of array f in range a to b '''
    n = len(f) - 1
    h = (b - a) / n
    sm = h * 0.5 * (f[0] + f[-1])
    for i in range(1, n):
        sm += h * f[i]
    return sm

def intd_smpsn(a, b, f):
    ''' (num, num, array) -> float
    Returns Integration of array f in range a to b '''
    n = len(f) - 1
    if n & 1 != 0:
        print("ERROR: Number of points in f should be odd...")
        return
    h = (b - a) / n
    smi = h * (f[0] + f[-1])
    smo = 0
    for i in range(1, n, 2):
        smo += h * f[i]
    sme = 0
    for i in range(2, n, 2):
        sme += h * f[i]
    return (smi + 4 * smo + 2 * sme) / 3

f = [i for i in range(11)]
a = 0; b = 2
print(intd_trpzdl(a, b, f))
print(intd_smpsn(a, b, f))
