#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#

# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        if len(heights) == 1:
            return heights[0]
        min_i, min_h = 0, heights[0]
        for i, h in enumerate(heights):
            if h < min_h:
                min_i = i
                min_h = h
        area = min_h * len(heights)
        left_max = self.largestRectangleArea(heights[:min_i])
        right_max = self.largestRectangleArea(heights[min_i + 1:])
        return max([area, left_max, right_max])
# @lc code=end
