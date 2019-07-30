'''
Knight movement on a chess board

Given any source point and destination point on a chess board, we need to find whether Knight can move to the destination or not.

Knight's movements on a chess board

The above figure details the movements for a knight ( 8 possibilities ). Note that a knight cannot go out of the board.

![Image](http://i.imgur.com/lmKL4AU.jpg)

If yes, then what would be the minimum number of steps for the knight to move to the said point.
If knight can not move from the source point to the destination point, then return -1

Input:

N, M, x1, y1, x2, y2
where N and M are size of chess board
x1, y1  coordinates of source point
x2, y2  coordinates of destination point
Output:

return Minimum moves or -1
Example

Input : 8 8 1 1 8 8
Output :  6
'''


class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @param E : integer
    # @param F : integer
    # @return an integer
    def knight(self, A, B, C, D, E, F):
        def find_neighbors(curr, A, B):
            deltas = [
                (2, 1), (1, 2),
                (2, -1), (-1, 2),
                (-2, -1), (-1, -2),
                (-2, 1), (1, -2),
            ]
            y, x = curr
            for yd, xd in deltas:
                yn, xn = y + yd, x + xd
                if not (0 < yn <= A):
                    continue
                if not (0 < xn <= B):
                    continue
                yield (yn, xn)

        queue = [((C, D), 0)]
        visited = set()
        dest = (E, F)
        while queue:
            curr, step = queue.pop(0)
            # print(curr, step)
            if curr == dest:
                return step
            if curr in visited:
                continue
            visited.add(curr)
            for ne in find_neighbors(curr, A, B):
                if ne in visited:
                    continue
                queue.append((ne, step + 1))
        return -1
