'''
Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

Try to solve it in linear time/space.

Example :

Input : [1, 10, 5]
Output : 5 
Return 0 if the array contains less than 2 elements.

You may assume that all the elements in the array are non-negative integers and fit in the 32-bit signed integer range.
You may also assume that the difference will not overflow.
'''

'''
Find min and max in the input. And then divide the gap between min and max into length - 1 of groups. For each group,
record the min and max of the number falling in the range. The maximum gap must appear accross groups -- why? Pigeon
hole theory.
'''

import math


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, A):
        n = len(A)
        if n < 2:
            return 0
        Min = min(A)
        Max = max(A)
        gap = (Max-Min) / float(n-1)
        if gap==0: return 0
        MIN = Min-1
        MAX = Max+1
        elems = [[MIN, MAX] for i in range(n)] # stores (min, max) for every gap range
        for num in A:
            pos = int((num - Min) / gap)
            elems[pos][0] = max(elems[pos][0], num)
            elems[pos][1] = min(elems[pos][1], num)
        ans = 0
        prev = elems[0][1] # Which would ofcourse be Min
        for i in range(n):
            if elems[i][0]==MIN and elems[i][1]==MAX:
                continue # These gap range doesn't have any elements
            ans = max(ans, elems[i][1]-prev)  # (min of this range) - (max of prev)
            prev = elems[i][0]   # Max for this gap range
        return ans