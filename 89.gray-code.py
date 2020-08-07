#
# @lc app=leetcode id=89 lang=python3
#
# [89] Gray Code
#

# @lc code=start
class Solution:
    def grayCode(self, n: int) -> List[int]:
        loop = [0, 1, 3, 2, 2, 3, 1, 0]
        result = []
        for i in range(2 ** n):
            d = 0
            for j in range((n + 1) // 2):
                x = loop[(i // (4 ** j)) % 8]
                d += x * (4 ** j)
            result.append(d)
        return result
# @lc code=end
