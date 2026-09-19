class BrowserHistory:
    
    def __init__(self, homepage: str):
        self.lst = [homepage,]
        self.idx = 0

    def visit(self, url: str) -> None:
        self.lst = self.lst[:self.idx + 1]
        self.idx += 1
        self.lst.append(url)

    def back(self, steps: int) -> str:
        self.idx = max(self.idx - steps, 0)
        return self.lst[self.idx]

    def forward(self, steps: int) -> str:
        self.idx = min(self.idx + steps, len(self.lst) - 1)
        return self.lst[self.idx]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)

'''
方法2
class Node():
    def __init__(self, url: str, next=None, prev=None):
        self.url = url
        self.next = next
        self.prev = prev

class BrowserHistory:
    def __init__(self, homepage: str):
        self.cur = Node(homepage)

    def visit(self, url: str) -> None:
        node = Node(url)
        self.cur.next = node
        node.prev = self.cur
        self.cur = node

    def back(self, steps: int) -> str:
        cnt = 0
        node = self.cur
        while cnt < steps and node.prev:
            node = node.prev
            cnt += 1
        self.cur = node
        return self.cur.url

    def forward(self, steps: int) -> str:
        cnt = 0
        node = self.cur
        while cnt < steps and node.next:
            node = node.next
            cnt += 1
        self.cur = node
        return self.cur.url


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
'''



'''
使用双向链表来实现浏览器历史记录，每个节点存储一个URL，并且有指向前一个节点和后一个节点的指针。
`visit` 方法会创建一个新的节点并将其添加到当前节点之后，同时切断前进方向的历史。`back` 和 `forward` 方法会根据给定的步数移动当前节点的指针，并返回当前节点的URL。
'''
