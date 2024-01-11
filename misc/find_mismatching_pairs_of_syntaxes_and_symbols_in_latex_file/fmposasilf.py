# Last updated: 18-Aug-2016
# Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
# Source: https://github.com/udy11, https://gitlab.com/udy11
# Program to find mismatching pairs of syntaxes and symbols in Latex file

# ALL YOU NEED TO DO:
# Call function txusfn() with:
# ifl = tex file name
# mprs = opening and closing symbols or syntaxes (which
#        are different from each other like [] or \begin{} \end{})
# meqs = opening and closing symbols or syntaxes (which
#        are same, like $)

# NOTE:
# Use double backslash \\ to denote single backslash \ in python strings
# The function changes the order of lists mprs and meqs, pass their copies
#   if you wish to preserve their orders
# The program can be used to test codes in other languages as well but I have
#   not tested it elsewhere and may give undesired results due to each code's
#   special circumstances
# Also, I have not checked it in great detail for Latex, so it may give
#   undesired results in Latex too, in which case please inform me

def txusfn(ifl, mprs, meqs):
    def trnsp(mch):
        n = len(mch)
        for i in range(n):
            for j in range(i+1, n):
                if mch[i][0] == mch[j][0]:
                    print('WARNING: Recheck matches, multiple entries found for %s...' % mch[i][0])
                elif mch[i][0] in mch[j][0]:
                    t = mch[i]
                    mch[i] = mch[j]
                    mch[j] = t
        return mch

    def trnse(mch):
        n = len(mch)
        for i in range(n):
            for j in range(i+1, n):
                if mch[i] == mch[j]:
                    print('WARNING: Recheck matches, multiple entries found for %s...' % mch[i][0])
                elif mch[i] in mch[j]:
                    t = mch[i]
                    mch[i] = mch[j]
                    mch[j] = t
        return mch
    fyl = open(ifl, 'r')
    dt = fyl.read()
    fyl.close()
    n = len(dt)
    mprs = trnsp(mprs)
    npr = [(len(m[0]), len(m[1])) for m in mprs]
    np = len(mprs)
    meqs = trnse(meqs)
    neq = [len(m) for m in meqs]
    ne = len(meqs)
    bs = []
    mpn = {m : [0, 0] for m in mprs}
    men = {m : 0 for m in meqs}
    nn = 1
    k = 0
    eok = True
    while k < n:
        for j in range(np):
            if k+npr[j][0] < n and dt[k:k+npr[j][0]] == mprs[j][0]:
                bs.append((nn, mprs[j][0]))
                mpn[mprs[j]][0] += 1
                k += npr[j][0]
                break
            elif k+npr[j][1] < n and dt[k:k+npr[j][1]] == mprs[j][1]:
                mpn[mprs[j]][1] += 1
                if bs[-1][1] == mprs[j][0]:
                    bs.pop()
                else:
                    eok = False
                    print('Expecting companion of %s from line %i, but found %s at line %i...' % (bs[-1][1], bs[-1][0], mprs[j][1], nn))
                    input('Press any key to continue searching...')
                k += npr[j][1]
                break
        else:
            for j in range(ne):
                if k+neq[j] < n and dt[k:k+neq[j]] == meqs[j]:
                    men[meqs[j]] += 1
                    if len(bs) > 0 and bs[-1][1] == meqs[j]:
                        bs.pop()
                    else:
                        bs.append((nn, meqs[j]))
                    k += neq[j]
                    break
            else:
                if dt[k] == '\n':
                    nn += 1
                    k += 1
#                elif dt[k] == '%':
#                    while k < n and dt[k] != '\n':
#                        k += 1
                else:
                    k += 1
    for m in mpn:
        if mpn[m][0] != mpn[m][1]:
            eok = False
            print('Number of %s found = %i but number of %s found = %i...' % (m[0], mpn[m][0], m[1], mpn[m][1]))
    for m in men:
        if men[m] & 1 == 1:
            eok = False
            print('Odd number of entries (%i) found for %s' % (men[m], m))
    if eok:
        print('No mismatching found among input syntaxes and symbols...')
    return eok

# INPUTS
ifl = 'tex_error_sample.tex'
mprs = [('(', ')'),
        ('{', '}'),
        ('[', ']'),
        ('\\begin{document}', '\\end{document}'),
        ('\\begin{equation}', '\\end{equation}'),]
meqs = ['$$', '$']

txusfn(ifl, mprs, meqs)
