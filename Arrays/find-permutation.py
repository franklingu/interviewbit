'''
Given a positive integer n and a string s consisting only of letters D or I, you have to find any permutation of first n positive integer that satisfy the given input string.

D means the next number is smaller, while I means the next number is greater.

Notes

Length of given string s will always equal to n - 1
Your solution should run in linear time and space.
Example :

Input 1:

n = 3

s = ID

Return: [1, 3, 2]
'''

'''
There are basically four combinations for two elements:
II, ID, DI, DD
For all I positions, candidates are bigger than D positions. And then we just need to make sure
II and DD satisfy the requirements.

Count number of 'I's. Then allocate all numbers from (B - count + 1) to B. For I, they start
from (B - count + 1) and for D they start from (B - count). If I is seen, increment num for I
and if D is seen, decrement num for D.
'''


class Solution:
    # @param A : string
    # @param B : integer
    # @return a list of integers
    def findPerm(self, A, B):
        i, c1, c2 = 0, 0, 0
        ret = []
        for e in A:
            if e == 'I':
                i += 1
        c1 = B - i
        c2 = c1 - 1
        ret.append(c1)
        for e in A:
            if e == 'I':
                c1 += 1
                ret.append(c1)
            else:
                ret.append(c2)
                c2 -= 1
        return ret
