#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#
class Solution:
    def __init__(self, debug=False):
        super().__init__()
        self.debug = debug
        self.cache = {}

    def nextPattern(self, p: str):
        if len(p) > 1 and p[1] == '*':
            return (p[0], p[1]), p[2:]
        else:
            return (p[0], 1), p[1:]

    def matches(self, s: str, p: str) -> bool:
        if self.debug:
            print(f's: {s}, p: {p}')
        s_len, p_len = len(s), len(p)
        if s_len > 0 and p_len == 0:
            return False
        if s_len == 0:
            return p_len == 0 or (
                p_len > 1 and p[1] == '*' and self.isMatch(s, p[2:]))
        (x, n), nxt_p = self.nextPattern(p)
        if n == '*' and self.isMatch(s, nxt_p):
            return True
        if x == '.' or s[0] == x:
            if self.isMatch(s[1:], nxt_p) or (
                    n == '*' and self.isMatch(s[1:], p)):
                return True
        return False

    def isMatch(self, s: str, p: str) -> bool:
        key = (s, p)
        if key not in self.cache:
            self.cache[key] = self.matches(s, p)
        elif self.debug:
            print(f'cache hit: {key}')
        return self.cache[key]
