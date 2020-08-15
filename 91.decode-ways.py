#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        nums = [0] * (len(s) + 1)  # nums[i]: num of decode ways of s[i:]
        nums[-1] = 1  # if last two digits can be decode
        nums[-2] = 0 if s[-1] == '0' else 1
        zero = ord('0')
        digits = [ord(c) - zero for c in s]
        for i in range(len(s) - 2, -1, -1):
            if 1 <= digits[i] <= 26:
                if 1 <= digits[i] * 10 + digits[i + 1] <= 26:
                    nums[i] = nums[i + 2] + nums[i + 1]
                else:
                    nums[i] = nums[i + 1]
            else:
                nums[i] = 0
        return nums[0]
# @lc code=end
