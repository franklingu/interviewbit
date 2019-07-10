'''
A long array A[] is given to you. There is a sliding window of size w which is moving from the very left of the array to the very right. You can only see the w numbers in the window. Each time the sliding window moves rightwards by one position. You have to find the maximum for each window. The following example will give you more clarity.

Example :

The array is [1 3 -1 -3 5 3 6 7], and w is 3.

Window position	Max

[1 3 -1] -3 5 3 6 7	3
1 [3 -1 -3] 5 3 6 7	3
1 3 [-1 -3 5] 3 6 7	5
1 3 -1 [-3 5 3] 6 7	5
1 3 -1 -3 [5 3 6] 7	6
1 3 -1 -3 5 [3 6 7]	7
Input: A long array A[], and a window width w
Output: An array B[], B[i] is the maximum value of from A[i] to A[i+w-1]
Requirement: Find a good optimal way to get B[i]

 Note: If w > length of the array, return 1 element with the max of the array.
'''


class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def slidingMaximum(self, A, B):
        from collections import deque
        Qi = deque()
        for i in xrange(B):
            while Qi and A[i] >= A[Qi[-1]]:
                Qi.pop()
            Qi.append(i)
        ret = []
        for i in xrange(B, len(A)):
            ret.append(A[Qi[0]])
            while Qi and Qi[0] <= i - B:
                Qi.popleft()
            while Qi and A[i] >= A[Qi[-1]] :
                Qi.pop()
            Qi.append(i)
        ret.append(A[Qi[0]])
        return ret
