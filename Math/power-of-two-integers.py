'''
Given a positive integer which fits in a 32 bit signed integer, find if it can be expressed as A^P where P > 1 and A > 0. A and P both should be integers.

Example

Input : 4
Output : True  
as 2^2 = 4. 
'''


class Solution:
    # @param A : integer
    # @return a boolean
    def isPower(self, A):
        if A == 1:
            return 1
        p = 2
        while 2 ** p <= A:
            pthRoot = round(A ** (1.0 / p), 8)
            if int(pthRoot) == pthRoot:
                return 1
            p += 1
        return 0
