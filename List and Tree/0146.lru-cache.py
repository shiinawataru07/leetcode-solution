class Node:
    def __init__(self, key: int, val: int, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.hashTable = dict()
        self.size = 0
        self.capacity = capacity
        self.head = None
        self.tail = None

    def moveTail(self, node: Node):
        if node == self.tail:
            return
        if node == self.head:
            self.head = node.next
            self.head.prev = None
        else:
            node.next.prev = node.prev
            node.prev.next = node.next
        node.prev = self.tail
        node.next = None
        self.tail.next = node
        self.tail = node

    def get(self, key: int) -> int:
        if key in self.hashTable:
            cur = self.hashTable[key]
            self.moveTail(cur)
            return cur.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashTable:
            cur = self.hashTable[key]
            cur.val = value
            self.moveTail(cur)
            return
        cur = Node(key, value, prev=self.tail)
        self.hashTable[key] = cur
        if self.head:
            self.tail.next = cur
            self.tail = cur
        else:
            self.head = cur
            self.tail = cur
        self.size += 1
        if self.size > self.capacity:
            self.size -= 1
            self.hashTable.pop(self.head.key)
            self.head = self.head.next
            self.head.prev = None


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


'''
使用哈希表和双向链表来实现LRU缓存。哈希表用于快速查找缓存中的键值对，双向链表用于维护访问顺序。
每次访问一个键时，将其对应的节点移动到链表的尾部，表示最近使用过。当缓存达到容量时，移除链表头部的节点，并从哈希表中删除对应的键值对。
'''
