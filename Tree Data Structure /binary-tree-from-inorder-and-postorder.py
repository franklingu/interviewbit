'''
Given inorder and postorder traversal of a tree, construct the binary tree.

 Note: You may assume that duplicates do not exist in the tree.
Example :

Input :
        Inorder : [2, 1, 3]
        Postorder : [2, 3, 1]

Return :
            1
           / \
          2   3
'''


# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return the root node in the tree
    def buildTree(self, A, B):
        def construct(A, B, astart, aend, bidx):
            # print(astart, aend, bidx)
            if astart > aend:
                return None
            val = B[bidx]
            node = TreeNode(val)
            i = 0
            for i, e in enumerate(A[astart:aend + 1]):
                if e == val:
                    break
            i += astart
            rstart, rend = i + 1, aend
            lstart, lend = astart, i - 1
            bidx -= 1
            right = construct(A, B, rstart, rend, bidx)
            bidx -= (rend - i)
            left = construct(A, B, lstart, lend, bidx)
            node.left = left
            node.right = right
            return node

        return construct(A, B, 0, len(A) - 1, len(B) - 1)
