#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def _hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return sum == 0
        s_ = sum - root.val
        if root.left and root.right:
            return self._hasPathSum(root.left, s_) or \
                self._hasPathSum(root.right, s_)
        if root.left:
            return self._hasPathSum(root.left, s_)
        if root.right:
            return self._hasPathSum(root.right, s_)
        return s_ == 0

    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        return self._hasPathSum(root, sum) if root else False
