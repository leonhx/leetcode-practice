#
# @lc app=leetcode id=97 lang=python3
#
# [97] Interleaving String
#

# @lc code=start
class Solution:
    def __init__(self):
        super().__init__()
        self._cache = {}

    def ret(self, s1: str, s2: str, s3: str, res: bool) -> bool:
        self._cache.setdefault(s3, {})[(s1, s2)] = res
        self._cache.setdefault(s3, {})[(s2, s1)] = res
        return res

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if s3 in self._cache:
            if (s1, s2) in self._cache[s3]:
                return self._cache[s3][(s1, s2)]
            if (s2, s1) in self._cache[s3]:
                return self._cache[s3][(s2, s1)]
        if len(s1) + len(s2) != len(s3):
            return False
        if not s1:
            return s2 == s3
        if not s2:
            return s1 == s3
        if s3[0] == s1[0]:
            if self.isInterleave(s1[1:], s2, s3[1:]):
                return self.ret(s1, s2, s3, True)
        if s3[0] == s2[0]:
            if self.isInterleave(s1, s2[1:], s3[1:]):
                return self.ret(s1, s2, s3, True)
        return self.ret(s1, s2, s3, False)
# @lc code=end
