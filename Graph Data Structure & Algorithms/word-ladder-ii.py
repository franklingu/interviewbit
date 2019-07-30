'''
Given two words (start and end), and a dictionary, find the shortest transformation sequence from start to end, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the dictionary
If there are multiple such sequence of shortest length, return all of them. Refer to the example for more details.

Example :

Given:

start = "hit"
end = "cog"
dict = ["hot","dot","dog","lot","log"]
Return

  [
    ["hit","hot","dot","dog","cog"],
    ["hit","hot","lot","log","cog"]
  ]
 Note:
All words have the same length.
All words contain only lowercase alphabetic characters.
'''


class Solution:
    # @param start : string
    # @param end : string
    # @param dictV : list of strings
    # @return a list of list of strings
    def findLadders(self, start, end, dictV):
        def diffByOne(word1, word2):
            diff = 0
            for c1, c2 in zip(word1, word2):
                if c1 != c2:
                    diff += 1
            return diff == 1

        def addToTrack(track, w1, w2):
            if w1 not in track:
                track[w1] = []
            track[w1].append(w2)

        def findNeighbors(curr, track):
            return track.get(curr, [])

        chain = dictV + [start, end]
        track = {}
        for word1 in chain:
            for word2 in chain:
                if diffByOne(word1, word2):
                    if word1 != end:
                        addToTrack(track, word1, word2)
                    if word2 != start:
                        addToTrack(track, word2, word1)
        queue = [(start, 0)]
        visited = {}
        minStep = None
        parent = {}
        while queue:
            curr, step = queue.pop(0)
            if curr in visited or (minStep is not None and minStep < step):
                continue
            visited[curr] = step
            if curr == end:
                minStep = step
            for ne in findNeighbors(curr, track):
                if ne in visited or step + 1 > visited.get(ne, step + 1):
                    continue
                if ne not in parent:
                    parent[ne] = {}
                if curr not in parent[ne]:
                    parent[ne][curr] = step + 1
                elif parent[ne][curr] < step + 1:
                    continue
                queue.append((ne, step + 1))
        if minStep is None:
            return []
        # print(start, end, minStep, parent)
        paths = [[end]]
        while minStep > 0:
            npaths = []
            for path in paths:
                last = path[0]
                if last not in parent:
                    continue
                for pp in parent[last]:
                    npaths.append([pp] + path)
            paths = npaths
            minStep -= 1
        return paths
