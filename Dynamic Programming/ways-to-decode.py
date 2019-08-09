'''
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

Example :

Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.
'''


class Solution:
    # @param A : string
    # @return an integer
    def numDecodings(self, A):
        def numWays(A, track, index):
            if index == len(A):
                return 1
            elif index > len(A):
                return 0
            curr = A[index]
            if curr == '0':
                return 0
            if index < len(A) - 1:
                nn = A[index + 1]
                s = int(curr + nn)
                if s <= 26:
                    result = numWays(A, track, index + 2)
                else:
                    result = 0
            else:
                result = 0
            result += numWays(A, track, index + 1)
            track[A[index:]] = result
            return result

        track = {}
        result = numWays(A, track, 0)
        # print(track)
        return result
