#
# @lc app=leetcode id=37 lang=python3
#
# [37] Sudoku Solver
#
class Solution:
    def isValid(self, i: int, j: int, n: int) -> bool:
        if self.rows[i][n - 1]:
            return False
        if self.cols[j][n - 1]:
            return False
        if self.boxs[i // 3][j // 3][n - 1]:
            return False
        return True

    def _mark(self, i: int, j: int, n: int, present: bool) -> None:
        self.rows[i][n - 1] = present
        self.cols[j][n - 1] = present
        self.boxs[i // 3][j // 3][n - 1] = present

    def reset(self, i: int, j: int) -> None:
        self._mark(i, j, int(self.board[i][j]), False)
        self.board[i][j] = '.'

    def update(self, i: int, j: int, n: int) -> None:
        self._mark(i, j, n, True)
        self.board[i][j] = str(n)

    def findMissing(self):
        missing = []
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == '.':
                    missing.append((i, j))
        return missing

    def propose(self, indices):
        candidates = {}
        for i, j in indices:
            ns = [n for n in range(1, 10) if self.isValid(i, j, n)]
            if ns:
                candidates[(i, j)] = ns
        return candidates

    def solve(self) -> bool:
        missing_indices = self.findMissing()
        if not missing_indices:
            return True
        candidates = self.propose(missing_indices)
        if not candidates:
            return False
        (i, j), ns = sorted(list(candidates.items()),
                            key=lambda x: len(x[1]))[0]
        for n in ns:
            self.update(i, j, n)
            solved = self.solve()
            if solved:
                return True
            self.reset(i, j)
        return False

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.rows = [[None] * 9 for _ in range(9)]
        self.cols = [[None] * 9 for _ in range(9)]
        self.boxs = [[[None] * 9 for _ in range(3)] for _ in range(3)]
        for i in range(9):
            for j in range(9):
                xij = self.board[i][j]
                if xij != '.':
                    self._mark(i, j, int(xij), True)
        if not self.solve():
            raise RuntimeError('it is not solveable')
