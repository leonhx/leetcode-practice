#
# @lc app=leetcode id=72 lang=python3
#
# [72] Edit Distance
#
class Solution:
    def _minDist(self, word1: str, word2: str) -> int:
        i = 0
        while i < len(word1) and i < len(word2) and word1[i] == word2[i]:
            i += 1
        word1, word2, d = word1[i:], word2[i:], 0
        if not word1:
            d = len(word2)
        elif not word2:
            d = len(word1)
        else:
            if (word1, word2) in self.cache:
                d = self.cache[(word1, word2)]
            else:
                d = min(
                    1 + self._minDist(word1, word2[1:]),  # insert
                    1 + self._minDist(word1[1:], word2),  # delete
                    1 + self._minDist(word1[1:], word2[1:])  # replace
                )
                self.cache[(word1, word2)] = d
        return d

    def minDistance(self, word1: str, word2: str) -> int:
        self.cache = {}
        return self._minDist(word1, word2)
