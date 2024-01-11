# Last upadted: 07-Feb-2013
# Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
# Source: https://github.com/udy11, https://gitlab.com/udy11
# Function to replace bad values in numerical data with
# constant values or linear filling

def is_numeric(s):
    "Checks if str s can be converted to numeric or not"
    try:
        float(s)
        return True
    except ValueError:
        return False

def dt_bdr(ifln, nh, bd, gd, ofln):
    ''' (input-filename, #header-lines, bad-values-list, good-values-list, output-filename)

        The function reads the data from input file specified by ifln
        and performs the following operations:
        1. Skips the header lines given by input nh
        2. Detects the bad values as specified by bd list/tuple
        3. Replaces bad values with good values as specified by gd list/tuple
        4. If gd has an element "linear", then bad values are replaced with linear interpolation
        5. If gd has a non-str element, that column is not touched
        The output data is written in output file specified
        by ofln along with header lines.

        INPUT:
        ifln = Input File Name
        nh = Number of Header Lines
        bd = list/tuple of Bad values or data points
             Note that each element itself can be a list/tuple
             specifying bad values, in that case it will consider any
             of those (in list/tuple) as bad values
             Also, each value must be of str class
             If 1 (integer/numeric) is specified, it will consider
             all non numeric data as bad
             Specify any other integer/numeric to skip modifying that column
        gd = list or tuple of values (must be of str class) which will
             replace Bad values
             "linear" element will cause linear filling in that column
             any other str element will cause that to be filled
             any other non str element will keep the column unmodified
             e.g. gd = ("0","NaN",1,"linear")
             will replace bad values in column 1 and 2 with 0 and NaN respectively
                                     in column 3, no modification
                                     in column 4, a linear filling
             Also note that in "linear" mode, the initial and final
             bad points will be copied to same as nearest numeric
             values found (i.e. linear fill will not be applied for initial
             and final bad data points)
        ofln = Output File Name (to write modified data with header lines)
    '''

    nc = len(bd)
    if nc != len(gd):
        print("ERROR: Number of elements in gd and bd are different")
        return
    ifl = open(ifln, 'r')
    hdr = ''
    for i in range(nh):
        hdr = hdr + ifl.readline()
# Change the separator of input file here, default is space ' '
    sep = ' '
    dt = [[] for i in range(nc)]
    dl = -1
    lyn = ifl.readline().strip()
    while lyn != '':
        dl += 1
        i = 0; dn = 0
        ll = len(lyn)
        while i < ll:
            if lyn[i] != sep:
                k = 1
                while i+k < ll and lyn[i+k] != sep:
                    k += 1
                dt[dn].append(lyn[i:i+k])
                i += k+1
                dn += 1
            else:
                i += 1
        if dn != nc:
            print("ERROR: Insufficient data in line " + str(dl+1+nh))
            return
        lyn = ifl.readline().strip()
    ifl.close()
    for j in range(nc):
        if bd[j] == 1:
            if gd[j] == "linear":
                mf = 0
                if not is_numeric(dt[j][mf]):
                    print(j,'f')
                    mf = 1
                    while not is_numeric(dt[j][mf]):
                        mf += 1
                    for m in range(mf):
                        dt[j][m] = dt[j][mf]
                ml = dl
                if not is_numeric(dt[j][dl]):
                    ml = dl - 1
                    while not is_numeric(dt[j][dl]):
                        ml -= 1
                    for m in range(ml+1, dl+1):
                        dt[j][m] = dt[j][ml]
                k = mf + 1
                while k < ml:
                    if not is_numeric(dt[j][k]):
                        mm = k + 1
                        while not is_numeric(dt[j][mm]):
                            mm += 1
                        mi = float(dt[j][k-1])
                        df = (float(dt[j][mm]) - mi)/(mm-k+1)
                        for l in range(k, mm):
                            dt[j][l] = str(mi + df * (l-k+1))
                    k += 1
            elif isinstance(gd[j], str):
                for m in range(dl+1):
                    if not is_numeric(dt[j][m]):
                        dt[j][m] = gd[j]
        elif isinstance(bd[j], (str, list, tuple)):
            if gd[j] == "linear":
                mf = 0
                if dt[j][0] in bd[j]:
                    mf = 1
                    while dt[j][mf] in bd[j]:
                        mf += 1
                    for m in range(mf):
                        dt[j][m] = dt[j][mf]
                ml = dl
                if dt[j][dl] in bd[j]:
                    ml = dl - 1
                    while dt[j][ml] in bd[j]:
                        ml -= 1
                    for m in range(ml+1, dl+1):
                        dt[j][m] = dt[j][ml]
                k = mf + 1
                while k < ml:
                    if dt[j][k] in bd[j]:
                        mm = k + 1
                        while dt[j][mm] in bd[j]:
                            mm += 1
                        mi = float(dt[j][k-1])
                        df = (float(dt[j][mm]) - mi)/(mm-k+1)
                        for l in range(k, mm):
                            dt[j][l] = str(mi + df * (l-k+1))
                    k += 1
            elif isinstance(gd[j], str):
                for m in range(dl+1):
                    if dt[j][m] in bd[j]:
                        dt[j][m] = gd[j]
    ofl = open(ofln, 'w')
    ofl.write(hdr)
    for w in range(dl+1):
        st = ''
        for l in range(nc):
            st = st + dt[l][w] + sep
        ofl.write(st[:-1] + '\n')
    ofl.close()

# This function takes only one file as input
# If you want to work this function on multiple files
# and combine all of them into one file, do the following:
# Comment out these lines in the function:
#   ofl = open(ofln,'w')
#   ofl.write(hdr)
#   ofl.close()
# and uncomment the following ## code:

##nh = 3
##bd = [0, 1, "NaN", ("Inf", "-Inf")]
##gd = ["0", "0.0", "linear", "NaN"]
##ofln = "out.txt"
##
##import glob
##fls = glob.glob("*.txt")
##ofl = open(ofln, 'w')
##for fl in fls:
##    dt_bdr(fl, nh, bd, gd, ofln)
##ofl.close()

# Above, define your own nh, bd, gd, ofln
# Also you need to specify your own input file name pattern inside
# glob.glob() function; above it is all *.txt files in the current folder
