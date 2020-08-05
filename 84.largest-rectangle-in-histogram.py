#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#

# @lc code=start
class Solution:
    def largestRectangleArea_1(self, heights: List[int]) -> int:
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
        left_max = self.largestRectangleArea_1(heights[:min_i])
        right_max = self.largestRectangleArea_1(heights[min_i + 1:])
        return max([area, left_max, right_max])

    def largestRectangleArea_2(self, heights: List[int]) -> int:
        if not heights:
            return 0
        total_num = len(heights)
        if total_num == 1:
            return heights[0]
        max_area = heights[0]
        for i in range(total_num):
            min_h = heights[i]
            if min_h > max_area:
                max_area = min_h
            for j in range(i + 1, total_num):
                if heights[j] < min_h:
                    area = (j - i) * min_h
                    if area > max_area:
                        max_area = area
                    min_h = heights[j]
                if j == total_num - 1:
                    area = (j - i + 1) * min_h
                    if area > max_area:
                        max_area = area
        return max_area

    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        total_num = len(heights)
        if total_num == 1:
            return heights[0]

        less_from_left = [None] * total_num
        less_from_left[0] = -1
        for i in range(total_num):
            p = i - 1
            while p >= 0 and heights[p] >= heights[i]:
                p = less_from_left[p]  # magic!
            less_from_left[i] = p

        less_from_right = [None] * total_num
        less_from_right[total_num - 1] = total_num
        for i in range(total_num - 2, -1, -1):
            p = i + 1
            while p < total_num and heights[p] >= heights[i]:
                p = less_from_right[p]
            less_from_right[i] = p

        max_area = 0
        for i in range(total_num):
            max_area = max(max_area, heights[i] * (
                less_from_right[i] - less_from_left[i] - 1))
        return max_area
# @lc code=end
