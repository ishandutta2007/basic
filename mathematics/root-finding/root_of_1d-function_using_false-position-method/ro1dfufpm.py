# Last updated: 18-Feb-2015
# Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
# Source: https://github.com/udy11, https://gitlab.com/udy11
# Function to find a root of a one
# dimensional function using False Position Method

# ALL YOU NEED TO DO:
# Call function falspos() with:
#   a,b = range in which root is to be found (inclusive)
#   er = tolerance below which root will be accepted,
#        i.e., when |f(c)|<er, c is accepted as root
# Define f(x), external function whose root is to be found
# Function falspos() outputs a tuple (istt, c), where
#   istt = status code of function's execution (see below for details)
#   c = found root

# STATUS CODE:
# istt=1, success: root found between a and b
# istt=2, success: root found at a
# istt=3, success: root found at b
# istt=-1, error: root could not be found between a and b

# NOTE:
# If f(x) does not cross the x-axis but only touches it,
#   like f(x)=x*x at x=0, then that root will most probably not be found
# Below method does not check for opposite signs to continue operating
#   as conventional false position method does, but it is then likely to
#   find a root if it exists, even if signs at boundaries are not opposite
# Method is optimized for minimum calls to f(x)

def falspos(a, b, er):
    ''' (float, float, float) -> (int, float)

        Function to find a root of f(x) using False Position Method
    '''
    fa = f(a)
    if abs(fa) < er:
        return (2, a)
    fb = f(b)
    if abs(fb) < er:
        return (3, b)
    if fa == fb:
        c = 0.5 * (a + b)
    else:
        c = (a * fb - b * fa) / (fb - fa)
    if c == 0:
        c0 = 1.0
    else:
        c0 = 0.0
    while True:
        fc = f(c)
        if abs(fc) < er:
            return (1, c)
        elif c == c0:
            return (-1, c)
        else:
            if fa * fc < 0:
                b = c
                ifa = False
            else:
                a = c
                ifa = True
            if ifa:
                fa = f(a)
            else:
                fb = f(b)
        c0 = c
        if fa == fb:
            c = 0.5 * (a + b)
        else:
            c = (a * fb - b * fa) / (fb - fa)

def f(x):
    ''' (float) -> float

        Input Function f(x), whose root is to be found
    '''
    return x * x - 1

a = -12.0
b = 3.0
er = 2.0e-16
r = falspos(a, b, er)
if r[0] == 1:
    print("Root found at", r[1])
elif r[0] == 2:
    print("Root found at a,", r[1])
elif r[0] == 3:
    print("Root found at b,", r[1])
elif r[0] == -1:
    print("Root could not be found in given range.")
