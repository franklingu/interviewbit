'''
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

Example :

Given numerator = 1, denominator = 2, return "0.5"
Given numerator = 2, denominator = 1, return "2"
Given numerator = 2, denominator = 3, return "0.(6)"
'''


class Solution:
    # @param A : integer
    # @param B : integer
    # @return a strings
    def fractionToDecimal(self, A, B):
        if B == 0:
            return '0'
        ret = []
        if (A > 0 and B < 0) or (A < 0 and B > 0):
            ret.append('-')
            A, B = abs(A), abs(B)
        track = {}
        has_point = False
        while A != 0:
            if A in track:
                ret.insert(track[A], '(')
                ret.append(')')
                break
            q, r = divmod(A, B)
            if has_point:
                track[A] = len(ret)
            if q == 0 and not has_point:
                if not ret or ret[-1] == '-':
                    ret.append('0')
                ret.append('.')
                has_point = True
            else:
                ret.append(str(q))
            if has_point:
                A = r * 10
            else:
                A = r
        if not ret:
            ret.append('0')
        return ''.join(ret)
