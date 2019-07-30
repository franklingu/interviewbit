'''
Merge k sorted linked lists and return it as one sorted list.

Example :

1 -> 10 -> 20
4 -> 11 -> 13
3 -> 8 -> 9
will result in

1 -> 3 -> 4 -> 8 -> 9 -> 10 -> 11 -> 13 -> 20
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : list of linked list
    # @return the head node in the linked list
    def mergeKLists(self, A):
        import heapq
        hp = []
        for node in A:
            hp.append((node.val, node))
        heapq.heapify(hp)
        head, curr = None, None
        while len(hp) > 0:
            val, node = heapq.heappop(hp)
            if head is None:
                head = node
            if curr is None:
                pass
            else:
                curr.next = node
            curr = node
            if node.next is None:
                continue
            heapq.heappush(hp, (node.next.val, node.next))
        return head
