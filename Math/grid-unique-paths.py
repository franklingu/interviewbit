'''
A robot is located at the top-left corner of an A x B grid (marked ‘Start’ in the diagram below).

Path Sum: Example 1

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked ‘Finish’ in the diagram below).

How many possible unique paths are there?

Note: A and B will be such that the resulting answer fits in a 32 bit signed integer.

Example :

Input : A = 2, B = 2
Output : 2

2 possible routes : (0, 0) -> (0, 1) -> (1, 1) 
              OR  : (0, 0) -> (1, 0) -> (1, 1)

'''

'''
N steps, select M steps to be right move and N - M to be down move.
So it is a combination problem.
'''

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def uniquePaths(self, A, B):
        def fact(h, l):
            ret = 1
            for i in xrange(l, h + 1):
                ret *= i
            return ret
        
        pl, rl = A + B - 2, B - 1
        return fact(pl, A - 1 + 1) / fact(rl, 1)