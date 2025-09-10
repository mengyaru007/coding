"""两数相加"""
from listNode import ListNode

def add_two_numbers(l1, l2):
    node1 = l1
    node2 = l2
    head = node3 = ListNode(0)
    add = 0
    while node1 or node2:
        num1 = node1.value if node1 else 0
        num2 = node2.value if node2 else 0
        temp = num1 + num2 + add
        node3.next = ListNode(temp % 10)
        node3 = node3.next
        add = int(temp / 10)
        node1 = node1.next if node1 else None
        node2 = node2.next if node2 else None
    if add != 0: node3.next = ListNode(add)
    return head.next