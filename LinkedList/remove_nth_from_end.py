"""删除链表倒数第N个节点"""

def remove_nth_from_end(head, n):
    slow_node = head
    fast_node = head.next
    count = 1
    while count < n and fast_node:
        fast_node = fast_node.next
        count += 1
    pre_node = slow_node
    # 若与链表头节点距离N的节点为None或者N大于链表长度则删除头节点
    if not fast_node:
        return head.next
    while fast_node:
        pre_node = slow_node
        slow_node = slow_node.next
        fast_node = fast_node.next
    pre_node.next = slow_node.next
    return head