#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#
class Solution:
    def jump(self, nums: List[int]) -> int:
        min_steps = list(reversed(range(len(nums))))
        for i in reversed(range(len(nums))):
            n = nums[i]
            if i + n >= len(nums) - 1:
                min_steps[i] = min([min_steps[i], 1])
            else:
                for j in range(i + n, i, -1):
                    min_steps[i] = min([min_steps[i], min_steps[j] + 1])
                    if min_steps[i] <= 2:
                        break
        return min_steps[0]
