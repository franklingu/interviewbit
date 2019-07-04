'''
Given an array A of integers, find the maximum of j - i subjected to the constraint of A[i] <= A[j].

If there is no solution possible, return -1.

Example :

A : [3 5 4 2]

Output : 2 
for the pair (3, 4)
'''

'''
From left to right, get minimum so far;
from right to left, get maximum so far and reverse it.
Then starting from 0 index for both result, if current minimum
is <= current maximum, we can try to increase maximum index to
right by 1, try to explore a potentially smaller maximum but bigger
index; if >, then current minimum is too big for the current
maximum, increase minimum index by 1. The idea is quite like
substring with window.
'''

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, A):
        if len(A) < 2:
            return 0
        mmax = []
        mmin = []
        for i, e in enumerate(A):
            if i == 0:
                mmin.append(i)
                continue
            if e < A[mmin[-1]]:
                mmin.append(i)
            else:
                mmin.append(mmin[-1])
        for i, e in enumerate(reversed(A)):
            if i == 0:
                mmax.append(len(A) - i - 1)
                continue
            if e > A[mmax[-1]]:
                mmax.append(len(A) - i - 1)
            else:
                mmax.append(mmax[-1])
        mmax = list(reversed(mmax))
        ret = -1
        i, j = 0, 0
        while i < len(A) and j < len(A):
            if A[mmin[i]] <= A[mmax[j]]:
                ret = max(ret, j - i)
                j += 1
            else:
                i += 1
        return ret