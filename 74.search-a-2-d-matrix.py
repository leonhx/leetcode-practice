#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#
class Solution:
    def convertIndex(self, idx: int):
        return (idx // self.n_col, idx % self.n_col)

    def binarySearchMatrix(self, low_i: int, high_i: int) -> bool:
        if low_i >= high_i:
            return False
        mid_i = (low_i + high_i) // 2
        mid_a, mid_b = self.convertIndex(mid_i)
        mid = self.M[mid_a][mid_b]
        if mid == self.t:
            return True
        elif mid < self.t:
            return self.binarySearchMatrix(mid_i + 1, high_i)
        else:
            return self.binarySearchMatrix(low_i, mid_i)

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        self.M, self.t = matrix, target
        self.n_row, self.n_col = len(self.M), len(self.M[0])
        total_len = self.n_row * self.n_col
        return self.binarySearchMatrix(0, total_len)
