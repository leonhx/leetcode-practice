#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            n = nums[i]
            while 1 <= n < len(nums) and nums[n - 1] != n:
                nums[i], nums[n - 1] = nums[n - 1], n
                n = nums[i]
        n_ = 1
        for n in nums:
            if n == n_:
                n_ += 1
            else:
                break
        return n_
