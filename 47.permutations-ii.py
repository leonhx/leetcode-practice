#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        nums.sort()
        combs = [[nums[0]]]
        for n in nums[1:]:
            new_combs = []
            for comb in combs:
                for i in range(len(comb) + 1):
                    if i < len(comb) and comb[i] == n:
                        continue
                    new_comb = list(comb)
                    new_comb.insert(i, n)
                    new_combs.append(new_comb)
            combs = new_combs
        return combs
