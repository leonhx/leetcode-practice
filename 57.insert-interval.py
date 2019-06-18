#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#
class Solution:
    def overlap(self, interval_a: List[int], interval_b: List[int]) -> bool:
        a_st, a_et = interval_a
        b_st, b_et = interval_b
        return a_st <= b_st <= a_et or a_st <= b_et <= a_et or \
            (b_st <= a_st and b_et >= a_et)

    def merge(self, interval_a: List[int], interval_b: List[int]) -> bool:
        return [min([interval_a[0], interval_b[0]]), max([interval_a[1], interval_b[1]])]

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        mid_i = len(intervals) // 2
        if self.overlap(intervals[mid_i], newInterval):
            newInterval = self.merge(intervals[mid_i], newInterval)
            i, j = mid_i - 1, mid_i + 1
            while i >= 0 and self.overlap(intervals[i], newInterval):
                newInterval = self.merge(intervals[i], newInterval)
                i -= 1
            while j < len(intervals) and self.overlap(intervals[j], newInterval):
                newInterval = self.merge(intervals[j], newInterval)
                j += 1
            return self.insert(intervals[:i + 1] + intervals[j:], newInterval)
        elif newInterval[1] < intervals[mid_i][0]:
            return self.insert(intervals[:mid_i], newInterval) + intervals[mid_i:]
        elif newInterval[0] > intervals[mid_i][1]:
            return intervals[:mid_i + 1] + self.insert(intervals[mid_i + 1:], newInterval)
        else:
            raise RuntimeError('should not reach here')
