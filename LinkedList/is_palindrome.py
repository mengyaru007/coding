"""是否为回文链表"""
from reverse_list import reverse_list

def find_middle_position(head):
    """寻找中间节点（快慢指针）"""
    quick_node = head
    slow_node = head
    while quick_node and quick_node.next:
        quick_node = quick_node.next.next
        slow_node = slow_node.next
    return slow_node

def is_palindrome(head):
    node_a = head
    node_b = find_middle_position(head)
    head_b = reverse_list(node_b)
    node_b = head_b
    while node_a and node_b:
        if node_a.value != node_b.value: return False
        node_a = node_a.next
        node_b = node_b.next
    return True