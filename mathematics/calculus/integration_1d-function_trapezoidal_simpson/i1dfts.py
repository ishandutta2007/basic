# Last updated: 07-Oct-2015
# Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
# Source: https://github.com/udy11, https://gitlab.com/udy11
# Functions to integrate one-dimensional function
# using Trapezoidal and Simpson's 1/3rd Rules

# ALL YOU NEED TO DO:
# Call required function with parameters
#   a, b = range in which to integrate
#   n = number of sample points to take for integration (including end-points)
# Specify the function to be integrated in f(x)

# NOTE:
# Choosing a large n will cause truncation error to reduce
#   but will increase roundoff error, so choose as per needs
# In case your function has some parameters, you can specify
#   them as global variables, they are then automatically passed to fx
# Note that integration(f(x),(a,b))=-integration(f(x),(b,a))
#   so specify the range a,b accordingly
# In case of Simpson's 1/3rd rule, number of points n should be odd (or
#   equivalently, number of intervals should be even); however, if n is
#   given even, the program uses n-1 points (maintaining the range a to b)

# Below is example of integration(d/(1+x*x),(x,0,1)), with d=4

import math
def f(x):
    return d / (1 + x * x)

def int_trpzdl(a, b, n):
    ''' (num, num, int) -> float
    Returns Integration of function f(x) in range a to b
    using ~ n points in between and Trapezoidal Rule
    Truncation Error = -(b-a)(h**2)f''(z)/12, a<z<b '''
    h = (b - a) / n
    sm = h * 0.5 * (f(a) + f(b))
    for i in range(1, n):
        sm += h * f(a + i * h)
    return sm

def int_smpsn(a, b, n):
    """ (num, num, int) -> float
    Returns Integration of function f(x) in range a to b
    using total n points and Simpson's 1/3rd Rule
    Truncation Error = -(b-a)(h**4)f''''(z)/180, a<z<b """
    if n & 1 == 0:
        m = n - 1
    else:
        m = n
    h = (b - a) / (m - 1)
    sm = h * (f(a) + f(b) + 4 * f(b - h)) / 3
    for i in range(1, m // 2):
        sm += h * (4 * f(a + (2 * i - 1) * h) + 2 * f(a + 2 * i * h)) / 3
    return sm

a = 0; b = 1; n = 199
d = 4
print(int_trpzdl(a, b, n))
print(int_smpsn(a, b, n))
