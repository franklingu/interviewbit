'''
You are given two positive numbers A and B. You need to find the maximum valued integer X such that:

X divides A i.e. A % X = 0
X and B are co-prime i.e. gcd(X, B) = 1
For example,

A = 30
B = 12
We return
X = 5
'''

'''
Find gcd of A and B, if gcd is 1, we found it already. Otherwise, remove all
prime factors of gcd from A -- A / num and retry.
'''


class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def cpFact(self, A, B):
        def gcd(a, b):
            if a == 0 or b == 0: 
                return 0
            if b > a:
                a, b = b, a
            while b != 0:
                a, b = b, a % b
            return a
        
        while True:
            num = gcd(A, B)
            if num <= 1:
                break
            A = A / num
        return A
