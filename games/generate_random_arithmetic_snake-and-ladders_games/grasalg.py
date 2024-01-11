# Last updated: 29-May-2013
# Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
# Source: https://github.com/udy11, https://gitlab.com/udy11
# Program to generate Mathematical Snake and Ladder Games

# Program prints a mathematical version of classical
# "Snake and Ladders" game. Instead of snake and ladders,
# here basic arithmetic operations are used:
# + - × / %
# % is for mod

# The program outs a txt file containing the tiles
# of the game, which can be copied to an excel file for
# further printing, etc. A sample excel file for 10 x 10
# grid is also provided with program to test the result

# The excel file can then be printed on hard paper
# and many players can play with a dice

# ALL YOU NEED TO DO:
# Fill all the inputs required in INPUT section

import random
import math

def prm_upto_n(n):
    ''' (int) -> list
        Returns the list of prime numbers upto n (inclusive)
    '''
    np = [2, 3]
    k = 2
    for i in range(5, n + 1):
        c = True
        j = 0
        while np[j] <= math.sqrt(i * 1.0):
            if i % np[j] == 0:
                c = False
                break
            j += 1
        if c:
            k += 1
            np.append(i)
    return np

def fctr(n):
    ''' (int) -> list
        Function to get all factors of n upto sqrt(n)
        Resulting list does not contain 1
    '''
    fc = []
    for i in range(2, 1 + math.ceil(math.sqrt(n))):
        if n % i == 0:
            fc.append(i)
    return fc

def mltp(n, m):
    ''' (int) -> list
        Function to get all multiples of n greater
        than n and upto m (inclusive)
    '''
    ml = []
    j = 2
    while True:
        p = n * j
        if p > m:
            break
        else:
            ml.append(p)
        j += 1
    return ml

def ot(op, n):
    ''' (str, int) -> str
        Outputs a random str based on operation op
        the operation is performed on appropriate random
        numbers to give result n.

        The function still has flaws, like the list ncl
        may turn out to be empty.

        LOCAL VARIABLES:
        op = operation: + - × / %
        ncl = list which contains all possible targets for a tile
        n0 = random target chosen from ncl
        n0 = n1 op n2
        n1l = list which decides n1
        n2l = list which decides n2

        GLOBAL VARIABLES:
        nopl = list of numbers which already contain operations
        nocl = list of numbers which were already targeted
        na = list of all allowed numbers
        nt = total tiles in game
        prms = list of prime numbers upto total allowed numbers
    '''
    if op == '+' or op == '-':
        ncl = []
        i = int(n - nc[0] * nt)
        if(i < 1):
            i = 1
        while i < n + nc[1] * nt and i < nt - 1:
            if (i < n-1 or i > n+1) and not i in nopl:
                ncl.append(i)
            i += 1
        n0 = random.choice(ncl)
        nocl.append(n0)
        if op == '+':
            n1l = list(range(na[0], n0 - 1))
            n1 = random.choice(n1l)
            n2 = n0 - n1
        else:
            n1l = list(range(n0 + 1, na[-1]))
            n1 = random.choice(n1l)
            n2 = n1 - n0
    elif op == '×' or op == '/':
        ncl = []
        i = int(n - nc[0] * nt)
        if(i < 4):
            i = 4
        while i < n + nc[1] * nt and i < nt - 1:
            if (i < n-1 or i > n+1) and not i in prms and not i in nopl:
                ncl.append(i)
            i += 1
        n0 = random.choice(ncl)
        nocl.append(n0)
        if op == '×':
            n2l = fctr(n0)
            n2 = random.choice(n2l)
            n1 = n0 // n2
        else:
            n1l = mltp(n0, na[-1])
            n1 = random.choice(n1l)
            n2 = n1 // n0
    elif op == '%':
        ncl = []
        i = int(n - nc[0] * nt)
        if(i < 4):
            i = 4
        while i < n + nc[1] * nt and i < nt - 1:
            if (i < n-1 or i > n+1) and not i in nopl:
                ncl.append(i)
            i += 1
        n0 = random.choice(ncl)
        nocl.append(n0)
        n2l = list(range(n0 + 1, nt))
        n2 = random.choice(n2l)
        n1l = []
        j = 1
        while True:
            n1e = n2 * j + n0
            if(n1e > na[-1]):
                break
            n1l.append(n1e)
            j += 1
        n1 = random.choice(n1l)
    return str(n1) + op + str(n2)

# INPUT
nt = 100                         # total tiles in game, keep at some n**2
nc = (0.3, 0.3)                  # fraction of back and forward tiles considered for operations
na = list(range(1,201))          # list of allowed numbers for operations
no = ['+', '-', '×', '/', '%']   # list of all operations considerable
otp = 0.4                        # ~ ratio of operation tiles to non-operation tiles
ofln = 'msl.txt'                 # output text file name

prms = prm_upto_n(na[-1])   # List of primes upto na[-1]
nopl = []                   # list of numbers which already contain operations
nocl = []                   # list of numbers which were already targeted
sl = ['1', '2', '3']        # the main list containing tiles to be printed
for i in range(4, nt - 2):
    r = random.random()
    if i == nt // 2:
        no.remove('%')
    if r > otp or i in nocl:
        sl.append(str(i))
    else:
        op = random.choice(no)
        sl.append(ot(op, i))
        nopl.append(i)

sl += [str(nt - 2), str(nt - 1), 'WIN']

ntsq = round(math.sqrt(nt))

##for i in range(0, ntsq, 2):
##    for j in range(ntsq):
##        print(sl[i * ntsq + j], end = '  ')
##    print()
##    for j in range(ntsq - 1, -1, -1):
##        print(sl[(i+1) * ntsq + j], end = '  ')
##    print()

ofl = open(ofln, 'w')
for i in range(0, ntsq, 2):
    for j in range(ntsq):
        ofl.write(sl[i * ntsq + j] + '  ')
    ofl.write('\n')
    for j in range(ntsq - 1, -1, -1):
        ofl.write(sl[(i+1) * ntsq + j] + '  ')
    ofl.write('\n')
ofl.close()
