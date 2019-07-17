'''
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or NULL.

Return a deep copy of the list.

Example

Given list

   1 -> 2 -> 3
with random pointers going from

  1 -> 3
  2 -> 1
  3 -> 1
You should return a deep copy of the list. The returned answer should not contain the same node as the original list, but a copy of them. The pointers in the returned list should not link to any node in the original input list.
'''

'''
This can be done with dict but the following algorithm is much more clever
'''


# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        dd = {}
        nh = None
        prev, curr = None, head
        while curr is not None:
            node = RandomListNode(curr.label)
            dd[curr] = node
            if nh is None:
                nh = node
            if prev is not None:
                prev.next = node
            prev = node
            curr = curr.next
        curr = head
        while curr is not None:
            if curr.random is not None:
                rand = dd[curr.random]
                dd[curr].random = rand
            curr = curr.next
        return nh
