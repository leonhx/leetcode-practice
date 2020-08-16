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

    def set_values(self, root: TreeNode, xs: List[int]) -> None:
        if root is None:
            return
        left_size = 0 if root.left is None else root.left.size
        root.val = xs[left_size]
        self.set_values(root.left, xs[:left_size])
        self.set_values(root.right, xs[left_size + 1:])

    def reset(self, root: TreeNode) -> None:
        """It is a solution using extra O(n) space"""
        xs = self.to_list(root)
        xs.sort()
        self.set_values(root, xs)

    def set_maxmin(self, root: TreeNode) -> None:
        if root is None:
            return
        self.set_maxmin(root.left)
        self.set_maxmin(root.right)
        max_node, min_node = root, root
        if root.left is not None:
            if root.left.max_node.val > max_node.val:
                max_node = root.left.max_node
            if root.left.min_node.val < min_node.val:
                min_node = root.left.min_node
        if root.right is not None:
            if root.right.max_node.val > max_node.val:
                max_node = root.right.max_node
            if root.right.min_node.val < min_node.val:
                min_node = root.right.min_node
        root.max_node = max_node
        root.min_node = min_node

    def swap(self, root: TreeNode) -> True:
        if root is None:
            return False
        queue = []
        if root.left is not None:
            queue.append(root.left.max_node)
        queue.append(root)
        if root.right is not None:
            queue.append(root.right.min_node)
        if len(queue) < 2:
            return False
        if queue[0].val > queue[-1].val:
            queue[0].val, queue[-1].val = queue[-1].val, queue[0].val
            return True
        for i in range(1, len(queue)):
            if queue[i - 1].val > queue[i].val:
                queue[i - 1].val, queue[i].val = queue[i].val, queue[i - 1].val
                return True
        if self.swap(root.left):
            return True
        if self.swap(root.right):
            return True
        return False

    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.set_maxmin(root)
        self.swap(root)
# @lc code=end
