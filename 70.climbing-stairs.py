#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#
class Solution:
    def __init__(self):
        self.cache = [1, 1]

    def climbStairs(self, n: int) -> int:
        if n >= len(self.cache) or self.cache[n] is None:
            result = self.climbStairs(n - 1) + self.climbStairs(n - 2)
            self.cache.extend([None] * (n - len(self.cache)))
            self.cache.append(result)
        return self.cache[n]
