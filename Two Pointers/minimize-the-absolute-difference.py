'''
Given three sorted arrays A, B and Cof not necessarily same sizes.

Calculate the minimum absolute difference between the maximum and minimum number from the triplet a, b, c such that a, b, c belongs arrays A, B, C respectively.
i.e. minimize | max(a,b,c) - min(a,b,c) |.

Example :

Input:

A : [ 1, 4, 5, 8, 10 ]
B : [ 6, 9, 15 ]
C : [ 2, 3, 6, 6 ]
Output:

1
Explanation: We get the minimum difference for a=5, b=6, c=6 as | max(a,b,c) - min(a,b,c) | = |6-5| = 1.
'''


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer
    def solve(self, A, B, C):
        def findMaxMinIdx(arrs, indices):
            mm = max(arrs[0][indices[0]], arrs[1][indices[1]], arrs[2][indices[2]])
            mi = min(arrs[0][indices[0]], arrs[1][indices[1]], arrs[2][indices[2]])
            if arrs[0][indices[0]] == mm:
                maxidx = 0
            elif arrs[1][indices[1]] == mm:
                maxidx = 1
            else:
                maxidx = 2
            if arrs[0][indices[0]] == mi:
                minidx = 0
            elif arrs[1][indices[1]] == mi:
                minidx = 1
            else:
                minidx = 2
            return maxidx, minidx

        def findAbsDiff(arrs, indices, maxidx, minidx):
            return arrs[maxidx][indices[maxidx]] - arrs[minidx][indices[minidx]]

        if not A or not B or not C:
            return 0
        arrs = [A, B, C]
        indices = [0, 0, 0]
        ret = None
        while True:
            maxidx, minidx = findMaxMinIdx(arrs, indices)
            val = findAbsDiff(arrs, indices, maxidx, minidx)
            if ret is None:
                ret = val
            else:
                ret = min(ret, val)
            indices[minidx] += 1
            if indices[minidx] >= len(arrs[minidx]):
                break
        return ret

    def triplet(self, a, b, c):
        return abs(max(a,b,c)-min(a,b,c))

    def solve2(self, A, B, C):
        m=float("inf")
        n1,n2=len(B),len(C)
        for i in A:
            l1,l2=0,0
            while (l1<n1 and l2<n2):
                t=self.triplet(i, B[l1], C[l2])
                if t==0:
                    return t
                if t<m:
                    m=t
                if B[l1]<=C[l2]:
                    l1+=1
                else:
                    l2+=1
        return m
