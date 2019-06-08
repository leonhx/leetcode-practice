#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#
class Solution:
    def jump(self, nums: List[int]) -> int:
        farthest_i, start, steps = 0, 0, 0
        while farthest_i < len(nums) - 1:
            steps += 1
            j = farthest_i + 1
            for i in range(start, farthest_i + 1):
                j = max([i + nums[i], j])
            start, farthest_i = farthest_i + 1, j
        return steps
