'''
Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.
'''


# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        track = {}
        queue = [node]
        visited = set()
        while len(queue) > 0:
            curr = queue[0]
            del queue[0]
            if curr in visited:
                continue
            visited.add(curr)
            newNode = UndirectedGraphNode(curr.label)
            if curr not in track:
                track[curr] = newNode
            for neighbor in curr.neighbors:
                queue.append(neighbor)
        queue = [node]
        visited = set()
        while len(queue) > 0:
            curr = queue[0]
            del queue[0]
            if curr in visited:
                continue
            visited.add(curr)
            newNode = track[curr]
            for neighbor in curr.neighbors:
                queue.append(neighbor)
                newNode.neighbors.append(track[neighbor])
        return track[node]
