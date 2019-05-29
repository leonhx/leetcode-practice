#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        last_layer = [1]
        for n in range(1, rowIndex + 1):
            cur_layer = []
            for i in range(n + 1):
                if i == 0 or i == n:
                    cur_layer.append(1)
                else:
                    cur_layer.append(last_layer[i - 1] + last_layer[i])
            last_layer = cur_layer
        return last_layer
