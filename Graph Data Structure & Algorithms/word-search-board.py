'''
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The cell itself does not count as an adjacent cell.
The same letter cell may be used more than once.

Example :

Given board =

[
  ["ABCE"],
  ["SFCS"],
  ["ADEE"]
]
word = "ABCCED", -> returns 1,
word = "SEE", -> returns 1,
word = "ABCB", -> returns 1,
word = "ABFSAB" -> returns 1
word = "ABCD" -> returns 0
Note that 1 corresponds to true, and 0 corresponds to false.
'''


class Solution:
    # @param A : list of strings
    # @param B : string
    # @return an integer
    def exist(self, A, B):
        def find_neighbors(A, i, j, ch):
            diffs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for y_diff, x_diff in diffs:
                if not 0 <= i + y_diff < len(A):
                    continue
                if not 0 <= j + x_diff < len(A[0]):
                    continue
                curr = A[i + y_diff][j + x_diff]
                if curr != ch:
                    continue
                yield (i + y_diff, j + x_diff)

        if not B or not A:
            return 0
        stack = []
        for i, word in enumerate(A):
            for j, ch in enumerate(word):
                if B[0] == ch:
                    stack.append((i, j, 1))
        while stack:
            i, j, index = stack.pop()
            if index == len(B):
                return 1
            for y, x in find_neighbors(A, i, j, B[index]):
                stack.append((y, x, index + 1))
        return 0
