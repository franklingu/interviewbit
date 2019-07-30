'''
There are a total of N courses you have to take, labeled from 1 to N. Some courses may have prerequisites, for example to take course 2 you have to first take course 1, which is expressed as a pair: [1,2].
Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses. return 1/0 if it is possible/not possible.
The list of prerequisite pair are given in two integer arrays B and C where B[i] is a prerequisite for C[i].

 Example: If N = 3 and the prerequisite pairs are [1,2] and [2,3], then you can finish courses in the following order: 1, 2 and 3. But if N = 2 and the prerequisite pairs are [1,2] and [2,1], then it is not possible for you to finish all the courses.
'''


class Solution:
    # @param A : integer
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer
    def solve(self, A, B, C):
        track = {}
        for b, c in zip(B, C):
            if b not in track:
                track[b] = []
            track[b].append(c)
        for b in track:
            stack = [b]
            visited = set()
            while stack:
                curr = stack.pop()
                if curr in visited:
                    return 0
                visited.add(curr)
                for ne in track.get(curr, []):
                    stack.append(ne)
        return 1
