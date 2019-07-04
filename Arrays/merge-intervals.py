'''
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

Given intervals [1,3],[6,9] insert and merge [2,5] would result in [1,5],[6,9].

Example 2:

Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] would result in [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].

Make sure the returned intervals are also sorted.
'''


'''
Find a place to insert and merge prev with current if necessary.
'''


# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param new_interval, a Interval
    # @return a list of Interval
    def insert(self, intervals, new_interval):
        ret = []
        inserted = False
        for interval in intervals:
            if inserted:
                ret.append(interval)
                continue
            if interval.start < new_interval.start:
                ret.append(interval)
            else:
                ret.append(new_interval)
                ret.append(interval)
                inserted = True
        if not inserted:
            ret.append(new_interval)
        prev = None
        ret2 = []
        for interval in ret:
            if prev is None:
                prev = interval
                continue
            if prev.end < interval.start:
                ret2.append(prev)
                prev = interval
                continue
            prev.start = min(prev.start, interval.start)
            prev.end = max(prev.end, interval.end)
        ret2.append(prev)
        return ret2
