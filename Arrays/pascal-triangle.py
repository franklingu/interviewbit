'''
Given numRows, generate the first numRows of Pascal’s triangle.

Pascal’s triangle : To generate A[C] in row R, sum up A’[C] and A’[C-1] from previous row R - 1.

Example:

Given numRows = 5,

Return

[
     [1],
     [1,1],
     [1,2,1],
     [1,3,3,1],
     [1,4,6,4,1]
]
'''

'''
Just observe the pattern and do it as the requirement.
'''


class Solution:
    # @param A : integer
    # @return a list of list of integers
    def solve(self, A):
        if A == 0:
            return []
        m = [[1]]
        for _ in xrange(1, A):
            prev = m[-1]
            row = []
            for idx, elem in enumerate(prev):
                if idx == 0:
                    row.append(1)
                    continue
                row.append(elem + prev[idx - 1])
            row.append(1)
            m.append(row)
        return m

