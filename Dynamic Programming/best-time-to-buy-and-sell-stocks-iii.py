'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

Example :

Input : [1 2 1 2]
Output : 2

Explanation :
  Day 1 : Buy
  Day 2 : Sell
  Day 3 : Buy
  Day 4 : Sell
'''


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        if len(A) < 2:
            return 0
        ret = 0
        K = 2
        track = [[0 for p in A] for _ in xrange(K + 1)]
        for i in xrange(1, K + 1):
            tmpMax = track[i - 1][0] - A[0]
            for ii in xrange(1, len(A)):
                track[i][ii] = max(track[i][ii - 1], A[ii] + tmpMax)
                tmpMax = max(tmpMax, track[i - 1][ii] - A[ii])
                ret = max(track[i][ii], ret)
        return ret



"""
Build on top of the idea of as many transactions as possible can remove
transaction until 2 level.
"""

class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        def get_transactions(prices):
            if len(prices) < 2:
                return []
            ret = []
            start = prices[0]
            for i, price in enumerate(prices):
                if i == 0:
                    continue
                if price < prices[i - 1]:
                    if start < prices[i - 1]:
                        ret.append(start)
                        ret.append(prices[i - 1])
                    start = price
            if prices[-1] > start:
                ret.append(start)
                ret.append(prices[-1])
            return ret

        def remove_one_transaction(prices):
            merge_pos = 0
            cost = None
            for i, price in enumerate(prices):
                if i == 0:
                    continue
                if cost is None or cost > abs(prices[i] - prices[i - 1]):
                    merge_pos = i - 1
                    cost = abs(prices[i] - prices[i - 1])
            del prices[merge_pos:merge_pos + 2]

        def get_profit(prices):
            ret = 0
            for i in range(0, len(prices), 2):
                ret = ret + prices[i + 1] - prices[i]
            return ret

        prices = get_transactions(prices)
        while len(prices) // 2 > 2:
            remove_one_transaction(prices)
        return get_profit(prices)
