'''
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, A):
        if A is None or A.next is None:
            return A
        nh = ListNode(None)
        nh.next = A
        prepre, pre, curr = nh, A, A.next
        should_remove = False
        while curr is not None:
            if pre.val == curr.val:
                should_remove = True
                curr = curr.next
            else:
                if should_remove:
                    prepre.next = curr
                    should_remove = False
                else:
                    prepre = pre
                pre = curr
                curr = curr.next
        if should_remove:
            prepre.next = curr
        return nh.next
