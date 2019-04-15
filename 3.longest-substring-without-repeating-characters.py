#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (27.98%)
# Total Accepted:    821.9K
# Total Submissions: 2.9M
# Testcase Example:  '"abcabcbb"'
#
# Given a string, find the length of the longest substring without repeating
# characters.
#
#
# Example 1:
#
#
# Input: "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
#
#
#
# Example 2:
#
#
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
#
#
#
# Example 3:
#
#
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# ⁠            Note that the answer must be a substring, "pwke" is a
# subsequence and not a substring.
#
#
#
#
#
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result: int = 0
        i: int = 0
        s_len: int = len(s)
        while i < s_len:
            chars = {}
            j: int = i
            while j < s_len:
                c = s[j]
                if c not in chars:
                    chars[c] = j
                    j += 1
                else:
                    break
            result = max(result, j - i)
            i = chars[c] + 1
        return result


