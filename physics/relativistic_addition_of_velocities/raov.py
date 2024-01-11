# Last updated: 02-Feb-2014
# Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
# Source: https://github.com/udy11, https://gitlab.com/udy11
# Functions to relativistically add velocities
# in one dimension, two dimensions and three dimensions

# ALL YOU NEED TO DO:
# Call any function with:
#   u and v as velocities to add

# NOTE:
# u and v should be in SI units
# Speed of light, c is 299792458 m/s (exact)
#   and NOT 3x10^8 m/s
# Input u and v with proper signs in cartesian coordinates,
#   they will add to (u+v) in in classical mechanics
# Do not forget to import math
# In case of 2D and 3D, u and v can be list, tuple, numpy.array or
#   any other indexable object, but output will be tuple

import math

def addvelrel_1d(u, v):
    ''' (num, num) -> num
        Function to relativistically add two velocities in one dimension
    '''
    rc2 = 1.11265005605361843e-17
    return (u + v) / (1.0 + u * v * rc2)

def addvelrel_2d(u, v):
    ''' (2d_vec, 2d_vec) -> 2-tuple
        Function to relativistically add two velocities in two dimension
    '''
    rc2 = 1.11265005605361843e-17
    uvc2 = (u[0] * v[0] + u[1] * v[1]) * rc2
    gmv = 1.0 / math.sqrt(1.0 - (v[0] * v[0] + v[1] * v[1]) * rc2)
    t1 = (1.0 + uvc2 / (1.0 + gmv))
    t2 = 1.0 / (1.0 + uvc2)
    w0 = (t1 * v[0] + u[0] / gmv) * t2
    w1 = (t1 * v[1] + u[1] / gmv) * t2
    return (w0, w1)

def addvelrel_3d(u, v):
    ''' (3d_vec, 3d_vec) -> 3-tuple
        Function to relativistically add two velocities in three dimension
    '''
    rc2 = 1.11265005605361843e-17
    uvc2 = (u[0] * v[0] + u[1] * v[1] + u[2] * v[2]) * rc2
    gmv = 1.0 / math.sqrt(1.0 - (v[0] * v[0] + v[1] * v[1] + v[2] * v[2]) * rc2)
    t1 = (1.0 + uvc2 / (1.0 + gmv))
    t2 = 1.0 / (1.0 + uvc2)
    w0 = (t1 * v[0] + u[0] / gmv) * t2
    w1 = (t1 * v[1] + u[1] / gmv) * t2
    w2 = (t1 * v[2] + u[2] / gmv) * t2
    return (w0, w1, w2)

# c=2.99792458e8 # m/s

u1 = 1.e8
v1 = -1.5e8
print(addvelrel_1d(u1, v1))

u2 = [ 1.e8, 1.e8 ]
v2 = [ 1.e8, -1.e8 ]
print(addvelrel_2d(u2, v2))

u3 = [ 1.e8, 2.e7, 5.e7 ]
v3 = [ -1.e8, 2.e7, -5.e7 ]
print(addvelrel_3d(u3, v3))
