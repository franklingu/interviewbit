'''
There are certain problems which are asked in the interview to also check how you take care of overflows in your problem.
This is one of those problems.
Please take extra care to make sure that you are type-casting your ints to long properly and at all places. Try to verify if your solution works if number of elements is as large as 105

 Food for thought :
Even though it might not be required in this problem, in some cases, you might be required to order the operations cleverly so that the numbers do not overflow. 
For example, if you need to calculate n! / k! where n! is factorial(n), one approach is to calculate factorial(n), factorial(k) and then divide them. 
Another approach is to only multiple numbers from k + 1 ... n to calculate the result. 
Obviously approach 1 is more susceptible to overflows.

You are given a read only array of n integers from 1 to n.

Each integer appears exactly once except A which appears twice and B which is missing.

Return A and B.

Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Note that in your output A should precede B.

Example:

Input:[3 1 2 5 3] 

Output:[3, 4] 

A = 3, B = 4
'''

'''
Method 1:
for all numbers in A and from 1 to n, take xor operation and
save to X.
find a bit in X that is 1: there must be at least 1 1 bit --
because if no 1 bit, then every number appear even number of times.
but A should have appeared once and B thrice
for all numbers in A and from 1 to n, take xor for two groups.
group 1, the bit is 0; group 2, the bit is 1

now need to check which is repeated and which is missing
calculate the expected sum and substract all numbers in A.
if result > 0, repeated is larger; else repected is smaller

Method 2:
first iterate from 1 to n, sum up i and i ** 2 -- s1 and s2;
then iterate nums, sum up num and num ** 2 -- s3 and s4;
say repeated is A and missing is B.
s3 - s1 = A - B
s4 - s2 = A ** 2 - B ** 2 = (A - B)(A + B)
'''


class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        res = 0
        ss = len(A) * (len(A) + 1) // 2
        for i, a in enumerate(A):
            res ^= a
            res ^= (i + 1)
            ss -= a
        first_bit = res & (~(res - 1))
        missing, repeated = 0, 0
        for i, a in enumerate(A):
            if a & first_bit == 0:
                missing ^= a
            else:
                repeated ^= a
            b = i + 1
            if b & first_bit == 0:
                missing ^= b
            else:
                repeated ^= b
        if (repeated - missing) * ss > 0:
            repeated, missing = missing, repeated
        return [repeated, missing]

    def repeatedNumber2(self, A):
        e1, e2, a1, a2 = 0, 0, 0, 0
        for i, a in enumerate(A, 1):
            e1 += i
            e2 += i * i
            a1 += a
            a2 += a * a
        diff = a1 - e1
        prod = a2 - e2
        ss = prod / diff
        return [(ss + diff) / 2, (ss - diff) / 2]
