'''
There is a rectangle with left bottom as  (0, 0) and right up as (x, y). There are N circles such that their centers are inside the rectangle.
Radius of each circle is R. Now we need to find out if it is possible that we can move from (0, 0) to (x, y) without touching any circle.

Note : We can move from any cell to any of its 8 adjecent neighbours and we cannot move outside the boundary of the rectangle at any point of time.


Input Format

1st argument given is an Integer x.
2nd argument given is an Integer y.
3rd argument given is an Integer N, number of circles.
4th argument given is an Integer R, radius of each circle.
5th argument given is an Array A of size N, where A[i] = x cordinate of ith circle
6th argument given is an Array B of size N, where B[i] = y cordinate of ith circle
Output Format

Return YES or NO depending on weather it is possible to reach cell (x,y) or not starting from (0,0).
Constraints

0 <= x, y, R <= 100
1 <= N <= 1000
Center of each circle would lie within the grid
For Example

Input:
    x = 2
    y = 3
    N = 1
    R = 1
    A = [2]
    B = [3]
Output:
    NO

Explanation:
    There is NO valid path in this case
'''

'''
Check while doing DFS
'''


class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @param E : list of integers
    # @param F : list of integers
    # @return a strings
    def solve(self, A, B, C, D, E, F):
        def within_ranges(neighbor, D, E, F):
            for x1, y1 in zip(E, F):
                x_diff = neighbor[0] - x1
                y_diff = neighbor[1] - y1
                if (x_diff ** 2 + y_diff ** 2) <= D * D:
                    return True
            return False

        def find_neighbors(curr, A, B, D, E, F):
            diffs = [-1, 0, 1]
            neighbors = []
            for x_diff in diffs:
                for y_diff in diffs:
                    if x_diff == 0 and y_diff == 0:
                        continue
                    neighbor = (curr[0] + x_diff, curr[1] + y_diff)
                    if (not (0 <= neighbor[0] <= A)) or (not (0 <= neighbor[1] <= B)):
                        continue
                    if within_ranges(neighbor, D, E, F):
                        continue
                    neighbors.append(neighbor)
            return neighbors

        stack = [(0, 0)]
        visited = set()
        while stack:
            curr = stack.pop()
            visited.add(curr)
            if curr[0] == A and curr[1] == B:
                return 'YES'
            for neighbor in find_neighbors(curr, A, B, D, E, F):
                if neighbor in visited:
                    continue
                stack.append(neighbor)
        return 'NO'
