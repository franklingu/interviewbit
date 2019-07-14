'''
Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

 Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combinations.
Example :

Given candidate set 10,1,2,7,6,1,5 and target 8,

A solution set is:

[1, 7]
[1, 2, 5]
[2, 6]
[1, 1, 6]
 Warning : DO NOT USE LIBRARY FUNCTION FOR GENERATING COMBINATIONS.
Example : itertools.combinations in python.
If you do, we will disqualify your submission retroactively and give you penalty points.
'''


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def combinationSum(self, A, B):
        def fillCombinations(arr, index, remain, curr, combinations):
            if remain == 0:
                combinations.add(tuple(curr))
                return
            elif index >= len(arr):
                return
            fillCombinations(arr, index + 1, remain, curr, combinations)
            curr.append(arr[index])
            fillCombinations(arr, index + 1, remain - arr[index], curr, combinations)
            curr.pop()

        combinations = set()
        fillCombinations(sorted(A), 0, B, [], combinations)
        return [list(a) for a in combinations]
