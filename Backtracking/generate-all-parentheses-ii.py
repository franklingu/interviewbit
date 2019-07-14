'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses of length 2*n.

For example, given n = 3, a solution set is:

"((()))", "(()())", "(())()", "()(())", "()()()"
Make sure the returned list of strings are sorted.
'''


class Solution:
    # @param A : integer
    # @return a list of strings
    def generateParenthesis(self, A):
        def populateResult(A, result, genResult, leftNum):
            if A == 0 and leftNum == 0:
                result.append(''.join(genResult))
                return
            if A > 0:
                genResult.append('(')
                populateResult(A - 1, result, genResult, leftNum + 1)
                genResult.pop()
            if leftNum > 0:
                genResult.append(')')
                populateResult(A, result, genResult, leftNum - 1)
                genResult.pop()

        result = []
        genResult = []
        populateResult(A, result, genResult, 0)
        return result
