#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
class Solution:
    def build_index(self, board: List[List[str]]):
        index = {}
        for i, row in enumerate(board):
            for j, c in enumerate(row):
                index.setdefault(c, []).append((i, j))
        return index

    def adjacent(self, a: int, b: int, m: int, n: int) -> bool:
        return (a == m and abs(b - n) == 1) or (abs(a - m) == 1 and b == n)

    def exist_near(self, m: int, n: int, index, word: str) -> bool:
        if not word:
            return True
        c = word[0]
        positions = index.get(c)
        if positions:
            for i, pos in enumerate(positions):
                if not pos:
                    continue
                if self.adjacent(m, n, pos[0], pos[1]):
                    positions[i] = None
                    match = self.exist_near(pos[0], pos[1], index, word[1:])
                    if match:
                        return True
                    positions[i] = pos
        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        index = self.build_index(board)
        positions = index.get(word[0])
        if positions:
            for i, pos in enumerate(positions):
                positions[i] = None
                match = self.exist_near(pos[0], pos[1], index, word[1:])
                if match:
                    return True
                positions[i] = pos
        return False
# @lc code=end
