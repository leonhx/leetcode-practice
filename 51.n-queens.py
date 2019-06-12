#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#
class Solution:
    def fast_check(self, board: List[List[str]], i: int, j: int) -> bool:
        N = len(board)
        for m in range(i):
            row = board[m]
            if row[j] == 'Q':
                return False
            delta = i - m
            if j - delta >= 0 and row[j - delta] == 'Q':
                return False
            if j + delta < N and row[j + delta] == 'Q':
                return False
        return True

    def format(self, board: List[List[str]]) -> List[str]:
        return [''.join(row) for row in board]

    def reset_row(self, board: List[List[str]], i: int) -> None:
        for j in range(len(board[i])):
            if board[i][j] == 'Q':
                board[i][j] = '.'

    def solve(self, board: List[List[str]], i: int) -> List[List[str]]:
        N = len(board)
        if i == N:
            return [self.format(board)]
        sols = []
        for j in range(N):
            if self.fast_check(board, i, j):
                self.reset_row(board, i)
                board[i][j] = 'Q'
                sols += self.solve(board, i + 1)
        return sols

    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.' for _ in range(n)] for _ in range(n)]
        return self.solve(board, 0)
