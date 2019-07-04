'''
Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Given n = 3,

You should return the following matrix:

[
  [ 1, 2, 3 ],
  [ 8, 9, 4 ],
  [ 7, 6, 5 ]
]
'''

'''
Spiral or diagnal or or any format, just keep track of directions,
current direction, limit and trigger next direction when limit is
reached for current direction and update limit.
'''


class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generateMatrix(self, A):
        m = [[0 for _ in xrange(A)] for _ in xrange(A)]
        l, r, u, d = 0, A - 1, 0, A - 1
        directions = [
            (0, 1),  # left
            (1, 0),  # down
            (0, -1),  # right
            (-1, 0),  # up
        ]
        direction = 0
        x, y = 0, 0
        for i in xrange(1, A * A + 1):
            m[y][x] = i
            if direction == 0 and x >= r:
                direction = (direction + 1) % 4
                u += 1
            elif direction == 2 and x <= l:
                direction = (direction + 1) % 4
                d -= 1
            elif direction == 1 and y >= d:
                direction = (direction + 1) % 4
                r -= 1
            elif direction == 3 and y <= u:
                direction = (direction + 1) % 4
                l += 1
            yd, xd = directions[direction]
            y, x = y + yd, x + xd
        return m
