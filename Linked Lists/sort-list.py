'''
Sort a linked list in O(n log n) time using constant space complexity.

Example :

Input : 1 -> 5 -> 4 -> 3

Returned list : 1 -> 3 -> 4 -> 5
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def sortList(self, A):
        def mergeSortList(n1, n2):
            m1 = self.sortList(n1)
            m2 = self.sortList(n2)
            return mergeList(m1, m2)

        def mergeList(m1, m2):
            nh = ListNode(None)
            curr = nh
            c1, c2 = m1, m2
            while c1 is not None and c2 is not None:
                if c1.val <= c2.val:
                    curr.next = c1
                    c1 = c1.next
                else:
                    curr.next = c2
                    c2 = c2.next
                curr = curr.next
            while c1 is not None:
                curr.next = c1
                c1 = c1.next
                curr = curr.next
            while c2 is not None:
                curr.next = c2
                c2 = c2.next
                curr = curr.next
            curr.next = None
            return nh.next

        def getMiddle(node):
            slow, fast = None, node
            while fast is not None:
                fast = fast.next
                if fast is None:
                    break
                fast = fast.next
                if slow is None:
                    slow = node
                else:
                    slow = slow.next
            if slow is None:
                return None
            nn = slow.next
            slow.next = None
            return nn

        if A is None or A.next is None:
            return A
        middle = getMiddle(A)
        return mergeSortList(A, middle)
