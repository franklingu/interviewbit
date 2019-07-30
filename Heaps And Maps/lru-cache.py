'''
Design and implement a data structure for LRU (Least Recently Used) cache. It should support the following operations: get and set.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
set(key, value) - Set or insert the value if the key is not already present. When the cache reaches its capacity, it should invalidate the least recently used item before inserting the new item.
The LRU Cache will be initialized with an integer corresponding to its capacity. Capacity indicates the maximum number of unique keys it can hold at a time.

Definition of “least recently used” : An access to an item is defined as a get or a set operation of the item. “Least recently used” item is the one with the oldest access time.

 NOTE: If you are using any global variables, make sure to clear them in the constructor.
Example :

Input :
         capacity = 2
         set(1, 10)
         set(5, 12)
         get(5)        returns 12
         get(1)        returns 10
         get(10)       returns -1
         set(6, 14)    this pushes out key = 5 as LRU is full.
         get(5)        returns -1

'''


class Node(object):
    def __init__(self, val):
        self.prev = None
        self.next = None
        self.val = val


class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.nums = 0
        self.track = {}
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head


    # @return an integer
    def get(self, key):
        if key not in self.track:
            return -1
        node = self.track[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        node.prev = self.head
        return node.val[1]


    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.track:
            self.get(key)
            self.track[key].val[1] = value
            return
        if self.capacity <= 0:
            return
        if self.nums >= self.capacity:
            old_key = self.tail.prev.val[0]
            del self.track[old_key]
            self.tail.prev = self.tail.prev.prev
            self.tail.prev.next = self.tail
            self.nums -= 1
        self.nums += 1
        node = Node([key, value])
        self.track[key] = node
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        node.prev = self.head

