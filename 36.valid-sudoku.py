#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#
class Solution:
    def __init__(self, debug=False):
        self.debug = debug

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[None] * 9 for _ in range(9)]
        cols = [[None] * 9 for _ in range(9)]
        boxs = [[[None] * 9 for _ in range(3)] for _ in range(3)]
        code_bias = ord('1')
        for i in range(9):
            for j in range(9):
                c = board[i][j]
                if c != '.':
                    n = ord(c) - code_bias
                    if rows[i][n]:
                        if self.debug:
                            print(f'row {i}: {c}; {i}, {j}')
                        return False
                    if cols[j][n]:
                        if self.debug:
                            print(f'col {j}: {c}; {i}, {j}')
                        return False
                    if boxs[i // 3][j // 3][n]:
                        if self.debug:
                            print(f'box {i // 3} {j // 3}: {c}; {i}, {j}')
                        return False
                    rows[i][n] = True
                    cols[j][n] = True
                    boxs[i // 3][j // 3][n] = True
                    if self.debug:
                        print(f'got row {i}: {c}')
                        print(f'got col {j}: {c}')
                        print(f'got box {i // 3} {j // 3}: {c}')
        return True
