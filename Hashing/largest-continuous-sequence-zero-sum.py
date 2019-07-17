'''
Find the largest continuous sequence in a array which sums to zero.

Example:


Input:  {1 ,2 ,-2 ,4 ,-4}
Output: {2 ,-2 ,4 ,-4}

 NOTE : If there are multiple correct answers, return the sequence which occurs first in the array.
'''


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def lszero(self, A):
        sums = {0: [-1]}
        ss = 0
        ml, start, end = 0, -1, -1
        for i, a in enumerate(A):
            ss += a
            if ss not in sums:
                sums[ss] = [i]
            elif len(sums[ss]) == 1:
                sums[ss].append(i)
            else:
                sums[ss][1] = i
            cl = 0
            if len(sums[ss]) > 1:
                cl = sums[ss][1] - sums[ss][0]
            if cl > ml:
                ml = cl
                if len(sums[ss]) == 1:
                    continue
                start, end = sums[ss]
        return A[start + 1:end + 1]
