'''
You are given an array of N integers, A1, A2 ,…, AN. Return maximum value of f(i, j) for all 1 ≤ i, j ≤ N.
f(i, j) is defined as |A[i] - A[j]| + |i - j|, where |x| denotes absolute value of x.

For example,

A=[1, 3, -1]

f(1, 1) = f(2, 2) = f(3, 3) = 0
f(1, 2) = f(2, 1) = |1 - 3| + |1 - 2| = 3
f(1, 3) = f(3, 1) = |1 - (-1)| + |1 - 3| = 4
f(2, 3) = f(3, 2) = |3 - (-1)| + |2 - 3| = 5

So, we return 5.
'''

'''
|A[i] - A[j]| + |i - j| can be expressed as:
1. A[i] >= A[j] and i > j: (A[i] + i) - (A[j] + j)
2. A[i] >= A[j] and i < j: (A[i] - i) - (A[j] - j)
3. A[i] < A[j] and i > j: (A[j] - j) - (A[i] - i)
4. A[i] < A[j] and i < j: (A[j] + j) - (A[i] + i)

There are two cases: A[i] + i or A[i] - i
find the min and max of A[i] + i, A[i] - i and we will get
the max diff by take the max of the two diffs
'''


class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArr(self, A):
        if len(A) < 0:
            return 0
        min1 = max1 = A[0]
        min2 = max2 = A[0]
        for i, a in enumerate(A):
            min1 = min(min1, a - i)
            min2 = min(min2, a + i)
            max1 = max(max1, a - i)
            max2 = max(max2, a + i)
        return max(max1 - min1, max2 - min2)
