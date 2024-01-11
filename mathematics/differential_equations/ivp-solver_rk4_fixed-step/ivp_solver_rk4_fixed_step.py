# Last updated: 25-Dec-2012
# Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
# Source: https://github.com/udy11, https://gitlab.com/udy11
# Function to solve coupled ordinary differential equations with
# initial values (coupled-ODEs-IVP) using Runge Kutta 4 (RK4) method

# The program solves coupled ODEs y'[i]=f(x,y[j])[i]; {i,j: 0-->n-1}

# ALL YOU NEED TO DO:
# Call function rk4() with:
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
# This implementation of Runge-Kutta 4 uses constant step size,
#   predefined by user
# If you want to run RK4 from x0 to x1, then h or ns can be calculated as:
#   h = (x1 - x0) / ns
#   ns = (x1 - x0) / h
# A higher order ODE can be broken into coupled ODEs, e.g.,
#   y''+100*y=0, can be broken as y0'=y1; y1'=-100*y0

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

def rk4(fx, h, ns, x0, y, ofln):
    ''' rk4(ODEs function, step size, # of steps, initial x, initial y, output file name) '''
    n = len(y0)
    x = x0
    y = list(y0)
    fl = open(ofln, 'w')
    fl.write(str(x) + ' ' + str(y)[1:-1].replace(',', '') + '\n')
    for i in range(1, ns + 1):
        f = fx(x, y)
        k1 = [h * f[j] for j in range(n)]
        f = fx(x + 0.5 * h, [y[j] + 0.5 * k1[j] for j in range(n)])
        k2 = [h * f[j] for j in range(n)]
        f = fx(x + 0.5 * h, [y[j] + 0.5 * k2[j] for j in range(n)])
        k3 = [h * f[j] for j in range(n)]
        f = fx(x + h, [y[j] + k3[j] for j in range(n)])
        k4 = [h * f[j] for j in range(n)]
        x = x0 + i * h
        y = [y[j] + (k1[j] + 2 * (k2[j] + k3[j]) + k4[j]) / 6 for j in range(n)]
        fl.write(str(x) + ' ' + str(y)[1:-1].replace(',', '') + '\n')
    fl.close()

# INPUTS
h = 0.0001                # step size in which iteration proceeds
ns = 10000                # number of steps
x0 = 0.0                  # initial value from which iteration begins
y0 = [0.0, 10.0]          # initial values for unknowns
ofln = "rk4_tst.py.txt"   # output file name (program gives error if it already exists)

rk4(gx, h, ns, x0, y0, ofln)
