'''
Given a singly linked list

    L: L0 → L1 → … → Ln-1 → Ln,
reorder it to:

    L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …
You must do this in-place without altering the nodes’ values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def reorderList(self, A):
        def breakListIntoHalves(node):
            prev = None
            slow, fast = node, node.next
            while fast is not None:
                fast = fast.next
                prev = slow
                slow = slow.next
                if fast is None:
                    break
                fast = fast.next
            else:
                prev = slow
                slow = slow.next
            if prev is not None:
                prev.next = None
            return node, slow

        def reverseList(node):
            prev, curr = None, node
            while curr is not None:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            return prev

        def printList(node):
            while node is not None:
                print(node.val)
                node = node.next
            print()

        if A is None or A.next is None:
            return A
        nh = ListNode(None)
        curr = nh
        h1, h2 = breakListIntoHalves(A)
        h2 = reverseList(h2)
        # printList(h1)
        # printList(h2)
        start_front = True
        c1, c2 = h1, h2
        while c1 is not None or c2 is not None:
            if start_front:
                curr.next = c1
                c1 = c1.next
            else:
                curr.next = c2
                c2 = c2.next
            curr = curr.next
            start_front = not start_front
        return nh.next
