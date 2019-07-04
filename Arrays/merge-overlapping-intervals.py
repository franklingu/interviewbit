'''
Given a collection of intervals, merge all overlapping intervals.

For example:

Given [1,3],[2,6],[8,10],[15,18],

return [1,6],[8,10],[15,18].

Make sure the returned intervals are sorted.
'''

'''
Sort interval by start and end. Merge prev and curr if possible.
'''


# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
 
class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge(self, intervals):
        intervals.sort(key=lambda x: (x.start, x.end))
        ret = []
        prev = None
        for interval in intervals:
            if prev is None:
                prev = interval
                continue
            if prev.end < interval.start:
                ret.append(prev)
                prev = interval
                continue
            prev.start = min(prev.start, interval.start)
            prev.end = max(prev.end, interval.end)
        ret.append(prev)
        return ret
