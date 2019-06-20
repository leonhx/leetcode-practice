#
# @lc app=leetcode id=60 lang=python3
#
# [60] Permutation Sequence
#
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        n_combs = 1
        for i in range(2, n + 1):
            n_combs *= i
        k -= 1
        digits = list(range(1, n + 1))
        result = []
        for i in range(n):
            n_combs //= n - i
            result.append(digits.pop(k // n_combs))
            k %= n_combs
        return ''.join(map(str, result))
