'''
Hamming distance between two non-negative integers is defined as the number of positions at which the corresponding bits are different.

For example,

HammingDistance(2, 7) = 2, as only the first and the third bit differs in the binary representation of 2 (010) and 7 (111).

Given an array of N non-negative integers, find the sum of hamming distances of all pairs of integers in the array.
Return the answer modulo 1000000007.

Example

Let f(x, y) be the hamming distance defined above.

A=[2, 4, 6]

We return,
f(2, 2) + f(2, 4) + f(2, 6) + 
f(4, 2) + f(4, 4) + f(4, 6) +
f(6, 2) + f(6, 4) + f(6, 6) = 

0 + 2 + 1
2 + 0 + 1
1 + 1 + 0 = 8
'''

'''
A pair of 1 and 0 create a distance count. So we can basically
calculate the number of 1s for each bit and number of 1s *
number of 0s * 2 is the distance for this bit.
'''


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def hammingDistance(self, A):
        ret = 0
        ones = [0] * 32
        for a in A:
            mask = 1 << 32
            index = 0
            while mask > 0:
                bit = a & mask
                if bit != 0:
                    ones[index] += 1
                index -= 1
                mask = mask >> 1
        for n in ones:
            ret += n * (len(A) - n) * 2
        return ret % 1000000007

