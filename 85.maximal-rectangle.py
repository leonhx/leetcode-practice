#
# @lc app=leetcode id=85 lang=python3
#
# [85] Maximal Rectangle
#

# @lc code=start
class Solution:
    def largestRecInHist(self, heights: List[int]) -> int:
        if not heights:
            return 0
        total_num = len(heights)
        if total_num == 1:
            return heights[0]

        less_from_left = [None] * total_num
        less_from_left[0] = -1
        for i in range(1, total_num):
            p = i - 1
            while p >= 0 and heights[p] >= heights[i]:
                p = less_from_left[p]
            less_from_left[i] = p

        less_from_right = [None] * total_num
        less_from_right[total_num - 1] = total_num
        for i in range(total_num - 2, -1, -1):
            p = i + 1
            while p < total_num and heights[p] >= heights[i]:
                p = less_from_right[p]
            less_from_right[i] = p

        area = 0
        for i in range(total_num):
            area = max(area, heights[i] * (
                less_from_right[i] - less_from_left[i] - 1))
        return area

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        prev_row = list(map(int, matrix[0]))
        area = self.largestRecInHist(prev_row)
        for row in matrix[1:]:
            row = list(map(int, row))
            for i in range(len(row)):
                if row[i] > 0:
                    row[i] += prev_row[i]
            area = max(area, self.largestRecInHist(row))
            prev_row = row
        return area
# @lc code=end
