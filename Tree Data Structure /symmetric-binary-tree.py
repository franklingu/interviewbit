'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

Example :

    1
   / \
  2   2
 / \ / \
3  4 4  3
The above binary tree is symmetric.
But the following is not:

    1
   / \
  2   2
   \   \
   3    3
Return 0 / 1 ( 0 for false, 1 for true ) for this problem
'''


# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def isSymmetric(self, A):
        def inorder(node):
            if node is None:
                return [None]
            left = inorder(node.left)
            right = inorder(node.right)
            return left + [node.val] + right

        if A is None:
            return 1
        elif A.left is None and A.right is None:
            return 1
        elif A.left is None or A.right is None:
            return 0
        left = inorder(A.left)
        right = inorder(A.right)
        if len(left) != len(right):
            return 0
        for i, n in enumerate(left):
            m = right[-i - 1]
            if n != m:
                return 0
        return 1

    # @param A : root node of tree
    # @return an integer
    def isSymmetric2(self, A):
        def is_sym(a, b):
            if a is None and b is None:
                return 1
            elif a is None or b is None:
                return 0
            elif a.val != b.val:
                return 0
            lr = is_sym(a.left, b.right)
            rl = is_sym(a.right, b.left)
            return 1 if lr == 1 or rl == 1 else 0

        if A is None:
            return 1
        return is_sym(A.left, A.right)
