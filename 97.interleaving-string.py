#
# @lc app=leetcode id=97 lang=python3
#
# [97] Interleaving String
#

# @lc code=start
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        if not s1:
            return s2 == s3
        if not s2:
            return s1 == s3
        if s3[0] == s1[0]:
            if self.isInterleave(s1[1:], s2, s3[1:]):
                return True
        if s3[0] == s2[0]:
            if self.isInterleave(s1, s2[1:], s3[1:]):
                return True
        return False
# @lc code=end
