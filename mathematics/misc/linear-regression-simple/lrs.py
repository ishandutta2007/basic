# Last updated: 01-Feb-2013
# Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
# Source: https://github.com/udy11, https://gitlab.com/udy11
# Functions to Linear Fit one-dimensional data points
# using Least Squares Method
# Also known as Simple Linear Regression

def lnr_ft1(x, y):
    ''' (x, y) -> (slope, intercept)

        Function to linear fit one dimensional data points
        using Least Square Method (or Simple Linear Regression)

        This function takes the following input:
        x = x array (can be list or tuple)
        y = y array (can be list or tuple)

        Also, to calculate Pearson Product-Moment Correlation Coefficient
        (or Pearson's r) simply remove all commented lines below, then
        program prints this quantity as well; to add it to returning list,
        simply replace return [m, c] --> return [m, c, pcc]
    '''
    n = len(x)
    sx = 0; sy = 0; sx2 = 0; sxy = 0; # sy2 = 0
    for i in range(n):
        sx = sx + x[i]
        sy = sy + y[i]
        sx2 = sx2 + x[i] * x[i]
        sxy = sxy + x[i] * y[i]
#        sy2 = sy2 + y[i] * y[i]
    m = (sxy - sx * sy / n)/(sx2 - sx * sx / n)
    c = sy / n - m * sx / n
#    import math
#    pcc = (n * sxy - sx * sy) / math.sqrt((n * sx2 - sx * sx) * (n * sy2 - sy * sy))
    print("Slope:", m)
    print("Intercept:", c)
#    print("Pearson's r:", pcc)
    return [m, c]

def lnr_ft2(ifln, nh, xc, yc):
    ''' (input-file, #-header-lines, x-col-#, y-col-#) -> (slope, intercept)

        Function to linear fit one dimensional data points
        using Least Square Method (or Simple Linear Regression)

        This function takes the following input:
        ifln = input filename from which data will be read
        nh = number of header lines to be skipped while reading file
        xc = column number of x (enter 1 for first column, not 0)
        yc = column number of y (enter 1 for first column, not 0)

        The default separator used for data in input file
        is space ' ', to change it to something else like
        comma, simply redefine sep below as sep = ','

        Also, to calculate Pearson Product-Moment Correlation Coefficient
        (or Pearson's r) simply remove all commented lines below, then
        program prints this quantity as well; to add it to returning list,
        simply replace return [m, c] --> return [m, c, pcc]
    '''
    ifl = open(ifln, 'r')
    sep = ' '
    x = []; y = []
    xc -= 1; yc -= 1
    n = 0
    for i in range(nh):
        ifl.readline()
    lyn = ifl.readline().strip()
    while lyn != '':
        n += 1
        j = 0; d0 = []
        while j < len(lyn):
            if lyn[j] != sep:
                k = 1
                while j+k < len(lyn) and lyn[j+k] != " ":
                    k += 1
                d0.append(lyn[j:j+k])
                j += k + 1
            else:
                j += 1
        x.append(float(d0[xc]))
        y.append(float(d0[yc]))
        lyn = ifl.readline().strip()

    sx = 0; sy = 0; sx2 = 0; sxy = 0; # sy2 = 0
    for i in range(n):
        sx = sx + x[i]
        sy = sy + y[i]
        sx2 = sx2 + x[i] * x[i]
        sxy = sxy + x[i] * y[i]
#        sy2 = sy2 + y[i] * y[i]
    m = (sxy - sx * sy / n)/(sx2 - sx * sx / n)
    c = sy / n - m * sx / n
#    import math
#    pcc = (n * sxy - sx * sy) / math.sqrt((n * sx2 - sx * sx) * (n * sy2 - sy * sy))
    print("Slope:", m)
    print("Intercept:", c)
#    print("Pearson's r:", pcc)
    return [m, c]
