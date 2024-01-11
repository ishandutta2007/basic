# Last updated: 09-Oct-2014
# Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
# Source: https://github.com/udy11, https://gitlab.com/udy11
# Program to solve Sudoku of any size using Backtracking

# ALL YOU NEED TO DO:
# Define sudoku object (say, sdk) with input grid
#   and number of rows of the small box
# Print output of function solve() on the object sdk

# NOTE:
# Grid should be a list of list of numbers
# Sudoku numbers should be 1, 2, 3, ...
# 0 in the grid stands for empty cell
# Algorithm for solving is Backtracking
# Input is expected to be consistent
# If solve() returns grid with 0 entries, it means the
#   Sudoku cannot be solved
# For a Sudoku with multiple solutions, solve() returns
#   one of the solutions

class sudoku():
    def __init__(self, grid0, nr):
        self.grid0 = grid0
        self.n = len(grid0)
        self.nr = nr
        self.nc = self.n // self.nr
        self.n1 = self.n + 1

    def solve(self):
        def ipt(r, c, k):
            for j in range(c):
                if grid[r][j] == k:
                    return False
            for j in range(c+1, self.n):
                if grid[r][j] == k:
                    return False
            for i in range(r):
                if grid[i][c] == k:
                    return False
            for i in range(r+1, self.n):
                if grid[i][c] == k:
                    return False
            r0 = (r // self.nr) * self.nr
            c0 = (c // self.nc) * self.nc
            for i in range(r0, r):
                for j in range(c0, c):
                    if grid[i][j] == k:
                        return False
            c1 = c0 + self.nc
            for i in range(r0, r):
                for j in range(c+1, c1):
                    if grid[i][j] == k:
                        return False
            r1 = r0 + self.nr
            for i in range(r+1, r1):
                for j in range(c0, c):
                    if grid[i][j] == k:
                        return False
            for i in range(r+1, r1):
                for j in range(c+1, c1):
                    if grid[i][j] == k:
                        return False
            return True
        def uas():
            for i in range(self.n):
                for j in range(self.n):
                    if emp[i][j]:
                        return (i, j)
            return False
        def slv():
            tt = uas()
            if tt:
                r, c = tt
                for k in range(1, self.n1):
                    if ipt(r, c, k):
                        grid[r][c] = k
                        emp[r][c] = False
                        if slv():
                            return True
                        grid[r][c] = 0
                        emp[r][c] = True
            else:
                return True
        grid = [list(g) for g in self.grid0]
        emp = [[False for i in range(self.n)] for j in range(self.n)]
        for i in range(self.n):
            for j in range(self.n):
                if grid[i][j] == 0:
                    emp[i][j] = True
        slv()
        return grid

# Sudoku of size 6 x 6 with 2 x 3 size boxes
g0 = [[0, 0, 3, 0, 5, 0],
      [2, 4, 5, 0, 3, 0],
      [0, 0, 0, 0, 6, 2],
      [1, 2, 0, 0, 0, 0],
      [0, 5, 0, 3, 1, 6],
      [0, 6, 0, 4, 0, 0]]

# World's Hardest Sudoku of size 9 x 9
g1 = [[8, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 3, 6, 0, 0, 0, 0, 0],
      [0, 7, 0, 0, 9, 0, 2, 0, 0],
      [0, 5, 0, 0, 0, 7, 0, 0, 0],
      [0, 0, 0, 0, 4, 5, 7, 0, 0],
      [0, 0, 0, 1, 0, 0, 0, 3, 0],
      [0, 0, 1, 0, 0, 0, 0, 6, 8],
      [0, 0, 8, 5, 0, 0, 0, 1, 0],
      [0, 9, 0, 0, 0, 0, 4, 0, 0]]

sdk = sudoku(g0, 2)
print(sdk.solve())
