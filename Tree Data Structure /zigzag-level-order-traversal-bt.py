'''
Given a binary tree, return the zigzag level order traversal of its nodes’ values. (ie, from left to right, then right to left for the next level and alternate between).

Example :
Given binary tree

    3
   / \
  9  20
    /  \
   15   7
return

[
         [3],
         [20, 9],
         [15, 7]
]
'''



# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def zigzagLevelOrder(self, A):
        def fillLevelOrder(node, levels, curr):
            if node is None:
                return
            if len(levels) < curr + 1:
                levels.append([])
            levels[curr].append(node.val)
            fillLevelOrder(node.left, levels, curr + 1)
            fillLevelOrder(node.right, levels, curr + 1)

        def flipLevel(levels):
            for i, ls in enumerate(levels):
                if i % 2 == 1:
                    levels[i] = ls[::-1]

        levels = []
        fillLevelOrder(A, levels, 0)
        flipLevel(levels)
        return levels
