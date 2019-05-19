#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#
class Solution:
    def __init__(self, debug=False):
        super().__init__()
        self.debug = debug
        self.mapping = [
            (), (), tuple('abc'), tuple('def'),
            tuple('ghi'), tuple('jkl'), tuple('mno'),
            tuple('pqrs'), tuple('tuv'), tuple('wxyz')
        ]

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        cs = [self.mapping[int(d)] for d in digits]
        result = cs[-1]
        for digit_chars in cs[-2::-1]:
            new_result = []
            for c in digit_chars:
                for s in result:
                    new_result.append(c + s)
            result = new_result
        return result
