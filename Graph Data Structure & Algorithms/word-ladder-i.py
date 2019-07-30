'''
Given two words (start and end), and a dictionary, find the length of shortest transformation sequence from start to end, such that:

You must change exactly one character in every transformation
Each intermediate word must exist in the dictionary
Example :

Given:

start = "hit"
end = "cog"
dict = ["hot","dot","dog","lot","log"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Note that we account for the length of the transformation path instead of the number of transformation itself.

 Note:
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
'''


class Solution:
    # @param start : string
    # @param end : string
    # @param dictV : list of strings
    # @return an integer
    def ladderLength(self, start, end, dictV):
        def find_neighbors(curr, words, visited):
            for word in words:
                if word in visited:
                    continue
                diff = False
                for ch1, ch2 in zip(curr, word):
                    if ch1 != ch2 and diff:
                        break
                    elif ch1 != ch2:
                        diff = True
                else:
                    if diff:
                        yield word

        queue = [(start, 1)]
        visited = set()
        while queue:
            curr, step = queue.pop(0)
            if curr == end:
                return step
            visited.add(curr)
            for neighbor in find_neighbors(curr, dictV, visited):
                queue.append((neighbor, step + 1))
        return 0
