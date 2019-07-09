'''
You are given an array of N non-negative integers, A0, A1 ,…, AN-1.
Considering each array element Ai as the edge length of some line segment, count the number of triangles which you can form using these array values.

Notes:

You can use any value only once while forming each triangle. Order of choosing the edge lengths doesn’t matter. Any triangle formed should have a positive area.

Return answer modulo 109 + 7.

For example,

A = [1, 1, 1, 2, 2]

Return: 4
'''

'''
Build on top of 3-sum
'''


class Solution:
    # @param A : list of integers
    # @return an integer
    def nTriang(self, A):
        A.sort()
        count = 0
        l = len(A)
        for i in xrange(l - 2):
            k = i + 2
            for j in xrange(i + 1, l - 1):
                while k < l and A[i] + A[j] > A[k]:
                    k += 1
                count += k - j - 1
        return count % (10 ** 9 + 7)
