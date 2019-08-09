'''
Given a grid of size m * n, lets assume you are starting at (1,1) and your goal is to reach (m,n). At any instance, if you are on (x,y), you can either go to (x, y + 1) or (x + 1, y).

Now consider if some obstacles are added to the grids. How many unique paths would there be?
An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Example :
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.

 Note: m and n will be at most 100.
'''

'''
DP or DFS
'''


class Solution:
    # @param A : list of list of integers
    # @return an integer
    def uniquePathsWithObstacles(self, A):
        if not A:
            return 0
        curr = (0, 0)
        m, n = len(A), len(A[0])
        stack = [curr]
        result = 0
        while len(stack) > 0:
            curr = stack.pop()
            if A[curr[0]][curr[1]] == 1:
                continue
            if curr[0] + 1 == m and curr[1] + 1 == n:
                result += 1
                continue
            neighbors = []
            if curr[1] < n - 1:
                neighbors.append((curr[0], curr[1] + 1))
            if curr[0] < m - 1:
                neighbors.append((curr[0] + 1, curr[1]))
            for nei in neighbors:
                stack.append(nei)
        return result
