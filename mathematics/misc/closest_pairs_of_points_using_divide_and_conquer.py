# Last updated: 2022-Dec-12
# Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
# Source: https://github.com/udy11, https://gitlab.com/udy11

# Function to find closest distance among all pairs of
# points in a 2d plane using divide-and-conquer algorithm

# Time Complexity: O(n * log(n)**2)

# Reference:
# https://people.csail.mit.edu/indyk/6.838-old/handouts/lec17.pdf
# https://www.geeksforgeeks.org/closest-pair-of-points-using-divide-and-conquer-algorithm/

import numpy as np

def closestPairs2d(xys):
    ''' (2d numpy array) -> float
        Finds closest distance among all pairs of points in array xys
        INPUT:
        xys = x,y positions of points in plane as ((x0,y0),(x1,y1),...) [2d numpy array]
        OUTPUT:
        closest distance among all points [float]
    '''
    def distance(p0, p1):
        return np.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)
    def closest(ps, n):
        if n == 2:
            return distance(ps[0], ps[1])
        elif n == 3:
            return min((distance(ps[0], ps[1]), distance(ps[0], ps[2]), distance(ps[1], ps[2])))
        nmid = n // 2
        xmid = ps[nmid, 0]
        d0 = min(closest(ps[:nmid], nmid), closest(ps[nmid:], n - nmid))
        strip = []
        for i in range(n):
            if abs(ps[i,0] - xmid) < d0:
                strip.append(ps[i])
        strip = np.array(strip)
        strip = strip[strip[:,1].argsort()]
        nstrip = len(strip)
        for i in range(nstrip):
            j = i + 1
            while (j < nstrip) and (strip[j,1] - strip[i,1] < d0):
                d0 = distance(strip[i], strip[j])
                j += 1
        return d0
    n = len(xys)
    xys0 = xys[xys[:,0].argsort()]
    return closest(xys0, n)

if __name__ == '__main__':
    a = np.array([[2, 3],
                  [0, 4],
                  [-8, 5],
                  [9, 5],
                  [3, 1],
                  [8, -6],
                  [2.1, 3],
                  [-3, 6],
                  [0, 1]])
    print(closestPairs2d(a))
