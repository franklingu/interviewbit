'''
Given two arrays A & B of size N each.
Find the maximum N elements from the sum combinations (Ai + Bj) formed from elements in array A and B.

For example if A = [1,2], B = [3,4], then possible pair sums can be 1+3 = 4 , 1+4=5 , 2+3=5 , 2+4=6
and maximum 2 elements are 6, 5

Example:

N = 4
a[]={1,4,2,3}
b[]={2,5,1,6}

Maximum 4 elements of combinations sum are
10   (4+6),
9    (3+6),
9    (4+5),
8    (2+6)
'''


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        import heapq
        A.sort()
        B.sort()
        acc = 0
        i, j = len(A) - 1, len(B) - 1
        hp = [(- A[-1] - B[-1], i, j)]
        track = set([(i, j)])
        ret = []
        while len(ret) < len(A):
            val, i, j = heapq.heappop(hp)
            # print(val, A[i], A[j])
            ret.append(-val)
            if (i, j - 1) not in track:
                heapq.heappush(hp, (-A[i] - B[j - 1], i, j - 1))
                track.add((i, j - 1))
            if (i - 1, j) not in track:
                heapq.heappush(hp, (-A[i - 1] - B[j], i - 1, j))
                track.add((i - 1, j))
        return ret
