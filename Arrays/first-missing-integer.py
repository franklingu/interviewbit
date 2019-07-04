'''
Given an unsorted integer array, find the first missing positive integer.

Example:

Given [1,2,0] return 3,

[3,4,-1,1] return 2,

[-8, -7, -6] returns 1

Your algorithm should run in O(n) time and use constant space.
'''


class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        missing = None
        mm = max(A)
        ss = set(A)
        for i in xrange(1, max(A) + 2):
            if i not in ss:
                return i
        return 1
