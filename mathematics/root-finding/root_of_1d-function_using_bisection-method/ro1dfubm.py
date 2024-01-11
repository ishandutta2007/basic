# Last updated: 04-Jun-2016
# Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
# Source: https://github.com/udy11, https://gitlab.com/udy11
# Function to find a root of a one
# dimensional function using Bisection Method

# ALL YOU NEED TO DO:
# Call function bsctn() with:
#   f = function whose root is to be found (must return num)
#   a,b = range in which root is to be found (inclusive)
#   er = tolerance below which root will be accepted,
#        i.e., when |f(c)|<er, c is accepted as root
# Define f(x), external function whose root is to be found
# Function bsctn() outputs a tuple (istt, c), where
#   istt = status code of function's execution (see below for details)
#   c = found root, if successful

# STATUS CODE:
# istt=1, success: root found between a and b
# istt=2, success: root found at a
# istt=3, success: root found at b
# istt=-1, error: root could not be found between a and b

# NOTE:
# If f(x) does not cross the x-axis but only touches it,
#   like f(x)=x*x at x=0, then that root will most probably not be found
# Below method does not check for opposite signs to continue operating
#   as conventional bisection method does, but it is then likely to find
#   a root if it exists, even if signs at boundaries are same
# Method is optimized for minimum calls to f(x)

def bsctn(f, a, b, er):
    ''' (function, float, float, float) -> (int, float)

        Function to find a root of f(x) using Bisection Method
    '''
    fa = f(a)
    fb = f(b)
    if abs(fa) < er:
        return (2, a)
    if abs(fb) < er:
        return (3, b)
    eps = 4.4408920985006262e-16
    ifa = False
    ifb = False
    c = 0.5 * (a + b)
    if abs(c - 1.0) < eps:
        c0 = 2.0
    else:
        c0 = 1.0
    while True:
        fc = f(c)
        if abs(fc) < er:
            return (1, c)
        elif c0 == 0.0 and c == 0.0:
            return (-1, c)
        elif c0 != 0.0 and abs(1 - c / c0) < eps:
            return (-1, c)
        else:
            if ifa:
                fa = f(a)
            elif ifb:
                fb = f(b)
            if fa * fc < 0.0:
                b = c
                ifa = False
                ifb = True
            elif fb * fc < 0.0:
                a = c
                ifa = True
                ifb = False
            elif abs(fa) < abs(fb):
                b = c
                ifa = False
                ifb = True
            else:
                a = c
                ifa = True
                ifb = False
        c0 = c
        c = 0.5 * (a + b)

def g(x):
    ''' (float) -> float

        Input Function g(x), whose root is to be found
    '''
    return x * x - 1

a = -2
b = 20.0
er = 5.0e-16
r = bsctn(g, a, b, er)
if r[0] == 1:
    print("Root found at", r[1])
elif r[0] == 2:
    print("Root found at a,", r[1])
elif r[0] == 3:
    print("Root found at b,", r[1])
elif r[0] == -1:
    print("Root could not be found in given range.")
