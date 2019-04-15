#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#
# https://leetcode.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (26.66%)
# Total Accepted:    488.2K
# Total Submissions: 1.8M
# Testcase Example:  '"babad"'
#
# Given a string s, find the longest palindromic substring in s. You may assume
# that the maximum length of s is 1000.
#
# Example 1:
#
#
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
#
#
# Example 2:
#
#
# Input: "cbbd"
# Output: "bb"
#
#
#
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        matrix = [[(True if i == j else None) for j in range(len(s))]
                  for i in range(len(s))]
        max_sz: int = 1
        s_i: int = 0
        s_j: int = 1
        for sz in range(2, len(s) + 1):
            for i in range(0, len(s) - sz + 1):
                is_pld = (s[i] == s[i + sz - 1]) and \
                    ((i + 1 >= i + sz - 2) or matrix[i + 1][i + sz - 2])
                matrix[i][i + sz - 1] = is_pld
                if is_pld and sz > max_sz:
                    s_i = i
                    s_j = i + sz
                    max_sz = sz
        return s[s_i:s_j]

