#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        mid_i = len(intervals) // 2
        mid_st, mid_et = intervals[mid_i]
        new_st, new_et = newInterval
        if mid_st <= new_st <= mid_et or mid_st <= new_et <= mid_et or \
                (new_st <= mid_st and new_et >= mid_et):
            newIntrvl = [min([mid_st, new_st]), max([mid_et, new_et])]
            return self.insert(intervals[:mid_i] + intervals[mid_i + 1:], newIntrvl)
        elif new_et < mid_st:
            return self.insert(intervals[:mid_i], newInterval) + intervals[mid_i:]
        elif new_st > mid_et:
            return intervals[:mid_i + 1] + self.insert(intervals[mid_i + 1:], newInterval)
        else:
            raise RuntimeError('should not reach here')
