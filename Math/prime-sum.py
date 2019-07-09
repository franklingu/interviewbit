'''
Given an even number ( greater than 2 ), return two prime numbers whose sum will be equal to given number.

NOTE A solution will always exist. read Goldbach’s conjecture

Example:


Input : 4
Output: 2 + 2 = 4

If there are more than one solutions possible, return the lexicographically smaller solution.

If [a, b] is one solution with a <= b,
and [c,d] is another solution with c <= d, then

[a, b] < [c, d] 

If a < c OR a==c AND b < d. 
'''

'''
Starting from (2, A - 2) and check for isPrime
'''


class Solution:
    # @param A : integer
    # @return a list of integers
    def primesum(self, A):
        if A <= 1:
            return []
        
        def isPrime(num):
            for i in xrange(2, int(math.sqrt(num)+1)): 
                if num % i == 0:
                    return 0
            return 1
        
        for i in xrange(2, A+1):
            if isPrime(i) and (A-i >= i) and isPrime(A-i):
                return [ i , A-i]
        
        return []
