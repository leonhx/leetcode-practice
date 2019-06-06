#
# @lc app=leetcode id=43 lang=python3
#
# [43] Multiply Strings
#
class Solution:
    def to_digits(self, num: str) -> List[int]:
        zero = ord('0')
        return [ord(c) - zero for c in num]

    def to_str(self, digits: List[int]) -> str:
        zero = ord('0')
        return ''.join(chr(d + zero) for d in digits)

    def shrink_inplace(self, rev_digits: List[int]):
        if rev_digits:
            while len(rev_digits) > 1 and rev_digits[-1] == 0:
                rev_digits.pop()

    def reversed_add(self, num1: List[int], num2: List[int]) -> List[int]:
        result, c, i = [], 0, 0
        if len(num1) < len(num2):
            num1, num2 = num2, num1
        while i < len(num1) and i < len(num2):
            s = num1[i] + num2[i] + c
            result.append(s % 10)
            c = s // 10
            i += 1
        while i < len(num1):
            s = num1[i] + c
            result.append(s % 10)
            c = s // 10
            i += 1
        if c > 0:
            result.append(c)
        return result

    def rev_multiply_by_digit(self, num1: List[int], d: int) -> List[int]:
        if d == 0:
            return [0]
        result, i, c = [], 0, 0
        while i < len(num1):
            p = num1[i] * d + c
            result.append(p % 10)
            c = p // 10
            i += 1
        if c > 0:
            result.append(c)
        return result

    def multiply(self, num1: str, num2: str) -> str:
        if len(num1) < len(num2):
            num1, num2 = num2, num1
        rev_num1 = self.to_digits(num1)[::-1]
        rev_num2 = self.to_digits(num2)[::-1]
        result = []
        for i, d in enumerate(rev_num2):
            rev_prod = self.rev_multiply_by_digit(rev_num1, d)
            result = self.reversed_add(result, [0] * i + rev_prod)
        return self.to_str(result[::-1])
