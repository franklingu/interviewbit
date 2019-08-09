'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

Example :

Input : [1 2 3]
Return : 2
'''


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        minProfit = []
        ret = 0
        mm = 0
        for i, p in enumerate(A):
            if i == 0:
                minProfit.append(p)
                continue
            if p < A[i - 1]:
                ret += mm
                mm = 0
                minProfit.append(p)
            else:
                minProfit.append(min(minProfit[-1], p))
                mm = max(p - minProfit[-1], mm)
        if mm > 0:
            ret += mm
        return ret
