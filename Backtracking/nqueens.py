'''
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

N Queens: Example 1

![Image](http://i.imgur.com/yaxpgda.png)

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens’ placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

For example,
There exist two distinct solutions to the 4-queens puzzle:

[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
'''


class Solution:
    # @param A : integer
    # @return a list of list of strings
    def solveNQueens(self, A):
        def checkValidForPosition(board, i, j):
            for y in xrange(A):
                if y == i:
                    continue
                cell = board[y][j]
                if cell == 'Q':
                    return False
            directions = [(1, 1), (-1, -1), (1, -1), (-1, 1)]
            for dy, dx in directions:
                y, x = i + dy, j + dx
                while 0 <= y < A and 0 <= x < A:
                    cell = board[y][x]
                    if cell == 'Q':
                        return False
                    y += dy
                    x += dx
            return True

        def checkValidBoard(board):
            for i in xrange(A):
                for j in xrange(A):
                    cell = board[i][j]
                    if cell == 'Q':
                        valid = checkValidForPosition(board, i, j)
                        if not valid:
                            return False
            return True

        def fillNQueens(n, board, possible):
            if n == 0:
                curr = [''.join(ls) for ls in board]
                possible.append(curr)
                return
            row = board[A - n]
            for i in xrange(A):
                row[i] = 'Q'
                valid = checkValidBoard(board)
                if not valid:
                    row[i] = '.'
                    continue
                fillNQueens(n - 1, board, possible)
                row[i] = '.'

        board = [['.'] * A for a in xrange(A)]
        possible = []
        fillNQueens(A, board, possible)
        return possible
