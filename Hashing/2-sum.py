'''
Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 < index2. Please note that your returned answers (both index1 and index2 ) are not zero-based.
Put both these numbers in order in an array and return the array from your function ( Looking at the function signature will make things clearer ). Note that, if no pair exists, return empty list.

If multiple solutions exist, output the one where index2 is minimum. If there are multiple solutions with the minimum index2, choose the one with minimum index1 out of them.

Input: [2, 7, 11, 15], target=9
Output: index1 = 1, index2 = 2
'''


class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def twoSum(self, A, B):
        track = {}
        for i, c in enumerate(A):
            if c not in track:
                track[c] = []
            track[c].append(i)
        i1 = i2 = len(A)
        for key, indice in track.iteritems():
            remaining = B - key
            if remaining not in track:
                continue
            can1, can2 = indice[0], track[remaining][0]
            if can2 == can1 and len(indice) < 2:
                continue
            if can2 == can1:
                can2 = indice[1]
            if can2 < can1:
                can2, can1 = can1, can2
            if can2 < i2 or (can2 == i2 and can1 < i1):
                i1, i2 = can1, can2
        if i1 == i2:
            return []
        return [i1 + 1, i2 + 1]
