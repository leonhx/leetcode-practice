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

    def _to_groups(self, p: List[str]):
        if not p:
            return []
        groups = []
        if p[0][0] != '*':
            groups.append([None, p[0]])
        else:
            groups.append([])
        for w in p[1:]:
            if w[0] == '*' and groups[-1]:
                groups.append([])
            else:
                groups[-1].append(w)
        if groups[-1]:
            groups[-1].append(None)
        else:
            groups.pop()
        return groups

    def _len(self, group: List[str]):
        return sum(len(w) for w in group if w)

    def _check(self, s: str, group: List[str], start: int) -> int:
        is_valid = True
        for w in group:
            if w is None:
                return start == len(s)
            elif w[0] == '?':
                is_valid = start + len(w) <= len(s)
            else:
                is_valid = s[start:].startswith(w)
            if not is_valid:
                break
            start += len(w)
        return is_valid

    def _find(self, s: str, group: List[str], start: int) -> int:
        if group[0] is None:
            if start != 0:
                return False
            return 0 if self._check(s, group[1:], 0) else -1
        bias = 0
        if group[0][0] == '?':
            bias += len(group[0])
            group = group[1:]
        start += bias
        while start <= len(s) - self._len(group):
            if group and group[0]:
                i = s.find(group[0], start)
                if i == -1:
                    return -1
                j = i + len(group[0])
            else:
                j = i = start
            if self._check(s, group[1:], j):
                return i - bias
            start = i + 1
        return -1

    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s
        p_index = self._parse(p)
        groups = self._to_groups(p_index)
        i = 0
        for group in groups:
            i = self._find(s, group, i)
            if i == -1:
                return False
            i += self._len(group)
            if i > len(s):
                return False
        return True
