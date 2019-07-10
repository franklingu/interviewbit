'''
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

    342 + 465 = 807
Make sure there are no trailing zeros in the output list
So, 7 -> 0 -> 8 -> 0 is not a valid response even though the value is still 807.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def addTwoNumbers(self, A, B):
        # def reverseList(head):
        #     if head is None or head.next is None:
        #         return head
        #     prev, curr, nn = None, head, head.next
        #     while curr is not None:
        #         curr.next = prev
        #         prev = curr
        #         curr = nn
        #         if nn is not None:
        #             nn = nn.next
        #     return prev

        def addTwoList(h1, h2):
            c1, c2 = h1, h2
            h, p = None, None
            carry = 0
            while c1 is not None or c2 is not None:
                v1 = c1.val if c1 is not None else 0
                v2 = c2.val if c2 is not None else 0
                carry, v = divmod(v1 + v2 + carry, 10)
                n = ListNode(v)
                if h is None:
                    h = n
                if p is not None:
                    p.next = n
                p = n
                if c1 is not None:
                    c1 = c1.next
                if c2 is not None:
                    c2 = c2.next
            if carry != 0:
                n = ListNode(carry)
                p.next = n
            return h

        return addTwoList(A, B)
