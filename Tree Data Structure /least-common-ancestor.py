'''
Find the lowest common ancestor in an unordered binary tree given two values in the tree.

 Lowest common ancestor : the lowest common ancestor (LCA) of two nodes v and w in a tree or directed acyclic graph (DAG) is the lowest (i.e. deepest) node that has both v and w as descendants.
Example :


        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2_     0        8
         /   \
         7    4
For the above tree, the LCA of nodes 5 and 1 is 3.

 LCA = Lowest common ancestor
Please note that LCA for nodes 5 and 4 is 5.

You are given 2 values. Find the lowest common ancestor of the two nodes represented by val1 and val2
No guarantee that val1 and val2 exist in the tree. If one value doesn’t exist in the tree then return -1.
There are no duplicate values.
You can use extra memory, helper functions, and can modify the node struct but, you can’t add a parent pointer.
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
    # @param C : integer
    # @return an integer
    def lca(self, A, B, C):
        def findLCA(node, p1, p2):
            if node is None:
                return None, False, False
            isP1 = node.val == p1
            isP2 = node.val == p2
            ln, ll, lr = findLCA(node.left, p1, p2)
            rn, rl, rr = findLCA(node.right, p1, p2)
            if ln is not None:
                return ln, True, True
            elif rn is not None:
                return rn, True, True
            if (ll or rl or isP1) and (lr or rr or isP2):
                return node, True, True
            else:
                return None, (ll or rl or isP1), (lr or rr or isP2)

        n, l, r = findLCA(A, B, C)
        return n.val if n is not None else -1
