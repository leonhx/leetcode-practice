#
# @lc app=leetcode id=107 lang=python3
#
# [107] Binary Tree Level Order Traversal II
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def listLayers(self, root: TreeNode, i: int):
        if root is None:
            return
        while len(self.layers) <= i:
            self.layers.append([])
        self.layers[i].append(root.val)
        self.listLayers(root.left, i + 1)
        self.listLayers(root.right, i + 1)

    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        self.layers = []
        self.listLayers(root, 0)
        return self.layers[::-1]
