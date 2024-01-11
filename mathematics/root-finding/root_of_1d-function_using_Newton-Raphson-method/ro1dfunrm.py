# Last updated: 26-Apr-2013
# Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
# Source: https://github.com/udy11, https://gitlab.com/udy11
# Function to find a root of a one
# dimensional function using Newton-Raphson Method

# ALL YOU NEED TO DO:
# Specify the initial guess x0,
#   it must be near the desired root
# Specify the function y(x), whose root is needed
# Specify the derivative of y(x) as yp(x)
# Specify positive small er; when |y(x1)|<er, further
#   computation stops and x1 is returned as root

def nwtn_rphsn(x0,er):
    ''' (num,num) -> num

        Function to find root of y(x)=0
        using Newton-Raphson Method
        x0 is initial guess
        er is a small positive number such that when
        |y(x1)|<er, further calculation is stopped
        and x1 is returned as root
    '''
    while True:
        x1=x0-y(x0)/yp(x0)
        if(abs(y(x1))<er):
            return x1
        x0=x1

import math
def y(x):
    ''' num -> num

        Input Function y(x), whose root is to be found
    '''
    return math.sin(x)

def yp(x):
    ''' num -> num

        Derivative of y(x), i.e. dy(x)/dx
    '''
    return math.cos(x)

x0=9.7
er=4.e-16
x1=nwtn_rphsn(x0,er)
print(x1,y(x1))
