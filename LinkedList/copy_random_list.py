"""随机链表的复制"""

class Node:

    def __init__(self, x):
        self.value = x
        self.next = None
        self.random = None

def copy_random_list(head):
