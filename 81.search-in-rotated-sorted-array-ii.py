#
# @lc app=leetcode id=81 lang=python3
#
# [81] Search in Rotated Sorted Array II
#

# @lc code=start
class Solution:
    def bin_search(self, t: int, nums: List[int], m: int, n: int) -> bool:
        if m >= n:
            return False
        mid_i = (m + n) // 2
        if nums[mid_i] == t:
            return True
        elif nums[mid_i] < t:
            return self.bin_search(t, nums, mid_i + 1, n)
        else:
            return self.bin_search(t, nums, m, mid_i)

    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False
        rotate_i = len(nums)
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                rotate_i = i
                break
        if nums[0] == target:
            return True
        elif nums[0] < target:
            return self.bin_search(target, nums, 1, rotate_i)
        else:
            return self.bin_search(target, nums, rotate_i, len(nums))
# @lc code=end
