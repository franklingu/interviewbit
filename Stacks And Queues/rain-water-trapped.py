'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

Example :

Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.

Rain water trapped: Example 1

![Image](http://i.imgur.com/0qkUFco.png)

The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
In this case, 6 units of rain water (blue section) are being trapped.
'''


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def trap(self, A):
        sums = []
        stk = []
        for i, a in enumerate(A):
            if i == 0:
                sums.append(a)
                stk.append((a, i))
                continue
            v, j = stk[-1]
            if a > v:
                stk.append((a, i))
            sums.append(sums[-1] + a)
        stk2 = []
        for i, a in enumerate(reversed(A)):
            if i == 0:
                stk2.append((a, len(A) - i - 1))
                continue
            v, j = stk2[-1]
            if a > v:
                stk2.append((a, len(A) - i - 1))
        stk = stk + stk2[::-1]
        area = 0
        v, j = None, None
        while stk:
            a, i = stk.pop()
            if v is None:
                v, j = a, i
                continue
            val = min(a, v) * (j - i - 1) - (sums[j] - sums[i] - A[j])
            area += val
            v, j = a, i
        return area
