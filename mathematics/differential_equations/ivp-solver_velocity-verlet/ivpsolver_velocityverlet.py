# Last updated: 30-Aug-2016
# Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
# Source: https://github.com/udy11, https://gitlab.com/udy11
# Function to solve 2nd order ordinary differential
# equation with initial values using Velocity Verlet algorithm

# This program solves for the following second order ODE:
#   y'' = f(y)
# i.e., f() depends only on y and NOT on x or y'

# ALL YOU NEED TO DO:
# Call function velverlet() with:
#   fx = external function that defines ODEs (see below INPUT FUNCTION)
#   h = step size in which x increases per iteration
#   ns = number of iterations
#   x0 = initial value of x, from which iteration begins
#   y0 = value of y at x0
#   yp0 = value of y' at x0
#   ofln = output file name

# OUTPUT:
# Output is in the text file as specified under INPUTS
# The three columns represent x, y and y' respectively

# NOTE:
# If you want to run RK5 from x0 to x1, then h or ns can be calculated as:
#   h = (x1 - x0) / ns
#   ns = (x1 - x0) / h
# Error ~ h**2

# INPUT FUNCTION
# Simply define it as the RHS of the 2nd order ODE y'' = f(y)
def gx(y):
    return -100 * y

def velverlet(fx, h, ns, x0, y0, ofln):
    ''' velverlet(ODE function, step size, # of steps, initial x, initial y, initial y', output file name) '''
    hh = h * 0.5
    y = y0
    yp = yp0
    fl = open(ofln, 'w')
    fl.write('%1.15e %1.15e %1.15e\n' % (x0, y, yp))
    for i in range(1, ns + 1):
        b = yp + fx(y) * hh
        y += b * h
        yp = b + fx(y) * hh
        fl.write('%1.15e %1.15e %1.15e\n' % (x0 + i * h, y, yp))
    fl.close()

# INPUTS
h = 1.e-4                      # step size in which iteration proceeds
ns = 10000                     # number of steps
x0 = 0.0                       # initial value from which iteration begins
y0 = 0.0                       # initial value of y
yp0 = 10.0                     # initial value of y'
ofln = "velverlet_tst.py.txt"  # output file name (overwrites if already exists)

velverlet(gx, h, ns, x0, y0, ofln)
