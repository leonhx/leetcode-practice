#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a, i, b = 0, 0, len(nums) - 1
        while i <= b:
            n_i = nums[i]
            if n_i == 1:
                i += 1
            elif n_i == 0:
                if i > a:
                    nums[a], nums[i] = n_i, nums[a]
                a += 1
                i += 1
            elif n_i == 2:
                nums[b], nums[i] = n_i, nums[b]
                b -= 1
            else:
                raise RuntimeError('should not reach here')
