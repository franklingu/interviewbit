'''
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note:

 Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
The solution set must not contain duplicate triplets. For example, given array S = {-1 0 1 2 -1 -4}, A solution set is:
(-1, 0, 1)
(-1, -1, 2)
'''

'''
Same as 3-sum
'''


class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def threeSum(self, A):
        ret = set()
        A = sorted(A)
        for i, e in enumerate(A):
            j, k = i + 1, len(A) - 1
            while j < k:
                ss = e + A[j] + A[k]
                if ss == 0:
                    ret.add((e, A[j], A[k]))
                    j += 1
                    k -= 1
                elif ss < 0:
                    j += 1
                else:
                    k -= 1
        return [list(e) for e in ret]
