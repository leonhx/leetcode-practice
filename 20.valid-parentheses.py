#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#
# https://leetcode.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (35.94%)
# Total Accepted:    525.2K
# Total Submissions: 1.5M
# Testcase Example:  '"()"'
#
# Given a string containing just the characters '(', ')', '{', '}', '[' and
# ']', determine if the input string is valid.
#
# An input string is valid if:
#
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
#
#
# Note that an empty string is also considered valid.
#
# Example 1:
#
#
# Input: "()"
# Output: true
#
#
# Example 2:
#
#
# Input: "()[]{}"
# Output: true
#
#
# Example 3:
#
#
# Input: "(]"
# Output: false
#
#
# Example 4:
#
#
# Input: "([)]"
# Output: false
#
#
# Example 5:
#
#
# Input: "{[]}"
# Output: true
#
#
#
class Solution:
    def isValid(self, s: str) -> bool:
        expecting: List[str] = []
        parens: Dict[str, str] = {'(': ')', '{': '}', '[': ']'}
        for i in range(len(s)):
            c = s[i]
            if c in parens:
                expecting.append(parens[c])
            elif len(expecting) > 0 and c == expecting[-1]:
                expecting.pop()
            else:
                expecting.append('error')
                break
        return len(expecting) == 0

