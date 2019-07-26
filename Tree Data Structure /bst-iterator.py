'''
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

The first call to next() will return the smallest number in BST. Calling next() again will return the next smallest number in the BST, and so on.

 Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
Try to optimize the additional space complexity apart from the amortized time complexity.
'''


# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import heapq

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        def fillStack(curr, stack):
            if curr is None:
                return
            fillStack(curr.left, stack)
            stack.append(curr.val)
            fillStack(curr.right, stack)

        self.root = root
        stack = []
        fillStack(root, stack)
        heapq.heapify(stack)
        self.stack = stack

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return len(self.stack) > 0


    # @return an integer, the next smallest number
    def next(self):
        return heapq.heappop(self.stack)

# Your BSTIterator will be called like this:
# i = BSTIterator(root)
# while i.hasNext(): print i.next(),


# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator2:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        def inorder_iter(node):
            if node is None:
                return
            # use yield from in Python 3
            for val in inorder_iter(node.left):
                yield val
            yield node.val
            # use yield from in Python 3
            for val in inorder_iter(node.right):
                yield val

        self.iter = inorder_iter(root)
        self.curr = None

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        if self.curr is not None:
            return True
        self.curr = next(self.iter, None)
        return self.curr is not None

    # @return an integer, the next smallest number
    def next(self):
        has_next = self.hasNext()
        if self.curr is not None:
            val = self.curr
            self.curr = None
        else:
            val = None
        return val

# Your BSTIterator will be called like this:
# i = BSTIterator(root)
# while i.hasNext(): print i.next(),

