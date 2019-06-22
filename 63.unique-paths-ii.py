#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#
class Solution:
    def getNumPaths(self, obstacleGrid: List[List[int]], i: int, j: int) -> int:
        if obstacleGrid[i][j] is None:
            n = 0
            if i > 0:
                n += self.getNumPaths(obstacleGrid, i - 1, j)
            if j > 0:
                n += self.getNumPaths(obstacleGrid, i, j - 1)
            obstacleGrid[i][j] = n
        return obstacleGrid[i][j]

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        for i in range(m):
            row = obstacleGrid[i]
            for j in range(n):
                row[j] = 0 if row[j] else None
        if obstacleGrid[0][0] is None:
            obstacleGrid[0][0] = 1
        return self.getNumPaths(obstacleGrid, m - 1, n - 1)
