'''
Given a set of reviews provided by the customers for different hotels and a string containing “Good Words”, you need to sort the reviews in descending order according to their “Goodness Value” (Higher goodness value first). We define the “Goodness Value” of a string as the number of “Good Words” in that string.

Note: Sorting should be stable. If review i and review j have the same “Goodness Value” then their original order would be preserved.

 You are expected to use Trie in an Interview for such problems

Constraints:

1.   1 <= No.of reviews <= 200
2.   1 <= No. of words in a review <= 1000
3.   1 <= Length of an individual review <= 10,000
4.   1 <= Number of Good Words <= 10,000
5.   1 <= Length of an individual Good Word <= 4
6.   All the alphabets are lower case (a - z)
Input:

S : A string S containing "Good Words" separated by  "_" character. (See example below)
R : A vector of strings containing Hotel Reviews. Review strings are also separated by "_" character.
Output:

A vector V of integer which contain the original indexes of the reviews in the sorted order of reviews.

V[i] = k  means the review R[k] comes at i-th position in the sorted order. (See example below)
In simple words, V[i]=Original index of the review which comes at i-th position in the sorted order. (Indexing is 0 based)
Example:

Input:
S = "cool_ice_wifi"
R = ["water_is_cool", "cold_ice_drink", "cool_wifi_speed"]

Output:
ans = [2, 0, 1]
Here, sorted reviews are ["cool_wifi_speed", "water_is_cool", "cold_ice_drink"]
'''

'''
Using trie or better hashing to solve this easily
'''


class TrieNode:
    def __init__(self):
        self.endOfWord = False
        self.children = [None] * 26

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        node = self.root
        for ch in word:
            val = ord(ch) - ord('a')
            if node.children[val] is not None:
                node = node.children[val]
            else:
                node.children[val] = TrieNode()
                node = node.children[val]
        node.endOfWord = True

    def checkWord(self, word):
        node = self.root
        for ch in word:
            val = ord(ch) - ord('a')
            if node.children[val] is None:
                return False
            node = node.children[val]
        return node.endOfWord

class Solution:
    # @param A : string
    # @param B : list of strings
    # @return a list of integers
    def solve(self, A, B):
        trie = Trie()
        word = []
        for c in A:
            if c == '_':
                trie.addWord(word)
                word = []
                continue
            word.append(c)
        if word:
            trie.addWord(word)
            word = []
        ret = []
        for i, s in enumerate(B):
            word = []
            tmp = 0
            for c in s:
                if c == '_':
                    contains = trie.checkWord(word)
                    if contains:
                        tmp += 1
                    word = []
                    continue
                word.append(c)
            if word:
                contains = trie.checkWord(word)
                if contains:
                    tmp += 1
                word = []
            ret.append((-tmp, i))
        ret.sort()
        return [e[1] for e in ret]

    # @param A : string
    # @param B : list of strings
    # @return a list of integers
    def solve2(self, A, B):
        V = set(A.split("_"))
        ans = sorted([
            (sum(-1 for w in b.split("_") if w in V), i)
            for i, b in enumerate(B)
        ])
        return [i for val, i in ans]
