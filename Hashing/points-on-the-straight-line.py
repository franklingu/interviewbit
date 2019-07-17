'''
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

Sample Input :

(1, 1)
(2, 2)
Sample Output :

2
You will be given 2 arrays X and Y. Each point is represented by (X[i], Y[i])
'''


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def maxPoints(self, A, B):
        if len(A) <= 1:
            return len(A)
        from fractions import Fraction
        track = {}
        points = [(a, b) for a, b in zip(A, B)]
        for i, p1 in enumerate(points):
            for j in xrange(i + 1, len(points)):
                p2 = points[j]
                if p2[0] - p1[0] == 0:
                    a = 'infinity'
                    b = p2[0]
                else:
                    frac = Fraction(p2[1] - p1[1], p2[0] - p1[0])
                    a = (frac.numerator, frac.denominator)
                    frac2 = Fraction(p1[0] * frac.numerator - p1[1] * frac.denominator, frac.denominator)
                    b = (frac2.numerator, frac2.denominator)
                rep = (a, b)
                if rep in track:
                    track[rep].add(i)
                    track[rep].add(j)
                else:
                    track[rep] = set((i, j))
        return max((len(val) for val in track.values()))
