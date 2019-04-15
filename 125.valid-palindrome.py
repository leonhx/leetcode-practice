#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#
# https://leetcode.com/problems/valid-palindrome/description/
#
# algorithms
# Easy (30.28%)
# Total Accepted:    324.8K
# Total Submissions: 1.1M
# Testcase Example:  '"A man, a plan, a canal: Panama"'
#
# Given a string, determine if it is a palindrome, considering only
# alphanumeric characters and ignoring cases.
#
# Note: For the purpose of this problem, we define empty string as valid
# palindrome.
#
# Example 1:
#
#
# Input: "A man, a plan, a canal: Panama"
# Output: true
#
#
# Example 2:
#
#
# Input: "race a car"
# Output: false
#
#
#
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i: int = 0
        j: int = len(s) - 1
        while i < j:
            a = s[i]
            if not a.isalnum():
                i += 1
                continue
            b = s[j]
            if not b.isalnum():
                j -= 1
                continue
            if a.lower() != b.lower():
                return False
            i += 1
            j -= 1
        return True

