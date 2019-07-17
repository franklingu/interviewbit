'''
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

 Note:
Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a ≤ b ≤ c ≤ d)
The solution set must not contain duplicate quadruplets.
Example :
Given array S = {1 0 -1 0 -2 2}, and target = 0
A solution set is:

    (-2, -1, 1, 2)
    (-2,  0, 0, 2)
    (-1,  0, 0, 1)
Also make sure that the solution set is lexicographically sorted.
Solution[i] < Solution[j] iff Solution[i][0] < Solution[j][0] OR (Solution[i][0] == Solution[j][0] AND ... Solution[i][k] < Solution[j][k])
'''

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def fourSum(self, A, B):
        pairSums = dict()
        for i, a in enumerate(A):
            for j in xrange(i + 1, len(A)):
                b = A[j]
                tmp = a + b
                if tmp not in pairSums:
                    pairSums[tmp] = []
                pairSums[tmp].append((i, j))
        ret = set()
        for k, vals in pairSums.iteritems():
            target = B - k
            if target not in pairSums:
                continue
            vals2 = pairSums[target]
            for p1 in vals:
                for p2 in vals2:
                    ss = set(p1 + p2)
                    if len(ss) != 4:
                        continue
                    ss = sorted([A[i] for i in list(ss)])
                    ret.add(tuple(ss))
        return sorted([list(e) for e in ret])
