'''
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

 Balanced tree : a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
Example :


Given A : [1, 2, 3]
A height balanced BST  :

      2
    /   \
   1     3
'''


# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : tuple of integers
    # @return the root node in the tree
    def sortedArrayToBST(self, A):
        def toBST(A, start, end):
            if start > end:
                return None
            elif start == end:
                return TreeNode(A[start])
            mid = (start + end) / 2
            node = TreeNode(A[mid])
            left = toBST(A, start, mid - 1)
            right = toBST(A, mid + 1, end)
            node.left = left
            node.right = right
            return node

        return toBST(A, 0, len(A) - 1)
