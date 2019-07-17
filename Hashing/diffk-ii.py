'''
Given an array A of integers and another non negative integer k, find if there exists 2 indices i and j such that A[i] - A[j] = k, i != j.

Example :

Input :

A : [1 5 3]
k : 2
Output :

1
as 3 - 1 = 2

Return 0 / 1 for this problem.
'''


class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, A, B):
        table = {}
        for i, e in enumerate(A):
            if e not in table:
                table[e] = set()
            table[e].add(i)
        for i, e in enumerate(A):
            t1 = e + B
            t2 = e - B
            if t1 in table and (i not in table[t1] or len(table[t1]) > 1):
                return 1
            if t2 in table and (i not in table[t2] or len(table[t2]) > 1):
                return 1
        return 0
