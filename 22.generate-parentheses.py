#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#
class Solution:
    def parse(self, acc: str):
        nl, nr = 0, 0
        for c in acc:
            if c == '(':
                nl += 1
            else:
                nr += 1
        return nl, nr

    def gen(self, n: int, acc: str) -> List[str]:
        nl, nr = self.parse(acc)
        if nr > nl:
            raise RuntimeError('should not reach here')
        if nl == n:
            acc += ')' * (n - nr)
            return [acc]
        if nl == nr:
            return self.gen(n, acc + '(')
        return self.gen(n, acc + '(') + self.gen(n, acc + ')')

    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []
        return self.gen(n, '')
