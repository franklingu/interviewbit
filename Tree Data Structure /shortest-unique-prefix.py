'''
Find shortest unique prefix to represent each word in the list.

Example:

Input: [zebra, dog, duck, dove]
Output: {z, dog, du, dov}
where we can see that
zebra = z
dog = dog
duck = du
dove = dov
 NOTE : Assume that no word is prefix of another. In other words, the representation is always possible.
'''


class TrieNode:
    def __init__(self):
        self.track = {}
        self.isEnd = False

    def add(self, word):
        curr = self
        for c in word:
            node = TrieNode()
            if c not in curr.track:
                curr.track[c] = [node, 1]
            else:
                node = curr.track[c][0]
                curr.track[c][1] = curr.track[c][1] + 1
            curr = node
        curr.isEnd = True

    def findUniquePrefix(self, word):
        ret = []
        curr = self
        for c in word:
            node, val = curr.track[c]
            ret.append(c)
            if val == 1:
                break
            curr = node
        return ''.join(ret)

class Solution:
    # @param A : list of strings
    # @return a list of strings
    def prefix(self, A):
        root = TrieNode()
        for word in A:
            root.add(word)
        ret = []
        for word in A:
            ret.append(root.findUniquePrefix(word))
        return ret
