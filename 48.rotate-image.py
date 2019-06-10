#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#
class Solution:
    def ord2coord(self, width: int, m: int, k: int):
        base_i, base_j = m, m
        edge_no = k // (width - 1)
        i_on_edge = k % (width - 1)
        if edge_no == 0:
            return (base_i, base_j + i_on_edge)
        elif edge_no == 1:
            return (base_i + i_on_edge, base_j + width - 1)
        elif edge_no == 2:
            return (base_i + width - 1, base_j + width - 1 - i_on_edge)
        elif edge_no == 3:
            return (base_i + width - 1 - i_on_edge, base_j)
        else:
            raise ValueError('impossible')

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for m in range(n // 2):
            width = n - 2 * m
            w1 = width - 1
            for k in range(w1):
                org_i, org_j = self.ord2coord(width, m, k)
                prev_x = matrix[org_i][org_j]
                for nxt_k in [k + w1, k + w1 * 2, k + w1 * 3]:
                    i, j = self.ord2coord(width, m, nxt_k)
                    tmp = matrix[i][j]
                    matrix[i][j] = prev_x
                    prev_x = tmp
                matrix[org_i][org_j] = prev_x
