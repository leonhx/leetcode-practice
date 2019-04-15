#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
# https://leetcode.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (33.04%)
# Total Accepted:    415.8K
# Total Submissions: 1.3M
# Testcase Example:  '["flower","flow","flight"]'
#
# Write a function to find the longest common prefix string amongst an array of
# strings.
#
# If there is no common prefix, return an empty string "".
#
# Example 1:
#
#
# Input: ["flower","flow","flight"]
# Output: "fl"
#
#
# Example 2:
#
#
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
#
#
# Note:
#
# All given inputs are in lowercase letters a-z.
#
#
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        i: int = 0
        while all(i < len(s) for s in strs):
            c0 = strs[0][i]
            all_the_same: bool = True
            for j in range(1, len(strs)):
                if strs[j][i] != c0:
                    all_the_same = False
                    break
            if not all_the_same:
                break
            i += 1
        return strs[0][:i]

