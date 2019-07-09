'''
Given an array of integers, every element appears thrice except for one which occurs once.

Find that element which does not appear thrice.

Note: Your algorithm should have a linear runtime complexity.

Could you implement it without using extra memory?

Example :

Input : [1, 2, 4, 3, 3, 2, 2, 3, 1, 1]
Output : 4
'''

'''
For this number, bit 0, if it is 0, then we have 3x + 1 0s for bit 0
and 3y 1s for bit 0; bit 1, if it is 1, then we have 3x' + 1 1s
and 3y' 0s ...
'''


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        bits = [0] * 32
        for n in A:
            for i in xrange(32):
                if n & (1 << i) != 0:
                    bits[i] += 1
        ret = 0
        for i in xrange(32):
            if (bits[i] - 1) % 3 == 0:
                ret = ret | (1 << i)
        return ret
