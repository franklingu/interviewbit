'''
Given three prime number(p1, p2, p3) and an integer k. Find the first(smallest) k integers which have only p1, p2, p3 or a combination of them as their prime factors.

Example:

Input :
Prime numbers : [2,3,5]
k : 5

If primes are given as p1=2, p2=3 and p3=5 and k is given as 5, then the sequence of first 5 integers will be:

Output:
{2,3,4,5,6}

Explanation :
4 = p1 * p1 ( 2 * 2 )
6 = p1 * p2 ( 2 * 3 )

Note: The sequence should be sorted in ascending order
'''


class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @return a list of integers
    def solve(self, A, B, C, D):
        import heapq
        primes = [A, B, C]
        pq = [1]
        ret = set()
        candidates = set((1,))
        while len(ret) < D:
            curr = heapq.heappop(pq)
            if curr != 1:
                ret.add(curr)
            for p in primes:
                elem = p * curr
                if elem in candidates:
                    continue
                heapq.heappush(pq, elem)
                candidates.add(elem)
        return sorted(ret)

