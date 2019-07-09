'''
Given an array of integers, every element appears twice except for one. Find that single one.

Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example :

Input : [1 2 2 3 1]
Output : 3
'''

'''
XOR. Same number becomes 0. 0 with some number still that number.
'''


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        ret = 0
        for a in A:
            ret = ret ^ a
        return ret
