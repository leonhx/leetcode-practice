#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []
        result = {'()'}
        for i in range(1, n):
            new_result = set()
            for x in result:
                new_result.add(x + '()')
                new_result.add('()' + x)
                new_result.add('(' + x + ')')
            result = new_result
        return list(result)
