'''
Given an array of integers, return the highest product possible by multiplying 3 numbers from the array

Input:

array of integers e.g {1, 2, 3}
 NOTE: Solution will fit in a 32-bit signed integer
Example:

[0, -1, 3, 100, 70, 50]

=> 70*50*100 = 350000
'''

'''
Largest 3 positive numbers and largest postive number with two smallest negative number
'''


class Solution:
    # @param A : list of integers
    # @return an integer
    def maxp3(self, A):
        mm1 = mm2 = mm3 = mi1 = mi2 = 0
        for a in A:
            if a > 0:
                if a >= mm1:
                    mm3, mm2, mm1 = mm2, mm1, a
                elif a >= mm2:
                    mm3, mm2 = mm2, a
                elif a > mm3:
                    mm3 = a
            elif a < 0:
                if a <= mi1:
                    mi2, mi1 = mi1, a
                elif a < mi2:
                    mi2 = a
        return max(mm1 * mm2 * mm3, mi1 * mi2 * mm1)
