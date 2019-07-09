'''
Given a N cross M matrix in which each row is sorted, find the overall median of the matrix. Assume N*M is odd.

For example,

Matrix=
[1, 3, 5]
[2, 6, 9]
[3, 6, 9]

A = [1, 2, 3, 3, 5, 6, 6, 9, 9]

Median is 5. So, we return 5.
Note: No extra memory is allowed.
'''

'''
If extra memory is allowed, we can use heap to find the median in (M * N)log(N) time.
Or we can take a binary search approach,
'''


from bisect import bisect_right
    
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def findMedian(self, A):
        def count(A, e):
            # number of elements smallers than e in A
            cnts = 0
            for elem in A:
                cnts += bisect_right(elem, e)
            return cnts

        # median is min number for which cnts>=c
        c = (len(A) * len(A[0])) / 2 + 1
        low = 0
        high = 2 ** 31
        while low < high:
            mid = (low + high) / 2
            cs = count(A, mid)
            if cs < c:
                low = mid + 1
            else:
                high = mid
        return low
