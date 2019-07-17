'''
Determine if a Sudoku is valid, according to: http://sudoku.com.au/TheRules.aspx

The Sudoku board could be partially filled, where empty cells are filled with the character ‘.’.

![Image](http://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sudoku-by-L2G-20050714.svg/250px-Sudoku-by-L2G-20050714.svg.png)

The input corresponding to the above configuration :

["53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1", "7...2...6", ".6....28.", "...419..5", "....8..79"]
A partially filled sudoku which is valid.

 Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.
Return 0 / 1 ( 0 for false, 1 for true ) for this problem
'''


class Solution:
    # @param A : tuple of strings
    # @return an integer
    def isValidSudoku(self, A):
        for i in xrange(9):
            track = [False] * 9
            for j in xrange(9):
                c = A[i][j]
                if c == '.':
                    continue
                pos = ord(c) - ord('1')
                if track[pos]:
                    return 0
                track[pos] = True
        for j in xrange(9):
            track = [False] * 9
            for i in xrange(9):
                c = A[i][j]
                if c == '.':
                    continue
                pos = ord(c) - ord('1')
                if track[pos]:
                    return 0
                track[pos] = True
        for i in xrange(0, 9, 3):
            for j in xrange(0, 9, 3):
                track = [False] * 9
                for y in xrange(3):
                    for x in xrange(3):
                        c = A[i + y][j + x]
                        if c == '.':
                            continue
                        pos = ord(c) - ord('1')
                        if track[pos]:
                            return 0
                        track[pos] = True
        return 1
