'''
You are given a string. The only operation allowed is to insert characters in the beginning of the string. How many minimum characters are needed to be inserted to make the string a palindrome string

Example:
Input: ABC
Output: 2
Input: AACECAAAA
Output: 2
'''

'''
Simple method: starting from last index + 1, get substring from start to target
index, compare with reversed string and see they are same. If they are same,
then from target index to end of string we do not need to add any characters
to make them palindrome.

Complex method: construct a string from A + special char + A[::-1]. Compute LPS
array for the new string and the result is len(A) - LPS[-1]. The definition of
LPS, find the length of longest prefix which is also a suffix ending at the
current position.
So for this case, the special character will break any count before that. And
start from after the special character, we compute LPS. By the end, the longest
prefix which is also suffix means that this part is already a palindrome. Whatever
is left will be the characters needed to make original string a palindrome.
'''


class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        if A == A[::-1]:
            return 0
        j = len(A) - 1
        while j >= 0:
            B = A[:j]
            if B == B[::-1]:
                return len(A) - j
            j -= 1
        return len(A) - 1

    # @param A : string
    # @return an integer
    def solve2(self, A):
        def computeLPSArray(string):
            M = len(string)
            lps = [None] * M
            length = 0
            lps[0] = 0 # lps[0] is always 0
            # the loop calculates lps[i]
            # for i = 1 to M-1
            i = 1
            while i < M:
                if string[i] == string[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                else: # (str[i] != str[len])
                    # This is tricky. Consider the example.
                    # AAACAAAA and i = 7. The idea is
                    # similar to search step.
                    if length != 0:
                        length = lps[length - 1]
                        # Also, note that we do not
                        # increment i here
                    else: # if (len == 0)
                        lps[i] = 0
                        i += 1
            return lps

        # Method returns minimum character
        # to be added at front to make
        # string palindrome
        def getMinCharToAddedToMakeStringPalin(string):
            revStr = string[::-1]
            # Get concatenation of string,
            # special character and reverse string
            concat = string + "$" + revStr
            # Get LPS array of this
            # concatenated string
            lps = computeLPSArray(concat)
            # By subtracting last entry of lps
            # vector from string length, we
            # will get our result
            return len(string) - lps[-1]

        return getMinCharToAddedToMakeStringPalin(A)
