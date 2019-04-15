#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
# https://leetcode.com/problems/3sum/description/
#
# algorithms
# Medium (23.48%)
# Total Accepted:    491.4K
# Total Submissions: 2.1M
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# Given an array nums of n integers, are there elements a, b, c in nums such
# that a + b + c = 0? Find all unique triplets in the array which gives the sum
# of zero.
#
# Note:
#
# The solution set must not contain duplicate triplets.
#
# Example:
#
#
# Given array nums = [-1, 0, 1, 2, -1, -4],
#
# A solution set is:
# [
# ⁠ [-1, 0, 1],
# ⁠ [-1, -1, 2]
# ]
#
#
#
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sols: Set[int] = set()
        for i in range(len(nums)):
            n_i = nums[i]
            j: int = 0
            k: int = len(nums) - 1
            while j < k:
                if j == i:
                    j += 1
                elif k == i:
                    k -= 1
                else:
                    n_j = nums[j]
                    n_k = nums[k]
                    s = n_i + n_j + n_k
                    if s == 0:
                        if n_i < n_j:
                            sols.add((n_i, n_j, n_k))
                        elif n_i < n_k:
                            sols.add((n_j, n_i, n_k))
                        else:
                            sols.add((n_j, n_k, n_i))
                        j += 1
                        k -= 1
                    elif s < 0:
                        j += 1
                    else:
                        k -= 1
        return list(list(sol) for sol in sols)

