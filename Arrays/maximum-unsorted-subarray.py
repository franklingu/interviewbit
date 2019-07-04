'''
You are given an array (zero indexed) of N non-negative integers, A0, A1 ,…, AN-1.
Find the minimum sub array Al, Al+1 ,…, Ar so if we sort(in ascending order) that sub array, then the whole array should get sorted.
If A is already sorted, output -1.

Example :

Input 1:

A = [1, 3, 2, 4, 5]

Return: [1, 2]

Input 2:

A = [1, 2, 3, 4, 5]

Return: [-1]
In the above example(Input 1), if we sort the subarray A1, A2, then whole array A should get sorted.
'''

'''
Method 1:
from left to right calculate the current max;
from right to left calculate the current min and reverse.
For a completely sorted input, max from left and min from right
should always be the same.

Method 2:
sort A and store it as B. If any corresponding value
does not match, we find some part that needs to be fixed.
'''


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def subUnsort(self, A):
        mmax, mmin = [0], [len(A) - 1]
        for i in range(len(A) - 2, -1, -1):
            if A[mmin[-1]] >= A[i]:
                mmin.append(i)
            else:
                mmin.append(mmin[-1])
        for i in range(1, len(A)):
            if A[mmax[-1]] <= A[i]:
                mmax.append(i)
            else:
                mmax.append(mmax[-1])
        mmin = mmin[::-1]
        min_idx, max_idx = len(A), -1
        for i in range(len(A)):
            if mmin[i] != mmax[i]:
                min_idx = min(i, min_idx)
                max_idx = max(i, max_idx)
        if max_idx <= min_idx:
            return [-1]
        return [min_idx, max_idx]
    
    def subUnsort2(self, A):
        B = sorted(A)
        min_idx, max_idx = len(A), -1
        for i in range(len(A)):
            if A[i] != B[i]:
                min_idx = min(i, min_idx)
                max_idx = max(i, max_idx)
        if max_idx <= min_idx:
            return [-1]
        return [min_idx, max_idx]
