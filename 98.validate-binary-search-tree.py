#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bst(self, root: TreeNode, m, n) -> bool:
        if root is None:
            return True
        if m is not None and root.val <= m:
            return False
        if n is not None and root.val >= n:
            return False
        return self.bst(root.left, m, root.val) and self.bst(
            root.right, root.val, n)

    def isValidBST(self, root: TreeNode) -> bool:
        return self.bst(root, None, None)
# @lc code=end
