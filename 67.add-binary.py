#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b = a[::-1], b[::-1]
        bias: int = ord('0')
        carry: int = 0
        i: int = 0
        reversed_result: str = ''
        while i < len(a) or i < len(b):
            a_i = ord(a[i]) - bias if i < len(a) else 0
            b_i = ord(b[i]) - bias if i < len(b) else 0
            sum_i = a_i + b_i + carry
            reversed_result += chr(bias + sum_i % 2)
            carry = sum_i // 2
            i += 1
        if carry > 0:
            reversed_result += chr(bias + carry % 2)
        return reversed_result[::-1]
