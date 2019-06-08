#
# @lc app=leetcode id=44 lang=python3
#
# [44] Wildcard Matching
#
class Solution:
    def _parse(self, p: str) -> List[str]:
        i, ps = 0, []
        while i < len(p):
            if p[i] == '*':
                ps.append('*')
                while i < len(p) and p[i] == '*':
                    i += 1
            elif p[i] == '?':
                j = i + 1
                while j < len(p) and p[j] == '?':
                    j += 1
                ps.append(p[i:j])
                i = j
            else:
                j = i + 1
                while j < len(p) and p[j] != '*' and p[j] != '?':
                    j += 1
                ps.append(p[i:j])
                i = j
        return ps

    def _findAll(self, s: str, w: str, start: int) -> List[int]:
        i, res = start, []
        while i < len(s):
            i = s.find(w, i)
            if i == -1:
                break
            res.append(i)
            i += 1
        return res

    def _try(self, s: str, p_with_index, i_range) -> bool:
        start_i, end_i = i_range
        if not p_with_index:
            return start_i <= len(s) < end_i
        w, p_index = p_with_index[0]
        if w[0] == '*':
            return self._try(s, p_with_index[1:], (start_i, len(s) + 1))
        elif w[0] == '?':
            i_range = (start_i + len(w), end_i + len(w))
            return self._try(s, p_with_index[1:], i_range)
        else:
            for i in p_index:
                if start_i <= i < end_i:
                    nxt_i = i + len(w)
                    nxt_range = nxt_i, nxt_i + 1
                    if self._try(s, p_with_index[1:], nxt_range):
                        return True
            return False

    def _buildIndex(self, s: str, p: List[str]):
        p_index, i = [], 0
        for w in p:
            if w[0] == '*':
                p_index.append(None)
            elif w[0] == '?':
                i += len(w)
                p_index.append(None)
            else:
                indices = self._findAll(s, w, i)
                if not indices:
                    return None
                p_index.append(indices)
                i = indices[0] + len(w)
        i = len(s)
        for w, indices in reversed(list(zip(p, p_index))):
            if w[0] == '*':
                continue  # do nothing
            elif w[0] == '?':
                i -= len(w)
            else:
                while indices and indices[-1] >= i:
                    indices.pop()
                if not indices:
                    return None
                else:
                    i = indices[-1]
        return p_index

    def isMatch(self, s: str, p: str) -> bool:
        p = self._parse(p)
        p_index = self._buildIndex(s, p)
        if p_index is None:
            return False
        p_with_index = list(zip(p, p_index))
        return self._try(s, p_with_index, (0, 1))

    def _isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s
        if not s:
            return not p or all(c == '*' for c in p)
        if p[0] == '?':
            return self.isMatch(s[1:], p[1:])
        elif p[0] == '*':
            i, qmark_cnt = 0, 0
            while i < len(p) and (p[i] == '*' or p[i] == '?'):
                if p[i] == '?':
                    qmark_cnt += 1
                i += 1
            if i == len(p):
                return len(s) >= qmark_cnt
            j = i + 1
            while j < len(p) and p[j] != '*' and p[j] != '?':
                j += 1
            nxt_seq = p[i:j]
            k = 0
            while k < len(s):
                s_i = s.find(nxt_seq, k)
                if s_i == -1:
                    break
                if s_i >= qmark_cnt and self.isMatch(s[s_i + j - i:], p[j:]):
                    return True
                k = s_i + 1
            return False
        else:
            return s[0] == p[0] and self.isMatch(s[1:], p[1:])
