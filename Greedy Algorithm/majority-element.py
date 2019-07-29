'''
Given an array of size n, find the majority element. The majority element is the element that appears more than floor(n/2) times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example :

Input : [2, 1, 2]
Return  : 2 which occurs 2 times which is greater than 1/2.
'''


s Solution:
    # @param A : tuple of integers
    # @return an integer
    def majorityElement(self, A):
        target = 0
        count = 1
        for i, a in enumerate(A):
            if i == 0:
                continue
            if a == A[target]:
                count += 1
            else:
                count -= 1
            if count == 0:
                target = i
                count = 1
        return A[target]
