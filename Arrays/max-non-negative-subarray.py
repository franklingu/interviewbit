'''
Find out the maximum sub-array of non negative numbers from an array.
The sub-array should be continuous. That is, a sub-array created by choosing the second and fourth element and skipping the third element is invalid.

Maximum sub-array is defined in terms of the sum of the elements in the sub-array. Sub-array A is greater than sub-array B if sum(A) > sum(B).

Example:

A : [1, 2, 5, -7, 2, 3]
The two sub-arrays are [1, 2, 5] [2, 3].
The answer is [1, 2, 5] as its sum is larger than [2, 3]
NOTE: If there is a tie, then compare with segment's length and return segment which has maximum length
NOTE 2: If there is still a tie, then return the segment with minimum starting index
'''

'''
Traverse the array, if negative is met, compare with max sum so far
and max length so far, update if necessary, and then reset current
sum and current length; if positive, just increment current sum and
current length. And do not forget compare after loop end.
'''


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        ms, ml, curr = 0, 0, []
        cs, cl = 0, 0
        for i, el in enumerate(A):
            if el < 0:
                if cs > ms or (cs == ms and cl > ml):
                    ms = cs
                    ml = cl
                    curr = A[i - cl: i]
                cs, cl = 0, 0
            else:
                cs += el
                cl += 1
        if cs > ms or (cs == ms and cl > ml):
            ms = cs
            ml = cl
            curr = A[i - cl + 1: i + 1]
        return curr
