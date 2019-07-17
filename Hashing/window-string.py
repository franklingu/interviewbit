'''
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in linear time complexity.
Note that when the count of a character C in T is N, then the count of C in minimum window in S should be at least N.

Example :

S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC"

 Note:
If there is no such window in S that covers all characters in T, return the empty string ''.
If there are multiple such windows, return the first occurring minimum window ( with minimum start index ).
'''


class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def minWindow(self, A, B):
        if len(B) == 0:
            return B
        track = {}
        for b in B:
            if b not in track:
                track[b] = 0
            track[b] += 1
        mlen, actual_start, start = None, 0, 0
        blen = len(B)
        for i, a in enumerate(A):
            if a not in track:
                continue
            if track[a] > 0:
                blen -= 1
            track[a] -= 1
            if blen > 0:
                continue
            while start <= i:
                if A[start] not in track:
                    start += 1
                elif track[A[start]] < 0:
                    track[A[start]] += 1
                    start += 1
                else:
                    break
            clen = i - start + 1
            if mlen is None or mlen > clen:
                mlen = clen
                actual_start = start
        return A[actual_start: actual_start + mlen] if mlen is not None else ''
