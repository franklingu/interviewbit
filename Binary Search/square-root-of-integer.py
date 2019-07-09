'''
Implement int sqrt(int x).

Compute and return the square root of x.

If x is not a perfect square, return floor(sqrt(x))

Example :

Input : 11
Output : 3
DO NOT USE SQRT FUNCTION FROM STANDARD LIBRARY
'''

'''
start is 0 and end is the number and search for the best point --
the best point is the point from where adding 1 or substracting 1
will cause the difference with A become larger.
'''


class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        if A == 1:
            return 1
        start, end = 0, A
        prev = None
        while True:
            mid = int((start + end) / 2)
            diff = mid * mid - A
            if diff > 0:
                end = mid
            elif diff < 0:
                start = mid
            else:
                return mid
            if prev is None:
                prev = diff
            elif prev == diff and diff < 0:
                return mid
            else:
                prev = diff
        return 0
