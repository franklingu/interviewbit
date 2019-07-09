'''
Given a sorted array of integers, find the starting and ending position of a given target value.

Your algorithm’s runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example:

Given [5, 7, 7, 8, 8, 10]

and target value 8,

return [3, 4].
'''

'''
Borrow the idea from Python's bisect module.
bisect_left ==> index, whose left elements are smaller than B
bisect_right ==> index, whose left elements are not greater than B
the middle are what we are looking for
'''


import bisect


class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def searchRange(self, A, B):
        if not A:
            return [0, 0]
        left = bisect.bisect_left(A, B)
        right = bisect.bisect_right(A, B)
        if left == len(A) or left == right:
            return [-1, -1]
        return [left, right - 1]
