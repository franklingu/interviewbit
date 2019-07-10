'''
Given a singly linked list, determine if its a palindrome. Return 1 or 0 denoting if its a palindrome or not, respectively.

Notes:

Expected solution is linear in time and constant in space.
For example,

List 1-->2-->1 is a palindrome.
List 1-->2-->3 is not a palindrome.
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return an integer
    def lPalin(self, A):
        def findLength(A):
            res = 0
            curr = A
            while curr is not None:
                res += 1
                curr = curr.next
            return res

        def breakList(A, index):
            prev, curr = None, A
            while index > 0:
                prev = curr
                curr = curr.next
                index -= 1
            prev.next = None
            reverseList(A)
            return prev, curr

        def reverseList(A):
            if A is None or A.next is None:
                return A
            prev, curr, nn = None, A, A.next
            while curr is not None:
                curr.next = prev
                prev = curr
                curr = nn
                if nn is not None:
                    nn = nn.next
            return prev

        def isEqualList(A, B):
            c1, c2 = A, B
            while c1 is not None and c2 is not None:
                if c1.val != c2.val:
                    return 0
                c1 = c1.next
                c2 = c2.next
            if c1 is not None or c2 is not None:
                return 0
            return 1

        def restoreList(A, B):
            nh = reverseList(A)
            A.next = B
            return nh

        l = findLength(A)
        if l <= 1:
            return 1
        breakIndex = l / 2
        h1, h2 = breakList(A, breakIndex)
        c1, c2 = h1, h2
        if l % 2 == 1:
            c2 = h2.next
        result = isEqualList(c1, c2)
        restoreList(h1, h2)
        return result
