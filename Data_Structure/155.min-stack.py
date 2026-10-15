class MinStack:

    def __init__(self):
        self.lst = list()
        self.size = 0

    def push(self, value: int) -> None:
        if self.size == 0 or self.lst[-1] > value:
            self.lst.append(value)
            self.lst.append(value)
        else:
            self.lst.append(value)
            self.lst.append(self.lst[-2])
        self.size += 1

    def pop(self) -> None:
        self.lst.pop()
        self.lst.pop()
        self.size -= 1

    def top(self) -> int:
        return self.lst[-2]

    def getMin(self) -> int:
        return self.lst[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


'''
用单个列表模拟双栈（每两个元素为一组：[实际值, 当前最小值]）
'''
