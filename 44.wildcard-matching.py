#
# @lc app=leetcode id=44 lang=python3
#
# [44] Wildcard Matching
#
class Solution:
    def _consume_seq(self, s: str, p: str, s_i: int, p_i: int):
        while p_i < len(p) and p[p_i] != '*':
            if s_i >= len(s) or (p[p_i] != s[s_i] and p[p_i] != '?'):
                return -1, -1
            s_i, p_i = s_i + 1, p_i + 1
        if p_i == len(p) and s_i != len(s): return -1, -1
        return s_i, p_i

    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s
        s_i, p_i = 0, 0
        if p[p_i] != '*' and p[p_i] != '?':
            s_i, p_i = self._consume_seq(s, p, s_i, p_i)
            if s_i == -1: return False
        could_skip = False
        while p_i < len(p):
            if p[p_i] == '*':
                p_i, could_skip = p_i + 1, True
            elif p[p_i] == '?':
                s_i, p_i = s_i + 1, p_i + 1
            else:
                s_i_, p_i_ = self._consume_seq(s, p, s_i, p_i)
                if s_i_ == -1:
                    if could_skip and s_i < len(s) - 1: s_i += 1
                    else: return False
                else:
                    s_i, p_i, could_skip = s_i_, p_i_, False
        return (could_skip and s_i <= len(s)) or s_i == len(s)
