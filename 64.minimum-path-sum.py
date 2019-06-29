#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#
class Solution:
    def propagation(self, grid: List[List[int]], n: int) -> None:
        if n == 0:
            return
        for i in range(len(grid)):
            j = n - i
            row = grid[i]
            if 0 <= j < len(row):
                candidates = []
                if i > 0:
                    candidates.append(grid[i - 1][j])
                if j > 0:
                    candidates.append(grid[i][j - 1])
                row[j] += min(candidates)

    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        for i in range(m + n - 1):
            self.propagation(grid, i)
        return grid[m - 1][n - 1]
