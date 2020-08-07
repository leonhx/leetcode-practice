#
# @lc app=leetcode id=87 lang=python3
#
# [87] Scramble String
#

# @lc code=start
class Solution:
    def find(self, x1: str, x2: str, s2: List[str]):
        for i in range(len(s2) - 1):
            if (s2[i] == x1 and s2[i + 1] == x2) or (
                    s2[i] == x2 and s2[i + 1] == x1):
                yield i

    def search(self, s1: List[str], s2: List[str]) -> bool:
        if len(s1) == len(s2) == 1:
            return s1[0] == s2[0]
        for i in range(len(s1) - 1):
            for j in self.find(s1[i], s1[i + 1], s2):
                hit = s1[i] + s1[i + 1]
                return self.search(s1[:i] + [hit] + s1[i + 2:],
                                   s2[:j] + [hit] + s2[j + 2:])
        return False

    def isScramble(self, s1: str, s2: str) -> bool:
        if not s1:
            return not s2
        if len(s1) != len(s2):
            return False
        return self.search(list(s1), list(s2))
# @lc code=end
