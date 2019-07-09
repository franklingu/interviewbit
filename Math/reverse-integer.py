'''
Reverse digits of an integer.

Example1:

x = 123,

return 321
Example2:

x = -123,

return -321

Return 0 if the result overflows and does not fit in a 32 bit signed integer
'''

'''
Record sign and reverse string version of integer. Convert to integer with sign.
'''


class Solution:
    # @param A : integer
    # @return an integer
    def reverse(self, A):
        isMinus = A < 0
        A = abs(A)
        A = int(''.join(reversed(str(A))))
        if ((not isMinus) and A > 2147483647) or (isMinus and A > 2147483648):
            return 0
        if isMinus:
            return -A
        return A
