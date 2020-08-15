from typing import List, Any  # noqa:F403


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def _parse_child_repr(self, child_node, prefix):
        lines = repr(child_node).split('\n')
        if lines and prefix:
            lines[0] = prefix + lines[0]
        return lines

    def __repr__(self):
        lines = []
        if self.left:
            lines += self._parse_child_repr(self.left, 'L: ')
        if self.right:
            lines += self._parse_child_repr(self.right, 'R: ')
        indent = ' ' * 2
        result = repr(self.val)
        for l in lines:
            result += '\n' + indent + l
        return result


def ensure_capacity(xs: List[Any], cap: int) -> None:
    while len(xs) < cap:
        xs.append(None)


def show_treenode(x: TreeNode, debug=False) -> List[Any]:
    result = [x] if x else []
    i = 0
    def _set(idx, nn):  # noqa:E306
        if nn:
            ensure_capacity(result, idx + 1)
            result[idx] = nn
    while i < len(result):
        n = result[i]
        left_i = 2 * i + 1
        right_i = left_i + 1
        i += 1
        if n:
            _set(right_i, n.right)
            _set(left_i, n.left)
    return [(n.val if n else None) for n in result]


def to_treenode(xs: List[Any]) -> TreeNode:
    ns = [(TreeNode(x) if x is not None else None) for x in xs]
    for i in range(len(ns) // 2):
        n = ns[i]
        if n:
            left_i = 2 * i + 1
            right_i = left_i + 1
            n.left = ns[left_i] if left_i < len(ns) else None
            n.right = ns[right_i] if right_i < len(ns) else None
    return ns[0] if ns else None


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'ListNode({show_listnode(self)})'


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
