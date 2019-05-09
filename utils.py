from typing import *  # noqa:F403


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
