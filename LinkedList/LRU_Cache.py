"""LRU（最近最少使用）缓存"""

class DLinkedNode:
    def __init__(self, key = 0, value = 0):
        self.key = key
        self.value = value
        self.pre = None
        self.next = None

class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.len = 0
        # 哈希表，记录链表位置
        self.cache = {}
        # 链表头节点和尾节点
        self.head = DLinkedNode(0)
        self.tail = DLinkedNode(0)
        self.head.next = self.tail
        self.tail.pre = self.head

    def insert_head_node(self, cen_node):
        """新节点插入到头节点后面"""
        next_node = self.head.next
        self.head.next = cen_node
        cen_node.pre = self.head
        cen_node.next = next_node
        next_node.pre = cen_node

    def delete_node(self, cen_node):
        """删除指定节点并返回该节点"""
        pre_node = cen_node.pre
        next_node = cen_node.next
        pre_node.next = next_node
        next_node.pre = pre_node

    def get(self, key):
        if key not in self.cache.keys(): return -1
        cen_node = self.cache[key]
        self.delete_node(cen_node)
        self.insert_head_node(cen_node)
        return cen_node.value

    def put(self, key, value):
        if key in self.cache.keys():
            cen_node = self.cache[key]
            cen_node.value = value
            self.delete_node(cen_node)
        else:
            cen_node = DLinkedNode(key, value)
            if self.len + 1 > self.capacity:
                del_node = self.tail.pre
                self.delete_node(del_node)
                self.cache.pop(del_node.key)
                self.len -= 1
            self.cache.update({key: cen_node})
            self.len += 1
        self.insert_head_node(cen_node)