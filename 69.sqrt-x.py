#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#
class Solution:
    def _sqrt(self, x: int, i: int, j: int) -> int:
        i_sq = i * i
        if i_sq > x:
            return i - 1
        if i_sq == x:
            return i
        if i == j:
            return i
        mid = (i + j) // 2
        mid_sq = mid * mid
        if mid_sq == x:
            return mid
        elif mid_sq < x:
            return self._sqrt(x, mid + 1, j)
        else:
            return self._sqrt(x, i, mid - 1)

    def mySqrt(self, x: int) -> int:
        return self._sqrt(x, 0, x // 2 + 1)
