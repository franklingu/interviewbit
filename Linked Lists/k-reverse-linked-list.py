'''
Given a singly linked list and an integer K, reverses the nodes of the

list K at a time and returns modified linked list.

 NOTE : The length of the list is divisible by K
Example :

Given linked list 1 -> 2 -> 3 -> 4 -> 5 -> 6 and K=2,

You should return 2 -> 1 -> 4 -> 3 -> 6 -> 5

Try to solve the problem using constant extra space.
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def reverseList(self, A, B):
        def reverseList(node):
            if node is None or node.next is None:
                return node
            prev, curr = None, node
            while curr is not None:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            return prev, node

        if B <= 1:
            return A
        nh = ListNode(None)
        nh.next = A
        head, prev, curr = nh, nh, A
        runner = 0
        while runner < B and curr is not None:
            prev = curr
            curr = curr.next
            runner += 1
            if runner == B:
                prev.next = None
                newHead, newTail = reverseList(head.next)
                head.next = newHead
                newTail.next = curr
                head = newTail
                runner = 0
        return nh.next
