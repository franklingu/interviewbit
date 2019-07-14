'''
The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:

00 - 0
01 - 1
11 - 3
10 - 2
There might be multiple gray code sequences possible for a given n.
Return any such sequence.
'''


class Solution:
    # @param A : integer
    # @return a list of integers
    def grayCode(self, A):
        if A == 0:
            return []
        ret = [[0], [1]]
        while A > 1:
            tmp = [[1] + ls for ls in ret[::-1]]
            ret = [[0] + ls for ls in ret]
            ret = ret + tmp
            A -= 1
        # print(ret)
        return [int(''.join((str(e) for e in ls)), 2) for ls in ret]
