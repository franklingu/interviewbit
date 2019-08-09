'''
Given two words A and B, find the minimum number of steps required to convert A to B. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
Example :
edit distance between
"Anshuman" and "Antihuman" is 2.

Operation 1: Replace s with t.
Operation 2: Insert i.
'''


class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def minDistance(self, A, B):
        matrix = [[0 for _ in xrange(len(A) + 1)] for _ in xrange(len(B) + 1)]
        for j in xrange(1, len(A) + 1):
            matrix[0][j] = j
        for i in xrange(1, len(B) + 1):
            matrix[i][0] = i
        for i in xrange(1, len(B) + 1):
            for j in xrange(1, len(A) + 1):
                if B[i - 1] == A[j - 1]:
                    val = matrix[i - 1][j - 1]
                else:
                    val = min(matrix[i][j - 1], matrix[i - 1][j], matrix[i - 1][j - 1]) + 1
                matrix[i][j] = val
        # print(matrix)
        return matrix[len(B)][len(A)]
