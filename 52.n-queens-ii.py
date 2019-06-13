#
# @lc app=leetcode id=52 lang=python3
#
# [52] N-Queens II
#
class Solution:
    def solve(self, queens: List[int], r: int) -> int:
        if r >= len(queens):
            return 1
        n_sols = 0
        for j in range(len(queens)):
            valid = True
            for r_ in range(r):
                j_ = queens[r_]
                if j_ == j or r_ + j_ == r + j or r_ - j_ == r - j:
                    valid = False
                    break
            if valid:
                queens[r] = j
                n_sols += self.solve(queens, r + 1)
        return n_sols

    def totalNQueens(self, n: int) -> int:
        queens = [0 for _ in range(n)]
        return self.solve(queens, 0)
