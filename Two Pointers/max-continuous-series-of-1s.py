'''
You are given with an array of 1s and 0s. And you are given with an integer M, which signifies number of flips allowed.
Find the position of zeros which when flipped will produce maximum continuous series of 1s.

For this problem, return the indices of maximum continuous series of 1s in order.

Example:

Input :
Array = {1 1 0 1 1 0 0 1 1 1 }
M = 1

Output :
[0, 1, 2, 3, 4]

If there are multiple possible solutions, return the sequence which has the minimum start index.
'''


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def maxone(self, nums, K):
        mmax, mstart = 0, 0
        start = 0
        zeros = 0
        for i, n in enumerate(nums):
            if n == 1:
                clen = i - start + 1
                if clen > mmax:
                    mmax = clen
                    mstart = start
            else:
                zeros += 1
                while zeros > K:
                    if nums[start] == 0:
                        zeros -= 1
                    start += 1
                clen = i - start + 1
                if clen > mmax:
                    mmax = clen
                    mstart = start
        if len(nums) - start > mmax:
            mmax = len(nums) - start
            mstart = start
        return [i for i in xrange(mstart, mstart + mmax)]
