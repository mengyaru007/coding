"""反转链表"""

def reverse_list(head):
    if not head: return None
    pre_node = head
    cur_node = head.next
    if not cur_node: return head
    pre_node.next = None
    while cur_node.next:
        next_node = cur_node.next
        cur_node.next = pre_node
        pre_node = cur_node
        cur_node = next_node
    cur_node.next = pre_node
    return cur_node
