'''
Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.

Example :

n = 5
n! = 120 
Number of trailing zeros = 1
So, return 1
'''

'''
There are a lot more 2 in factorial than 5. So just count numbers
ending with 5.
'''


class Solution:
    # @param A : integer
    # @return an integer
    def trailingZeroes(self, A):
        count = 0
        i = 5
        while A >= i:
            count += A / i
            i = i * 5
        return count
