'''
Given a binary search tree T, where each node contains a positive integer, and an integer K, you have to find whether or not there exist two different nodes A and B such that A.value + B.value = K.

Return 1 to denote that two such nodes exist. Return 0, otherwise.

Notes

Your solution should run in linear time and not take memory more than O(height of T).
Assume all values in BST are distinct.
Example :

Input 1:

T :       10
         / \
        9   20

K = 19

Return: 1

Input 2:

T:        10
         / \
        9   20

K = 40

Return: 0
'''


# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def t2Sum(self, A, B):
        def inorder1(A):
            if A.left is not None:
                yield from inorder1(A.left)
            yield A.val
            if A.right is not None:
                yield from inorder1(A.right)

        def inorder2(A):
            if A.right is not None:
                yield from inorder2(A.right)
            yield A.val
            if A.left is not None:
                yield from inorder2(A.left)

        i1, i2, = inorder1(A), inorder2(A)
        n1, n2 = next(i1), next(i2)
        while n1 != n2:
            try:
                if n1 + n2 > B:
                    n2 = next(i2)
                elif n1 + n2 < B:
                    n1 = next(i1)
                else:
                    return 1
            except StopIteration:
                break
        return 0
