#
# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
#
class Solution:
    def simplifyPath(self, path: str) -> str:
        parts = path.split('/')
        result = []
        if not parts[0]:
            parts = parts[1:]
        for p in parts:
            if p == '..':
                if result:
                    result.pop()
            elif p and p != '.':
                result.append(p)
        return '/' + '/'.join(result)
