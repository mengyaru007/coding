"""链表排序"""
from merge_two_lists import merge_two_lists

def sort_list(head):
    if not head or not head.next: return head
    # 寻找中间节点
    slow_node = head
    fast_node = head.next
    while fast_node and fast_node.next:
        fast_node = fast_node.next.next
        slow_node = slow_node.next
    mid = slow_node.next
    # 关键：断开链表，避免无限递归
    slow_node.next = None
    return merge_two_lists(sort_list(head), sort_list(mid))