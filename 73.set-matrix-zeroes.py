#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
        n_row, n_col = len(matrix), len(matrix[0])
        rows, cols = [False] * n_row, [False] * n_col
        for i in range(n_row):
            row = matrix[i]
            for j in range(n_col):
                if row[j] == 0:
                    rows[i] = True
                    cols[j] = True
        for i, ch_row in enumerate(rows):
            if ch_row:
                matrix[i] = [0] * n_col
        for j, ch_col in enumerate(cols):
            if ch_col:
                for i in range(n_row):
                    matrix[i][j] = 0
