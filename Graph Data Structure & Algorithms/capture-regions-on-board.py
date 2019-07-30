'''
Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

For example,

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
'''


class Solution:
    # @param A : list of list of chars
    def solve(self, A):
        def find_neighbors(A, y, x):
            candidates = [
                (y + 1, x),
                (y - 1, x),
                (y, x + 1),
                (y, x - 1),
            ]
            neighbors = []
            for y1, x1 in candidates:
                if 0 <= y1 < len(A) and 0 <= x1 < len(A[0]) and A[y1][x1] == 'O':
                    neighbors.append((y1, x1))
            return neighbors

        if not A:
            return
        track = []
        danger = []
        for i in xrange(len(A)):
            for j in xrange(len(A[0])):
                cell = A[i][j]
                if cell == 'O':
                    track.append((i, j))
                    if i == 0 or j == 0 or i == len(A) - 1 or j == len(A[0]) - 1:
                        danger.append((i, j))
        visited = set()
        perserves = set()
        for point in danger:
            stack = [point]
            while stack:
                y, x = stack.pop()
                perserves.add((y, x))
                for y1, x1 in find_neighbors(A, y, x):
                    if (y1, x1) not in visited:
                        stack.append((y1, x1))
                        visited.add((y1, x1))
        for point in track:
            if point in perserves:
                continue
            A[point[0]][point[1]] = 'X'

