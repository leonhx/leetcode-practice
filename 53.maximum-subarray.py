#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#
# https://leetcode.com/problems/maximum-subarray/description/
#
# algorithms
# Easy (42.85%)
# Total Accepted:    502.3K
# Total Submissions: 1.2M
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
# Given an integer array nums, find the contiguous subarray (containing at
# least one number) which has the largest sum and return its sum.
#
# Example:
#
#
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
#
#
# Follow up:
#
# If you have figured out the O(n) solution, try coding another solution using
# the divide and conquer approach, which is more subtle.
#
#
class Solution:
    def _divideAndConquer(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        mid = len(nums) // 2
        left_max = left_sum = 0
        for i in range(mid - 1, -1, -1):
            left_sum += nums[i]
            left_max = max([left_max, left_sum])
        right_max = right_sum = 0
        for j in range(mid + 1, len(nums)):
            right_sum += nums[j]
            right_max = max([right_max, right_sum])
        mid_max = left_max + right_max + nums[mid]
        results = [mid_max]
        left, right = nums[:mid], nums[mid + 1:]
        if len(left) > 0:
            results.append(self._divideAndConquer(left))
        if len(right) > 0:
            results.append(self._divideAndConquer(right))
        return max(results)

    def _ohN(self, nums: List[int]) -> int:
        max_sum, cur_sum = nums[0], nums[0]
        for i in range(1, len(nums)):
            if cur_sum < 0 and nums[i] > cur_sum:
                cur_sum = nums[i]
            else:
                cur_sum += nums[i]
            max_sum = max_sum if max_sum > cur_sum else cur_sum
        return max_sum

    def maxSubArray(self, nums: List[int]) -> int:
        return self._divideAndConquer(nums)
