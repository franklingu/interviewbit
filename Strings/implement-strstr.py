'''
Implement strStr().

 strstr - locate a substring ( needle ) in a string ( haystack ).
Try not to use standard library string functions for this question.

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 NOTE: Good clarification questions:
What should be the return value if the needle is empty?
What if both haystack and needle are empty?
For the purpose of this problem, assume that the return value should be -1 in both cases.
'''

'''
Classic KMP algorithm -- build and use LPS
'''


class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def strStr(self, A, B):
        def computeLPS(B):
            lps = [0] * len(B)
            l, i = 0, 1
            while i < len(B):
                if B[i] == B[l]:
                    l += 1
                    lps[i] = l
                    i += 1
                else:
                    if l > 0:
                        l = lps[l - 1]
                    else:
                        lps[i] = 0
                        i += 1
            return lps

        if len(B) > len(A):
            return -1
        lps = computeLPS(B)
        i, j = 0, 0
        while i < len(A):
            if A[i] == B[j]:
                i += 1
                j += 1
                if j >= len(B):
                    return i - len(B)
            else:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        return -1
