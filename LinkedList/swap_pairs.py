"""两两交换链表中的节点"""

def swap_pairs(head):
    if not head: return None
    if not head.next: return head
    next_node = head.next.next
    new_head = head.next
    new_head.next = head
    head.next = swap_pairs(next_node)
    return new_head