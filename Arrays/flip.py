'''
You are given a binary string(i.e. with characters 0 and 1) S consisting of characters S1, S2, …, SN. In a single operation, you can choose two indices L and R such that 1 ≤ L ≤ R ≤ N and flip the characters SL, SL+1, …, SR. By flipping, we mean change character 0 to 1 and vice-versa.

Your aim is to perform ATMOST one operation such that in final string number of 1s is maximised. If you don’t want to perform the operation, return an empty array. Else, return an array consisting of two elements denoting L and R. If there are multiple solutions, return the lexicographically smallest pair of L and R.

Notes:

Pair (a, b) is lexicographically smaller than pair (c, d) if a < c or, if a == c and b < d.
For example,

S = 010

Pair of [L, R] | Final string
_______________|_____________
[1 1]          | 110
[1 2]          | 100
[1 3]          | 101
[2 2]          | 000
[2 3]          | 001

We see that two pairs [1, 1] and [1, 3] give same number of 1s in final string. So, we return [1, 1].
Another example,

If S = 111

No operation can give us more than three 1s in final string. So, we return empty array [].
'''

'''
Observe that we want to maximum number of 0 and miminum number
of 1 in the subarray. We see 0 as adding 1 and 1 as substracting
1. Then we transform the problem into finding the maximum subarray
sum which can be solved with Kadane’s Algorithm
'''


class Solution:
    # @param A : string
    # @return a list of integers
    def flip(self, A):
        numZeros = 0
        maxZeros = 0
        curr_start = 0
        start = 0
        end = len(A) - 1
        for i, e in enumerate(A):
            if e == '0':
                numZeros += 1
            else:
                numZeros -= 1
            if numZeros < 0:
                numZeros = 0
                curr_start = i + 1
            if numZeros > maxZeros:
                maxZeros = numZeros
                start = curr_start
                end = i
        if maxZeros == 0:
            return []
        return [start + 1, end + 1]
