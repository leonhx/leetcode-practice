#
# @lc app=leetcode id=44 lang=python3
#
# [44] Wildcard Matching
#
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s
        if not s:
            return not p or all(c == '*' for c in p)
        if p[0] == '?':
            return self.isMatch(s[1:], p[1:])
        elif p[0] == '*':
            i, qmark_cnt = 0, 0
            while i < len(p) and (p[i] == '*' or p[i] == '?'):
                if p[i] == '?':
                    qmark_cnt += 1
                i += 1
            if i == len(p):
                return len(s) >= qmark_cnt
            j = i + 1
            while j < len(p) and p[j] != '*' and p[j] != '?':
                j += 1
            nxt_seq = p[i:j]
            k = 0
            while k < len(s):
                s_i = s.find(nxt_seq, k)
                if s_i == -1:
                    break
                if s_i >= qmark_cnt and self.isMatch(s[s_i + j - i:], p[j:]):
                    return True
                k = s_i + 1
            return False
        else:
            return s[0] == p[0] and self.isMatch(s[1:], p[1:])
