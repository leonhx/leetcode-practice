# ByteDance interview


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# recursive solution
def inorder_traversal_sol1(root):
    if root is None:
        return []
    left = inorder_traversal_sol1(root.left) if root.left else []
    right = inorder_traversal_sol1(root.right) if root.right else []
    return left + [root.val] + right


# non-recursive solution
def inorder_traversal_sol2(root):
    if root is None:
        return []
    result = []
    stack = [root]
    current = root
    while stack:
        if current and current.left:
            stack.append(current.left)
            prev = current
            current = current.left
            prev.left = None
        else:
            current = stack.pop()
            result.append(current.val)
            if current.right:
                stack.append(current.right)
                prev = current
                current = current.right
                prev.right = None
    return result


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    print(inorder_traversal_sol2(root))
