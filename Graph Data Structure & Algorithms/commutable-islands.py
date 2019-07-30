'''
There are n islands and there are many bridges connecting them. Each bridge has some cost attached to it.

We need to find bridges with minimal cost such that all islands are connected.

It is guaranteed that input data will contain at least one possible scenario in which all islands are connected with each other.

Example :
Input

         Number of islands ( n ) = 4
         1 2 1
         2 3 4
         1 4 3
         4 3 2
         1 3 10
In this example, we have number of islands(n) = 4 . Each row then represents a bridge configuration. In each row first two numbers represent the islands number which are connected by this bridge and the third integer is the cost associated with this bridge.

In the above example, we can select bridges 1(connecting islands 1 and 2 with cost 1), 3(connecting islands 1 and 4 with cost 3), 4(connecting islands 4 and 3 with cost 2). Thus we will have all islands connected with the minimum possible cost(1+3+2 = 6).
In any other case, cost incurred will be more.
'''

'''
Minimum spanning tree
'''


class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        import heapq
        pq = []
        track = {}
        min_cost, mstart, mend = None, None, None
        for start, end, cost in B:
            if start not in track:
                track[start] = {}
            if end not in track:
                track[end] = {}
            track[start][end] = cost
            track[end][start] = cost
            if min_cost is None or min_cost > cost:
                min_cost, mstart, mend = cost, start, end
        pq.append((min_cost, mstart, mend))
        visited = set()
        ret = 0
        while pq and len(visited) < A:
            cost, start, end = heapq.heappop(pq)
            if start in visited and end in visited:
                continue
            ret += cost
            candidates = []
            if start not in visited:
                visited.add(start)
                candidates.append(start)
            if end not in visited:
                visited.add(end)
                candidates.append(end)
            for point in candidates:
                for neighbor, cost in track[point].iteritems():
                    if neighbor in visited:
                        continue
                    heapq.heappush(pq, (cost, point, neighbor))
        return ret
