"""随机链表的复制"""

hash_node = {}

class Node:

    def __init__(self, x):
        self.value = x
        self.next = None
        self.random = None

def copy_random_list(head):
    if not head: return None
    if head in hash_node: return hash_node[head]
    else:
        new_node = Node(head.value)
        hash_node[head] = new_node
        new_node.next = copy_random_list(head.next)
        new_node.random = copy_random_list(head.random)
        return new_node