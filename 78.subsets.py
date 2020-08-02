#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [nums]
        else:
            leading_subsets = self.subsets(nums[:-1])
            return leading_subsets + [
                subset[:] + [nums[-1]] for subset in leading_subsets]
# @lc code=end
