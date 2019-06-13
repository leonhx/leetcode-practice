#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        if m > 0:
            n = len(matrix[0])
        else:
            return []
        result = []
        low_i, up_i, low_j, up_j = 0, m, 0, n
        while low_i < up_i and low_j < up_j:
            if low_i < up_i:
                result += matrix[low_i][low_j:up_j]
                low_i += 1
            if low_j < up_j:
                for i in range(low_i, up_i):
                    result.append(matrix[i][up_j - 1])
                up_j -= 1
            if low_i < up_i:
                result += reversed(matrix[up_i - 1][low_j:up_j])
                up_i -= 1
            if low_j < up_j:
                for i in range(up_i, low_i, -1):
                    result.append(matrix[i - 1][low_j])
                low_j += 1
        return result
