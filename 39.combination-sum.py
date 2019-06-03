#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#
class Solution:
    def findAll(self, i: int, t: int) -> List[List[int]]:
        if i >= len(self.ns):
            return []
        n = self.ns[i]
        if n == t:
            return [[t]]
        elif n < t:
            return self.findAll(i + 1, t) + [
                [n] + nl for nl in self.findAll(i, t - n)]
        else:
            return []

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ns = candidates
        self.ns.sort()
        return self.findAll(0, target)
