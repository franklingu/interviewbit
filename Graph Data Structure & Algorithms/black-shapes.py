'''
Given N * M field of O's and X's, where O=white, X=black
Return the number of black shapes. A black shape consists of one or more adjacent X's (diagonals not included)

Example:

OOOXOOO
OOXXOXO
OXOOOXO

answer is 3 shapes are  :
(i)    X
     X X
(ii)
      X
 (iii)
      X
      X
Note that we are looking for connected shapes here.

For example,

XXX
XXX
XXX
is just one single connected black shape.
'''


class Solution:
    # @param A : list of strings
    # @return an integer
    def black(self, A):
        def find_neighbors(curr, A):
            deltas = [(-1, 0), (1, 0), (0, 1), (0, -1)]
            y, x = curr
            for yd, xd in deltas:
                yn, xn = y + yd, x + xd
                if not (0 <= yn < len(A)):
                    continue
                if not (0 <= xn < len(A[0])):
                    continue
                if A[yn][xn] == 'X':
                    yield (yn, xn)

        if not A:
            return 0
        candidates = []
        covered = set()
        for i, row in enumerate(A):
            for j, elem in enumerate(row):
                if elem != 'X':
                    continue
                candidates.append((i, j))
        cnt = 0
        for position in candidates:
            if position in covered:
                continue
            cnt += 1
            stack = [position]
            visited = set()
            while stack:
                curr = stack.pop()
                if curr in visited:
                    continue
                visited.add(curr)
                covered.add(curr)
                for ne in find_neighbors(curr, A):
                    if ne in visited:
                        continue
                    stack.append(ne)
        return cnt
