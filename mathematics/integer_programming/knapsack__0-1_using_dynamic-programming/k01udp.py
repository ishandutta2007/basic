# Last updated: 19-Aug-2014
# Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
# Source: https://github.com/udy11, https://gitlab.com/udy11
# Function to solve Knapsack 0-1 Problem
# using Dynamic Programming

# Knapsack 0-1 Problem is:
# Given m items with values v and weights w
#   which items to choose so that the total value is maximized
#   and the total weight is <= [given] knapsack capacity, wm
# i.e. maximize sum(tt[i] * v[i]) for sum(tt[i] * w[i]) <= wm
#   where tt[i] is 0 or 1, and i runs on items

# ALL YOU NEED TO DO:
# Call function knapsack_01_dp(v, w, wm) with:
#   v = list/tuple of values (int)
#   w = list/tuple of weights (int)
#   wm = maximum capacity of knapsack (int)

# OUTPUT:
# The function returns a bool list which tells which
#   item to include in the knapsack

# NOTE:
# The algorithm gives "one" solution, there may actually be many

def knapsack_01_dp(v, w, wm):
    ''' (int list, int list, int) -> bool list

        Solves Knapsack 0-1 Problem using Dynamic Programming
        v = list/tuple of values (int)
        w = list/tuple of weights (int)
        wm = maximum capacity of knapsack (int)

        Returns bool array whose i^th entry tells whether
          i^th item should be in knapsack or not
    '''
    m = len(v)
    kv = [[0 for j in range(wm+1)] for i in range(m)]
    for j in range(w[0]-1, wm):
        kv[0][j] = v[0]
    for i in range(1, m):
        for j in range(w[i] - 1):
            kv[i][j] = kv[i-1][j]
        for j in range(w[i] - 1, wm):
            kv[i][j] = max(kv[i-1][j], kv[i-1][j-w[i]] + v[i])
    j = wm - 1
    i = m - 1
    tt = [False for i in range(m)]
    while i > 0:
        if kv[i][j] != kv[i-1][j]:
            tt[i] = True
            j -= w[i]
        i -= 1
    if kv[0][j] != 0:
        tt[0] = True
    return tt

v = (92, 57, 49, 68, 60, 43, 67, 84, 87, 72)
w = (23, 31, 29, 44, 53, 38, 63, 85, 89, 82)
wm = 165

print(knapsack_01_dp(v, w, wm))
