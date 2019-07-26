'''
Given an inorder traversal of a cartesian tree, construct the tree.

 Cartesian tree : is a heap ordered binary tree, where the root is greater than all the elements in the subtree.
 Note: You may assume that duplicates do not exist in the tree.
Example :

Input : [1 2 3]

Return :
          3
         /
        2
       /
      1
'''


# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : list of integers
    # @return the root node in the tree
    def buildTree(self, A):
        if not A:
            return None
        mm, mi = A[0], 0
        for i, e in enumerate(A):
            if e > mm:
                mm = e
                mi = i
        node = TreeNode(mm)
        left = self.buildTree(A[:mi])
        right = self.buildTree(A[mi + 1:])
        node.left = left
        node.right = right
        return node
