'''
Given a binary tree, return the level order traversal of its nodes’ values. (ie, from left
to right, level by level).

Example :
Given binary tree

    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:

[
  [3],
  [9,20],
  [15,7]
]
Also think about a version of the question where you are asked to do a level order traversal of the tree
when depth of the tree is much greater than number of nodes on a level.
'''


# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def levelOrder(self, A):
        def fillLevels(node, levels, curr=0):
            if node is None:
                return
            if len(levels) == curr:
                levels.append([])
            levels[curr].append(node.val)
            fillLevels(node.left, levels, curr + 1)
            fillLevels(node.right, levels, curr + 1)

        levels = []
        fillLevels(A, levels)
        return levels
