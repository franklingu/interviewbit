'''
Find if Given number is power of 2 or not.
More specifically, find if given number can be expressed as 2^k where k >= 1.

Input:

number length can be more than 64, which mean number can be greater than 2 ^ 64 (out of long long range)
Output:

return 1 if the number is a power of 2 else return 0

Example:

Input : 128
Output : 1
'''


class Solution:
    # @param A : string
    # @return an integer
    def power(self, A):
        if A == '0' or A == '1':
            return 0
        A = list(A)
        while len(A) > 9:
            ret = []
            remainder = 0
            for e in A:
                val = int(e) + remainder * 10
                q, remainder = divmod(val, 2)
                if q == 0 and len(ret) == 0:
                    continue
                ret.append(q)
            if remainder > 0:
                return 0
            A = ret
        A = int(''.join([str(e) for e in A]))
        if A & (A - 1) == 0:
            return 1
        else:
            return 0
