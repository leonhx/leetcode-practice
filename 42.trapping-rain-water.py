#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#
class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        max_h = 0
        for h in height:
            if h <= max_h:
                result += max_h - h
            else:
                max_h = h
        max_rh = 0
        for h in height[::-1]:
            max_rh = max([max_rh, h])
            if h < max_h:
                result -= max_h - max_rh
            else:
                break
        return result
