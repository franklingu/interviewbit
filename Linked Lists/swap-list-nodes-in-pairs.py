'''
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def swapPairs(self, A):
        if A is None or A.next is None:
            return A
        nh = ListNode(None)
        nh.next = A
        prev, curr, post = nh, A, A.next
        while post is not None:
            tmp = post.next
            prev.next = post
            curr.next = tmp
            post.next = curr
            prev = curr
            curr = tmp
            if tmp is not None:
                post = tmp.next
            else:
                post = None
        return nh.next
