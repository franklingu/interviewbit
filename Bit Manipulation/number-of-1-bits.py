'''
Write a function that takes an unsigned integer and returns the number of 1 bits it has.

Example:

The 32-bit integer 11 has binary representation

00000000000000000000000000001011
so the function should return 3.

Note that since Java does not have unsigned int, use long for Java
'''

'''
Method 1: check last bit, and shift to right by 1
Method 2: A = A & (A - 1). If A is 101, after first update A is 100 already.
This is porpotional to number 1s in A instead of number of bits in A.
'''


class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        ret = 0
        while A > 0:
            if A & 1 == 1:
                ret += 1
            A = A >> 1
        return ret

    # @param A : integer
    # @return an integer
    def numSetBits2(self, A):
        ret = 0
        while A > 0:
            ret += 1
            A = A & (A - 1)
        return ret
