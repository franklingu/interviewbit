'''
Given a collection of integers that might contain duplicates, S, return all possible subsets.

 Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
The subsets must be sorted lexicographically.
Example :
If S = [1,2,2], the solution is:

[
[],
[1],
[1,2],
[1,2,2],
[2],
[2, 2]
]
'''


class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def subsetsWithDup(self, A):
        def fillSubsets(arr, index, curr, subsets):
            if index >= len(arr):
                subsets.add(tuple(curr))
                return
            fillSubsets(arr, index + 1, curr, subsets)
            curr.append(arr[index])
            fillSubsets(arr, index + 1, curr, subsets)
            curr.pop()

        subsets = set()
        fillSubsets(sorted(A), 0, [], subsets)
        return sorted([list(a) for a in subsets])
