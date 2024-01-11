# Last updated: 19-Feb-2015
# Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
# Source: https://github.com/udy11, https://gitlab.com/udy11
# Template function to generate arbitrary number of nested for-loops

# ALL YOU NEED TO DO:
# Call ffor() function with ranges of for-loops:
#   r1 = list/tuple of beginning of loops
#   r2 = list/tuple of ending of loops
#   st = list/tuple of step sizes of loops (it is optional and
#        by default it will be a list of 1)
# Mention the required procedures in the places marked in the
#   function, noting that m is (m+1)^th loop, so if there are
#   4 nested loop, the topmost has m=0, innermost has m=3;
#   and k is current loop's iterator

# NOTE:
# For any other parameters within loops, you will have to
#   include those in nonlocal statement
# Ranges follow Python's convention, so all entries in r2 are
#   excluded, i.e., if r1 = (1, ...) and r2 = (5, ...) then
#   the first loop will run on 1, 2, 3 and 4 only
# It uses recursions, which is limited, but can be changed by
#   sys.setrecursionlimit(1500) command; use it at your own risk

# Method self-discovered...

def ffor(r1, r2, st = 7):
    r = len(r1) - 1
    if r != len(r2) - 1:
        return
    if st == 7:
        st = [1 for m in range(r+1)]
    m = 0
    def frc():
        nonlocal m, r, r1, r2
        if m < r:
            for k in range(r1[m], r2[m], st[m]):
                
                # Pre-procedure for mth for-loop
                print(' '*2*m, 'Procedure', str(m)+'a', k)
                
                m += 1
                frc()
                m -= 1
                
                # Post-procedure for mth for-loop
                print(' '*2*m, 'Procedure', str(m)+'b', k)
                
        else:
            for k in range(r1[m], r2[m], st[m]):
                
                # Procedure for innermost for-loop
                print(' '*2*m, 'Procedure', str(m), k)

    frc()

ffor((0, 10, 100, 1000), (2, 12, 106, 1009), (1, 1, 2, 3))
