"""获取两个链表的相交节点"""
from listNode import ListNode

def get_intersection_node(headA, headB):
    next_a = headA
    next_b = headB
    while next_a or next_b:
        if next_a == next_b: return next_a
        next_a = next_a.next
        next_b = next_b.next
        if not next_a and next_b: next_a = headB
        if not next_b and next_a: next_b = headA
    return None