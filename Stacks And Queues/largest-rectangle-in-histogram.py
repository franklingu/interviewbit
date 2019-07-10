'''
Given n non-negative integers representing the histogram’s bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

Largest Rectangle in Histogram: Example 1

![Image1](http://i.imgur.com/1OutEEI.png)

Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

Largest Rectangle in Histogram: Example 2

![Image1](http://i.imgur.com/F2bePvG.png)

The largest rectangle is shown in the shaded area, which has area = 10 unit.

For example,
Given height = [2,1,5,6,2,3],
return 10.
'''


class Solution:
    # @param A : list of integers
    # @return an integer
    def largestRectangleArea(self, A):
        maxArea = 0
        stack = []
        index = 0
        while index < len(A):
            if len(stack) == 0 or A[stack[-1]] <= A[index]:
                stack.append(index)
                index += 1
            else:
                target = stack.pop()
                area = A[target] * (index - stack[-1] - 1 if stack else index)
                maxArea = max(area, maxArea)
        while len(stack) > 0:
            target = stack.pop()
            area = A[target] * (index - stack[-1] - 1 if stack else index)
            maxArea = max(area, maxArea)
        return maxArea
