#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#
class Solution:
    def findAll(self, i: int, t: int) -> List[List[int]]:
        if i >= len(self.ns):
            return []
        n = self.ns[i]
        if n == t:
            return [[n]]
        elif n < t:
            j = i + 1
            while j < len(self.ns) and self.ns[j] == n:
                j += 1
            return self.findAll(j, t) + [
                [n] + nl for nl in self.findAll(i + 1, t - n)]
        else:
            return []

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ns = candidates
        self.ns.sort()
        return self.findAll(0, target)
