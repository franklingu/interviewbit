'''
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7  might become 4 5 6 7 0 1 2 ).

You are given a target value to search. If found in the array, return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Input : [4 5 6 7 0 1 2] and target = 4
Output : 0

NOTE : Think about the case when there are duplicates. Does your current solution work? How does the time complexity change?*
'''

'''
Think of a varian for normal binary search. If mid element is target,
return mid; otherwise see if the first half is sorted and mid is in that
range, if so enter first first half or second half if not; if first
half is not sorted, second half must be sorted and if mid in second half
range, search second half.
'''


class Solution:
    def search(self, nums, target):
        if not nums:
            return -1
        start, end = 0, len(nums) - 1
        while start < end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            if nums[start] <= nums[mid]:
                if nums[start] <= target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if nums[mid] < target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
        if start < len(nums) and nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1
