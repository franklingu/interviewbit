'''
For Given Number N find if its COLORFUL number or not

Return 0/1

COLORFUL number:

A number can be broken into different contiguous sub-subsequence parts.
Suppose, a number 3245 can be broken into parts like 3 2 4 5 32 24 45 324 245.
And this number is a COLORFUL number, since product of every digit of a contiguous subsequence is different
Example:

N = 23
2 3 23
2 -> 2
3 -> 3
23 -> 6
this number is a COLORFUL number since product of every digit of a sub-sequence are different.

Output : 1
'''


class Solution:
    # @param A : integer
    # @return an integer
    def colorful(self, A):
        def calculateProd(s, start, end):
            ret = 1
            for i in xrange(start, end):
                ret *= int(s[i])
            return ret

        A = str(A)
        prods = set()
        for i in xrange(0, len(A) + 1):
            j = 0
            while j + i < len(A):
                prod = calculateProd(A, j, j + i + 1)
                if prod in prods:
                    return 0
                prods.add(prod)
                j += 1
        return 1
