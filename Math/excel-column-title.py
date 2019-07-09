'''
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
'''


class Solution:
    # @param A : integer
    # @return a strings
    def convertToTitle(self, A):
        ret = []
        while A > 0:
            q, r = divmod(A, 26)
            if r != 0:
                ret.append(chr(ord('A') + r - 1))
            else:
                q -= 1
                ret.append('Z')
            A = q
        return ''.join(reversed(ret))
