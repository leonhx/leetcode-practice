#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, last, rep = 0, None, 0
        for j in range(len(nums)):
            if nums[j] == last:
                rep += 1
            else:
                rep = 1
                last = nums[j]
            if j != i:
                nums[i] = nums[j]
            if rep <= 2:
                i += 1
        return i
# @lc code=end
