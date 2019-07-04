'''
Give a N*N square matrix, return an array of its anti-diagonals. Look at the example for more details.

Example:

        
Input:  

1 2 3
4 5 6
7 8 9

Return the following :

[ 
  [1],
  [2, 4],
  [3, 5, 7],
  [6, 8],
  [9]
]


Input : 
1 2
3 4

Return the following  : 

[
  [1],
  [2, 3],
  [4]
]
'''

'''
from the first row, and then start from last column
'''


class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def diagonal(self, A):
        if len(A) < 1:
            return []
        m = []
        for i, elem in enumerate(A[0]):
            x, y = i, 0
            row = []
            while x >= 0:
                row.append(A[y][x])
                x -= 1
                y += 1
            m.append(row)
        for i, row in enumerate(A):
            x, y = len(A[0]) - 1, i
            if y == 0:
                continue
            while y < len(A):
                row.append(A[y][x])
                x -= 1
                y += 1
            m.append(row)
        return m
