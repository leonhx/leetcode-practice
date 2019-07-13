#
# @lc app=leetcode id=68 lang=python3
#
# [68] Text Justification
#
class Solution:
    def split(self, words: List[str], maxWidth: int) -> List[List[str]]:
        if not words:
            return []
        lines, cur_len = [[words[0]]], len(words[0])
        for w in words[1:]:
            if cur_len + 1 + len(w) <= maxWidth:
                lines[-1].append(w)
                cur_len += 1 + len(w)
            else:
                lines.append([w])
                cur_len = len(w)
        return lines

    def justify(self, words: List[str], width: int, full: bool = False) -> str:
        word_len = sum(map(len, words))
        space_len = width - word_len
        space_cnt = len(words) - 1
        if space_cnt == 0:
            return words[0] + ' ' * space_len
        if full:
            return ' '.join(words) + ' ' * (space_len - space_cnt)
        space_sizes = [0] * (space_cnt + 1)
        while space_cnt > 0:
            sz = space_len // space_cnt
            space_sizes[space_cnt - 1] = sz
            space_len -= sz
            space_cnt -= 1
        return ''.join(w + ' ' * sz for w, sz in zip(words, space_sizes))

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines = self.split(words, maxWidth)
        lines[-1] = self.justify(lines[-1], maxWidth, full=True)
        for i in range(len(lines) - 1):
            lines[i] = self.justify(lines[i], maxWidth)
        return lines
