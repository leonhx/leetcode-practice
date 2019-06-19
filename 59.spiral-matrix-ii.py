#
# @lc app=leetcode id=59 lang=python3
#
# [59] Spiral Matrix II
#
class Solution:
    def fillMatrix(self, matrix: List[List[int]], n: int, i: int, x: int) -> int:
        w = n - i * 2
        if w < 1:
            return
        for j in range(i, i + w):
            matrix[i][j] = x
            x += 1
        for j in range(i + 1, i + w):
            matrix[j][i + w - 1] = x
            x += 1
        for j in reversed(range(i, i + w - 1)):
            matrix[i + w - 1][j] = x
            x += 1
        for j in reversed(range(i + 1, i + w - 1)):
            matrix[j][i] = x
            x += 1
        return x

    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        x = 1
        for i in range((n + 1) // 2):
            x = self.fillMatrix(matrix, n, i, x)
        return matrix
