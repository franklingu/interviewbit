'''
Given a binary tree, determine if it is height-balanced.

 Height-balanced binary tree : is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
Return 0 / 1 ( 0 for false, 1 for true ) for this problem

Example :

Input :
          1
         / \
        2   3

Return : True or 1

Input 2 :
         3
        /
       2
      /
     1

Return : False or 0
         Because for the root node, left subtree has depth 2 and right subtree has depth 0.
         Difference = 2 > 1.
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
    def isBalanced(self, A):
        def checkBalanced(node):
            if node is None:
                return True, 0
            isOK1, h1 = checkBalanced(node.left)
            isOK2, h2 = checkBalanced(node.right)
            if not isOK1 or not isOK2 or abs(h2 - h1) >= 2:
                return False, max(h2, h1) + 1
            return True, max(h2, h1) + 1


        isOK, h = checkBalanced(A)
        return int(isOK)
