'''
Given an integer, convert it to a roman numeral, and return a string corresponding to its roman numeral version

Input is guaranteed to be within the range from 1 to 3999.

Example :

Input : 5
Return : "V"

Input : 14
Return : "XIV"
 Note : This question has a lot of scope of clarification from the interviewer. Please take a moment to think of all the needed clarifications and see the expected response using “See Expected Output” For the purpose of this question, https://projecteuler.net/about=roman_numerals has very detailed explanations.

'''


class Solution:
    # @param A : integer
    # @return a strings
    def intToRoman(self, A):
        mapping = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
        ret = []
        for k in reversed([1, 10, 100, 1000]):
            q, r = divmod(A, k)
            if q > 0:
                if q <= 3:
                    ret.append(mapping[k] * q)
                elif q == 4:
                    ret.append(mapping[k] + mapping[k * 5])
                elif q == 5:
                    ret.append(mapping[k * 5])
                elif q <= 8:
                    ret.append(mapping[k * 5] + mapping[k] * (q - 5))
                else:
                    ret.append(mapping[k] + mapping[k * 10])
            A = r
        return ''.join(ret)
