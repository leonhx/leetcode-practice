#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return nums
        combs = [[nums[0]]]
        for n in nums[1:]:
            new_combs = []
            for comb in combs:
                for i in range(len(comb) + 1):
                    new_comb = list(comb)
                    new_comb.insert(i, n)
                    new_combs.append(new_comb)
            combs = new_combs
        return combs
