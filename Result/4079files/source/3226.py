# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None:
            return head

        a, b = head, head.next
        prev = None
        head = b or a
        while a is not None and b is not None:
            c = b.next
            a.next = c
            b.next = a
            if prev is not None:
                prev.next = b
            prev = a
            if c is None:
                a, b = None, None
            else:
                a, b = c, c.next
        return head


def make_link_list(*vals):
    if not vals:
        return None
    start = curr = ListNode(vals[0])
    for idx in range(1, len(vals)):
        curr.next = ListNode(vals[idx])
        curr = curr.next
    return start


def display_link_list(node):
    from io import StringIO
    vals = []
    while node is not None:
        vals.append(node.val)
        node = node.next
    return " -> ".join([str(val) for val in vals])

if __name__ == '__main__':
    sol = Solution()
    l = make_link_list(1, 2, 3, 4)
    print(display_link_list(sol.swapPairs(l)))  # 2 -> 1 -> 4 -> 3
    l = make_link_list(1, 2, 3, 4, 5)
    print(display_link_list(sol.swapPairs(l)))  # 2 -> 1 -> 4 -> 3 -> 5
    l = make_link_list(1)
    print(display_link_list(sol.swapPairs(l)))  # 1
    l = make_link_list(1, 2)
    print(display_link_list(sol.swapPairs(l)))  # 2 -> 1
