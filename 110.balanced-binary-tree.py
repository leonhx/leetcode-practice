#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def checkBalance(self, root: TreeNode):
        if root is None:
            return True, 0
        elif root.left is None and root.right is None:
            return True, 1
        else:
            left_b, left_h = self.checkBalance(root.left)
            right_b, right_h = self.checkBalance(root.right)
            b = left_b and right_b and abs(left_h - right_h) <= 1
            h = max([left_h, right_h]) + 1
            return b, h

    def isBalanced(self, root: TreeNode) -> bool:
        return self.checkBalance(root)[0]
