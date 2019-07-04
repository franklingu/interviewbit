'''
Given a list of non negative integers, arrange them such that they form the largest number.

For example:

Given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.
'''

'''
Custom compare function: s1 + s2 compares with s2 + s1
'''


class Solution:
    # @param A : tuple of integers
    # @return a strings
    def largestNumber(self, A):
        def comp(x1, x2):
            x12 = x1 + x2
            x21 = x2 + x1
            if x12 > x21:
                return 1
            elif x12 < x21:
                return -1
            else:
                return 0

        A = [str(e) for e in A]
        A.sort(cmp=comp)
        A = list(reversed(A))
        start = 0
        for i, e in enumerate(A):
            if e == '0':
                start = i
            else:
                break
        return ''.join(A[start:])
