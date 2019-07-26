'''
Given a binary tree, return the inorder traversal of its nodes’ values.

Example :
Given binary tree

   1
    \
     2
    /
   3
return [1,3,2].

Using recursion is not allowed.
'''


# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def inorderTraversal(self, A):
        if A is None:
            return []
        stack = [A]
        ret = []
        visited = set()
        while len(stack) > 0:
            curr = stack[-1]
            left = curr.left
            while left is not None and left not in visited:
                stack.append(left)
                left = left.left
            curr = stack.pop()
            ret.append(curr.val)
            if curr.right is not None:
                stack.append(curr.right)
            visited.add(curr)
        return ret
