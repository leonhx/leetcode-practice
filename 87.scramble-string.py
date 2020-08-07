#
# @lc app=leetcode id=87 lang=python3
#
# [87] Scramble String
#

# @lc code=start
from collections import Counter


class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if not s1:
            return not s2
        if len(s1) != len(s2):
            return False
        if s1 == s2:
            return True
        s1_counter = Counter(s1)
        s2_counter = Counter(s2)
        if s1_counter != s2_counter:
            return False
        s1_left_c = Counter()
        s2_left_c = Counter()
        s2_right_c = Counter()
        for i in range(1, len(s1)):
            s1_left_c.update(s1[i - 1])
            s2_left_c.update(s2[i - 1])
            s2_right_c.update(s2[len(s2) - i])
            if s1_left_c == s2_left_c and \
                    (s1_counter - s1_left_c) == (s2_counter - s2_left_c):
                if self.isScramble(s1[:i], s2[:i]) and \
                        self.isScramble(s1[i:], s2[i:]):
                    return True
            elif s1_left_c == s2_right_c and \
                    (s1_counter - s1_left_c) == (s2_counter - s2_right_c):
                if self.isScramble(s1[:i], s2[-i:]) and \
                        self.isScramble(s1[i:], s2[:-i]):
                    return True
        return False
# @lc code=end
