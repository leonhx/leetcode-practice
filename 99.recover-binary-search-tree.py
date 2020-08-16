#
# @lc app=leetcode id=99 lang=python3
#
# [99] Recover Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def to_list(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        xs = self.to_list(root.left) + [root.val] + self.to_list(root.right)
        root.size = len(xs)
        return xs

    def size(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return self.size(root.left) + 1 + self.size(root.right)

    def set_values(self, root: TreeNode, xs: List[int]) -> None:
        if root is None:
            return
        left_size = 0 if root.left is None else root.left.size
        root.val = xs[left_size]
        self.set_values(root.left, xs[:left_size])
        self.set_values(root.right, xs[left_size + 1:])

    def reset(self, root: TreeNode) -> None:
        xs = self.to_list(root)
        xs.sort()
        self.set_values(root, xs)

    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.reset(root)
# @lc code=end
