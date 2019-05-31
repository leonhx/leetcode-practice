#
# @lc app=leetcode id=30 lang=python3
#
# [30] Substring with Concatenation of All Words
#
class Solution:
    def __init__(self, debug=False):
        self.debug = debug

    def find_all(self, s: str, word: str) -> List[int]:
        indices = []
        start = 0
        while True:
            try:
                i = s.index(word, start)
            except ValueError:
                return indices
            indices.append(i)
            start = i + 1
        return indices

    def count(self, words):
        word_counts = {}
        for word in words:
            word_counts.setdefault(word, 0)
            word_counts[word] += 1
        return word_counts

    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words:
            return []
        word_len = len(words[0])
        if word_len * len(words) > len(s):
            return []
        word_counts = self.count(words)
        result = []
        n = len(s) // word_len
        for i in range(word_len):
            words_i = [s[i + j * word_len:i + (j + 1) * word_len]
                       for j in range(n)]
            if self.debug:
                print(i, words_i)
            for j in range(n):
                sub_words_counts = self.count(words_i[j:j + len(words)])
                match = True
                for w, c in word_counts.items():
                    if sub_words_counts.get(w, 0) != c:
                        match = False
                        break
                if match:
                    result.append(j * word_len + i)
        return result
