'''
Find largest distance
Given an arbitrary unweighted rooted tree which consists of N (2 <= N <= 40000) nodes. The goal of the problem is to find largest distance between two nodes in a tree. Distance between two nodes is a number of edges on a path between the nodes (there will be a unique path between any pair of nodes since it is a tree). The nodes will be numbered 0 through N - 1.

The tree is given as an array P, there is an edge between nodes P[i] and i (0 <= i < N). Exactly one of the i’s will have P[i] equal to -1, it will be root node.

 Example:
If given P is [-1, 0, 0, 0, 3], then node 0 is the root and the whole tree looks like this:
          0
       /  |  \
      1   2   3
               \
                4
 One of the longest path is 1 -> 0 -> 3 -> 4 and its length is 3, thus the answer is 3. Note that there are other paths with maximal distance.
'''


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        root = 0
        children = {}
        for i, val in enumerate(A):
            if val == -1:
                root = i
            elif val not in children:
                children[val] = []
            if val != -1:
                children[val].append(i)
        stack = [(root, 0)]
        max_child, max_step = root, 0
        while len(stack) > 0:
            curr, step = stack[-1]
            del stack[-1]
            if step > max_step:
                max_step = step
                max_child = curr
            chs = children.get(curr, [])
            for ch in chs:
                stack.append((ch, step + 1))
        stack = [(max_child, 0)]
        visited = set()
        while len(stack) > 0:
            curr, step = stack[-1]
            visited.add(curr)
            del stack[-1]
            if step > max_step:
                max_step = step
            chs = children.get(curr, [])
            if A[curr] != -1:
                chs.append(A[curr])
            for ch in chs:
                if ch not in visited:
                    stack.append((ch, step + 1))
        return max_step
