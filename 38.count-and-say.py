#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#
# https://leetcode.com/problems/count-and-say/description/
#
# algorithms
# Easy (39.60%)
# Total Accepted:    272.3K
# Total Submissions: 679.8K
# Testcase Example:  '1'
#
# The count-and-say sequence is the sequence of integers with the first five
# terms as following:
#
#
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
#
#
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
#
# Given an integer n where 1 ≤ n ≤ 30, generate the n^th term of the
# count-and-say sequence.
#
# Note: Each term of the sequence of integers will be represented as a
# string.
#
#
#
# Example 1:
#
#
# Input: 1
# Output: "1"
#
#
# Example 2:
#
#
# Input: 4
# Output: "1211"
#
#
class Solution:
    def __init__(self):
        self.cache = ["1"] + [None] * 30

    def countAndSay(self, n: int) -> str:
        if self.cache[n - 1] is None:
            b = self.countAndSay(n - 1)
            s = ""
            last_chr, count = b[0], 1
            for c in b[1:]:
                if c == last_chr:
                    count += 1
                else:
                    s += str(count) + last_chr
                    last_chr, count = c, 1
            s += str(count) + last_chr
            self.cache[n - 1] = s
        return self.cache[n - 1]
