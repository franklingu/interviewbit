'''
Given a binary tree, flatten it to a linked list in-place.

Example :
Given


         1
        / \
       2   5
      / \   \
     3   4   6
The flattened tree should look like:

   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6
Note that the left child of all nodes should be NULL.
'''


# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return the root node in the tree
    def flatten(self, A):
        def inner(node):
            if node is None:
                return None, None
            curr = node
            h1, t1 = inner(node.left)
            h2, t2 = inner(node.right)
            if h1 is not None and h2 is not None:
                curr.left = None
                curr.right = h1
                t1.right = h2
                t2.left = None
            elif h1 is not None:
                curr.left = None
                curr.right = h1
                t2 = t1
            elif h2 is not None:
                curr.left = None
                curr.right = h2
            else:
                curr.left = None
                curr.right = None
                t2 = curr
            return curr, t2

        if A is None:
            return None
        inner(A)
        return A
