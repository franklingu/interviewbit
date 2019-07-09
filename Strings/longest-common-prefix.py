'''
Write a function to find the longest common prefix string amongst an array of strings.

Longest common prefix for a pair of strings S1 and S2 is the longest string S which is the prefix of both S1 and S2.

As an example, longest common prefix of "abcdefgh" and "abcefgh" is "abc".

Given the array of strings, you need to find the longest S which is the prefix of ALL the strings in the array.

Example:

Given the array as:

[

  "abcdefgh",

  "aefghijk",

  "abcefgh"
]
The answer would be “a”.
'''

'''
Prefix ==> Trie
'''


class TrieNode:
    def __init__(self):
        self.children = [None] * 256
        self.num = 0
 
 
class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.num = 0
    
    def add(self, ss):
        curr = self.root
        for c in ss:
            n = ord(c)
            if curr.children[n] is None:
                curr.children[n] = TrieNode()
            curr = curr.children[n]
            curr.num += 1
        self.root.num += 1
        self.num += 1
    
    def findLongestCommonPrefix(self):
        queue = [(self.root, '', 0)]
        ret = []
        parents = {}
        max_len, node = 0, None
        while len(queue) > 0:
            curr, cc, curr_len = queue.pop(0)
            if max_len < curr_len:
                max_len = curr_len
                node = (curr, cc)
            if curr.num < self.num:
                continue
            for i, ch in enumerate(curr.children):
                if ch is None:
                    continue
                if ch.num < self.num:
                    continue
                queue.append((ch, chr(i), curr_len + 1))
                parents[ch] = (curr, cc)
        while node is not None:
            ret.append(node[1])
            node = parents.get(node[0], None)
        return ''.join(reversed(ret))
 
class Solution:
    # @param A : list of strings
    # @return a strings
    def longestCommonPrefix(self, A):
        trie = Trie()
        for ss in A:
            trie.add(ss)
        return trie.findLongestCommonPrefix()
