'''
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.

Read more details about roman numerals at Roman Numeric System

Example :

Input : "XIV"
Return : 14
Input : "XX"
Output : 20
'''


class Solution:
    # @param A : string
    # @return an integer
    def romanToInt(self, A):
        mapping = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        prev, curr = None, None
        acc = 0
        for i, curr in enumerate(A):
            if i == 0:
                prev = curr
                continue
            if prev == curr:
                acc += mapping[prev]
                prev = curr
            elif mapping[curr] > mapping[prev]:
                acc -= mapping[prev]
                prev = curr
            else:
                acc += mapping[prev]
                prev = curr
        acc += mapping[prev]
        return acc
