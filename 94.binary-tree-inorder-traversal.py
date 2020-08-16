#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recur(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        return self.recur(root.left) + [root.val] + self.recur(root.right)

    def iter(self, root: TreeNode) -> List[int]:
        result = []
        stack = [root]
        while stack:
            n = stack[-1]
            if n is None:
                stack.pop()
                continue
            if n.left is None:
                result.append(n.val)
                stack[-1] = n.right
            else:
                stack.append(n.left)
                n.left = None
        return result

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        return self.iter(root)
# @lc code=end
