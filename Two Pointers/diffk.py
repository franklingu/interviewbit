'''
Given an array ‘A’ of sorted integers and another non negative integer k, find if there exists 2 indices i and j such that A[i] - A[j] = k, i != j.

 Example: Input :
    A : [1 3 5]
    k : 4
 Output : YES as 5 - 1 = 4
Return 0 / 1 ( 0 for false, 1 for true ) for this problem

Try doing this in less than linear space complexity.
'''


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, A, B):
        if len(A) <= 1:
            return 0
        slow, fast = 0, 1
        while slow < fast and fast < len(A):
            diff = A[fast] - A[slow]
            if diff == B:
                return 1
            elif diff < B:
                fast += 1
            elif fast == slow + 1:
                slow += 1
                fast += 1
            else:
                slow += 1
        return 0
