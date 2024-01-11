# Last updated: 26-Sept-2014
# Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
# Source: https://github.com/udy11, https://gitlab.com/udy11
# Program to solve "Move" puzzle game

# ALL YOU NEED TO DO:
# Under the INPUT section:
#   grid (tuple of str) = grid with entries: 'X' for wall, '_' for space and color boxes by their respective letters
#   blls (tuple of str) = balls in grid with entries: '_' for no-ball and colors by their respective letters
# With inputs grid and blls, define an object (say gm) of class movegame
# Call process gm.solve() to solve the puzzle (store it in say soln)
# Print solution by calling the process gm.prntsoln(soln)

# GAME RULES:
# A grid is given (e.g. check in INPUT) with 'X' as wall and '_' as blank space
# The color codes (e.g. 'R' for Red, etc.) represent color boxes
# An initial grid of balls is also specified denoting the position of balls
# If a move "up" is made, then all possible balls move up in the grid
# The objective of the game is to make moves (up, down, left, right) such that all balls
# reach their respective color boxes

# NOTE:
# Game is a well known puzzle game and can be checked on android
#   app "Move: a brain shifting game" by "Nitako Brain Puzzles"
# Link: https://play.google.com/store/apps/details?id=com.nitako.move
# Program assumes that grid and balls are correct and consistent
# The program can work for rectangular grids
# Algorithm is Brute Force checking
# Example given is Level 51 from "Killer Move" pack from the app

import copy
import operator

class movegame:
    def __init__(self, grid, balls):
        ''' Initializes grid, number of rows and columns and
            positions of colors in grid and balls. '''
        self.grid = grid
        self.nrow = len(self.grid)
        self.ncol = len(self.grid[0])
        self.grcpos = {}
        self.bpud = []
        for i in range(self.nrow):
            for j in range(self.ncol):
                if balls[i][j] != '_':
                    self.bpud.append([i, j, balls[i][j]])
                if self.grid[i][j] != '_' and self.grid[i][j] != 'X':
                    self.grcpos[(i, j)] = self.grid[i][j]
        self.nbls = len(self.bpud)
    def chksoln(self, blls):
        ''' Checks if the puzzle has been solved. '''
        for bps in blls:
            if (bps[0], bps[1]) in self.grcpos:
                if self.grcpos[(bps[0], bps[1])] != bps[2]:
                    return False
            else:
                return False
        return True
    def mvup(self, bpud):
        ''' Moves the balls up '''
        mvd = False
        for m in range(self.nbls):
            if bpud[m][0] != 0:
                m0 = m
                break
        else:
            m0 = self.nbls
        for m in range(m0, self.nbls):
            if bpud[m][0] != 0 and self.grid[bpud[m][0] - 1][bpud[m][1]] != 'X':
                ch = True
                for k in range(m):
                    if bpud[k][0] == bpud[m][0] - 1 and bpud[k][1] == bpud[m][1]:
                        ch = False
                        break
                if ch:
                    bpud[m][0] -= 1
                    mvd = True
        return mvd
    def mvdn(self, bpud):
        ''' Moves the balls down '''
        mvd = False
        for m in range(self.nbls - 1, -1, -1):
            if bpud[m][0] != self.nrow - 1:
                m0 = m
                break
        else:
            m0 = -1
        for m in range(m0, -1, -1):
            if bpud[m][0] != self.nrow - 1 and self.grid[bpud[m][0] + 1][bpud[m][1]] != 'X':
                ch = True
                for k in range(m + 1, self.nbls):
                    if bpud[k][0] == bpud[m][0] + 1 and bpud[k][1] == bpud[m][1]:
                        ch = False
                        break
                if ch:
                    bpud[m][0] += 1
                    mvd = True
        return mvd
    def mvlf(self, bplr):
        ''' Moves the balls left '''
        mvd = False
        for m in range(self.nbls):
            if bplr[m][1] != 0:
                m0 = m
                break
        else:
            m0 = self.nbls
        for m in range(m0, self.nbls):
            if bplr[m][1] != 0 and self.grid[bplr[m][0]][bplr[m][1] - 1] != 'X':
                ch = True
                for k in range(m):
                    if bplr[k][0] == bplr[m][0] and bplr[k][1] == bplr[m][1] - 1:
                        ch = False
                        break
                if ch:
                    bplr[m][1] -= 1
                    mvd = True
        return mvd
    def mvrt(self, bplr):
        ''' Moves the balls right '''
        mvd = False
        for m in range(self.nbls - 1, -1, -1):
            if bplr[m][1] != self.ncol - 1:
                m0 = m
                break
        else:
            m0 = -1
        for m in range(m0, -1, -1):
            if bplr[m][1] != self.ncol - 1 and self.grid[bplr[m][0]][bplr[m][1] + 1] != 'X':
                ch = True
                for k in range(m + 1, self.nbls):
                    if bplr[k][0] == bplr[m][0] and bplr[k][1] == bplr[m][1] + 1:
                        ch = False
                        break
                if ch:
                    bplr[m][1] += 1
                    mvd = True
        return mvd
    def prntsoln(self, st):
        ''' Prints the solution obtained from solve() '''
        for s in st:
            if s == 'u':
                print('up', end=' ')
            elif s == 'd':
                print('down', end=' ')
            elif s == 'l':
                print('left', end=' ')
            elif s == 'r':
                print('right', end=' ')
    def solve(self):
        ''' Solves the puzzle by brute force checking '''
        tbls = {'' : self.bpud}
        while True:
            tmp = {}
            for tk in tbls:
                tbls[tk].sort()
                tt = copy.deepcopy(tbls[tk])
                if self.mvup(tt):
                    tmp[tk + 'u'] = tt
                    if self.chksoln(tt):
                        return tk + 'u'
                tt = copy.deepcopy(tbls[tk])
                if self.mvdn(tt):
                    tmp[tk + 'd'] = tt
                    if self.chksoln(tt):
                        return tk + 'd'
                tbls[tk].sort(key=operator.itemgetter(1))
                tt = copy.deepcopy(tbls[tk])
                if self.mvlf(tt):
                    tmp[tk + 'l'] = tt
                    if self.chksoln(tt):
                        return tk + 'l'
                tt = copy.deepcopy(tbls[tk])
                if self.mvrt(tt):
                    tmp[tk + 'r'] = tt
                    if self.chksoln(tt):
                        return tk + 'r'
            tbls = tmp

# INPUT
grid = ('_X__R',
        '_BXXG',
        'X_OX_',
        '___Y_',
        '_____')
blls = ('B_RGY',
        'O____',
        '_____',
        '_____',
        '_____')

gm = movegame(grid, blls)
soln = gm.solve()
gm.prntsoln(soln)
