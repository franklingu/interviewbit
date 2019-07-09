'''
There are two sorted arrays A and B of size m and n respectively.

Find the median of the two sorted arrays ( The median of the array formed by merging both the arrays ).

The overall run time complexity should be O(log (m+n)).

Sample Input

A : [1 4 5]
B : [2 3]

Sample Output

3

 NOTE: IF the number of elements in the merged array is even, then the median is the average of n / 2 th and n/2 + 1th element. 
For example, if the array is [1 2 3 4], the median is (2 + 3) / 2.0 = 2.5 
'''

'''
Finding medium is like finding an element, with exactly half elements smaller than it.
Let A be the shorter array. The maximum range for searching for such an element is [0, len(A)) for
A. And the position i in A, we can always find a corresponding j in B and i + j = half
of elements. If A[i - 1] > B[j], then i is too big and we try to make i smaller; if
A[i] < B[j - 1], then i is too small and we can make i bigger. The ending condition
would be i is already 0 or m or (B[j] > A[i - 1] and A[i] > B[j - 1]).
'''


class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a double
    def findMedianSortedArrays(self, A, B):
        if len(A) > len(B):
            A, B = B, A
        m, n = len(A), len(B)
        start, end, half = 0, m, (m + n + 1) // 2
        while start <= end:
            i = (start + end) // 2
            j = half - i
            if i < m and B[j - 1] > A[i]:
                start = i + 1
            elif i > 0 and A[i - 1] > B[j]:
                end = i - 1
            else:
                if i == 0:
                    max_of_left = B[j - 1]
                elif j == 0:
                    max_of_left = A[i - 1]
                else:
                    max_of_left = max(A[i - 1], B[j - 1])
                if (m + n) % 2 == 1:
                    return max_of_left * 1.0
                if i == m:
                    min_of_right = B[j]
                elif j == n:
                    min_of_right = A[i]
                else:
                    min_of_right = min(A[i], B[j])
                return (max_of_left + min_of_right) / 2.0 
