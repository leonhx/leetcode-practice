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

    def init(self) -> None:
        for i in range(9):
            for j in range(9):
                xij = self.board[i][j]
                if xij != '.':
                    self._mark(i, j, int(xij), True)

    def backtrace(self):
        i, j = self.decision_seq[self.seq_i]
        self.seq_i -= 1
        self._mark(i, j, int(self.board[i][j]), False)
        self.board[i][j] = '.'
        return i, j

    def update(self, i: int, j: int, n: int) -> None:
        if len(self.decision_seq) - 1 > self.seq_i:
            while len(self.decision_seq) - 2 > self.seq_i:
                self.attempts.pop(self.decision_seq.pop(), None)
            self.decision_seq.pop()
        self.decision_seq.append((i, j))
        self.seq_i += 1
        self.attempts.setdefault((i, j), set()).add(n)
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
            blackset = self.attempts.get((i, j), set())
            ns = [n for n in range(1, 10)
                  if self.isValid(i, j, n) and n not in blackset]
            if ns:
                candidates[(i, j)] = ns
        return candidates

    def solve(self) -> bool:
        pass

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.rows = [[None] * 9 for _ in range(9)]
        self.cols = [[None] * 9 for _ in range(9)]
        self.boxs = [[[None] * 9 for _ in range(3)] for _ in range(3)]
        self.decision_seq = []
        self.seq_i = -1
        self.attempts = {}
        self.init()
        missing_indices = self.findMissing()

        while missing_indices:
            candidates = self.propose(missing_indices)
            if candidates:
                updated = False
                for (i, j), ns in candidates.items():
                    if len(ns) == 1:
                        print(f'confident set {i} {j} to {ns[0]}')
                        self.update(i, j, ns[0])
                        updated = True
                if not updated:
                    (i, j), ns = sorted(list(candidates.items()),
                                        key=lambda x: len(x[1]))[0]
                    print(f'try set {i} {j} to {ns[0]}')
                    self.update(i, j, ns[0])
            else:  # no candidates, backtrace now
                i, j = self.backtrace()
                print(f'backtrace {i} {j}')
            missing_indices = self.findMissing()
            print('---')
