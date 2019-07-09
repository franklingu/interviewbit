'''
Given an array of N integers, find the pair of integers in the array which have minimum XOR value. Report the minimum XOR value.

Examples :
Input
0 2 5 7
Output
2 (0 XOR 2)
Input
0 4 7 9
Output
3 (4 XOR 7)

Constraints:
2 <= N <= 100 000
0 <= A[i] <= 1 000 000 000
'''


class Solution:
    # @param A : list of integers
    # @return an integer
    def findMinXor(self, A):
        prev = None
        A.sort()
        mm = None
        for c in A:
            if prev is None:
                prev = c
                continue
            if mm is None:
                mm = prev ^ c
                prev = c
                continue
            mm = min(mm, prev ^ c)
            prev = c
        return mm
