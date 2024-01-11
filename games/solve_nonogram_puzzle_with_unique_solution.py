# Last updated: 28-Mar-2016
# Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
# Source: https://github.com/udy11, https://gitlab.com/udy11
# Program to solve nonogram puzzle with unique solution

# Also commonly known as picross, hanjie, griddlers

# ALL YOU NEED TO DO:
# Call the function nngmsolv() with:
#   rws = list of list containing entries in rows (top to bottom)
#   cms = list of list containing entries in columns (left to right)
# and store its output in some temporary variable (say, gm)
# To see gm as text, use prtgm(gm) or to see the plot,
# use pltgm(gm)

import matplotlib.pyplot as plt

def rcfl(cs, gr):
    ''' Row Column Filler required to solve nonogram puzzle. '''
    nc = len(cs)
    ng = len(gr)
    r1 = [0 for i in range(nc)]
    r2 = [ng - sum(cs) - nc + 2] + [0 for i in range(nc - 1)]
    m = 0
    g = [-1 for i in range(ng)]
    gs = False
    def setg(n1, n2, g):
        nonlocal ng
        for i in range(n1, n2):
            g[i] = 1
        if n1 > 0:
            g[n1 - 1] = -1
        if n2 < ng:
            g[n2] = -1
    def frc():
        nonlocal m, nc, r1, r2, g, gs
        if m < nc - 1:
            for k in range(r1[m], r2[m]):
                setg(k, k + cs[m], g)
                r1[m + 1] = k + cs[m] + 1
                if m < nc - 2:
                    ss = sum(cs[m + 2:]) + nc - m - 2
                else:
                    ss = 0
                r2[m + 1] = ng - ss - cs[m + 1] + 1
                m += 1
                frc()
                g[r2[m] - 1 : r2[m] - 1 + cs[m]] = [-1] * cs[m]
                m -= 1
        else:
            for k in range(r1[m], r2[m]):
                setg(k, k + cs[m], g)
                ps = True
                for i in range(ng):
                    if gr[i] == 1 and g[i] != 1:
                        ps = False
                    if gr[i] == -1 and g[i] != -1:
                        ps = False
                if ps:
                    if not gs:
                        gs = list(g)
                    else:
                        for i in range(ng):
                            if gs[i] != g[i]:
                                gs[i] = 0
    frc()
    return gs

def nngmsolv(rws, cms):
    ''' Solves the nonogram puzzle. '''
    nr = len(rws)
    nc = len(cms)
    gm = [[0 for i in range(nc)] for j in range(nr)]
    cnt = True
    while cnt:
        gm1 = [list(gm[j]) for j in range(nr)]
        for i in range(nr):
            gt = rcfl(rws[i], gm[i])
            if not gt:
                cnt = False
            else:
                gm[i] = gt
        for j in range(nc):
            gt = [gm[i][j] for i in range(nr)]
            gt = rcfl(cms[j], gt)
            if not gt:
                cnt = False
            else:
                for i in range(nr):
                    gm[i][j] = gt[i]
        if not cnt:
            print('ERROR: inconsistent input...')
            break
        if gm1 == gm:
            print('ERROR: multiple solutions...')
            break
        cnt = False
        for r in gm:
            if 0 in r:
                cnt = True
    return gm

def prtgm(g):
    ''' Text representation of solution of nonogram puzzle '''
    print('_' * (len(g[0]) + 2))
    for r in g:
        print('|', end = '')
        for c in r:
            if c == 1:
                print('M', end = '')
            elif c == 0:
                print('*', end = '')
            elif c == -1:
                print(' ', end = '')
        print('|')
    print('-' * (len(g[0]) + 2))

def pltgm(g):
    ''' Plot of solution of nonogram puzzle '''
    plt.imshow(g, interpolation = 'none', aspect = 1)
    plt.show()

# INPUT
rws = [[1,1,1,1,1,3],[1,1,1,1,1,1],[1,3,1,1,2],[2,1,1,1,1,1],[2,1,1,1],[1,1,1],[1,3,1],[1,1,2,5],[2,2,2,2,1],[1,3,2,2],[2,2,3],[4,4],[4,1,1,6],[1,4,1,1,2],[4,4,3,1]]
cms = [[2],[2,2],[2,2,3,1,1],[1,2,2,1,1],[2,1,1,1],[3,2,2],[2,1,3],[3,1,3,1,1],[2,1,1,1,2],[1,4,1,1],[2,3,1,2],[2,3,1],[1,2,2],[3,3,2,1],[4,1,5],[1,1,1,1],[1,2,1],[3,2],[2],[0]]

gm = nngmsolv(rws, cms)

# To print output as text
prtgm(gm)
# To plot output
pltgm(gm)
