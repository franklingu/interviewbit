'''
Find the intersection of two sorted arrays.
OR in other words,
Given 2 sorted arrays, find all the elements which occur in both the arrays.

Example :

Input :
    A : [1 2 3 3 4 5 6]
    B : [3 3 5]

Output : [3 3 5]

Input :
    A : [1 2 3 3 4 5 6]
    B : [3 5]

Output : [3 5]
 NOTE : For the purpose of this problem ( as also conveyed by the sample case ),
  assume that elements that appear more than once in both arrays should be included multiple
   times in the final output.
'''


class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a list of integers
    def intersect(self, A, B):
        ret = []
        s1, s2 = 0, 0
        l1, l2 = len(A), len(B)
        while s1 < l1 and s2 < l2:
            e1 = A[s1]
            e2 = B[s2]
            if e1 == e2:
                ret.append(e1)
                s1 += 1
                s2 += 1
            elif e1 > e2:
                # notice this be faster than linear
                # by doing binary search
                s2 += 1
            else:
                # notice this be faster than linear
                # by doing binary search
                s1 += 1
        return ret
