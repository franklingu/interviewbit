'''
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers % 1003.

Example :

    1
   / \
  2   3
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = (12 + 13) % 1003 = 25 % 1003 = 25.
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
    def sumNumbers(self, A):
        def lsToNum(ls):
            a = 0
            for n in ls:
                a = a * 10 + n
            return a

        def sumNums(A, ls, ss):
            if A is None:
                return
            ls.append(A.val)
            if A.left is None and A.right is None:
                ss[0] = ss[0] + lsToNum(ls)
                ls.pop()
                return
            if A.left is not None:
                sumNums(A.left, ls, ss)
            if A.right is not None:
                sumNums(A.right, ls, ss)
            ls.pop()

        ss = [0]
        sumNums(A, [], ss)
        return ss[0] % 1003

