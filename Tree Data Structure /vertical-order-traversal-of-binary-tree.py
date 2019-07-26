'''
Given a binary tree, return a 2-D array with vertical order traversal of it.
Go through the example and image for more details.

Example :
Given binary tree:

      6
    /   \
   3     7
  / \     \
 2   5     9
returns

![Image](https://s3-us-west-2.amazonaws.com/ib-assessment-tests/problem_images/main-qimg-3e9496c2af705dc0f985edb9dce803d3.png)

[
    [2],
    [3],
    [6 5],
    [7],
    [9]
]


Note : If 2 Tree Nodes shares the same vertical level then the one with lesser depth will come first.
'''


# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def verticalOrderTraversal(self, A):
        def findVerticalLevels(node, level):
            if node.left is not None:
                minL, maxL = findVerticalLevels(node.left, level - 1)
            else:
                minL, maxL = level, level
            if node.right is not None:
                minR, maxR = findVerticalLevels(node.right, level + 1)
            else:
                minR, maxR = level, level
            return min(minL, minR), max(maxL, maxR)

        def fillOrders(node, ret, vlevel, hlevel):
            while len(ret) <= vlevel:
                ret.append([])
            ret[vlevel].append((hlevel, node.val))
            if node.left is not None:
                fillOrders(node.left, ret, vlevel - 1, hlevel + 1)
            if node.right is not None:
                fillOrders(node.right, ret, vlevel + 1, hlevel + 1)

        if A is None:
            return []
        ret = []
        mi, ma = findVerticalLevels(A, 0)
        levelA = 0 - mi
        fillOrders(A, ret, levelA, 0)
        ls = []
        # print(ret)
        for ll in ret:
            ll.sort(key=lambda x: x[0])
            ls.append([e[1] for e in ll])
        return ls
