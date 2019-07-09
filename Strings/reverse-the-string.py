'''
Given an input string, reverse the string word by word.

Example:

Given s = "the sky is blue",

return "blue is sky the".

A sequence of non-space characters constitutes a word.
Your reversed string should not contain leading or trailing spaces, even if it is present in the input string.
If there are multiple spaces between words, reduce them to a single space in the reversed string.
'''

class Solution:
    # @param A : string
    # @return string
    def reverseWords(self, A):
        words = []
        start = False
        for c in A:
            if c == ' ':
                start = False
            elif start:
                words[-1].append(c)
            else:
                words.append([c])
                start = True
        return ' '.join(reversed([''.join(w) for w in words]))
