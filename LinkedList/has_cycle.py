"""判断链表是否有环"""

def has_cycle(head):
    if not head: return False
    quick_node = head.next
    slow_node = head
    while quick_node and quick_node.next:
        if quick_node == slow_node: return True
        quick_node = quick_node.next.next
        slow_node = slow_node.next
    return False