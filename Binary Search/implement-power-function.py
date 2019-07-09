'''
Implement pow(x, n) % d.

In other words, given x, n and d,

find (xn % d)

Note that remainders on division cannot be negative. 
In other words, make sure the answer you return is non negative.

Input : x = 2, n = 3, d = 3
Output : 2

2^3 % 3 = 8 % 3 = 2.
'''

'''
Take the binary representation of n. If the bit is 1, multiple the current
result with x ** bit_position. Take modulo along the way.
'''


class Solution:
    # @param x : integer
    # @param n : integer
    # @param d : integer
    # @return an integer
    def pow(self, x, n, d):
        x = x % d
        ret = 1
        acc = x
        while n > 0:
            if n & 1 == 1:
                ret = (acc * ret) % d
            n = n >> 1
            acc = acc * acc % d
        return ret