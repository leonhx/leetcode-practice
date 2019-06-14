#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        traps = []
        for i in range(len(nums) - 2, -1, -1):
            n = nums[i]
            if n == 0:
                traps.append(i)
            else:
                while traps and traps[-1] < i + n:
                    traps.pop()
        return not traps
