#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        if divisor == 1:
            return dividend
        if divisor == -1:
            return -dividend
        is_pos = (dividend > 0 and divisor > 0) or (
            dividend < 0 and divisor < 0)
        result = 0
        step = 1 if is_pos else -1
        divisor = divisor if is_pos else -divisor
        cmp_fn = (lambda de, di: de >= di) if dividend > 0 else (
            lambda de, di: de <= di)
        while cmp_fn(dividend, divisor):
            temp, i = divisor, step
            while cmp_fn(dividend, temp):
                result += i
                dividend -= temp
                i <<= 1
                temp <<= 1
        return result
