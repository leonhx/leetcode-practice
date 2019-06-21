#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        n_moves = (m - 1) + (n - 1)
        n_combs, n_perms = 1, 1
        for i in range(min([m - 1, n - 1])):
            n_combs *= n_moves - i
            n_perms *= i + 1
        return n_combs // n_perms
