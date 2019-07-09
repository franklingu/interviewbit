'''
Reverse bits of an 32 bit unsigned integer

Example 1:

x = 0,

          00000000000000000000000000000000
=>        00000000000000000000000000000000
return 0

Example 2:

x = 3,

          00000000000000000000000000000011
=>        11000000000000000000000000000000
return 3221225472

Since java does not have unsigned int, use long
'''


class Solution:
    # @param A : unsigned integer
    # @return an unsigned integer
    def reverse(self, A):
        br = list(reversed(bin(A)[2:]))
        while len(br) < 32:
            br.append('0')
        return int(''.join(br), 2)
