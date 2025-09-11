"""k个一组翻转链表"""
from reverse_list import reverse_list

def reverse_k_group(head, k):
    end_node = head
    number = 1
    while number < k and end_node:
        end_node = end_node.next
        number += 1
    if not end_node: return head
    next_node = end_node.next
    end_node.next = None
    start_node = reverse_list(head)
    head.next = reverse_k_group(next_node, k)
    return start_node
