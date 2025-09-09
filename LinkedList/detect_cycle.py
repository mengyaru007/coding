"""找出环形链表的入口"""

def detect_cycle(head):
    if not head: return None
    quick_node = head
    slow_node = head
    while quick_node and quick_node.next:
        quick_node = quick_node.next.next
        slow_node = slow_node.next
        # 链表有环
        if quick_node == slow_node:
            quick_node = head
            while quick_node != slow_node:
                quick_node = quick_node.next
                slow_node = slow_node.next
            return quick_node
    # 退出循环表示链表无环
    return None