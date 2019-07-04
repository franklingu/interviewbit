'''
Implement the next permutation, which rearranges numbers into the numerically next greater permutation of numbers.

If such arrangement is not possible, it must be rearranged as the lowest possible order ie, sorted in an ascending order.

The replacement must be in-place, do not allocate extra memory.

Examples:

1,2,3 → 1,3,2

3,2,1 → 1,2,3

1,1,5 → 1,5,1

20, 50, 113 → 20, 113, 50
Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

 Warning : DO NOT USE LIBRARY FUNCTION FOR NEXT PERMUTATION.
 Use of Library functions will disqualify your submission retroactively and will give you penalty points.
'''

'''
If current element is bigger than previous element(left by 1), then we see a place for making previous
element slightly larger. From right to the current index, find the minimum value that is bigger thank previous
element. Swap them and reverse all the elements from current element to tail. If no current element is found,
then reverse all elements.
'''


class Solution:
    def nextPermutation(self, nums):
        def reverse(nums, start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
            
        if len(nums) < 2:
            return nums
        target = None
        for index in range(len(nums) - 2, -1, -1):
            prev, curr = nums[index + 1], nums[index]
            if curr < prev:
                target = index
                break
        start, end = 0, len(nums) - 1
        if target is not None:
            for index in range(len(nums) - 1, target, -1):
                if nums[index] > nums[target]:
                    break
            nums[target], nums[index] = nums[index], nums[target]
            start = target + 1
        reverse(nums, start, end)
        return nums
