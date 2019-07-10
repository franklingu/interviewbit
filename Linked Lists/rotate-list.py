'''
Given a list, rotate the list to the right by k places, where k is non-negative.

For example:

Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
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
    def rotateRight(self, A, B):
        def findLen(node):
            cnt = 0
            while node is not None:
                cnt += 1
                node = node.next
            return cnt

        l = findLen(A)
        if A is None or B % l == 0:
            return A
        B = B % l
        nh = ListNode(None)
        nh.next = A
        prev, curr = nh, A
        count, fast, pfast = 0, A, nh
        while fast is not None:
            if count >= B:
                break
            count += 1
            pfast = fast
            fast = fast.next
        if fast is None:
            return A
        while fast is not None:
            prev = curr
            curr = curr.next
            pfast = fast
            fast = fast.next
        prev.next = None
        nh.next = curr
        pfast.next = A
        return nh.next
