'''
Given a string S, find the longest palindromic substring in S.

Substring of string S:

S[i...j] where 0 <= i <= j < len(S)

Palindrome string:

A string which reads the same backwards. More formally, S is palindrome if reverse(S) = S.

Incase of conflict, return the substring which occurs first ( with the least starting index ).

Example :

Input : "aaaabaaa"
Output : "aaabaaa"
'''

'''
Starting for len(A), for each l, try to find a substring with l that is a palindrome. If found,
return the current substring. Otherwise l is too large.
'''


class Solution:
    # @param A : string
    # @return a strings
    def longestPalindrome(self, A):
        l = len(A)
        while l > 0:
            for i in xrange(0, len(A) - l + 1):
                start = i
                end = i + l - 1
                while start < end:
                    if A[start] != A[end]:
                        break
                    start += 1
                    end -= 1
                else:
                    return A[i:i + l]
            l -= 1
        return ''
