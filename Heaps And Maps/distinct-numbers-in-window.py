'''
You are given an array of N integers, A1, A2 ,…, AN and an integer K. Return the of count of distinct numbers in all windows of size K.

Formally, return an array of size N-K+1 where i’th element in this array contains number of distinct elements in sequence Ai, Ai+1 ,…, Ai+k-1.

Note:

If K > N, return empty array.
For example,

A=[1, 2, 1, 3, 4, 3] and K = 3

All windows of size K are

[1, 2, 1]
[2, 1, 3]
[1, 3, 4]
[3, 4, 3]

So, we return an array [2, 3, 3, 2].
'''


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def dNums(self, A, B):
        track = {}
        ret = []
        for i, a in enumerate(A):
            if i < B:
                track[a] = track.get(a, 0) + 1
                continue
            ret.append(len(track))
            val = A[i - B]
            if track[val] == 1:
                del track[val]
            else:
                track[val] = track[val] - 1
            track[a] = track.get(a, 0) + 1
        ret.append(len(track))
        return ret
