#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i: i[0])
        result = []
        for interval in intervals:
            if not result:
                result.append(interval)
            else:
                last_interval = result[-1]
                if last_interval[1] >= interval[0]:
                    last_interval[1] = max([last_interval[1], interval[1]])
                else:
                    result.append(interval)
        return result
