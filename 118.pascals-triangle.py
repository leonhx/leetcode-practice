#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        result = [[1]]
        for n in range(2, numRows + 1):
            last_layer, new_layer = result[-1], []
            for i in range(n):
                if i == 0 or i == n - 1:
                    new_layer.append(1)
                else:
                    new_layer.append(last_layer[i - 1] + last_layer[i])
            result.append(new_layer)
        return result
