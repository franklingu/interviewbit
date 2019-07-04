'''
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example:

Given the array [-2,1,-3,4,-1,2,1,-5,4],

the contiguous subarray [4,-1,2,1] has the largest sum = 6.

For this problem, return the maximum sum.
'''

'''
classic problem. maxSum for the final result. while traversing, add num to current sum,
if current sum is negative, forget it as this sum will only do bad to a bigger sum.
'''


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        if len(A) < 1:
            return 0
        sumSofar, maxSum = 0, A[0]
        for elem in A:
            if sumSofar < 0:
                sumSofar = 0
            sumSofar += elem
            maxSum = max(sumSofar, maxSum)
        return maxSum
