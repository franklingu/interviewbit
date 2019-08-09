'''
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Example :

Input : [1 2]
Return :  1
'''


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        minSofar = []
        for i, e in enumerate(A):
            if i == 0:
                minSofar.append(e)
            else:
                minSofar.append(min(minSofar[-1], e))
        mm = 0
        for i, e in enumerate(A):
            mm = max(mm, e - minSofar[i])
        return mm
