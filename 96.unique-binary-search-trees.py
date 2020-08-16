#
# @lc app=leetcode id=96 lang=python3
#
# [96] Unique Binary Search Trees
#

# @lc code=start
class Solution:
    def __init__(self):
        super().__init__()
        self._cache = [None] * 20
        self._cache[0] = 1
        self._cache[1] = 1

    def numTrees(self, n: int) -> int:
        if self._cache[n] is None:
            self._cache[n] = sum([
                self.numTrees(left_n) * self.numTrees(n - 1 - left_n)
                for left_n in range(n)])
        return self._cache[n]
# @lc code=end
