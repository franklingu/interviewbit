'''
Given a binary search tree, write a function to find the kth smallest element in the tree.

Example :

Input :
  2
 / \
1   3

and k = 2

Return : 2

As 2 is the second smallest element in the tree.
 NOTE : You may assume 1 <= k <= Total number of nodes in BST
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
    # @return an integer
    def kthsmallest(self, A, B):
        def inorder(A, B):
            if A is None:
                return None, B
            target1, B1 = inorder(A.left, B)
            if target1 is not None:
                return target1, B1
            B1 -= 1
            if B1 == 0:
                return A, 0
            return inorder(A.right, B1)

        return inorder(A, B)[0].val
