#
# @lc app=leetcode id=6 lang=python3
#
# [6] ZigZag Conversion
#
# https://leetcode.com/problems/zigzag-conversion/description/
#
# algorithms
# Medium (30.76%)
# Total Accepted:    290.4K
# Total Submissions: 943.9K
# Testcase Example:  '"PAYPALISHIRING"\n3'
#
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number
# of rows like this: (you may want to display this pattern in a fixed font for
# better legibility)
#
#
# P   A   H   N
# A P L S I I G
# Y   I   R
#
#
# And then read line by line: "PAHNAPLSIIGYIR"
#
# Write the code that will take a string and make this conversion given a
# number of rows:
#
#
# string convert(string s, int numRows);
#
# Example 1:
#
#
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
#
#
# Example 2:
#
#
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
#
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
#
#
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        lines = ['' for _ in range(numRows)]
        cycle_len: int = numRows * 2 - 2
        for i in range(len(s)):
            m = i % cycle_len
            if m < numRows:
                lines[m] += s[i]
            else:
                li = 2 * numRows - 2 - m
                for j in range(numRows):
                    if j == li:
                        lines[j] += s[i]
        return ''.join(lines)

