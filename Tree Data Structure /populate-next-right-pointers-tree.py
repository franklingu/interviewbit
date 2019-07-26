'''
Given a binary tree

    struct TreeLinkNode {
      TreeLinkNode *left;
      TreeLinkNode *right;
      TreeLinkNode *next;
    }
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

 Note:
You may only use constant extra space.
Example :

Given the following binary tree,

         1
       /  \
      2    3
     / \  / \
    4  5  6  7
After calling your function, the tree should look like:

         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \  / \
    4->5->6->7 -> NULL
 Note 1: that using recursion has memory overhead and does not qualify for constant space.
Note 2: The tree need not be a perfect binary tree.
'''

"""
The following code is tested for https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

The interviewbit testing code is weird. I gave up trying this for interviewbit
"""


"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return root
        curr, next_head, next_curr = root, None, None
        while curr is not None:
            if next_curr is None:
                if curr.left is not None:
                    next_curr = curr.left
                    next_head = next_curr
                    if curr.right is not None:
                        curr.left.next = curr.right
                        next_curr = curr.right
                elif curr.right is not None:
                    next_curr = curr.right
                    next_head = next_curr
            else:
                if curr.left is not None:
                    next_curr.next = curr.left
                    next_curr = curr.left
                    if curr.right is not None:
                        curr.left.next = curr.right
                        next_curr = curr.right
                elif curr.right is not None:
                    next_curr.next = curr.right
                    next_curr = curr.right
            if curr.next is not None:
                curr = curr.next
            else:
                curr = next_head
                next_head, next_curr = None, None
        return root
