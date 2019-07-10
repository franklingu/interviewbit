'''
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Try solving it using constant additional space.

Example :

Input :

                  ______
                 |     |
                 \/    |
        1 -> 2 -> 3 -> 4

Return the node corresponding to node 3.
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the first node in the cycle in the linked list
    def detectCycle(self, A):
        if A is None or A.next is None:
            return None
        slow, fast = A, A.next
        while fast is not None:
            if fast == slow:
                break
            fast = fast.next
            if fast is None:
                return None
            fast = fast.next
            slow = slow.next
        if fast is None:
            return None
        fast = fast.next
        slow = A
        while slow != fast:
            # print(fast.val, slow.val)
            fast = fast.next
            slow = slow.next
        return slow
