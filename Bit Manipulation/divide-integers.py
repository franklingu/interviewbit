'''
Divide two integers without using multiplication, division and mod operator.

Return the floor of the result of the division.

Example:

5 / 2 = 2
Also, consider if there can be overflow cases. For overflow case, return INT_MAX.
'''

'''
Doing division at the bit level
'''

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def divide(self, A, B):
        if A == -2147483648 and B == -1:
            return 2147483647
        sign = (-1 if (A < 0) or (B < 0) else 1);
        # remove sign of operands
        A = abs(A)
        B = abs(B)
        quotient = 0
        temp = 0
        for i in range(31, -1, -1):
            if (temp + (B << i) <= A):
                temp += B << i
                quotient |= 1 << i
        return quotient if sign > 0 else -quotient
