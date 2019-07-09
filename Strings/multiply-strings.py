'''
Given two numbers represented as strings, return multiplication of the numbers as a string.

 Note: The numbers can be arbitrarily large and are non-negative.
Note2: Your answer should not have leading zeroes. For example, 00 is not a valid answer.
For example,
given strings "12", "10", your answer should be “120”.

NOTE : DO NOT USE BIG INTEGER LIBRARIES ( WHICH ARE AVAILABLE IN JAVA / PYTHON ).
We will retroactively disqualify such submissions and the submissions will incur penalties.
'''


class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def multiply(self, A, B):
        def addNumbers(a, b):
            i, j = len(a) - 1, len(b) -1
            ret = []
            carry = 0
            while i >= 0 and j >= 0:
                carry, r = divmod(a[i] + b[j] + carry, 10)
                ret.append(r)
                i -= 1
                j -= 1
            while i >= 0:
                carry, r = divmod(a[i] + carry, 10)
                ret.append(r)
                i -= 1
            while j >= 0:
                carry, r = divmod(b[j] + carry, 10)
                ret.append(r)
                j -= 1
            if carry > 0:
                ret.append(carry)
            return ret[::-1]

        def multiply(a, b):
            if b == 0:
                return [0]
            carry = 0
            ret = []
            for s in reversed(a):
                carry, r = divmod(int(s) * b + carry, 10)
                ret.append(r)
            if carry > 0:
                ret.append(carry)
            while ret and ret[-1] == 0:
                ret.pop()
            return ret[::-1]

        ret = None
        for i, b in enumerate(reversed(B)):
            tmp = multiply(A, int(b))
            tmp = tmp + ([0] * i)
            if ret is None:
                ret = tmp
            else:
                ret = addNumbers(ret, tmp)
        return ''.join((str(s) for s in ret))
