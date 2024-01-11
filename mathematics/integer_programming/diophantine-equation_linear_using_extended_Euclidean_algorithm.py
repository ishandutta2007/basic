# Last updated: 29-Nov-2015
# Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
# Source: https://github.com/udy11, https://gitlab.com/udy11
# Function to solve Linear Diophantine Equation
# using Extended Euclidean Algorithm

# Linear Diophantine Equation:
# a * x + b * y == c
# where a, b and c are integers and
# solution (x, y) integers are required.
# If c is a multiple of gcd(a, b), infinite
# solutions exist, otherwise none.

# ALL YOU NEED TO DO:
# Call lindioeqprm(a, b, c) with:
#   a, b, c as parameters of equation
#   described above and store its output
#   in a temporary variable (say pr)
# Call lindioeqsol(pr, n) with any integer n
#   to get one solution (x, y) of equation
#   corresponding to n

def lindioeqprm(a, b, c):
    ''' (int, int, int) -> (int, int, int, int, int)
        Solves the Linear Diophantine Equation for (x, y):
        a * x + b * y == c, all integers
        Using Extended Euclidean Algorithm.
        Returns parameters required by lindioeqsol() function.
    '''
    g = a
    b0 = b
    qq = []
    while b0 != 0:
        t = b0
        b0 = g // t
        qq.append(b0)
        b0 = g - b0 * t
        g = t
    if c % g != 0:
        return ()
    s0 = 1; s1 = 0
    t0 = 0; t1 = 1
    for q in qq:
        t = s1
        s1 = s0 - q * t
        s0 = t
        t = t1
        t1 = t0 - q * t
        t0 = t
    return (a // g, b // g, c // g, s0, t0)

def lindioeqsol(pr, n):
    ''' (array, int) -> (int, int)
        Solves the Linear Diophantine Equation for (x, y):
        a * x + b * y == c, all integers
        Using Extended Euclidean Algorithm.
        Requires parameters returned by lindioeqprm() function.
    '''
    if pr == ():
        return ()
    return (pr[2] * pr[3] - n * pr[1], pr[2] * pr[4] + n * pr[0])

pr = lindioeqprm(3, 5, 13)
for n in [-1, 0, 1, 3, 7]:
    print(lindioeqsol(pr, n))
