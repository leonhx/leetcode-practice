#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#
class Solution:
    def jump(self, nums: List[int]) -> int:
        min_steps = list(range(len(nums)))
        for i, n in enumerate(nums):
            for j in range(i + 1, min([i + 1 + n, len(min_steps)])):
                min_steps[j] = min([min_steps[j], min_steps[i] + 1])
        return min_steps[-1]
