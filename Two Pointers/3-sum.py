'''
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target.
Return the sum of the three integers.

Assume that there will only be one solution

Example:
given array S = {-1 2 1 -4},
and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2)
'''

'''
Fix one pointer, two pointers starting from pointer + 1 and end on a sorted array
'''


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def threeSumClosest(self, A, B):
        if len(A) == 3:
            return sum(A)
        target = A[0] + A[1] + A[2] - B
        A = sorted(A)
        for i in xrange(len(A) - 2):
            j, k = i + 1, len(A) - 1
            while j < k:
                diff = A[i] + A[j] + A[k] - B
                if abs(diff) < abs(target):
                    target = diff
                if diff == 0:
                    return B
                elif diff > 0:
                    k -= 1
                else:
                    j += 1
        return target + B
