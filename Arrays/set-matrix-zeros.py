'''
Given an m x n matrix of 0s and 1s, if an element is 0, set its entire row and column to 0.

Do it in place.

Example

Given array A as

1 0 1
1 1 1 
1 1 1
On returning, the array A should be :

0 0 0
1 0 1
1 0 1
Note that this will be evaluated on the extra memory used. Try to minimize the space and time complexity.
'''

'''
Use array of booleans to keep track of which row and column need to be set to zero
'''


class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def setZeroes(self, A):
        if len(A) < 1:
            return A
        rs = [False for n in range(len(A))]
        cs = [False for n in range(len(A[0]))]
        for i, row in enumerate(A):
            for j, el in enumerate(row):
                if el == 0:
                    rs[i] = True
                    cs[j] = True
        for i, row in enumerate(A):
            for j, el in enumerate(row):
                if rs[i] or cs[j]:
                    row[j] = 0
        return A
