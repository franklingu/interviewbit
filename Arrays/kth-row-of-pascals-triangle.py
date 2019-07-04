'''
Given an index k, return the kth row of the Pascal’s triangle.

Pascal’s triangle : To generate A[C] in row R, sum up A’[C] and A’[C-1] from previous row R - 1.

Example:

Input : k = 3

Return : [1,3,3,1]
 NOTE : k is 0 based. k = 0, corresponds to the row [1]. 
Note:Could you optimize your algorithm to use only O(k) extra space?
'''

'''
keep track of prev row only.
'''


class Solution:
    # @param A : integer
    # @return a list of integers
    def getRow(self, A):
        if A == 0:
            return [1]
        row = [1]
        for _ in xrange(A):
            prev = row
            row = []
            for idx, elem in enumerate(prev):
                if idx == 0:
                    row.append(1)
                    continue
                row.append(prev[idx - 1] + elem)
            row.append(1)
        return row
