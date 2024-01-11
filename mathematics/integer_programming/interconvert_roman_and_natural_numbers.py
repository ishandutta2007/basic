# Last updated: 20-May-2013
# Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
# Source: https://github.com/udy11, https://gitlab.com/udy11
# Functions to interconvert Roman Numerals and Natural Numbers

# Input and Output of Roman Numerals is in str
# Roman Numerals must be greater than 0
# For info on Subtractive Notation and valid Roman Numerals, read:
#   http://en.wikipedia.org/wiki/Roman_numerals#Reading_Roman_numerals

def num_to_roman(n):
    ''' (int) ->  str
        Converts a decimal number to a Roman Numeral
        which follows Minimal Subtractive Notation

        Some Examples:
        num_to_roman(4) ---> 'IV'
        num_to_roman(49) ---> 'XLIX'
        num_to_roman(2194) ---> 'MMCXCIV'
        num_to_roman(459) ---> 'CDLIX'
    '''
    rmtr = (('M', 1000), ('CM', 900), ('D', 500), ('CD', 400), ('C', 100), ('XC', 90), ('L', 50), ('XL', 40), ('X', 10), ('IX', 9), ('V', 5), ('IV', 4), ('I', 1))
    s = ''
    for k in rmtr:
        ss = n // k[1]
        s += k[0] * ss
        n -= ss * k[1]
    return s

def roman_to_num(s):
    ''' (str) ->  int
        Converts a valid Roman Numeral to a decimal number
        A valid Roman Numeral is one which follows Subtractive Notation
        but need not be Minimal

        Some Examples:
        roman_to_num('IV') ---> 4
        roman_to_num('XXXXVIIII') ---> 49
        roman_to_num('MMCXCIV') ---> 2194
        roman_to_num('CCCCLIX') ---> 459
    '''
    rmtr = (('M', 1000), ('CM', 900), ('D', 500), ('CD', 400), ('C', 100), ('XC', 90), ('L', 50), ('XL', 40), ('X', 10), ('IX', 9), ('V', 5), ('IV', 4), ('I', 1))
    n = 0
    for k in rmtr:
        j = 0
        c = 0
        if len(k[0]) == 2:
            while True:
                if(j >= len(s)):
                    break
                if s[j:j+2] == k[0]:
                    c += 1
                    j += 2
                else:
                    break
            s = s[j:]
            n += k[1] * (j//2)
        else:
            while True:
                if(j >= len(s)):
                    break
                if s[j] == k[0]:
                    c += 1
                    j += 1
                else:
                    break
            s = s[j:]
            n += k[1] * j
    return n
