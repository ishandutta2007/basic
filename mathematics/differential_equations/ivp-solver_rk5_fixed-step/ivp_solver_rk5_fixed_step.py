# Last updated: 13-Jul-2015
# Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
# Source: https://github.com/udy11, https://gitlab.com/udy11
# Function to solve coupled ordinary differential equations with
# initial values (coupled-ODEs-IVP) using Butcher's Runge Kutta 5 method

# The program solves coupled ODEs y'[i]=f(x,y[j])[i]; {i,j: 0-->n-1}

# ALL YOU NEED TO DO:
# Call function brk5() with:
#   fx = external function that defines ODEs (see below INPUT FUNCTION)
#   h = step size in which x increases per iteration
#   ns = number of iterations
#   x0 = initial value of x, from which iteration begins
#   y0 = initial value(s) of y at x0
#   ofln = output file name

# OUTPUT:
# Output is in the text file as specified under INPUTS.
# Data is arranged as x variable followed by y vector.

# NOTE:
# This implementation of Butcher's Runge-Kutta 5 uses
#   constant step size, predefined by user
# If you want to run RK5 from x0 to x1, then h or ns can be calculated as:
#   h = (x1 - x0) / ns
#   ns = (x1 - x0) / h
# A higher order ODE can be broken into coupled ODEs, e.g.,
#   y''+100*y=0, can be broken as y1'=y2; y2'=-100*y1

# INPUT FUNCTION
# Simply define functions in a list: [f0, f1, ...]
# for coupled ODEs: y'[i]=f(x,y[j])[i]
# Example:
# Suppose you want to solve: y'[0]=y[1]; y'[1]=-100*y[0]
# Then define f = [y[1], -100 * y[0]]
# This means f are simply the RHS in the coupled ODEs when arranged properly.
def gx(x, y):
    f = [y[1], -100 * y[0]]
    return f

def brk5(fx, h, ns, x0, y0, ofln):
    ''' brk5(ODEs function, step size, # of steps, initial x, initial y, output file name) '''
    n = len(y0)
    x = x0
    y = list(y0)
    fl = open(ofln, 'w')
    fl.write(str(x) + ' ' + str(y)[1:-1].replace(',', '') + '\n')
    for i in range(1, ns + 1):
        f = fx(x, y)
        k1 = [h * f[j] for j in range(n)]
        f = fx(x + 0.25 * h, [y[j] + 0.25 * k1[j] for j in range(n)])
        k2 = [h * f[j] for j in range(n)]
        f = fx(x + 0.25 * h, [y[j] + 0.125 * (k1[j] + k2[j]) for j in range(n)])
        k3 = [h * f[j] for j in range(n)]
        f = fx(x + 0.5 * h, [y[j] - 0.5 * k2[j] + k3[j] for j in range(n)])
        k4 = [h * f[j] for j in range(n)]
        f = fx(x + 0.75 * h, [y[j] + 0.1875 * k1[j] + 0.5625 * k4[j] for j in range(n)])
        k5 = [h * f[j] for j in range(n)]
        f = fx(x + h, [y[j] + (-3 * k1[j] + 2 * k2[j] + 12 * k3[j] - 12 * k4[j] + 8 * k5[j]) / 7 for j in range(n)])
        k6 = [h * f[j] for j in range(n)]
        x = x0 + i * h
        y = [y[j] + (7 * k1[j] + 32 * k3[j] + 12 * k4[j] + 32 * k5[j] + 7 * k6[j]) / 90 for j in range(n)]
        fl.write(str(x) + ' ' + str(y)[1:-1].replace(',', '') + '\n')
    fl.close()

# INPUTS
h = 0.0001                # step size in which iteration proceeds
ns = 10000                # number of steps
x0 = 0.0                  # initial value from which iteration begins
y0 = [0.0, 10.0]          # initial values for unknowns
ofln = "brk5_tst.py.txt"  # output file name (overwrites if already exists)

brk5(gx, h, ns, x0, y0, ofln)
