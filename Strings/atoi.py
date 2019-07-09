'''
Implement atoi to convert a string to an integer.

Example :

Input : "9 2704"
Output : 9
Note: There might be multiple corner cases here. Clarify all your doubts using “See Expected Output”.

 Questions: Q1. Does string contain whitespace characters before the number?
A. Yes Q2. Can the string have garbage characters after the number?
A. Yes. Ignore it. Q3. If no numeric character is found before encountering garbage characters, what should I do?
A. Return 0. Q4. What if the integer overflows?
A. Return INT_MAX if the number is positive, INT_MIN otherwise.
Warning : DO NOT USE LIBRARY FUNCTION FOR ATOI.
If you do, we will disqualify your submission retroactively and give you penalty points.
'''


class Solution:
    # @param A : string
    # @return an integer
    def atoi(self, A):
        is_negative = False
        seen_number = False
        seen_part = False
        ret = 0
        for e in A:
            if e == '-':
                seen_part = True
                if seen_number:
                    break
                else:
                    is_negative = True
            elif e == '+':
                seen_part = True
                if seen_number:
                    break
                else:
                    is_negative = False
            elif ord('0') <= ord(e) <= ord('9'):
                seen_part = True
                ret = ret * 10 + (ord(e) - ord('0'))
                seen_number = True
            elif e == ' ':
                if seen_part:
                    break
            else:
                break
        ret = ret if not is_negative else -ret
        if ret > 2147483647:
            return 2147483647
        elif ret < -2147483648:
            return -2147483648
        return ret
