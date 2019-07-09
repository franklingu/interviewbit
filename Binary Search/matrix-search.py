'''
Write an efficient algorithm that searches for a value in an m x n matrix.

This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than or equal to the last integer of the previous row.
Example:

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return 1 ( 1 corresponds to true )

Return 0 / 1 ( 0 if the element is not present, 1 if the element is present ) for this problem
'''

'''
Search first column for a just smaller element and that row is the target row.
Search in the target row.
During searching, if B is found, just return True.
'''


import bisect

class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def searchMatrix(self, A, B):
        if not A or not A[0]:
            return 0
        first_column = [row[0] for row in A]
        row_index = bisect.bisect_left(first_column, B)
        if row_index < len(A) and first_column[row_index] == B:
            return 1
        row_index -= 1
        if row_index < 0 or A[row_index][-1] < B:
            return 0
        column_index = bisect.bisect_left(A[row_index], B)
        if column_index < len(A[0]) and A[row_index][column_index] == B:
            return 1
        return 0