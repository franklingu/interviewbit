'''
Given a collection of numbers, return all possible permutations.

Example:

[1,2,3] will have the following permutations:

[1,2,3]
[1,3,2]
[2,1,3]
[2,3,1]
[3,1,2]
[3,2,1]
 NOTE
No two entries in the permutation sequence should be the same.
For the purpose of this problem, assume that all the numbers in the collection are unique.
 Warning : DO NOT USE LIBRARY FUNCTION FOR GENERATING PERMUTATIONS.
Example : next_permutations in C++ / itertools.permutations in python.
If you do, we will disqualify your submission retroactively and give you penalty points.
'''


class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def permute(self, A):
        def fillPermutations(remaining, curr, ss, permutations):
            if remaining == 0:
                permutations.append(list(curr))
                return
            for c in ss:
                curr.append(c)
                fillPermutations(remaining - 1, curr, ss - set([c]), permutations)
                curr.pop()

        permutations = []
        fillPermutations(len(A), [], set(A), permutations)
        return permutations
