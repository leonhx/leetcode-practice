#
# @lc app=leetcode id=32 lang=python3
#
# [32] Longest Valid Parentheses
#
class Solution:
    def __init__(self, debug=False):
        self.debug = debug

    def _check(self, s: str):
        ln, rn = 0, 0
        for c in s:
            if c == '(':
                ln += 1
            else:
                rn += 1
            if ln < rn:
                return False
        return ln == rn

    def check(self, s: str):
        is_valid = self._check(s)
        if self.debug:
            print(s, is_valid)
        return is_valid

    def naiveSolution(self, s: str) -> int:
        longest = 0
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                if self.check(s[i:j + 1]):
                    if j + 1 - i > longest:
                        longest = j + 1 - i
        return longest

    def longestValidParentheses(self, s: str) -> int:
        valid_ranges = []
        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i - 1] == '(':
                    valid_ranges.append((i - 1, i))
                elif valid_ranges:
                    last_i, last_j = valid_ranges[-1]
                    if last_i > 0 and s[last_i - 1] == '(':
                        valid_ranges[-1] = (last_i - 1, i)
                if len(valid_ranges) > 1:
                    l2_i, l2_j = valid_ranges[-2]
                    l1_i, l1_j = valid_ranges[-1]
                    if l2_j + 1 == l1_i:
                        valid_ranges.pop()
                        valid_ranges[-1] = (l2_i, l1_j)
            if self.debug:
                print(i, valid_ranges)
        if not valid_ranges:
            return 0
        return max([j - i + 1 for i, j in valid_ranges])
