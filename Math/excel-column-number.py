'''
Given a column title as appears in an Excel sheet, return its corresponding column number.

Example:

    A -> 1
    
    B -> 2
    
    C -> 3
    
    ...
    
    Z -> 26
    
    AA -> 27
    
    AB -> 28 
'''


class Solution:
    # @param A : string
    # @return an integer
    def titleToNumber(self, A):
        ret = 0
        l = len(A)
        for i, c in enumerate(A):
            ret += (ord(c) - ord('A') + 1) * (26 ** (l - i - 1))
        return ret