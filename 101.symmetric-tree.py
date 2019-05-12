#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def _recursiveSolution(self, left: TreeNode, right: TreeNode) -> bool:
        if left is None:
            return right is None
        elif right is None:
            return False
        else:
            return left.val == right.val \
                and self._recursiveSolution(left.left, right.right) \
                and self._recursiveSolution(left.right, right.left)

    def isSymmetric(self, root: TreeNode) -> bool:
        return root is None or self._recursiveSolution(root.left, root.right)
