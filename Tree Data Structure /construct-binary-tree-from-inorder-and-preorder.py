'''
Given preorder and inorder traversal of a tree, construct the binary tree.

 Note: You may assume that duplicates do not exist in the tree.
Example :

Input :
        Preorder : [1, 2, 3]
        Inorder  : [2, 1, 3]

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
        def construct(A, B, bstart, bend, aidx):
            # print(bstart, bend, aidx)
            if bstart > bend:
                return None
            elif bstart == bend:
                return TreeNode(A[aidx])
            val = A[aidx]
            node = TreeNode(val)
            i = 0
            for i, e in enumerate(B[bstart:bend + 1]):
                if e == val:
                    break
            i += bstart
            rstart, rend = i + 1, bend
            lstart, lend = bstart, i - 1
            aidx += 1
            left = construct(A, B, lstart, lend, aidx)
            aidx += (i - bstart)
            # print(rstart, rend, aidx, "right")
            right = construct(A, B, rstart, rend, aidx)
            node.left = left
            node.right = right
            return node

        return construct(A, B, 0, len(A) - 1, 0)
