'''
Given an integer array, find if an integer p exists in the array such that the number of integers greater than p in the array equals to p
If such an integer is found return 1 else return -1.
'''

'''
sort and pay attention to duplicate numbers
'''


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A = sorted(A)
        prev = None
        l = len(A)
        for i, p in enumerate(A):
            if prev is None:
                prev = p
                continue
            if prev != p:
                idx = l - i
                if idx == prev:
                    return 1
            prev = p
        # if last prev is 0, then it will match
        if prev == 0:
            return 1
        return -1
