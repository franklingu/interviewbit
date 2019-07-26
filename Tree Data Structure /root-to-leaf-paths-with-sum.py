'''
Given a binary tree and a sum, find all root-to-leaf paths where each path’s sum equals the given sum.

For example:
Given the below binary tree and sum = 22,

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return

[
   [5,4,11,2],
   [5,8,4,5]
]
'''


# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return a list of list of integers
    def pathSum(self, A, B):
        def findPaths(node, num, path, paths):
            if node is None:
                return
            num -= node.val
            path.append(node.val)
            if node.left is None and node.right is None:
                if num == 0:
                    paths.append(list(path))
                path.pop()
                return
            if node.left is not None:
                findPaths(node.left, num, path, paths)
            if node.right is not None:
                findPaths(node.right, num, path, paths)
            path.pop()

        paths = []
        findPaths(A, B, [], paths)
        return paths
