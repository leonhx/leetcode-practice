#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n == 1:
            return x
        elif n == -1:
            return 1 / x
        elif n % 2 == 0:
            half_pow = self.myPow(x, n // 2)
            return half_pow * half_pow
        else:
            return x * self.myPow(x, n - 1)
