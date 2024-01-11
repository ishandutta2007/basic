# Last updated: 17-Jun-2013
# Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
# Source: https://github.com/udy11, https://gitlab.com/udy11
# Functions to check a non-negative integer for
# triangle, square, pentagon, hexagon, heptagon or octagon number

# ALL YOU NEED TO DO:
# Call appropriate function with non-negative n
# Don't forget to import math

# All functions are independent of each other

import math

def is_trin(n):
    ''' (int) -> logical
        To check if a non-negative integer n is a triangle number
        Tr(n) = n * (n + 1) // 2
    '''
    if n % 9 in (0, 1, 3, 6):
        n2 = n * 2
        r = round(math.sqrt(n2))
        if r * (r + 1) == n2:
            return True
    return False
        
    return

def is_sqrn(n):
    ''' (int) -> logical
        To check if a non-negative integer n is a square number
        Sq(n) = n * n
    '''
    if n % 4 == 0 or n % 8 == 1:
        r = round(math.sqrt(n))
        if r * r == n:
            return True
    return False

def is_pntn(n):
    ''' (int) -> logical
        To check if a non-negative integer n is a pentagon number
        Pn(n) = n * (3 * n - 1) // 2
    '''
    if n % 5 < 3:
        x = 24 * n + 1
        if x % 4 == 0 or x % 8 == 1:
            r = round(math.sqrt(x))
            if r * r == x and r % 6 == 5:
                return True
    return False

def is_hexn(n):
    ''' (int) -> logical
        To check if a non-negative integer n is a hexagon number
        Hx(n) = n * (2 * n - 1)
    '''
    if n % 9 in (0, 1, 3, 6):
        x = 8 * n + 1
        r = round(math.sqrt(x))
        if r * r == x and r % 4 == 3:
            return True
    return False

def is_hptn(n):
    ''' (int) -> logical
        To check if a non-negative integer n is a heptagon number
        Hp(n) = n * (5 * n - 3) // 2
    '''
    if n % 9 in (0, 1, 4, 7):
        x = 40 * n + 9
        r = round(math.sqrt(x))
        if r * r == x and r % 10 == 7:
            return True
    return False

def is_octn(n):
    ''' (int) -> logical
        To check if a non-negative integer n is a octagon number
        Oc(n) = n * (3 * n - 2)
    '''
    if n % 8 in (0, 1, 5):
        x = 3 * n + 1
        r = round(math.sqrt(x))
        if r * r == x and r % 3 == 2:
            return True
    return False
