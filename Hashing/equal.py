'''
Given an array A of integers, find the index of values that satisfy A + B = C + D, where A,B,C & D are integers values in the array

Note:

1) Return the indices `A1 B1 C1 D1`, so that
  A[A1] + A[B1] = A[C1] + A[D1]
  A1 < B1, C1 < D1
  A1 < C1, B1 != D1, B1 != C1

2) If there are more than one solutions,
   then return the tuple of values which are lexicographical smallest.

Assume we have two solutions
S1 : A1 B1 C1 D1 ( these are values of indices int the array )
S2 : A2 B2 C2 D2

S1 is lexicographically smaller than S2 iff
  A1 < A2 OR
  A1 = A2 AND B1 < B2 OR
  A1 = A2 AND B1 = B2 AND C1 < C2 OR
  A1 = A2 AND B1 = B2 AND C1 = C2 AND D1 < D2
Example:

Input: [3, 4, 7, 1, 2, 9, 8]
Output: [0, 2, 3, 5] (O index)
If no solution is possible, return an empty list.
'''


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def equal(self, A):
        table = {}
        for i, e in enumerate(A):
            for j in xrange(i + 1, len(A)):
                s = e + A[j]
                if s not in table:
                    table[s] = []
                table[s].append((i, j))

        ret = None
        for k, v in table.iteritems():
            if len(v) < 2:
                continue
            ss = set(v[0])
            vc = None
            for vt in v[1:]:
                if vt[0] in ss or vt[1] in ss:
                    continue
                vc = vt
                break
            if vc is None:
                continue
            tmp = list(v[0]) + list(vc)
            if ret is None:
                ret = tmp
            if tmp < ret:
                ret = tmp
        return ret
