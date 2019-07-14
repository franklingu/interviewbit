'''
Write a program to solve a Sudoku puzzle by filling the empty cells.
Empty cells are indicated by the character '.'
You may assume that there will be only one unique solution.

![Image1](http://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sudoku-by-L2G-20050714.svg/250px-Sudoku-by-L2G-20050714.svg.png)

A sudoku puzzle,

![Image2](http://upload.wikimedia.org/wikipedia/commons/thumb/3/31/Sudoku-by-L2G-20050714_solution.svg/250px-Sudoku-by-L2G-20050714_solution.svg.png)

and its solution numbers marked in red.

Example :

For the above given diagrams, the corresponding input to your program will be

[[53..7....], [6..195...], [.98....6.], [8...6...3], [4..8.3..1], [7...2...6], [.6....28.], [...419..5], [....8..79]]
and we would expect your program to modify the above array of array of characters to

[[534678912], [672195348], [198342567], [859761423], [426853791], [713924856], [961537284], [2
'''


class Solution:
    # @param A : list of list of chars
    # @return nothing
    def solveSudoku(self, A):
        def validateSudoku(A):
            for i in xrange(9):
                ss = set()
                for j in xrange(9):
                    cell = A[i][j]
                    if cell in ss:
                        return False
                    if cell != '.':
                        ss.add(cell)
            for j in xrange(9):
                ss = set()
                for i in xrange(9):
                    cell = A[i][j]
                    if cell in ss:
                        return False
                    if cell != '.':
                        ss.add(cell)
            for i in xrange(0, 9, 3):
                for j in xrange(0, 9, 3):
                    ss = set()
                    for y in xrange(3):
                        for x in xrange(3):
                            cell = A[i + y][j + x]
                            if cell in ss:
                                return False
                            if cell != '.':
                                ss.add(cell)
            return True

        def fillSudoku(y, x, A):
            if y == 8 and x == 8:
                cell = A[y][x]
                if cell != '.':
                    return True
                for i in xrange(1, 10):
                    A[y][x] = str(i)
                    valid = validateSudoku(A)
                    if valid:
                        return True
                A[y][x] = '.'
                return False
            cell = A[y][x]
            if x == 8:
                ny = y + 1
                nx = 0
            else:
                ny = y
                nx = x + 1
            if cell != '.':
                return fillSudoku(ny, nx, A)
            for i in xrange(1, 10):
                A[y][x] = str(i)
                valid = validateSudoku(A)
                if not valid:
                    continue
                final = fillSudoku(ny, nx, A)
                if final:
                    return final
            A[y][x] = '.'
            return False

        fillSudoku(0, 0, A)
