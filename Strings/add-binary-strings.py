'''
Given two binary strings, return their sum (also a binary string).

Example:

a = "100"

b = "11"
Return a + b = “111”.
'''

'''
This is very easy in Python. Otherwise, need to reverse, add and reverse back.
'''


class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def addBinary(self, A, B):
        return bin(int(A, 2) + int(B, 2))[2:]

