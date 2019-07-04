'''
Given an array of real numbers greater than zero in form of strings.
Find if there exists a triplet (a,b,c) such that 1 < a+b+c < 2 . 
Return 1 for true or 0 for false.

Example:

Given [0.6, 0.7, 0.8, 1.2, 0.4] ,

You should return 1

as

0.6+0.7+0.4=1.7

1<1.7<2

Hence, the output is 1.

O(n) solution is expected.

Note: You can assume the numbers in strings don’t overflow the primitive data type and
 there are no leading zeroes in numbers. Extra memory usage is allowed.
'''

'''
There are 3 numbers to keep track of. So we can keep track of sum, max and min -- the
third one is easy to compute. If sum is bigger than 2, try to replace max with current
element if current is smaller; if smaller than 1, try to replace min with current
if current is bigger; else we found a triplet.
'''


class Solution:
    # @param A : list of strings
    # @return an integer
    def solve(self, A):
        if len(A) < 3:
            return 0
        currSum = 0
        maxElem, minElem = None, None
        for i, a in enumerate(A):
            a = float(a)
            if i < 3:
                currSum += a
                if maxElem is None or maxElem < a:
                    maxElem = a
                if minElem is None or minElem > a:
                    minElem = a
                continue
            if currSum >= 2:
                if a >= maxElem:
                    continue
                else:
                    currSum = currSum + a - maxElem
                    maxElem = max(currSum - a - minElem, a)
                    minElem = min(minElem, a)
            elif currSum <= 1:
                if a <= minElem:
                    continue
                else:
                    currSum = currSum + a - minElem
                    minElem = min(currSum - a - maxElem, a)
                    maxElem = max(maxElem, a)
            else:
                return 1
        if 1 < currSum < 2:
            return 1
        return 0
