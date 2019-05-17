from typing import *  # noqa:F403
from dataclasses import dataclass


@dataclass
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def show_treenode(x: TreeNode) -> List[Any]:
    cur_layer = [x]
    has_next = True
    result = []
    while has_next:
        has_next = False
        next_layer = []
        for n in cur_layer:
            if n is None:
                result.append(None)
                next_layer += [None, None]
            else:
                result.append(n.val)
                next_layer += [n.left, n.right]
                if n.left is not None or n.right is not None:
                    has_next = True
        cur_layer = next_layer
    return result


def to_treenode(xs: List[Any]) -> TreeNode:
    if not xs:
        return None
    root: TreeNode = TreeNode(xs[0])
    xs = xs[1:]
    cur_layer = [root]
    i, layer_no = 0, 1
    while i < len(xs):
        layer_node_num = 2 ** layer_no
        next_layer = [(TreeNode(x) if x is not None else None)
                      for x in xs[i:(i + layer_node_num)]]
        if len(next_layer) != 2 * len(cur_layer):
            raise RuntimeError('size not match')
        for j in range(len(cur_layer)):
            if cur_layer[j] is None:
                continue
            else:
                cur_layer[j].left = next_layer[2 * j]
                cur_layer[j].right = next_layer[2 * j + 1]
        cur_layer = next_layer
        layer_no += 1
        i += layer_node_num
    return root


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def show_listnode(x: ListNode) -> List[Any]:
    xs = []
    while x is not None:
        xs.append(x.val)
        x = x.next
    return xs


def to_listnode(xs: List[Any]) -> ListNode:
    n = None
    result = None
    for x in xs:
        if result is None:
            result = ListNode(x)
            n = result
        else:
            n.next = ListNode(x)
            n = n.next
    return result
