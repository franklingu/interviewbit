'''
Remove Duplicates from Sorted Array

Given a sorted array, remove the duplicates in place such that each element can appear atmost twice and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

Note that even though we want you to return the new length, make sure to change the original array as well in place

For example,
Given input array A = [1,1,1,2],

Your function should return length = 3, and A is now [1,1,2].
'''


class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        fast, slow = 0, 0
        prev = None
        cnt = 1
        while fast < len(A):
            curr = A[fast]
            if curr == prev and cnt >= 2:
                pass
            elif curr == prev and cnt < 2:
                cnt += 1
                A[slow] = curr
                slow += 1
            else:
                A[slow] = curr
                slow += 1
                cnt = 1
                prev = curr
            fast += 1
        return slow
