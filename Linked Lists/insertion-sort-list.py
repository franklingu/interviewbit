'''
Sort a linked list using insertion sort.

We have explained Insertion Sort at Slide 7 of Arrays

Insertion Sort Wiki has some details on Insertion Sort as well.

Example :

Input : 1 -> 3 -> 2

Return 1 -> 2 -> 3
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def insertionSortList(self, A):
        def insertIntoList(head, target):
            prev, curr = head, head.next
            while curr is not None:
                if curr.val > target.val:
                    break
                prev = curr
                curr = curr.next
            prev.next = target
            target.next = curr
            return head


        nh = ListNode(None)
        curr1 = A
        while curr1 is not None:
            tmp = curr1.next
            insertIntoList(nh, curr1)
            curr1 = tmp
        return nh.next
